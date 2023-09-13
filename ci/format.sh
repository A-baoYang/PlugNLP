#!/bin/bash

set -eu

check_python_command_exist() {
    if ! [ -x "$(command -v "$1")" ]; then
        echo "$1 not installed. Install the python package with: pip install $1"
        exit 1
    fi
}

check_format() {
    case "$1" in
        flake8)
            echo "$(date): $1 starting......"
            git ls-files -- "*.py" | xargs $1
            ;;
        isort)
            echo "$(date): $1 starting......"
            git ls-files -- "*.py" | xargs $1 --check-only
            ;;
        black)
            echo "$(date): $1 starting......"
            git ls-files -- "*.py" | xargs $1 --check
            ;;
        *)
            echo "$1 is not supported."
            exit 1
    esac

    exit_status=$?
    if [ $exit_status -eq 0 ]; then
        echo "$(date): $1 All done!"
    fi
}

# Check commands exist
check_python_command_exist flake8
check_python_command_exist isort
check_python_command_exist black

# Check the format
check_format flake8
check_format isort
check_format black

check_all_format() {
    git ls-files -- "*.py" | xargs flake8

    git ls-files -- "*.py" | xargs isort --check-only

    git ls-files -- "*.py" | xargs black --check
}

# git ls-files -- "*.py" == ls | egrep "\.py"
# git ls-files -- "*.py" | xargs flake8
