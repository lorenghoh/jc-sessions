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

    ## Lesson 01: Getting started

    Computer programs consist of commands, each command instructing the computer to take some action. A computer executes these commands one by one. Among other things, commands can be used to perform calculations, compare things in the computer's memory, cause changes in how the program functions, relay messages or ask for information from the program's user.

    Let's begin programming by getting familiar with the print command, which prints text. In this context, printing essentially means that the program will show some text on the screen.

    This is a classic example of a *hello world* program, which is traditionally how you get started with a new programming language.
    """
    )
    return


@app.cell
def _():
    print("Hello World!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The program will not work unless the code is written exactly as it is above. For example, trying to run the print command without the quotation marks, like so""")
    return


app._unparsable_cell(
    r"""
    print(Hello World!)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Example

    Write a Python script that prints out the following lines *exactly* as they are written.

    ```
    > Row, row, row your boat,
    > Gently down the stream.
    > Merrily, merrily, merrily, merrily,
    > Life is but a dream.
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In summary, if you want to print text, the text must all be encased in quotation marks or Python will not interpret it correctly.

    In Python, the *text* wrapped in quotation marks are called *strings*. Before we delve into the details of variable types, however, we need to first talk about variables and variable assignments in Python.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Variables

    In programming, you assign **data** to **variables**. A *variable* is defined by a named used to store some *value*, like a string or a number. You store a value into a variable so that it can be used later, or be changed.

    For example, if you want to store a value of $10$ into a variable named *x*, you would write
    """
    )
    return


@app.cell
def _():
    x = 10
    print(x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The assignment operator "`=`" assigns a value to a variable.

    Because Python is a dynamic, *type-inferred* programming language, you do not have to worry about matching variable types. In fact, we can re-assign text into the variable like the following.
    """
    )
    return


@app.cell
def _():
    y = 10
    print(y)

    y = "Some Text"
    print(y)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In Python, you can assign multiple values to multiple variables by *chaining* the assignment statements.""")
    return


@app.cell
def _():
    a, b, c = 1, 2, "Hello?"

    print(a)
    print(b)
    print(c)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""You can also ask for an input from the user to define a variable. You would use a Python command named `input()` to do this. Write the following program that asks for the user's name and prints out a message.""")
    return


@app.cell
def _():
    name = input("Tell me your name: ")
    print("Hello, " + name)
    return (name,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Example

    Write a program that asks for the user's name and prints the name twice, on two different lines. The following shows an example of the output from the program.

    ```
    > What is your name? Steve
    > Steve
    > Steve
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""A variable can be referenced multiple times in a program. With strings in Python, combining multiple texts (strings) are as easy as simply adding multiple variables.""")
    return


@app.cell
def _(name):
    print("Hello, " + name + " That is a nice name, " + name + ".")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""You could, of course, ask for more than one input.""")
    return


@app.cell
def _():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")

    print("Your name is " + first_name + " " + last_name + "?")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Example

    Write a program that asks for a user's name and address. The program will then print out the given information.

    ```
    > What is your first name? Steve
    > What is your last name? Sanders
    > What is your street address? 91 Station Road
    > City and postal code? London EC05 6AW

    > Steve Sanders
    > 91 Station Road
    > London EC05 6AW
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Example

    Write a program that asks for three words, and prints out the combination of the three words. For example,

    ```
    > First word: Bibbidi
    > Second word: Bobbidi
    > Third word: Boo
    >
    > Bibbidi-Bobbidi-Boo
    ```
    """
    )
    return


if __name__ == "__main__":
    app.run()
