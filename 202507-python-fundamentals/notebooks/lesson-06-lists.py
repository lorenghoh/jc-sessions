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
    # Lesson 6: Lists

    # List Basics

    In our programs, we've been storing data using variables where each piece of information has its own name. However, this can become complicated when dealing with a large amount of data because it requires creating many separate variables.

    A list is like a collection basket or container in programming. You can store multiple items within it. Instead of creating a new variable for each item, all the items are stored together under one variable name.

    In Python, you define a list by placing its contents within square brackets.

    For example, if I have names "John," "Paul," and "Sarah," I can group them into a single list named "**people**".

    It might look like this:
    """
    )
    return


@app.cell
def _():
    people = ["John", "Paul", "Sarah"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Each item inside the list is called an *element* or an *item*.

    This way, instead of assigning each name to a variable, they're all stored together, making it easier to manage and access.

    A list can also be defined with no items.
    """
    )
    return


@app.cell
def _():
    numbers = []

    print(numbers)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Individual *items* (or *elements*) can be accessed using square brackets.""")
    return


@app.cell
def _():
    num_list = [8, 32, 4, 6]

    print(num_list[0])
    print(num_list[1])
    print(num_list[2])
    print(num_list[3])

    print(f"The sum of first and third element is: {num_list[0] + num_list[2]}")
    return (num_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Lists are *mutable*, which means that the elements can be updated (changed).""")
    return


@app.cell
def _(num_list):
    num_list[1] = 13

    print(num_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Lastly, if you want to know the *length* of the list (i.e. the number of elements, or items, in the list), use the `len()` function.""")
    return


@app.cell
def _(num_list):
    print(len(num_list))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 1

    First, create a list with values `[0, 1, 2, 3, 4, 5]`.

    Swap every value in the list so that the elements are sorted in a descending order; that is, the resulting list starts with the largest number and ends with the smallest number. Then print out the following line.

    ```
    The sum between the first three numbers are: 12
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # List Manipulations

    ## Adding items

    Items or elements can be added to a list using the `append()` method.
    """
    )
    return


@app.cell
def _():
    empty_list = []

    empty_list.append(13)
    empty_list.append(14)
    empty_list.append(16)

    print(empty_list)
    return (empty_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Adding items at a specific index

    The `append()` method always adds the item at the end. If you want to add the item at a specific position (based on an index), you can use the `insert()` method instead. If there are any items at the specific position, all items to the right of the inserted position get pushed to the right, in the direction of the increasing index.
    """
    )
    return


@app.cell
def _(empty_list):
    print(f"Before insert: {empty_list}")

    empty_list.insert(2, 15)

    print(f"After insert: {empty_list}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Removing items

    Just like adding items, there are two ways to remove an item from a list.

    - `pop()` if you want to remove an item at a specific index
    - `remove()` if you want to remove an item based on its value
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Index-based `pop()`

    Like `insert()` method, `pop()` required the index of the element you want to remove. The following example removes items at index 2 from the list.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _(empty_list):
    print(f"Before removal: {empty_list}")

    empty_list.pop(2)

    print(f"After removal: {empty_list}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""It might be useful to know that `pop()` method removes the item and also returns the item.""")
    return


@app.cell
def _(empty_list):
    print(empty_list)

    removed = empty_list.pop(1)

    print(empty_list)
    print(removed)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Example 2

    Create a list with the following items: `[1, 2, 3, 4, 5]`.

    Using the `pop()` function, remove all odd numbers from the list, and output the resulting list. You may use `while` loop, which will make it easier.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Value-based `remove()`

    On the other hand, the `remove()` method requires the value of an item to be removed.
    """
    )
    return


@app.cell
def _():
    remove_list = [1, 1, 2, 3, 3, 6]

    remove_list.remove(1)

    print(remove_list)
    return (remove_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Notice that the `remove()` method removed the **fist** element that appears.

    You need to call the `remove()` method multiple times in this case. However, if you try to remove an item that does not exist, Python will throw and error. In this case, you may want to check if the item exists in the list using the `in` operator.
    """
    )
    return


@app.cell
def _(remove_list):
    if 1 in remove_list:
        remove_list.remove(1)

    print(remove_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Example 3

    Create a list with the following items: `[1, 1, 2, 1, 3, 6]`.

    Write a `while` loop that iterates through this list and removes the number 1 from the list until all 1s are removed from the list. Then output the resulting list.
    """
    )
    return


if __name__ == "__main__":
    app.run()
