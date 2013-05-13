#!/bin/bash

/workspace/github/djangoblog/./manage.py convert_to_south blog
/workspace/github/djangoblog/./manage.py convert_to_south works

/workspace/github/djangoblog/./manage.py migrate

/workspace/github/djangoblog/./manage.py runscript /workspace/github/djangoblog/prepare.py
