# bloodytests
Extension of python3 [unittest library](https://docs.python.org/3/library/unittest.html).

Extension was inspired by [Haki Benita](https://hakibenita.com/timing-tests-in-python-for-fun-and-profit).


## Features
- provides information about each tests time
- actually fails on test failure (exit code 1)

## Setup using pip
```sh
(env)$ pip install -e git+https://github.com/Bloodmallet/bloodytests.git@master#egg=bloodytests
```

## Usage
```sh
(env)$ python -m bloodytests
```
Bloodytests will collect tests just like `unittests` does.

## How to develop
TBD
