
# Difference Calculation algorithm.

Project intended to calculate differences between filese (json and yaml formats are supproted)

[![Maintainability](https://api.codeclimate.com/v1/badges/33d5b28bb3429efa8a22/maintainability)](https://codeclimate.com/github/mascai/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/33d5b28bb3429efa8a22/test_coverage)](https://codeclimate.com/github/mascai/python-project-lvl2/test_coverage)

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
