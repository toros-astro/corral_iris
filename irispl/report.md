# irispl Quality Report

- **Created at:** 2017-03-21 04:05:50.675319
- **Corral Version:** 0.2.6


## 1. Summary

- **Tests Success:** `Yes`
- **Tests Ran:** `1`
- **Processors:** `6`
- **Coverage:** `61.75%`
- **Maintainability & Style Errors:** `6`

<!-- -->

- **QA Index:** `8.60%`
- **QA Qualification:** `F`


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


- QAI >= 0.00% -- `F`
- QAI >= 60.00% -- `D-`
- QAI >= 63.00% -- `D`
- QAI >= 67.00% -- `D+`
- QAI >= 70.00% -- `C-`
- QAI >= 73.00% -- `C`
- QAI >= 77.00% -- `C+`
- QAI >= 80.00% -- `B-`
- QAI >= 83.00% -- `B`
- QAI >= 87.00% -- `B+`
- QAI >= 90.00% -- `A-`
- QAI >= 93.00% -- `A`
- QAI >= 95.00% -- `A+`



## 2. Full Output

### 2.1 Tests
```
runTest (irispl.tests.MyTestCase) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.409s

OK

```
---

### 2.2 Coverage
```
Name                 Stmts   Miss  Cover
----------------------------------------
irispl/__init__.py       1      0   100%
irispl/alerts.py         7      0   100%
irispl/commands.py       5      1    80%
irispl/load.py          25     14    44%
irispl/models.py        34      1    97%
irispl/pipeline.py       4      0   100%
irispl/settings.py      17      0   100%
irispl/steps.py         76     54    29%
irispl/tests.py         14      0   100%
----------------------------------------
TOTAL                  183     70    62%

```
---

### 2.3 MAINTAINABILITY & STYLE
```
Found pep8-style errors.
Please check the Python code style reference: https://www.python.org/dev/peps/pep-0008/

Errors found: 
irispl/settings.py:41:8: E126 continuation line over-indented for hanging indent
irispl/steps.py:36:37: E225 missing whitespace around operator
irispl/steps.py:53:43: E225 missing whitespace around operator
irispl/steps.py:84:43: E225 missing whitespace around operator
irispl/steps.py:115:43: E225 missing whitespace around operator
irispl/tests.py:39:41: E225 missing whitespace around operator
irispl/tests.py:45:56: E225 missing whitespace around operator
```

