# gitlab-ci-lint

This CLI allows you to send a yaml configuration to the API CI linter of a GitLab instance.

## Usage

Set following environment variables to get started:

- `GITLAB_API`: 'https://gitlab.example.com/api/v4'
- `GITLAB_TOKEN`: 'XXXXXXXXXXXXXXXXXXXX'

```
gitlab-ci-lint --help

NAME
    main.py

SYNOPSIS
    main.py FILENAME <flags>

POSITIONAL ARGUMENTS
    FILENAME
        Type: str

FLAGS
    --ci=CI
        Type: bool
        Default: False
    --include_merged_yaml=INCLUDE_MERGED_YAML
        Type: bool
        Default: False

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```

## Output

```
❯ python3 main.py test/valid.yml
Status: valid
Errors: []
Warnings: []

❯ python3 main.py test/invalid.yml
Status: invalid
Errors: ['jobs invalid config should implement a script: or a trigger: keyword', 'jobs config should contain at least one visible job']
Warnings: []
```
