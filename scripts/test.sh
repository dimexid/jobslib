#!/bin/bash -e

COMPONENTDIR="$(cd "${0%/*}/.." 2>/dev/null; pwd)"

export PYTHONPATH="$PYTHONPATH:$COMPONENTDIR"

case $1 in
    "benchmark")
        shift
        python3 -m pytest --benchmark-storage=tests/benchmarks --benchmark-compare --benchmark-group-by=func -vv $@ "$COMPONENTDIR/tests/"
        ;;
    "benchmark-save")
        shift
        python3 -m pytest --benchmark-storage=tests/benchmarks --benchmark-save=benchmark --benchmark-group-by=func -vv $@ "$COMPONENTDIR/tests/"
        ;;
    *)
        python3 -m pytest --benchmark-disable -vv --duration 10 $@ "$COMPONENTDIR/tests/"
esac