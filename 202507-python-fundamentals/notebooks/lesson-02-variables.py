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

    ## Lesson 02: Variables

    ## Creating variables with assignments

    In Python, the primary way to create a variable is to **assign** a value to the variable using the assignment operator `=`.

    ```{python}
    variable_name = value
    ```

    Here, the name of the variable is on the left-hand side of the statement, and the assignment operator `=`, then the value that is to be stored in the variable.

    ## Naming the variable

    Variable names in Python can be of any length, and can consist of uppercase letters [A-Z] and lowercase letters [a-z], numbers [0-9], and understore [_].

    The one restriction in Python is that the first character cannot be a number [0-9].

    For example, the following variables are declared with valid names.
    """
    )
    return


@app.cell
def _():
    name = "Lawrence"
    today = "04-07-2025"
    is_adult = True
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    However, the following is not a valid variable declaration (try the following code).

    ```{python}
    999_birds = 10
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Sometimes, you will need more than one word to properly describe your variable. When using multi-word names, you can struggle to read them if there isn’t a distinguishable boundary between words:""")
    return


@app.cell
def _():
    numberofgraduates = 200
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The most common practices for multi-word variable names are the following:

    - Snake case: Lowercase words are separated by underscores. For example: number_of_graduates.

    - Camel case: The second and subsequent words are capitalized to make word boundaries easier to see. For example: numberOfGraduates.

    - Pascal case: Similar to camel case, except the first word is also capitalized. For example: NumberOfGraduates.

    Python recommends the snake-case style. That is, the above multi-word variable should be named:
    """
    )
    return


@app.cell
def _():
    number_of_graduates = 200
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    With everything we have learned so far, let's work on some examples.

    Write a program that create a variable called `month`, and assign "July" as its value. Print out the variable.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Example

    You are tasked with building a Python program based on some databse. One of the entries in the database looks like the following table.

    | Last Name | First Name | State | Gender |
    |-----------|------------|-------|--------|
    | Rahn      | Sid        | NJ    | Male   |

    Write a program that creates four variables, whose names and values correspond to each of the columns in the above table, then print out the results. The output of the program could look like the following.

    ```
    Sid Rahn (NJ), Male
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Numeric Types: Integers

    So far, we have mainly dealt with texts (strings). But there are many other types of data. We will now take a look at integers. An **integer** is a whole number (not a fraction or decimal) that can be negative, zero, or positive.

    Let's define a variable named `age`, which will contain an integer value.
    """
    )
    return


@app.cell
def _():
    age = 20
    print(age)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In fact, if we were to add quotation marks around the number, this would mean our variable would no longer be an integer, but a string instead. A string can contain numbers, but it is processed differently.

    So, why does it matter that variables have a type, when the following program still prints out the same thing twice?
    """
    )
    return


@app.cell
def _():
    number1 = 100
    number2 = "100"

    print(number1)
    print(number2)
    return number1, number2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Variable types matter because different operations affect different types of variables in different ways. Let's have a look at an example:""")
    return


@app.cell
def _(number1, number2):
    print(number1 + number1)
    print(number2 + number2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Can you tell what happened here?

    Similarly, you cannot simply add a string and an integer together. For example, try the following code:

    ```{python}
    print("Some text " + 12)
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The above code did not work because the text ("Some text") is of type `string`, but the number (12) is of type `integer`. 

    What if you do want to print some numbers with the text?

    We will need a *function* that converts an `integer` to a `string`, so that we can add it to another text, which will then concatenate the two strings together.

    Luckily, Python has a `str()` function that will convert the input into `string`. But how would we used a function? In Python, a *function* is defined by its name, followed by `()`, and if there is an output, you call the function using a statement that is structured like the following.

    ```{pythoh}
    output = function(input)
    ```

    So for the `str()` function, we can do something like
    """
    )
    return


@app.cell
def _():
    number = input("Enter a number: ")
    number_as_text = str(number)
    print("The number is " + number_as_text + ".")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Actually the above example isn't exactly truthful, because the output from the `input()` function is always a string (we were just pretending that the input is an integer, because that's what we asked).

    So, if we do want to import a number, we should really be *casting* `number` (from the `input()` function) to integer first. We can use `int()` function to do so.

    ```{pythoh}
    number = input("Enter a number: ")
    number = int(number)
    number_as_text = str(number)
    print("The number is " + number_as_text + ".")
    ```

    But can we simplify this a bit further?

    You can always *nest* multiple functions. Let's say there are two functions, `func1` then `func2`, you want to apply to a variable. Then, you would write

    ```{pythoh}
    output = func2(func(input))
    ```

    In our case, the above code can be simplified as 

    ```{pythoh}
    number = int(input("Enter a number: "))
    number_as_text = str(number)
    print("The number is " + number_as_text + ".")
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Example

    Write a program that asks for a number from the user, increment the number by one, and print the result. The following shows a possible interaction with this program.

    ```
    Enter a number: 4
    The increment is: 5
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Example

    Write a program that asks for two numbers from the user and display the total and the difference of the two numbers. The following shows a possible interaction with this program.

    ```
    > Define x = 27
    > Define y = 12

    > 27 + 12 = 39
    > 27 - 12 = 15
    ```
    """
    )
    return


if __name__ == "__main__":
    app.run()
