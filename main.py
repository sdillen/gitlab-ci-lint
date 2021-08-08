from requests import request
from os import getenv
from yaml import FullLoader
from yaml import load as yload
from json import dumps as jdumps
from json import loads as jloads
from fire import Fire


def lint(filename: str, ci: bool = False, include_merged_yaml: bool = False):
    gitlab_api_url = ''
    gitlab_token = ''

    if ci:
        gitlab_api_url = getenv('CI_API_V4_URL')
        gitlab_token = getenv('CI_JOB_TOKEN')
    else:
        gitlab_api_url = getenv('GITLAB_API')
        gitlab_token = getenv('GITLAB_TOKEN')

    f = open(filename, 'r')
    ci_file = yload(f, Loader=FullLoader)
    f.close()

    payload = jdumps({
        'content': str(ci_file),
        'include_merged_yaml': include_merged_yaml,
    })

    headers = {
        'Content-Type': 'application/json',
        'PRIVATE-TOKEN': gitlab_token,
    }

    response = request(
        'POST',
        f'{gitlab_api_url}/ci/lint',
        headers=headers,
        data=payload
    )

    response = jloads(response.text)
    print(f'Status: {response["status"]}')
    print(f'Errors: {response["errors"]}')
    print(f'Warnings: {response["warnings"]}')


if __name__ == '__main__':
    Fire(lint)
