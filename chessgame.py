# dictionary for conversion of coordinates from chess notation to python index
conversion = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "1": 7,
    "2": 6,
    "3": 5,
    "4": 4,
    "5": 3,
    "6": 2,
    "7": 1,
    "8": 0,
}

# dictionary for deconversion of numerical representation back to the standard chess notation that humans use
convert_x = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

# dictionary for deconversion
convert_y = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}

# dictionary to store black piece inputs for evaluation and output
b_inputs = {}

# list that defines the valid piece types for black pieces in a chess game
valid_pieces = ["pawn", "rook", "knight", "bishop", "queen", "king"]


def main():
    """In main() function we accept white piece input in format 'pawn a5', corresponding to chess rules (e.g., a-h, 1-8)
    We then proceed with black piece input until up to 16 pieces are added or function is terminated with entering 'done'
    Based on white figure (pawn and rook allowed), we evaluate which balck figures can be taken and print them.
    """

    board_state = get_new_board_state()

    print(
        "Welcome to a chess question game. This program will answer if the placed white chess piece \
    will be able to take any of the placed black pieces. For this version of the program, you can choose to \
    play with either a pawn or a rook."
    )

    # function to input a valid white piece
    while True:
        figure_placement = (
            input("Enter your figure (pawn or rook) and its square (e.g. c6): ")
            .strip()
            .lower()
        )

        try:
            w_move = piece_coordinates(
                figure_placement
            )  # parse input to get piece and position
            if w_move[0] not in valid_pieces[:2]:  # Only allow "pawn" or "rook"
                raise ValueError(
                    f"Invalid piece name: {w_move[0]}. Please enter 'pawn' or 'rook'."
                )
            break
        except ValueError as e:
            print(e)

    # return three-value list: figure name, transformed coords (a8 -> 0,0; d5 -> 3,3 and etc.)
    adjusted_w = converter(w_move)
    board_state = place_white_piece(
        board_state, adjusted_w
    )  # func updates board_state with user input

    # function that asks user to input 1-16 black pieces
    board_state = places_black_pieces(
        board_state
    )  # function that returns a sequence with final board configuration
    print("All figures successfully placed!")
    print_board(board_state)

    if w_move[0] == "pawn":
        checked_pieces = pawn_moves(board_state, adjusted_w)
        deconvert(b_inputs, checked_pieces)
    elif w_move[0] == "rook":
        checked_pieces = rook_moves(board_state, adjusted_w)
        deconvert(b_inputs, checked_pieces)
    else:
        pass


def get_new_board_state():  # initial function with empty e.g. list of lists
    """Chess board x-axis is (a-h), y-axis is (1-8)
    This means that for our purpose we'll need a converter, where
    input alpha character takes index (0-7), num character takes (7-0)
    and the logic is inversed as list indexing starts with y, not x
    e.g. a5 = input[3][0]; g3 = input[5][6] etc. This is done with converter()
    """

    return [[" " for _ in range(8)] for _ in range(8)]


def piece_coordinates(figure_placement):
    """returns three-value list of transformed coordinates"""

    figure_square = (
        figure_placement.split()
    )

    if len(figure_square) != 2:
        raise ValueError(
            "Invalid input format. Please enter 'piece position' (e.g., 'pawn a5')."
        )

    piece = figure_square[
        0
    ]  # the first element of the figure_square list (the piece name) is assigned to the piece variable
    position = figure_square[
        1
    ]  # the second element (the position) is assigned to the position variable

    if (
        len(position) != 2
        or position[0] not in "abcdefgh"
        or position[1] not in "12345678"
    ):
        raise ValueError("Position must be 2 characters long and from 'a1' to 'h8'.")

    return [
        piece,
        position[0],
        position[1],
    ]  # The return keyword sends this list back as the result of the function


def converter(move):
    """returns three-value list of coordinates as indices"""
    # move = [piece, alpha, num]
    move[1] = conversion.get(
        move[1]
    )  # replacing column letter with the corresponding index.
    move[2] = conversion.get(
        move[2]
    )  # replacing row number with the corresponding index.
    return move


def place_white_piece(board_state, w_move):
    """returns updated board state with white piece placement"""
    piece = w_move[0]
    x_coordinate = w_move[1]
    y_coordinate = w_move[2]

    if piece == "rook":
        marker = "R"
    elif piece == "pawn":
        marker = "P"
    else:
        raise ValueError(
            f"Unknown piece type: {piece}"
        )

    # Place the marker on the board
    board_state[y_coordinate][x_coordinate] = marker

    # Convert x, y coordinates back to chess notation
    column_letter = chr(ord("a") + x_coordinate)
    row_number = 8 - y_coordinate

    print(f"Successfully added white {piece} at {column_letter}{row_number}")

    # returns the modified board_state, which now includes the placed white piece
    return board_state


