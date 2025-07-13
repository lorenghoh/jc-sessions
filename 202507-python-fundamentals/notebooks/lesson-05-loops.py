import marimo

__generated_with = "0.14.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Lesson 6: Loops

    Last time, we have tried the `while True` loop to repeat sections of code. Because the condition of the loop is set to `True`, the condition is met every time the loop iterates. We need to explicitly break out of the loop when we want to stop the loop.
    """
    )
    return


@app.cell
def _():
    # Print numbers until the variable a equals 5
    a = 1

    while True:
        print(a)
        a += 1
        if a == 5:
            break
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The general structure of the while statement is as follows:

    ```
    while CONDITION:
        BLOCK
    ```

    Notice that the syntax for the `while` loop is similar to that of the `if` statement: both statements consist of some Boolean expression (condition) and the code block that you want to repeat.

    In the followin example, we want to count up from a given number. The block is executed if and only if the variable `number` is less than 10.
    """
    )
    return


@app.cell
def _():
    number = 4

    while (number < 10):
        print(number)
        number = number + 1

    print("Done!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Loop Structure

    To create a loop, you need three components: initilization, condition, and update.

    **Initialization** deals with setting the initiali values for the variables being used in the loop. This has to be performed before the loop begins.

    **Condition** defines how long the loop will run.

    **Update** needs to be performed within the loop, in a way that each iteration will bring the loop one step closer to the completion of the loop.

    ## Example

    Write a program that prints out all even numbers between 2 and 30.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example: Fix the code

    The program below has some syntactic issues:

    ```{python}
    print("Are you ready?")
    number = int(input("Please type in a number: "))
    while number = 0:
    print(number)
    print("Now!")
    ```

    Please fix the code so that it prints out the following:

    ```
    Are you ready?
    Please type in a number: 5
    5
    4
    3
    2
    1
    Now!
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Write a program that asks the user for an integer value as input, and prints out all integers greater than zero but smaller than the number give.

    ```
    Enter a number: 5
    1
    2
    3
    4
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Write a program that asks the user for an integer value, which will be the upper limit. The program prints out numbers, starting from 1, so that each subsequent number is twice as large as the last number, up to the upper limit given by the user.

    ```
    Upper limit: 8
    1
    2
    4
    8
    ```

    ```
    Upper limit: 20
    1
    2
    4
    8
    16
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Let's write a program that asks the user to enter a number, and calculates the sum of all numbers starting from 1, until the sum is at least equal to the number entered by the user.

    ```
    Limit: 2
    3
    ```

    ```
    Limit: 10
    10
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Strings, revisited

    Remember that you can append strings by adding them together.
    """
    )
    return


@app.cell
def _():
    words = "word 1"
    words = words + " word 2"
    words = words + " word 3"

    print(words)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can, however, simplify this using the loop syntax.""")
    return


@app.cell
def _():
    n = 1
    w = ""

    while n <= 3:
        w = w + f"word {n} "
        n = n + 1

    print(w)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Let's update our code from the previous example. In addition to the result, let's also print the actual calculation.

    ```
    Limit: 2
    The consecutive sum: 1 + 2 = 3
    ```

    ```
    Limit: 10
    The consecutive sum: 1 + 2 + 3 + 4 = 10
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Nested loops

    As we have practiced using the `if` statements, loops can also be nested inside another loop. For example, the following program uses a loop to ask the user to input numbers. It then uses another loop inside the first one to print a countdown from the given number down to 1.
    """
    )
    return


@app.cell
def _():
    x = 3

    while x >= 0:
        i = x
        s = ""

        while i >= 0:
            s = s + f"{i} "
            i = i - 1
        print(s)

        x = x - 1

    print("Iteration complete.")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Example

    Write a program that asks the user for an integer value. The program then prints out a list of multiplication operations until both operands reach the number given by the user.

    ```
    Please type in a number: 2
    1 x 1 = 1
    1 x 2 = 2
    2 x 1 = 2
    2 x 2 = 4
    ```

    ```
    Please type in a number: 3
    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    ```
    """
    )
    return


if __name__ == "__main__":
    app.run()
