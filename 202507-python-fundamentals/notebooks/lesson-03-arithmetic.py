import marimo

__generated_with = "0.14.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # Python Fundamentals

    ## Lesson 03: Arithmetic operations
    """
    )
    return


if __name__ == "__main__":
    app.run()
