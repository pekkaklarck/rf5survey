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
    comments: list

    @property
    def url(self):
        return f'https://github.com/robotframework/robotframework/issues/{self.id}'


PRIORITY_1 = 5
PRIORITY_2 = 3
PRIORITY_3 = 1
RESPONSES = 'responses.csv'
RESULTS = 'results.md'


def main():
    responses = read_responses()
    prio1 = get_issues(responses, col_no=1, max_per_row=1)
    prio2 = get_issues(responses, col_no=3, max_per_row=3)
    prio3 = get_issues(responses, col_no=5)
    issues_and_priorities = combine_issues(prio1, prio2, prio3)
    comments = read_prio1_comments(responses)
    issues = process_issues(issues_and_priorities, comments)
    write_results(issues)


def read_responses():
    responses = []
    header = True
    with open(RESPONSES) as file:
        for row in csv.reader(file):
            if header:
                header = False
            else:
                responses.append(row)
    return responses


def get_issues(data, col_no, max_per_row=None):
    def split_issues(row):
        issues = [int(i) for i in [i.strip() for i in row.split(',')] if i]
        return issues[:max_per_row] if max_per_row else issues

    issues = {}
    for row in data:
        for issue in split_issues(row[col_no-1]):
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
            comments.setdefault(int(id), []).append(comment)
    return comments


def process_issues(issues_and_priorities, comments):
    repo = get_repo()
    issues = []
    for id, prio in issues_and_priorities.items():
        issue = repo.get_issue(id)
        if issue.state == 'open':
            issues.append(Issue(id, issue.title, prio, comments.get(id, [])))
    return sorted(issues, key=lambda issue: -issue.priority)


def get_repo():
    username = os.getenv('GITHUB_USERNAME')
    password = os.getenv('GITHUB_PASSWORD')
    if not (username and password):
        sys.exit('Mandatory GitHub username/password not given.')
    return Github(username, password).get_repo('robotframework/robotframework')


def write_results(issues):
    marker = '<!-- insert issues below -->\n'
    with open(RESULTS) as file:
        content = file.read().split(marker)[0]
    with open(RESULTS, 'w') as file:
        file.write(content)
        file.write(marker)
        for issue in issues:
            file.write(f'- [#{issue.id}]({issue.url}) {issue.title} '
                       f'(weighted priority: {issue.priority})\n')
            for comment in issue.comments:
                file.write(f'    - {comment}\n')


if __name__ == '__main__':
    main()
