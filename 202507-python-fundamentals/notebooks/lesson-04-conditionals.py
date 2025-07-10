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
    # Lesson 04: Conditional Statements

    So far, the programs we wrote executetd line-by-line. That is, the computer *executes* every line of the written code top-to-bottom every single time. However, sometimes you want to do different things under different conditions, in which case we use *if-statements*.

    If-statements are essential in programming because they allow code to branch out—think of them as decision-making tools for computers. Imagine you're planning your route home during rush hour traffic: you decide whether to take the train, car, or bike based on how much time you have. Similarly, programs need to make choices to navigate through tasks efficiently.

    In Python, if-statements are implemented using the `if` keyword. They follow a specific
    structure:

    1. **Condition:** A statement that evaluates as either `True` or `False`.
    2. **Colon:** Followed by a colon to introduce the indented block of code.
    3. **Indentation:** The code inside the if-statement is indented, and Python executes it
    only when the condition is true.
    """
    )
    return


@app.cell
def _():
    user_input = "yes"

    if user_input == "yes":
        print("Hello world!")
    return (user_input,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The code above prints "Hello world!" only when the input is "yes". The indented line is executed only when the condition is met. For example,""")
    return


@app.cell
def _(user_input):
    if user_input == "no":
        print("Hello world!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Nothing happens when the code above is run, because the condition is not met.

    The if-statements follow the same structure.

    ```
    if CONDITION:
        EXECUTE
    ```

    Notice the tap (or 4 spaces) before `EXECUTE`? In Python, tapped lines define a *code block*. In the above code, the `EXECUTE` block is executed if and only if the condition is met for the if-statement.

    A **block** of code is a group of lines that can be executed as a single unit, typically defined by indentation.

    This structure allows for better organization and readability, particularly within control structures like if-else statements and loops. The use of indentation helps group related lines of code logically, making it easier to manage nested conditions and loops.

    A code block within an `if` statement in Python is defined as a set of statements that follow the colon (`:`) after the `if` keyword. These statements, indented to a specific level, execute only when the condition specified by the `if` statement is met. The indentation signifies which lines are part of the conditional block, allowing nested structures for more complex logic. This structure helps in organizing code and managing multiple conditions or loops within the same scope.
    """
    )
    return


@app.cell
def _():
    # This is the start of the `main` block
    age = 20

    if age >= 18:
        # beginning of the conditional block
        print("You are an adult!")
        age = age + 1
        print("You are now one year older...")
        # end of the conditional block

    print("This here belongs to the main block")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Write a program which asks for the hourly wage, hours worked, and the day of the week.

    The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

    ```
    Hourly wage dollars: 8.5
    Hours worked: 3
    Day of the week: Monday
    Daily wages: 25.5 dollars
    ```

    ```
    Hourly wage: 12.5
    Hours worked: 10
    Day of the week: Sunday
    Daily wages: 250.0 dollars
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Logical operators

    To evaluate the *condition*, we need first to talk about truth values of variables. The variables that can hold the values of `True` and `False` are called **boolean variables**, named after the English mathematician George Boole. In Python, this corresponds to the `bool` data type.

    Any expressions that result in a Boolean value, either `True` or `False`, are called *Boolean expressions*. The *condition* in the example above is of course a Boolean expression as well.

    Remember that the result of a Boolean expression is always a Boolean value, either `True` or `False`, which means that the result can be assigned into a variable.
    """
    )
    return


@app.cell
def _():
    condition = True

    if condition:
        print("The condition is met.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Usually, Boolean expressions are defined by *Boolean operators*, used to define the truth values of an expression. Here are the common Boolean operators we will be using in this course.

    | Operator | Purpose | Example |
    |----------|---------|:--------|
    | `==` | Equal to | `x == y` |
    | `!=` | Not equal to | `x != y` |
    | `>` | Greater than | `x > y` |
    | `<` | Less than | `x < y` |
    | `>=` | Greater than or equal to | `x >= y` |
    | `<=` | Less than or euqal to | `x <= y` |

    Let's consider the following example. You have two numbers (integer values) `x` and `y`, and you'd like to print the larger of the two numbers. Using an if-statement, the program will look like the following.
    """
    )
    return


@app.cell
def _():
    x = 8
    y = 3

    if (x > y):
        print(f"The larger number is: {x}.")

    if (y > x):
        print(f"The larger number is: {y}.")

    if (x == y):
        print("The two numbers are the same.")
    return x, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## If-else statements

    This looks a bit clumsy and repetitive. We only ever want to execute one of the if blocks, because one of the two numbers will always be either larger (or equal to) the other. So, the first conditional statement actually contains all we need here. If it is true, `x` is larger. If it is false, either `y` is larger or they are the same.

    Instead of creating a whole another conditional statement, as in the example above, it is possible to create another branch of the same conditional statement to cover all cases where the condition was false. This is called the `else` statement.

    Let's rewrite the previous example.
    """
    )
    return


