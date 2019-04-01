#!/usr/bin/env sh
set -e

TOOLS=./build/tools
GLOG_logtostderr=0 GLOG_log_dir=examples/cifar10/log/ \
$TOOLS/caffe train \
    --solver=examples/cifar10/cifar10_full_solver_changed_half_the_channel_number.prototxt $@

# reduce learning rate by factor of 10
GLOG_logtostderr=0 GLOG_log_dir=examples/cifar10/log/ \
$TOOLS/caffe train \
    --solver=examples/cifar10/cifar10_full_solver_lr1_changed_half_the_channel_number.prototxt \
    --snapshot=examples/cifar10/cifar10_full_changed_half_the_channel_number_iter_60000.solverstate.h5 $@

# reduce learning rate by factor of 10
GLOG_logtostderr=0 GLOG_log_dir=examples/cifar10/log/ \
$TOOLS/caffe train \
    --solver=examples/cifar10/cifar10_full_solver_lr2_changed_half_the_channel_number.prototxt \
    --snapshot=examples/cifar10/cifar10_full_changed_half_the_channel_number_iter_65000.solverstate.h5 $@
