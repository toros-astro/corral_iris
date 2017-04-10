# irispl Quality Report

- **Created at:** 2017-04-10 21:06:01.083159
- **Corral Version:** 0.2.6


## 1. Summary

- **Tests Success:** `Yes`
- **Tests Ran:** `1`
- **Processors:** `6`
- **Coverage:** `62.83%`
- **Maintainability & Style Errors:** `8`

<!-- -->

- **QA Index:** `8.67%`
- **QA Qualification:** `FAIL`


### 1.1 About The Corral Quality Assurance Index (QAI)

```
QAI = 2 * (TP * (T/PNC) * COV) / (1 + exp(MSE/tau))

        Where:
            TP: If all tests passes is 1, 0 otherwise.
            T: The number of test cases.
            PCN: The number number of processors (Loader, Steps and Alerts)
                 and commands.
            COV: The code coverage (between 0 and 1).
            MSE: The Maintainability and Style Errors.
            tau: Tolerance of style errors per file

        
```

**Current Value of Tau:**: `13.00` per file


### 1.2 About The Qualification

The Corral qualification is a quantitave scale based on QAI


- QAI >= 0.00% -- `FAIL`
- QAI >= 60.00% -- `PASS`



## 2. Full Output

### 2.1 Tests
```
runTest (irispl.tests.StatisticsCreateAnyNameTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.436s

OK

```
---

### 2.2 Coverage
```
Name                 Stmts   Miss  Cover
----------------------------------------
irispl/__init__.py       1      0   100%
irispl/alerts.py        10      1    90%
irispl/commands.py       6      1    83%
irispl/load.py          25     14    44%
irispl/models.py        34      1    97%
irispl/pipeline.py       4      0   100%
irispl/settings.py      18      0   100%
irispl/steps.py         79     54    32%
irispl/tests.py         14      0   100%
----------------------------------------
TOTAL                  191     71    63%

```
---

### 2.3 MAINTAINABILITY & STYLE
```
Found pep8-style errors.
Please check the Python code style reference: https://www.python.org/dev/peps/pep-0008/

Errors found: 
irispl/alerts.py:51:0: W391 blank line at end of file
irispl/commands.py:27:0: E302 expected 2 blank lines, found 1
irispl/settings.py:41:8: E126 continuation line over-indented for hanging indent
irispl/settings.py:85:8: E126 continuation line over-indented for hanging indent
irispl/settings.py:87:4: E121 continuation line under-indented for hanging indent
irispl/steps.py:36:37: E225 missing whitespace around operator
irispl/steps.py:53:43: E225 missing whitespace around operator
irispl/steps.py:85:43: E225 missing whitespace around operator
irispl/steps.py:117:43: E225 missing whitespace around operator
irispl/tests.py:39:41: E225 missing whitespace around operator
irispl/tests.py:45:56: E225 missing whitespace around operator
```

