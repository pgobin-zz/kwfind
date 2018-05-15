# kwfind

## Running:
```
$ python kwfind.py ./dir ^[a-zA-Z]+_TESTResult.*
```
Or:
```
$ python kwfind.py ./dir "^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
```

## Unit test scenarios:

### Tests:
  1. Expect if missing both arguments:
	  -  Return `TypeError`.
  2. Expect if both empty string arguments:
	  - Print  `Invalid directory` and return `None`.
  3. Expect if directory doesn't exist in filesystem:
	  - Print `Invalid directory` and return `None`.
  4. Expect if `(x, y)` passed:
	  - Return dictionary whose count matches tuples in mock(s) of `os.walk()`.
  5. Expect if `(x, y)` passed:
	  - Print `z found` and additional formatted text.
  6. Expect if invalid regex:
	  - Rrint `Invalid...` and return `None`.

### Mocks:
1. `os.walk()`

## Automated or manual E2E test scenarios:
### pyenv automated script, VM, containerized machine, etc.:
  1. Module should not fail on Python 2.7.x - 3.x.
  2. Module should print missing packages if not installed.

### VM:
  1. Module should not fail on Windows, Mac, and Linux systems.

## Performance:
  1. Calculate time and space complexity and investigate:
	  - Multithreaded approach
	  - Distributed approach
