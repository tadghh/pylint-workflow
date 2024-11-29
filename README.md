# Pylint workflow
Lints python files in a given directory, then updates the repositories readme with the recommendations.

## Setup instructions
*The following permissions are required: workflow read and write access*
#### Configure the following in the workflow
- paths: directory to watch for push events
- python-version: Your projects python version(s)
- PYTHON_FOLDER: The parent folder containing all your python files
- REQUIREMENTS_FOLDER: The location of your projects required pip modules
- STRING_TO_ADD: A string in your readme to add the recommendations below

## Notes
- Utilizes parallel execution with the -j pylint parameter
  - This should speed up larger projects, also look into ruff linter
- No files are added to the repository
## Testing
- You can use the following [project](https://github.com/nektos/act) to test the action locally

## Example

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

[![Pylint](https://github.com/tadghh/pylint-workflow/actions/workflows/pylint.yml/badge.svg?branch=main&event=push)](https://github.com/tadghh/pylint-workflow/actions/workflows/pylint.yml) 


The following changes should be made.
```python
************* Module snake
snake_says_hello/snake.py:15:4: C0116: Missing function or method docstring (missing-function-docstring)
snake_says_hello/snake.py:15:35: W0613: Unused argument 'radio_band' (unused-argument)
snake_says_hello/snake.py:18:4: C0116: Missing function or method docstring (missing-function-docstring)
snake_says_hello/snake.py:22:0: C0115: Missing class docstring (missing-class-docstring)
snake_says_hello/snake.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
snake_says_hello/snake.py:27:14: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
snake_says_hello/snake.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
snake_says_hello/snake.py:46:0: C0103: Constant name "GRrETING" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module fruit
snake_says_hello/fruit.py:1:0: C0114: Missing module docstring (missing-module-docstring)
snake_says_hello/fruit.py:4:0: C0115: Missing class docstring (missing-class-docstring)
snake_says_hello/fruit.py:4:0: C0103: Class name "Fruit_Object" doesn't conform to PascalCase naming style (invalid-name)
snake_says_hello/fruit.py:20:15: W0718: Catching too general exception Exception (broad-exception-caught)
snake_says_hello/fruit.py:14:20: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
snake_says_hello/fruit.py:9:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
snake_says_hello/fruit.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)

-----------------------------------
Your code has been rated at 6.59/10

```
