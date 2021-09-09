"""Perform integer squaring with different approaches."""

# TODO: import the Callable class for type annotations from the typing module
# TODO: import the List class for type annotations from the typing module

from enum import Enum

# TODO: import the Path class from the pathlib module

# TODO: import the typer module

from rich.console import Console

# create a Typer object to support the command-line interface
cli = typer.Typer()


class IntegerSquareApproach(str, Enum):
    """Define the name for the approach to squaring a number."""

    for_loop = "for"
    while_loop = "while"


def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # TODO: determine if the file is not None and if it is a file
    return False


def compute_square_while(value: int) -> int:
    """Compute the square of a number through iteration with a while loop."""
    # TODO: initialize the number of iterations and the answer
    # TODO: repeatedly increase the answer until getting to the value
    # TODO: return the computed integer square


def compute_square_for(value: int) -> int:
    """Compute the square of a number through iteration with a for loop."""
    # TODO: initialize the answer to zero
    # TODO: repeatedly add to the answer the absolute value of the variable called value
    # TODO: return the computed integer square


def compute_square_iterative(
    contents: str, square_function: Callable[[int], int]
) -> List[int]:
    """Compute the square of all of the integer values inside of the contents."""
    # TODO: create an empty list for the squared values
    # TODO: iterate through all of the items in the contents
    # --> TODO: convert the line into a number
    # --> TODO: perform the number squaring computation with square_function
    # --> TODO: add the squared_number to the square_list
    # TODO: return the list of the squared numbers


@cli.command()
def square(
    approach: IntegerSquareApproach = IntegerSquareApproach.for_loop,
    dir: Path = typer.Option(None),
    file: Path = typer.Option(None),
) -> None:
    """Process a file by searching for a specified word."""
    # create a console for rich text output
    console = Console()
    # add extra space after the command to run the program
    console.print()
    # create the full name of the file
    file_fully_qualified = dir / file
    # display a message to explain the file that will be input
    console.print(f":smiley: Squaring numbers in a file called {file_fully_qualified}!")
    console.print()
    # the file is value and so the program should search through it for the word
    if confirm_valid_file(file_fully_qualified):
        # read in the contents of the file
        contents_text = file_fully_qualified.read_text()
        square_list = []
        # the for loop approach should be invoked
        if approach.value == IntegerSquareApproach.for_loop:
            # create the square function to be compute_square_for
            square_function = compute_square_for
            # call the compute_square_iterative function with:
            # --> the contents_text variable with the numerical values as text
            # --> the square function that is set to be compute_square_for
            square_list = compute_square_iterative(contents_text, square_function)
        # the while loop approach should be invoked
        elif approach.value == IntegerSquareApproach.while_loop:
            # create the square function to be compute_square_while
            # call the compute_square_iterative function with:
            # --> the contents_text variable with the numerical values as text
            # --> the square function that is set to be compute_square_while
            square_function = compute_square_while
            square_list = compute_square_iterative(contents_text, square_function)
        # display the list of squared values
        console.print(square_list)
    # the file was no valid and thus you cannot perform the number squaring
    else:
        console.print(
            f":person_shrugging: {file_fully_qualified} was not a valid file! Sorry, cannot square the numbers!"
        )
        console.print()
