#!/bin/bash

rm -r /workspace/github/djangoblog/blog/migrations
rm -r /workspace/github/djangoblog/works/migrations
rm -r /workspace/github/djangoblog/pages/migrations

mysql<<EOF
drop database djangoblog;
create database djangoblog;
exit
