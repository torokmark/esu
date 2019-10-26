#!/usr/bin/env bash

black esu

py.test -v esu/tests/test_struct.py
py.test -v esu/tests/test_open_struct.py
