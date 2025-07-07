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
    # Python Fundamentals

    ## Lesson 03: Arithmetic Operations

    We have done a couple of simple mathematical operations, and now it is time to properly introduce common arithmetic operators in Python. See the following table.

    | Operator | Operation | Example |
    |:--------:|:----------|:--------|
    | `+` | Addition  | 1 + 2 = 3 |
    | `-` | Subtraction| 2 - 1 = 1 |
    | `*` | Multiplication | 2 * 2 = 4 |
    | `**` | Exponentiation | 2 ** 3 = 8 |
    | `/` | Division | 9 / 2 = 4.5 |
    | `//` | Floor Division | 9 / 2 = 4 |
    | `%` | Modulo | 9 / 2 = 1 |

    The data type of an operand usually determines the data type of the result: if two integers are added together, the result will also be an integer. If a floating point number is subtracted from another floating point number, the result is a floating point number. In fact, if a single one of the operands in an expression is a floating point number, the result will also be a floating point number, regardless of the other operands.

    Division `/` is an exception to this rule. Its result is a floating point number, even if the operands are integers. For example `1 / 5` will result in the floating point number 0.2.
    """
    )
    return


@app.cell
def _():
    height = 172.5
    weight = 68.55

    # the Body Mass Index, or BMI, is calculated by dividing body mass with the square of height
    # height is converted into metres in the formula
    bmi = weight / (height / 100) ** 2

    print(f"The BMI is {bmi}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Python also has the floor division, or integer division, operator `//`, which returns an integer by flooring the resulting value.""")
    return


@app.cell
def _():
    x = 3
    y = 2

    print(f"/ operator {x / y}")
    print(f"// operator {x // y}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Write a program that asks the user to input the number of days. The program then prints out the number of seconds for the given number of days.

    The following shows a possible interaction with this program.

    ```
    Enter number of days: 7
    Number of Seconds: 604800
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Write a program that asks the user for two numbers. The program then prints the sum and the product of the two numbers.

    The following shows a possible interaction with this program.

    ```
    Enter Number 1: 3
    Enter Number 2: 7
    The sum of the numbers: 10
    The product of the numbers: 21
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Write a program which estimates a user's typical food expenditure.

    The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

    Based on this information the program calculates the user's typical food expenditure both weekly and daily.

    The program should function as follows.

    ```
    How many times a week do you eat at the student cafeteria? 4
    The price of a typical student lunch? 2.5
    How much money do you spend on groceries in a week? 28.5

    Average food expenditure:
    Daily: 5.5 euros
    Weekly: 38.5 euros
    ```
    """
    )
    return


if __name__ == "__main__":
    app.run()
