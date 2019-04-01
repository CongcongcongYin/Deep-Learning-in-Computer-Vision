#!/usr/bin/env sh
set -e

TOOLS=./build/tools
GLOG_logtostderr=0 GLOG_log_dir=examples/cifar10/log/ \
$TOOLS/caffe train \
    --solver=examples/cifar10/plain20_cifar_train_test_solver.prototxt $@