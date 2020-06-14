
# Difference Calculation algorithm.

Project intended to calculate differences between filese (json and yaml formats are supproted)

[![Maintainability](https://api.codeclimate.com/v1/badges/33d5b28bb3429efa8a22/maintainability)](https://codeclimate.com/github/mascai/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/33d5b28bb3429efa8a22/test_coverage)](https://codeclimate.com/github/mascai/python-project-lvl2/test_coverage)

[![Build Status](https://travis-ci.org/mascai/python-project-lvl2.svg?branch=master)](https://travis-ci.org/mascai/python-project-lvl2)


### Example

```
$ gendiff before.json after.json

{
    host: hexlet.io
  + timeout: 20
  - timeout: 50
  - proxy: 123.234.53.22
  + verbose: true
}
```


```
// before.json
{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22"
}
```

```
// after.json
{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}
```

### 1. Installation
``` pip install --user --extra-index-url https://test.pypi.org/simple/ mascai_gendiff ```

[![asciicast](https://asciinema.org/a/BXXoYnHRqyEAKpv54OHjcoRyM.svg)](https://asciinema.org/a/BXXoYnHRqyEAKpv54OHjcoRyM)


### 2. Examples of work
#### 2.1 Comparation of two json files
[![asciicast](https://asciinema.org/a/JV5pLE982NGs3PpE51wAC2QrB.svg)](https://asciinema.org/a/JV5pLE982NGs3PpE51wAC2QrB)

#### 2.2 Comparation of two yaml files
[![asciicast](https://asciinema.org/a/892gMv8CO7RTONCdPfzMnte45.svg)](https://asciinema.org/a/892gMv8CO7RTONCdPfzMnte45)

#### 2.3 Comparation of nested files
[![asciicast](https://asciinema.org/a/dAbvzoOQich4SN4vZnB3UfgJq.svg)](https://asciinema.org/a/dAbvzoOQich4SN4vZnB3UfgJq)
