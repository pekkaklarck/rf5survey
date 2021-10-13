#!/usr/bin/env python3

import os
import sys
import csv
from dataclasses import dataclass

from github import Github


@dataclass
class Issue:
    id: int
    title: str
    priority: int
    open: bool

    @property
    def url(self):
        return f'https://github.com/robotframework/robotframework/issues/{self.id}'


PRIORITY_1 = 5
PRIORITY_2 = 3
PRIORITY_3 = 1
DATA = 'responses.csv'
RESPONSES = 'RESPONSES.md'
ISSUES = 'ISSUES.md'


def read_responses(path):
    responses = []
    header = True
    with open(path) as file:
        for row in csv.reader(file):
            if header:
                header = False
            else:
                responses.append(row)
    return responses


def get_issues(responses):
    prio1 = get_issues_from_column(responses, col_no=0, max_per_row=1)
    prio2 = get_issues_from_column(responses, col_no=2, max_per_row=3)
    prio3 = get_issues_from_column(responses, col_no=4)
    issues_and_priorities = combine_issues(prio1, prio2, prio3)
    return process_issues(issues_and_priorities)


def format_responses_and_issues(responses, issues):
    format_responses(responses, issues)
    format_issues(responses, issues)


def format_issues(responses, issues):
    comments = read_prio1_comments(responses)
    write_results(issues, comments)


def format_responses(responses, issues):
    with open(RESPONSES, 'w') as file:
        file.write('# Responses to survey questions\n')
        format_prio('What is the single most important feature for you?', 0, 1,
                    responses, issues, file)
        format_prio('What three issues have second-highest priority?', 2, 3,
                    responses, issues, file)
        format_prio('What other issues you would like to see included?', 4, None,
                    responses, issues, file)
        format_comments('Free comments to the development team', 5,
                        responses, file)
        format_comments('Free comments to Robot Framework Foundation', 6,
                        responses, file)


def format_prio(title, col_no, max_per_row, responses, issues, file):
    file.write(f'## {title}\n')
    file.write('| Issue | Comment |\n')
    file.write('|-------|---------|\n')
    issue_col = [split_issues(row[col_no],max_per_row) for row in responses]
    comment_col = [row[col_no+1].replace('\n', '<br>') for row in responses]
    for indices, comment in zip(issue_col, comment_col):
        if indices:
            issue = ', '.join(f'[#{issue.id}]({issue.url} "{issue.title}")'
                              for issue in [issues[i] for i in indices])
            file.write(f'| {issue} | {comment} |\n')


def format_comments(title, col_no, responses, file):
    file.write(f'## {title}\n')
    comments = [row[col_no].replace('\n', '<br>') for row in responses]
    for comment in comments:
        if comment:
            file.write(f'- {comment}\n')


def split_issues(row, max_per_row=None):
    try:
        issues = [int(i) for i in [i.strip() for i in row.split(',')] if i]
    except ValueError:
        return []
    return issues[:max_per_row] if max_per_row else issues


def get_issues_from_column(data, col_no, max_per_row=None):
    issues = {}
    for row in data:
        for issue in split_issues(row[col_no], max_per_row):
            issues.setdefault(issue, 0)
            issues[issue] += 1
    return issues


def combine_issues(prio1_issues, prio2_issues, prio3_issues):
    issues = {}
    for issues_by_prio, prio_weight in [(prio1_issues, PRIORITY_1),
                                        (prio2_issues, PRIORITY_2),
                                        (prio3_issues, PRIORITY_3)]:
        for issue, count in issues_by_prio.items():
            issues.setdefault(issue, 0)
            issues[issue] += count * prio_weight
    return issues


def read_prio1_comments(responses):
    comments = {}
    for row in responses:
        id, comment = row[:2]
        if comment:
            comments.setdefault(int(id), []).append(comment.replace('\n', '<br>'))
    return comments


def process_issues(issues_and_priorities):
    repo = get_repo()
    issues = {}
    for id, prio in sorted(issues_and_priorities.items(), key=lambda item: -item[1]):
        issue = repo.get_issue(id)
        issues[id] = Issue(id, issue.title, prio, issue.state == 'open')
    return issues


def get_repo():
    username = os.getenv('GITHUB_USERNAME')
    password = os.getenv('GITHUB_PASSWORD')
    if not (username and password):
        sys.exit('Mandatory GitHub username/password not given.')
    return Github(username, password).get_repo('robotframework/robotframework')


def write_results(issues, comments):
    marker = '<!-- insert issues below -->\n'
    with open(ISSUES) as file:
        content = file.read().split(marker)[0]
    with open(ISSUES, 'w') as file:
        file.write(content)
        file.write(marker)
        for issue in issues.values():
            if issue.open:
                file.write(f'- [#{issue.id}]({issue.url}) {issue.title} '
                           f'(weighted priority: {issue.priority})\n')
                for comment in comments.get(issue.id, ()):
                    file.write(f'    - {comment}\n')


if __name__ == '__main__':
    usage = f'Usage: {sys.argv[0]} responses|issues|both'
    if len(sys.argv) < 2:
        sys.exit(usage)
    action = sys.argv[1]
    actions = {'responses': format_responses,
               'issues': format_issues,
               'both': format_responses_and_issues}
    if action not in actions:
        sys.exit(usage)
    path = DATA if len(sys.argv) == 2 else sys.argv[2]
    responses = read_responses(path)
    issues = get_issues(responses)
    actions[action](responses, issues)
