#!/bin/sh

git config --global user.email "cong.yin17@student.xjtlu.edu.cn"
git config --global user.name "congcongcongyin"
git add .
git commit -am "$1"
git pull origin master
git push -u origin master
