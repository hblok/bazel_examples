#!/bin/sh

export PATH=/usr/bin:$PATH

which mocha > /dev/null || (echo "\nERROR: ** Mocha installation required. (apt install mocha)\n"; exit 1)

NODE_PATH=.
for f in "$@"; do
  if [ -f $f ]; then
    NODE_PATH="$NODE_PATH:`dirname $f`"
  fi
done

export NODE_PATH

cmd="mocha $*"

echo "NODE_PATH=$NODE_PATH"
echo "$cmd"

$cmd
