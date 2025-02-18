#/bin/bash

git init && git symbolic-ref HEAD refs/heads/main
git add .
git commit -m "First commit"
gh repo create