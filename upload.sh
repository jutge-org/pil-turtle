#!/bin/bash

echo "Current version: " `grep "version =" setup.py | awk '{print $3}'`

echo -n "New version? "
read version

perl -p -i -e "s/^version = .*/version = '$version'/" setup.py

git commit -a
git push
git tag $version -m "Release $version"
git push --tags origin master
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
