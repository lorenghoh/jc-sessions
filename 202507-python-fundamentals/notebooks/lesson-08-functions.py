import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Lesson 8: Functions

    ## Function definitions

    So far in this class, we have used a number of functions built into Python; for example, we have been using `len`, `print` and `input` to solve the problems.

    Of course, it is possible to come up with our own functions.

    To do so, we must **define** our function. The syntax for the function definition is as follows.

    ```{python}
    def NAME():
        CODE_BLOCK
    ```

    The **definition** of a function always begins with the `def` keyword, followed by the **name** of the function. The code block following the colon is also called the **body** of the function.

    For example, consider a simple function that prints a message.
    """
    )
    return


@app.function
def greet():
    print("This is the function body.")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Nothing happens when you run the code above. This is because *defining* a function, by itself, does not perform any actions. To execute the function body, a function must be **called**.""")
    return


@app.cell
def _():
    greet()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Once defined, a function can be called multiple times.""")
    return


@app.cell
def _():
    greet()
    greet()
    greet()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Function arguments

    Every function can take input *arguments* and produce an output. For example, the `input()` function takes a string as an input, and returns a string as an output.

    Let's define a function with arguments.
    """
    )
    return


@app.cell
def _():
    def greet_name(name):
        print(f"Hello, {name}!")

    greet_name("Alan")
    greet_name("World")
    return


@app.cell
def _(mo):
    mo.md(r"""Of course, a function can take more than one argument.""")
    return


@app.cell
def _():
    def greet_names(n1, n2, n3):
        print(f"Hello {n1}, {n2}, and {n3}!")

    greet_names("Steve", "Alan", "Nick")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Example 1

    The following shows the outline a function `first_character()`.

    Complete the function so that it prints out the first character of the string it takes as its argument.

    ```{python}
    def first_character(text):
         # write your code here
    ```

    such that running the following code

    ```
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')
    ```

    results in the following output.

    ```
    p
    y
    t
    h
    o
    n
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 2

    Write a function called `sum` that takes two numbers as arguments and calculates the sum of the two numbers. Then call your function to test the sum of the two numbers is printed.

    ```{python}
    sum(5, 3)
    sum(10, 1)
    ```

    ```
    8
    11
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Example 3

    Write a function called `mean` that takes a list of any length as its argument, and calculates the average among all the items included in the list.

    Call your function to test if the averages are correct.

    ```{python}
    mean([5, 3, 1, 8, 9])
    mean([10, 7, 1])
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Nested function Calls

    As we have done many times before, functions calls can be made within another function.
    """
    )
    return


@app.cell
def _():
    def hello(name):
        print("Hello there,", name)

    def greet_many_times(name, times):
        while times > 0:
            hello(name)
            times -= 1

    greet_many_times("Emily", 3)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Example 4

    Let's define a function called `line()` that takes two arguments: an integer and a string.

    The function prints out a line of text, the length of which is specified by the first argument.

    The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars.

    ```
    line(7, "%")
    line(10, "Python")
    line(3, "")
    ```

    ```
    %%%%%%%
    PPPPPPPPPP
    ***
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Example 5

    Write a function called `square_of_hashes()`, which uses the `line()` function that you just defined.

    The function takes one argument, which determines the length of the side of the square.

    ```{python}
    square_of_hashes(5)
    print()
    square_of_hashes(3)
    ```

    ```
    #####
    #####
    #####
    #####
    #####

    ###
    ###
    ###
    ```

    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Example 6

    Write a function called `triangle()`, which takes one argument and draws a trangle of hashes. The argument should be an integer, that is both the width and height of the triangle. You should use the `line()` function from previous examples.

    ```{python}
    triangle(6)
    print()
    triangle(3)
    ```

    ```
    #
    ##
    ###
    ####
    #####
    ######

    #
    ##
    ###
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Example 7""")
    return


if __name__ == "__main__":
    app.run()
