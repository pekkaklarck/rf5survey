#!/usr/bin/env python3

import os
import sys
import csv
from dataclasses import dataclass
from pathlib import Path

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
DATA = Path('responses.csv')
README = Path('README.md')


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


def add_issues(responses, issues):
    comments = read_prio1_comments(responses)
    write_results(issues, comments)


def add_responses(responses, issues):
    lines = []
    format_prio('What is the single most important feature for you?', 0, 1,
                responses, issues, lines)
    format_prio('What three issues have second-highest priority?', 2, 3,
                responses, issues, lines)
    format_prio('What other issues you would like to see included?', 4, None,
                responses, issues, lines)
    format_comments('Free comments to the development team', 5,
                    responses, lines)
    format_comments('Free comments to Robot Framework Foundation', 6,
                    responses, lines)
    add_content('\n'.join(lines), 'responses')


def format_prio(title, col_no, max_per_row, responses, issues, lines):
    lines.append(f'### {title}')
    lines.append('| Issue | Comment |')
    lines.append('|-------|---------|')
    issue_col = [split_issues(row[col_no],max_per_row) for row in responses]
    comment_col = [format_comment(row[col_no+1]) for row in responses]
    for indices, comment in zip(issue_col, comment_col):
        if indices:
            issue = ', '.join(f'[#{issue.id}]({issue.url} "{issue.title}")'
                              for issue in [issues[i] for i in indices])
            lines.append(f'| {issue} | {comment} |')


def format_comment(comment):
    if comment.upper() == 'NONE':
        return ''
    return comment.replace('\n', '<br>')


def format_comments(title, col_no, responses, lines):
    lines.append(f'## {title}')
    comments = [format_comment(row[col_no]) for row in responses]
    for comment in comments:
        if comment:
            lines.append(f'- {comment}')


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
        comment = format_comment(comment)
        if comment:
            comments.setdefault(int(id), []).append(comment)
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
    lines = []
    for issue in issues.values():
        if issue.open:
            lines.append(f'- [#{issue.id}]({issue.url}) {issue.title} '
                         f'(weighted priority: {issue.priority})')
            for comment in comments.get(issue.id, ()):
                lines.append(f'    - {comment}')
    add_content('\n'.join(lines), 'issues')


def add_content(content, name):
    start = f'\n<!-- start {name} -->\n'
    end = f'\n<!-- end {name} -->\n'
    old = README.read_text()
    before, old = old.split(start)
    old, after = old.split(end)
    with open(README, 'w') as file:
        file.write(before)
        file.write(start)
        file.write(content)
        file.write(end)
        file.write(after)


if __name__ == '__main__':
    path = DATA if len(sys.argv) == 1 else sys.argv[1]
    responses = read_responses(path)
    issues = get_issues(responses)
    add_issues(responses, issues)
    add_responses(responses, issues)
