# pylint-workflow
Lints python files pushed into a given directory, then updates the repositories ReadMe with the recommendations.



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
