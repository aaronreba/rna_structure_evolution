#!/bin/bash

bin_dir=$(dirname "$0")
base_dir=$(readlink -m $bin_dir/..)
pushd $base_dir > /dev/null

export PYTHONPATH=$base_dir
python3 $@

popd > /dev/null

