#!/bin/bash

mysql<<EOF
drop database djangoblog;
create database djangoblog;
exit
EOF

rm -r /workspace/github/djangoblog/blog/migrations
rm -r /workspace/github/djangoblog/works/migrations

/workspace/github/djangoblog/./manage.py syncdb
