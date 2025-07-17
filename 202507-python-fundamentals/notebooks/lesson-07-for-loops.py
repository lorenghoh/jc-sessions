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
    # Lesson 07: Definite Iterations

    Accessing all items from a list is troublesome as the list bocomes longer and longer. We can do this iteratively using the `while` loop, as shown below.
    """
    )
    return


@app.cell
def _():
    while_list = [3, 2, 4, 5, 2]

    index = 0
    while index < len(while_list):
        print(while_list[index])
        index = index + 1
    return (while_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In the Python programming language, fortunately, there is an easier, and more intuitive way to perform this operation.

    # The `for` loop

    The `for` loop is a type of a definite iteration, where the number of loops is known before the loop begins. This is because the loop is defined for a *collection*; for example, we have dealt with strings (collections of characters) and list (collections of values).

    The syntax for a for loop is as follows.

    ```{python}
    for INDEX in COLLECTION:
        EXECUTE
    ```

    For example, we can re-write the above `while` loop as follows.
    """
    )
    return


@app.cell
def _(while_list):
    for item in while_list:
        print(item)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Likewise, as we have noted, strings can be considered to be a collection of characters, which can be used in a `for` loop.""")
    return


@app.cell
def _():
    name = "Grace"

    for character in name:
        print(character)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 1

    Write a program that asks the user to enter his name. The program then outputs each character on separate lines, with a dash (`-`) in between. The following shows a possible interaction with this program.

    ```
    Enter your name: Steve
    S
    -
    t
    -
    e
    -
    v
    -
    e
    -
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # The `range()` function

    Very often, we want to repeat a certain block of code only a set number of time. For example, we want to go through a list containing 10 numbers:
    """
    )
    return


@app.cell
def _():
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(i)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Python has a helper function to support a use case like this. The `range()` function, when used in a loop, can be used to loop through a *range* of numbers.

    There are a few different ways to use the `range()` function. The simplest way is to give it a number, and the loop will iterate from 0 to the number being given. For example,
    """
    )
    return


@app.cell
def _():
    for r in range(10):
        print(r)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""You can also use the `range()` function with two numbers, in which case the loop with start with the first number, and terminate at the second number - 1. For example,""")
    return


@app.cell
def _():
    for j in range(1, 6):
        print(j)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Finally, if you use the `range()` function with three numbers, the last number will be used to determine the *step size*. For example, the following code goes through even numbers between 0 and 10.""")
    return


@app.cell
def _():
    for k in range(0, 11, 2):
        print(k)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 2

    Create the following list: `[3, 7, 1, 1, 2]`.

    Write a program that prints lines of stars (`*`), one per item in the given list. For example, the above list should print the following output.

    Use `string` multiplication here; if you multiply (`*`) a `string` object, it gets repeated by the number being multiplied.

    ```
    ***
    *******
    *
    *
    **
    ```

    Also test your code with the following list: `[1, 3, 2, 4, 6]`.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 3

    Write a program, using a for loop, that outputs the sum of the following two lists as a new list. You can manually write down the two lists in your script.

    ```{python}
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Nested loops

    Depending on the task at hand, you may need to *nest* your `for` loops. Here, the inner loop gets repeated by the outer loop.
    """
    )
    return


@app.cell
def _():
    for a in range(1, 3 + 1):

        for b in range(1, 3 + 1):
            print(a, b)

        print("")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 4

    Let's revisit a previous example.

    Create the following list: `[3, 2, 1, 3, 2]`.

    Write a program that prints lines of stars (`*`), one per item in the given list. For example, the above list should print the following output.

    Do not use `string` multiplication here; instead, write the star (`*`) using nested loops.

    ```
    ***
    **
    *
    ***
    **
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 5

    Write a program that, given the following list of numbers, prints out only the distinctive (unique) items in the given list.

    You can create a new list, only containing unique items, or use the `remove()` function to modify the given list. There are also a number of other ways to solve this problem; be creative, but make sure to use `for` loops.

    ```{python}
    my_list = [3, 2, 2, 1, 3, 3, 1]
    ```

    `[1, 2, 3]`
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Finding extremes

    For example, the following `for` loop goes through a list to find the largest item in that list. In order to solve this problem using the loop structure, one must **remember** the current largest value during the iteration.

    To do that, the simplest way is to create a `temporary` variable. This temporary value is compared to every value in the list, and whenever the target value in the list is larger the temporary value, we assign the larger value to the temporary variable. Once the loop finishes, we will have looked at every item in the list, and our temporary variable will hold the largest value in the list.
    """
    )
    return


@app.cell
def _():
    largest = 0
    l = [1, 2, 3, 4, 5]

    for num in l:
        if num > largest:
            largest = num

    print(f"The large number is: {largest}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 6

    Write a program that, given a list of strings, prints the length of the longest string in the list. Use `len()` function to determine the length of each string item in the list.

    ```{python}
    my_list = ["first", "second", "fourth", "eleventh"]
    ```

    ```
    The longest string is 8 characters long.
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 7

    Write a program that, given a list of strings, prints the text of the longest string in the list. Use `len()` function to determine the length of each string item in the list.

    ```{python}
    my_list = ["first", "second", "fourth", "eleventh"]
    ```

    ```
    The longest string is: "eleventh".
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 8

    Write a program that, given a list of strings, prints **all** the longest string items in the list. This time, the given list might contain multiple strings of the same length, and the output must be given as a list.

    Use `len()` function to determine the length of each string item in the list.

    ```{python}
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    ```

    ```
    ['dorothy', 'richard']
    ```
    """
    )
    return


if __name__ == "__main__":
    app.run()