@app.cell
def _(x, y):
    if (x > y):
        print(f"The larger number is: {x}.")
    else:
        print(f"The larger number is: {y}.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    When using an if-else construction, one and exactly one of the branches will always be executed.

    ## Example

    Write a program that checks whether a number given by the user is even or odd. Parity can be checked with the modulo operator `%`, which produces the remainder of an integer division operation. When divided by two, if the remainder is zero, the number is even. Otherwise the number is odd.

    ```
    Please type in a number: 2
    The number is even.
    ```

    ```
    Please type in a number: 3
    The number is odd.
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## If-elif-else statements

    Actually, in the previous example, we did not cover the last case, which is that the two numbers are the same, and therefore no number is larger than the other. Now we have more than three cases:

    1. `x` is larger
    2. `y` is larger
    3. They are the same number

    A conditional statement can be added to with an `elif` branch. It is short for the words "else if", which means the branch will contain an alternative to the original condition. Importantly, an `elif` statement is executed only if none of the preceding branches is executed.

    ## Example

    Let's finish the number comparison program that we started at the beginning of this class. The program asks for two numbers, and tells the user whichever one is larger. If the two numbers are the same, the program should print a different message accordingly.

    ```
    Please type in the first number: 5
    Please type in another number: 3
    The larger number is: 5
    ```

    ```
    Please type in the first number: 5
    Please type in another number: 5
    The numbers are the same!
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Python comparison operators can also be used on strings. String a is smaller than string b if it comes alphabetically before b.

    Write a program that asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

    ```
    Please type in the first word: car
    Please type in the second word: scooter
    scooter comes alphabetically last.
    ```

    ```
    Please type in the 1st word: python
    Please type in the 2nd word: python
    You gave the same word twice.
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Combining Conditions

    You can combine conditions with the logical operators `and` and `or`. The operator `and` specifies that all the given conditions must be true at the same time. The operator `or` specifies that at least one of the given conditions must be true.

    Let's say you want to determine if a number is between 5 and 8. There are two conditions, `number >= 5` **and** `number <= 8`. Normally, you would want to paranthesize each condition. So you can write `(number >= 5) and (number <= 8)`.
    """
    )
    return


@app.cell
def _():
    number = 5

    if (number >= 5) and (number <= 8):
        print("The number is between 5 and 8")
    return (number,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Meanwhile, the condition `(number < 5) or (number > 8)` determines that number must be either less than 5 or greater than 8. That is, it must not be within the range of 5 to 8.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Write a program that asks for four integers, and prints the largest of the four numbers given. Use `if-elif-else` statements and consider the four cases: `n1` is the largest, `n2` is the largest, `n3` is the largest, or `n4` is the largest.

    ```
    Number 1: 2
    Number 2: 4
    Number 3: 1
    Number 4: 1

    4 is the greatest of the numbers.
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    The table below outlines the grade boundaries on a certain university course. Write a program that asks for the amount of points received and then prints out the grade attained according to the table.

    | Points | Grade |
    |--------|-------|
    | < 0 | Impossible|
    | 0 - 49 | Fail |
    | 50 - 59 | D |
    | 60 - 69 | C |
    | 70 - 79 | B |
    | 80 - 90 | A |
    | 90 - 100 | A+ |
    | > 100 | Impossible |

    ```
    Enter points [0-100]: 37
    Grade: fail
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Nested Conditionals

    Conditional statements can also be nested within other conditional statements. For example, the following program checks whether a number is above zero, and then whether it is odd or even:
    """
    )
    return


@app.cell
def _(number):
    if number > 0:
        if number % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")
    else:
        print("The number is negative or zero")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

    Write a program that asks the user for a year, and then prints out whether that year is a leap year or not.

    ```
    Type in a year: 2011
    That year is not a leap year.
    ```

    ```
    Please type in a year: 2020
    That year is a leap year.
    ```

    ```
    Please type in a year: 1800
    That year is not a leap year.
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    Write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

    ```
    1st letter: x
    2nd letter: c
    3rd letter: p
    The letter in the middle is p
    ```
    """
    )
    return


if __name__ == "__main__":
    app.run()
