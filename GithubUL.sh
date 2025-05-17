#/bin/bash

git init && git symbolic-ref HEAD refs/heads/main
git add .
git commit -m "First commit"
gh repo create

# for folders or storage locations that don't track ownership (flashdrive), may need:
# git config --global --add safe.directory '<folder path>'
