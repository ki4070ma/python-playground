## Count steps

```
$cloc {dir}
```

## Count num of class

```
$grep -r '^class ' {dir}
$grep -r 'class [A-Z]' .
```

## Count num of method

### public method

```
grep -r 'def [a-z]' .
```

### protected method

```
grep -r 'def _[a-z]' .
```

### private method

```
grep -r 'def __[a-z]' .
```
