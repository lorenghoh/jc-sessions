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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 1

    Write a function called `sum` that takes two numbers as arguments and calculates the sum of the two numbers. Then call your function to test the sum of the two numbers is printed.

    ```{python}
    sum(5, 3)
    sum(10, 1)
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Example 2

    Write a function called `mean` that takes a list of any length as its argument, and calculates the average among all the items included in the list.

    Call your function to test if the averages are correct.

    ```{python}
    mean([5, 3, 1, 8, 9])
    mean([10, 7, 1])
    ```
    """
    )
    return


if __name__ == "__main__":
    app.run()
