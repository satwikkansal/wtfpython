"""
Parses the README.md and generated the table
`CONTRIBUTORS.md`.
"""

import pprint
import re
import requests

regex = ("[sS]uggested by @(\S+) in \[this\]\(https:\/\/github\.com\/satwikkansal"
         "\/wtf[pP]ython\/issues\/(\d+)\) issue")


fname = "README.md"
contribs = {}

table_header = """
| Contributor | Github | Issues |
|-------------|--------|--------|
"""

table_row = '| {} | [{}](https://github.com/{}) | {} |'
issue_format = '[#{}](https:/github.com/satwikkansal/wtfpython/issues/{})'
rows_so_far = []

github_rest_api = "https://api.github.com/users/{}"


with open(fname, 'r') as f:
    file_content = f.read()
    matches = re.findall(regex, file_content)
    for match in matches:
        if contribs.get(match[0]) and match[1] not in contribs[match[0]]:
            contribs[match[0]].append(match[1])
        else:
            contribs[match[0]] = [match[1]]

for handle, issues in contribs.items():
    issue_string = ', '.join([issue_format.format(i, i) for i in issues])
    resp = requests.get(github_rest_api.format(handle))
    name = handle
    if resp.status_code is 200:
        pprint.pprint(resp.json()['name'])
    else:
        print(handle, resp.content)
    rows_so_far.append(table_row.format(name,
                                        handle,
                                        handle,
                                        issue_string))

print(table_header + "\n".join(rows_so_far))