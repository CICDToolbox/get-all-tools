<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/CICDToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/cicdtoolbox/black-and-white-circle-256.png" alt="CICDToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/CICDToolbox/get-all-tools/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/CICDToolbox/get-all-tools/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/CICDToolbox/get-all-tools/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/CICDToolbox/get-all-tools?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/CICDToolbox/get-all-tools">
        <img src="https://img.shields.io/github/created-at/CICDToolbox/get-all-tools?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/CICDToolbox/get-all-tools/releases/latest">
        <img src="https://img.shields.io/github/v/release/CICDToolbox/get-all-tools?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/CICDToolbox/get-all-tools/releases/latest">
        <img src="https://img.shields.io/github/release-date/CICDToolbox/get-all-tools?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/CICDToolbox/get-all-tools/releases/latest">
        <img src="https://img.shields.io/github/commits-since/CICDToolbox/get-all-tools/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/CICDToolbox/get-all-tools/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/CICDToolbox/get-all-tools/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/CICDToolbox/get-all-tools/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/CICDToolbox/get-all-tools/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

This is a simple script that we use internally to download all of the tools from the [CICD Toolbox](https://github.com/CICDToolbox).

It will pull the latest copy from each repository and place the script into ~/bin, ideally ~/bin will be in your $PATH.

## Current Toolset

The following is a list of all the tools that will be downloaded when the script is executed.

| Name                                                                              | Purpose                                                                                                            |
| :-------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| [Action Lint](https://github.com/CICDToolbox/action-lint)                         | Validate your GitHub action files using [actionlint](https://github.com/rhysd/actionlint).                         |
| [Awesomebot](https://github.com/CICDToolbox/awesomebot)                           | Link check your files with [awesome_bot](https://rubygems.org/gems/awesome_bot).                                   |
| [Bandit](https://github.com/CICDToolbox/bandit)                                   | Inspect your Python projects for security issues using [bandit](https://pypi.org/project/bandit/).                 |
| [Hadolint](https://github.com/CICDToolbox/hadolint)                               | Validate your Dockerfiles using [hadolint](https://github.com/hadolint/hadolint).                                  |
| [JSON Lint](https://github.com/CICDToolbox/json-lint)                             | Validate your JSON files using [jq](https://stedolan.github.io/jq/).                                               |
| [Markdown Lint](https://github.com/CICDToolbox/markdown-lint)                     | Validate your markdown files in using [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli).       |
| [Perl Lint](https://github.com/CICDToolbox/perl-lint)                             | Validate your Perl scripts using the native perl linter.                                                           |
| [PHP Lint](https://github.com/CICDToolbox/php-lint)                               | Validate your PHP code using the native php linter.                                                                |
| [Puppet Lint](https://github.com/CICDToolbox/puppet-lint)                         | Validate your Puppet files using [puppet-lint](https://rubygems.org/gems/puppet-lint).                             |
| [Pur](https://github.com/CICDToolbox/pur)                                         | Verify your Python projects requirements.txt for updates using [pur](https://pypi.org/project/pur/).               |
| [PyCodeStyle](https://github.com/CICDToolbox/pycodestyle)                         | Inspect your Python projects for code smells using [pycodestyle](https://pypi.org/project/pycodestyle/).           |
| [PyDocStyle](https://github.com/CICDToolbox/pydocstyle)                           | Validate your Python project documentation for compliance with [pydocstyle](https://pypi.org/project/pydocstyle/). |
| [Pylama](https://github.com/CICDToolbox/pylama)                                   | Validate your Python project documentation for compliance with [pylama](https://pypi.org/project/pylama/).         |
| [Pylint](https://github.com/CICDToolbox/pylint)                                   | Inspect your Python projects for code smells using [pylint](https://pypi.org/project/pylint/).                     |
| [Reek](https://github.com/CICDToolbox/reek)                                       | Inspect your Ruby code for code smells using [reek](https://rubygems.org/gems/reek).                               |
| [Rubocop](https://github.com/CICDToolbox/rubocop)                                 | Perform static code analysis on Ruby code using [rubocop](https://rubygems.org/gems/rubocop).                      |
| [ShellCheck](https://github.com/CICDToolbox/shellcheck)                           | Perform static code analysis on shell scripts using [ShellCheck](https://github.com/koalaman/shellcheck).          |
| [Validate Citations File](https://github.com/CICDToolbox/validate-citations-file) | Validate CITATIONS.cff using [cffconvert](https://pypi.org/project/cffconvert/).                                   |
| [YAML Lint](https://github.com/CICDToolbox/yaml-lint)                             | Validate your yaml files in CI/CD pipelines using [yamllint](https://pypi.org/project/yamllint/).                  |

## TODO

[ ] - Be able to specify if you pull from HEAD or the latest version / tag.

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
