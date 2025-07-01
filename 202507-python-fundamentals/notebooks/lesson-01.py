import marimo

__generated_with = "0.14.9"
app = marimo.App(layout_file="layouts/lesson-01.slides.json")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Python Fundamentals

    ## Getting started

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
    > What is your name? Loren
    > Loren
    > Loren
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
    mo.md(r"""You could, of course, ask for more than one input. """)
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


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Example

    Write another program that write a story. You allow the user to give it a name and a year, and the program writes the following.

    ```
    > Type in a name: Mary
    > Type in a year: 1572
    >
    > Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: a dragon was approaching the village. Only Mary could save the village's residents.
    ```
    """
    )
    return


@app.cell
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


@app.cell
def _(mo):
    mo.md(
        r"""
    Notice the lack of quotation marks here. In fact, if we were to add quotation marks around the number, this would mean our variable would no longer be an integer, but a string instead. A string can contain numbers, but it is processed differently.

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


@app.cell
def _(mo):
    mo.md(r"""Variable types matter because different operations affect different types of variables in different ways. Let's have a look at an example:""")
    return


@app.cell
def _(number1, number2):
    print(number1 + number1)
    print(number2 + number2)
    return


@app.cell
def _(mo):
    mo.md(r"""Can you tell what happened here?""")
    return


@app.cell
def _(mo):
    mo.md(r"""Similarly, you cannot simply add a string and an integer together. For example,""")
    return


@app.cell
def _():
    print("Some text " + 12)
    return


@app.cell
def _(mo):
    mo.md(r"""If we do want to print out a string and an integer in a single command, the integer can be cast as a string with the `str` function, and the two strings can then be combined normally. For example, this would work:""")
    return


@app.cell
def _():
    print("Some text " + str(12))
    return


@app.cell
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