def places_black_pieces(board_state):
    """initializes looped placement of 1-16 black pieces"""
    count = (
        0  # A counter is initialized to keep track of the number of black pieces placed
    )
    while (
        count < 16
    ):  # The loop continues until 16 black pieces are placed or the user enters 'done'.
        try:
            b_move = (
                input(
                    "Enter coordinates of 1 to 16 black pieces (e.g. pawn a2), or enter 'done' when finished: "
                )
                .strip()
                .lower()
            )

            if count > 0 and b_move == "done":
                break
            if count == 0 and b_move == "done":
                raise ValueError("Cannot finish before placing at least one piece.")

            b_split = b_move.split()
            if len(b_split) != 2:
                raise ValueError("Invalid input format. Please enter 'piece position'")

            piece = b_split[0]
            if piece not in valid_pieces:
                raise ValueError(
                    f"Invalid piece type. Allowed: {', '.join(valid_pieces)}"
                )

            place_black = piece_coordinates(
                b_move
            )  # Extracts the piece type and its coordinates from the user's input.
            coordinates = converter(
                place_black
            )  #  Converts the chess notation coordinates into numerical indices using the conversion dictionary.

            # Verifies if the target square is already occupied.
            # If the square is empty (check_occupancy returns False).
            # If the square is occupied (check_occupancy returns True):
            if not check_occupancy(board_state, coordinates):
                # move = [piece, alpha, num]
                x_coordinate = coordinates[1]
                y_coordinate = coordinates[2]
                marker = "B"
                board_state[y_coordinate][x_coordinate] = marker
                # Stores the black piece in the b_inputs dictionary using its position as the key and its type as the value
                # The program only adds a black piece to b_inputs after the square is successfully updated on the board.
                b_inputs.update({b_split[1]: b_split[0]})
                print(f"Successfully added black {place_black[0]} at {b_move[-2:]}")
                count += 1  # Increments the counter after a successful piece placement.
            else:
                raise ValueError("Square is already occupied!")

        except ValueError as e:
            print(
                str(e)
            )

            continue

    return board_state


def check_occupancy(board_state, piece_coordinates):
    """function used in places_black_pieces() to check if the square is free"""
    x_coordinate = piece_coordinates[
        1
    ]  # Extracts the x coordinate from the piece_coordinates list.
    y_coordinate = piece_coordinates[2]
    square = board_state[y_coordinate][
        x_coordinate
    ]  # Retrieves the value of the specified square on the chessboard using the coordinates.
    # isalpha() method checks if the value stored in square is an alphabetic character (a letter). If yes, it's occupied, returns True. If no, it's unoccupied, returns False.
    return square.isalpha()


def pawn_moves(board_state, adjusted_w):
    """checks if pawn can take any black figures; appends them to list"""
    checked_pieces = []
    # move = [piece, alpha, num]
    # adjusted_w = [piece, x, y]
    temp_x = adjusted_w[1]
    temp_y = adjusted_w[2]
    try:
        if board_state[(temp_y) - 1][(temp_x) - 1] == "B":
            piece_1 = []
            piece_1.append((temp_x) - 1)
            piece_1.append((temp_y) - 1)
            checked_pieces.append(piece_1)
    except IndexError:
        pass
    try:
        if board_state[(temp_y) - 1][(temp_x) + 1] == "B":
            piece_2 = []
            piece_2.append((temp_x) + 1)
            piece_2.append((temp_y) - 1)
            checked_pieces.append(piece_2)
    except IndexError:
        pass
    return checked_pieces


def rook_moves(board_state, adjusted_w):
    """Checks if rook can take any black figures; returns their positions."""
    checked_pieces = []
    temp_x = adjusted_w[1]
    temp_y = adjusted_w[2]

    # Define direction vectors: (dx, dy) for up, down, right, left
    directions = [
        (0, -1),  # Up
        (0, 1),  # Down
        (1, 0),  # Right
        (-1, 0),  # Left
    ]

    for dx, dy in directions:
        for i in range(1, 8):  # max 7 steps in one direction
            new_x = temp_x + dx * i
            new_y = temp_y + dy * i

            # Stop if out of bounds
            if not (0 <= new_x <= 7 and 0 <= new_y <= 7):
                break

            square = board_state[new_y][new_x]

            if square == "B":
                checked_pieces.append([new_x, new_y])
                break
            elif square != " ":
                break  # Path is blocked
            # If square == " ", continue

    return checked_pieces


def print_board(board_state):
    """board printer for visualizing the board state"""
    for row in board_state:
        print(row)


def deconvert(b_inputs, checked_pieces):
    """reconverts indices to a proper chess input format"""
    de_coordinates = (
        []
    )  # This list stores the chess notation coordinates of the black pieces that can be captured.

    if not checked_pieces:  # Check if no black pieces were captured
        print("No black pieces were captured.")
        return  # Exit the function early if no pieces were captured

        # Convert the coordinates to chess notation
    for i in checked_pieces:
        x = convert_x.get(
            i[0]
        )  # for each captured piece, it uses convert_x and convert_y to get the letter and number of the position in chess notation.
        y = convert_y.get(i[1])
        xy = (
            x + y
        )  # concatenates the letter and number to form the chess notation (e.g., "a5").
        de_coordinates.append(xy)

    for w in de_coordinates:
        piece = b_inputs.get(
            w
        )  # uses the b_inputs dictionary to find the type of the black piece at that position.
        print(
            f"White piece can take {piece} {w}"
        )  # prints a message stating that the white piece can capture the specified black piece at its position.


main()
