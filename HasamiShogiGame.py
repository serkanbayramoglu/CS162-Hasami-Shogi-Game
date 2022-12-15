# Author: Serkan Bayramoglu
# Date: 03/12/2021
# Course: CS162
# Email: bayramoglu.serkan@gmail.com
#                                               PORTFOLIO PROJECT
#
# Description: This is a program for the Hasami Shogi game, Variant 1, which is played by the rules explained below.
# I am using one main class - HasamiShogiGame class, to represent game, with details provided below in thr docstrings
# and the DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS section attached to the end.
#
# Summary of the rules of this game:
# The game is played between two players, each holding 9 pieces. player_red holds 9 red pieces, player_black holds 9
# black pieces. The game has a 9x9 board, consisting of squares of 9 rows and 9 columns, rows are named from 1 to 9,
# and rows are named from 'a' to 'i', such that each square is named like 'a2' or 'h5'.
# Initially, all black pieces are placed on the row i, and all red pieces are placed on square a. player_black starts
# playing, after each move, the other player plays next. each player can move one of their pieces every turn, to either
# moving horizontally or vertically to an empty square they want, without jumping over any other piece. Thee aim of the
# game is winning the game by capturing the opponents pieces, until the opponent has 1 or no pieces left. In order to
# capture the opponent's piece, either of the below;
#   -   the player should move his/her piece to a square adjacent to a corner, where the opponent already has a piece on
#       the corner, and the player already has another piece adjacent to the other side of the corner. in this case the
#       player captures the opponent's piece on the corner and the piece is removed from the board.
#   -   the player should move his/her piece to a square adjacent to a square where one or several of the opponent's
#       pieces are located, in a line, and on the other end of the line, the player has one more piece. All the player's
#       and opponent's pieces should be aligned vertically or horizontally. In this case all the opponent's pieces
#       between the player's two pieces are captured and removed from the board.
#  The game ends when either of the player wins, where 8 or 9 pieces of the opponent's pieces are captured, and only 1
#  or no opponent's pieces are left on the board.


class HasamiShogiGame:
    """
    This class represents a game. The class holds the Board class and the Player class.
    The class also holds __init__(), get_game_state(), set_game_state(), get_active_player(), set_active_player(),
    get_num_captured_pieces(), make_move(), validate_move(), check_and_capture(), get_square_occupant(), and
    print_status_matrix() methods.
    This class communicates with Board and Player class.
    """

    def __init__(self):
        """
        Initializes the game parameters which are; _board, _player_red, _player_black, _active_player, _inactive_player,
        and _game_state
        """
        self._board = self.Board()
        self._player_red = self.Player("RED")
        self._player_black = self.Player("BLACK")
        self._active_player = self._player_black
        self._inactive_player = self._player_red
        self._game_state = "UNFINISHED"

    class Board:
        """
        This class represents the board used for the game. It has __init__(), get_status_matrix(), and
        set_status_matrix() methods.
        This class communicates with HasamiShogiGame class.
        """

        def __init__(self):
            """
            Dictionary of lists is used for the board status. The first row (list) shows the numbers ‘1’ to
            ‘9’, and the first column (index 0) of each list shows the labels ‘a’ to ‘i’.This way, printing of
            the status will be easier, and the indexing will be easier (the indices of the lists to locate
            the pieces will range from ‘1’ to ‘9’).
            :return: None
            """

            self._status_matrix = {"header": [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                                        "a": ["a", "R", "R", "R", "R", "R", "R", "R", "R", "R"],
                                        "b": ["b", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                                        "c": ["c", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                                        "d": ["d", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                                        "e": ["e", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                                        "f": ["f", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                                        "g": ["g", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                                        "h": ["h", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                                        "i": ["i", "B", "B", "B", "B", "B", "B", "B", "B", "B"]}

        def get_status_matrix(self):
            """returns the status matrix of the board"""
            return self._status_matrix

        def set_status_matrix(self, square, new_value):
            """
            Changes the specified square of the status matrix to new_value, which may be 'R', 'B', or '.'
            :param square: the reference to the square (such as 'a2') where the new value will be set
            :param new_value: 'R', 'B', or '.'
            :return: None
            """
            self._status_matrix[square[0]][int(square[1])] = new_value

    class Player:
        """
        This class takes the color as the parameter, represents the player, initiating the number of stones
        on board to 9, and number of stones captured to 0.
        This class communicates with HasamiShogiGame class.
        """

        def __init__(self, color):
            """
            Initializes the parameters; _on_board_pieces to 9, _captured_pieces to 0, _color
            :param color: the color of the pieces of the player
            """
            self._on_board_pieces = 9
            self._captured_pieces = 0
            self._color = color

        def inc_num_captured_pieces(self, pieces):
            """
            This method takes pieces as the parameter representing the number of pieces to be increased or decreased,
            increases _captured_pieces, the number of captured pieces of the player by ‘pieces’, and decreases
            _on_board_pieces, the number of on board pieces of the player by ‘pieces’.
            :param pieces: the number of pieces to be increased or decreased
            :return: None
            """
            self._captured_pieces += pieces
            self._on_board_pieces -= pieces

        def get_captured_pieces(self):
            """
            Takes no parameter, returns _captured_pieces, the number of captured pieces, of the player.
            :return: number of captured pieces of the player
            """
            return self._captured_pieces

        def get_on_board_pieces(self):
            """
            Takes no parameter, returns _on_board_pieces, the number of pieces left on board, of the player.
            :return: number of pieces left on board, of the player
            """
            return self._on_board_pieces

        def get_color(self):
            """
            Takes no parameter, returns _color, the color of pieces of the player.
            :return: color of the pieces of the player
            """
            return self._color

    def get_game_state(self):
        """
        Takes no parameters and returns the game status; 'UNFINISHED', 'RED_WON' or 'BLACK_WON'.
        :return: 'UNFINISHED', 'RED_WON' or 'BLACK_WON'
        """
        return self._game_state

    def set_game_state(self):
        """
        Takes no parameters and turns self._game_state from 'UNFINISHED' to 'RED_WON', if the last move was made by
        self._player_red or 'BLACK_WON', if the last move was made by self._player_black
        :return: None
        """
        if self._active_player == self._player_black:
            self._game_state = "BLACK_WON"
        else:
            self._game_state = "RED_WON"

        print(self._game_state)

    def get_active_player(self):
        """
        takes no parameters and returns whose turn it is - either 'RED' or 'BLACK’
        :return: 'RED' or 'BLACK’
        """
        return self._active_player.get_color()

    def set_active_player(self):
        """
        takes no parameter and switches the player every time the method is called; the _active_player becomes
        _inactive_player and the _inactive_player becomes _active_player. returns the new active_player
        :return: the new _active_player (the player object, not the color of his/her pieces)
        """
        temp_player = self._active_player
        self._active_player = self._inactive_player
        self._inactive_player = temp_player

        return self._active_player

    def get_num_captured_pieces(self, color):
        """
        Takes color as the parameter, and returns the number of pieces of that color that have been captured.
        If color = ‘RED’: returns self._playerRed._captured_Pieces().
        If color = ‘BLACK: returns self._playerBlack._captured_Pieces()
        Otherwise, returns None
        :param color: 'RED' or 'BLACK'
        :return: number of captured pieces of the player who holds the pieces in the queried color
        """
        if color == "RED":
            return self._player_red.get_captured_pieces()
        elif color == "BLACK":
            return self._player_black.get_captured_pieces()
        else:
            return None

    def make_move(self, from_square, to_square):
        """
        Takes two parameters that represent the square moved from and the square moved to (ex:make_move('b3', 'b9'))
        Calls validate_move(from_square, to_square) method,
        If check_move(fromSquare, toSquare) method returns False;
        -   Returns False
        If check_move(fromSquare, toSquare) method returns True;
        -   updates the board with the new move (set from_square to ".", to_square to "B" if self._active_player is
            "BLACK" or "R" if self._active_player is "RED"
        -   calls check_and_capture() method, which will capture pieces to be captured
        -   uses get_on_board_pieces() method, to check the on board pieces of the inactive player
        -   if the number of opponent's pieces <= 1;
        -       he game has ended, calls self.set_game_state() method, which will set the winner and print on screen
        -   calls self.set_active_player method to switch to the next player
        -   Returns True
        :param from_square: the square where the active player's piece is currently located
        :param to_square: the destination square, where the piece on from_square will be moved to
        :return: True or False
        """
        if not self.validate_move(from_square, to_square):
            return False

        self._board.set_status_matrix(from_square, ".")
        self._board.set_status_matrix(to_square, self._active_player.get_color()[0])

        self.check_and_capture(to_square)

        if self._inactive_player.get_on_board_pieces() <= 1:
            self.set_game_state()

        self.set_active_player()

        return True

    def validate_move(self, from_square, to_square):
        """
        Checks whether:
        -	The get_game_state() method returns ‘UNFINISHED’
        -	active_player has a piece on from_square
        -   the from_square and to_square parameter length are 2
        -	to_square is a valid location (not out of the board)
        -   from_square and to_square have to be different
        -	from_square and to_square have to be on the same line (horizontal or vertical)
        -	get_square_occupant() is "NONE" for to_square, and any square between from_square and to_square
        returns True (if the move is valid) or False (if not valid)
        :param from_square:
        :param to_square:
        :return: True or False
        """
        if self.get_game_state() != "UNFINISHED":
            return False

        if self.get_square_occupant(from_square) != self._active_player.get_color():
            return False

        if not (len(to_square) == len(from_square) == 2):
            return False

        if not (ord('a') <= ord(to_square[0]) <= ord('i') and 1 <= int(to_square[1]) <= 9):
            return False

        if to_square == from_square:
            return False

        if to_square[0] != from_square[0] and to_square[1] != from_square[1]:
            return False

        # check horizontal:
        if to_square[0] == from_square[0]:
            for index in range(int(from_square[1]) + 1, int(to_square[1]) + 1):
                square = to_square[0] + str(index)
                if self.get_square_occupant(square) != "NONE":
                    return False

        # check vertical:
        if to_square[1] == from_square[1]:
            range_step = 1
            if ord(from_square[0]) > ord(to_square[0]):
                range_step = -1
            for index in range(ord(from_square[0]) + range_step, ord(to_square[0]) + range_step, range_step):
                square = chr(index) + to_square[1]
                if self.get_square_occupant(square) != "NONE":
                    return False

        return True

    def check_and_capture(self, to_square):
        """
        Group 1 checks - corner captures:
        -   check each of the four corners if there is any inactive player's piece
        -   for each of the corner that has inactive player's piece, check if the to_square is adjacent to it
        -   if the to_square is a square adjacent to a corner that is occupied with inactive player's piece, check if
            the other square adjacent to the corner has the active player’s piece.
        If true:
        -   call the inc_num_captured_pieces method of the self._inactive_player, which will increase the
            self._captured_pieces by 1, and decrease the self._on_board_pieces by 1,
        -   remove the piece from the board by calling set_status_matrix() and setting the square to ".".

        Group 2 checks, horizontal and vertical captures - Checks in each direction (right, left, up, down) one by one:
        -   Independent of Group 1 checks,
        -   chose each direction with (right, left, up, left) using for loop
        -   for each direction independently, check if;
        -     there is an inactive player’s piece next to the to_square
        -     if yes, check one square next, towards the same direction, whether there is any black or red piece
        -     If there is another inactive player’s piece, repeat checking the next square on the same direction, until
        -      either an empty square, or square with the active player’s piece, or the end of the board is reached,
        -      and each time increment a counter representing pieces to capture, while iterating.
        If in the end, the active player’s piece is reached,
        -   call the inactive player’s inc_num_captured_pieces() method, passing the counter as pieces to capture from
            the inactive player, which will increase the self._captured_pieces by counter, and decrease the
            self._on_board_pieces by counter.
        -   remove the captured piece(s) from the board by calling set_status_matrix() and setting the square(s) to ".".
        :param to_square: address of the suqare to which the piece has moved
        :return: None
        """
        # corner captures
        corner_list = ["a9", "i9", "i1", "a1"]
        for corner in corner_list:
            if self.get_square_occupant(corner) == self._inactive_player.get_color():
                # if to_square is above / below corner
                if (chr(ord(corner[0]) + 1)) + corner[1] == to_square \
                        or (chr(ord(corner[0]) - 1)) + corner[1] == to_square:
                    square_to_right = corner[0] + (str(int(corner[1]) + 1))
                    square_to_left = corner[0] + (str(int(corner[1]) - 1))
                    if self.get_square_occupant(square_to_left) == self._active_player.get_color() \
                            or self.get_square_occupant(square_to_right) == self._active_player.get_color():
                        self._inactive_player.inc_num_captured_pieces(1)
                        self._board.set_status_matrix(corner, ".")
                # if to_square is left / right of the corner
                elif corner[0] + (str(int(corner[1]) + 1)) == to_square or corner[0] + (
                                                                    str(int(corner[1]) - 1)) == to_square:
                    square_above = (chr(ord(corner[0]) - 1)) + corner[1]
                    square_below = (chr(ord(corner[0]) + 1)) + corner[1]
                    if self.get_square_occupant(square_above) == self._active_player.get_color() \
                            or self.get_square_occupant(square_below) == self._active_player.get_color():
                        self._inactive_player.inc_num_captured_pieces(1)
                        self._board.set_status_matrix(corner, ".")

        # horizontal and vertical captures
        direction_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for direction in direction_list:
            counter = 0
            square_next = (chr(ord(to_square[0]) + direction[0])) + (str(int(to_square[1]) + direction[1]))
            while self.get_square_occupant(square_next) == self._inactive_player.get_color():
                counter += 1
                square_next = (chr(ord(square_next[0]) + direction[0])) + (str(int(square_next[1]) + direction[1]))
            if counter != 0 and self.get_square_occupant(square_next) == self._active_player.get_color():
                self._inactive_player.inc_num_captured_pieces(counter)
                for count in range(counter):
                    square_next = (chr(ord(square_next[0]) - direction[0])) + (str(int(square_next[1]) - direction[1]))
                    self._board.set_status_matrix(square_next, ".")

    def get_square_occupant(self, square):
        """
        Takes one parameter - a string representing a square (such as 'i7'), and returns 'RED', 'BLACK', or
        'NONE', depending on whether the specified square is occupied by a red piece, a black piece, or neither.
        :param square: address of the square that is queried
        :return: 'RED', 'BLACK', or 'NONE'
        """
        if len(square) == 2:
            if ord('a') <= ord(square[0]) <= ord('i') and 1 <= int(square[1]) <= 9:
                result = self._board.get_status_matrix()[square[0]][int(square[1])]
                if result == "R":
                    return "RED"
                elif result == "B":
                    return "BLACK"
                elif result == ".":
                    return "NONE"
        return None

    def print_status_matrix(self):
        """
        Prints the status matrix, by retrieving using self._board.get_status_matrix()
        """
        matrix = self._board.get_status_matrix()
        for list in matrix:
            print(matrix[list])


def main():
    game = HasamiShogiGame()
    game.print_status_matrix()


if __name__ == '__main__':
    main()


# HALF WAY PROGRESS REPORT
#
# DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
#
# 1) Determining how to store the board
#       The board is designed to look exactly like the physical board such that at the top of the board there are column
#       labels from "1" to" 9", and on the left column of the board there are the row labels from "a" to "i". the upper
#       left corner of the board is blank (corresponding to empty space " ")
#       For this purpose, the board, which is an object of the game (HasamiShogiGame), is stored in the form of a
#       dictionary of lists, such that the first list of the dictionary has the key of "header", and consists of numbers
#       from 1 to 9 (the list starts with an empty " " data to provide space for the first column), the keys of the
#       dictionary, after the header, range from 'a' to 'i', and the first data of each list in the dictionary is the
#       same as the keys.
#
#       Please see the code above for the of the matrix, which is already initialized.
#
#       There are three reasons for deciding on this structure: First, when the board is printed, it will show the
#       complete board with the headers 1 to 9 and a to i, without any need to print the keys, and the numbers 1 to 9,
#       to make the board look complete when printed. Second, the indices to be used for the lists will correspond to
#       the column numbers of the squares we want to reach (we will not need to deduct 1 from the column numbers to get
#       the index everytime). Third, it makes the "check and capture" method in the program easier, as "index - 1" of
#       some of the corners will not result in a "-1" index (which will mean the last element of the list),  therefore
#       I do not need to add an additional statement to check whether the current index is 0 or not.
#
#
# 2) Initializing the board
#       The board will be hard coded as shown in the __init__() method above, for two reasons:
#
#       First, I believe it is easier for the programmer to visualize the board by hard coding, specifically while
#       testing different scenarios, where I can simply set the board to test specific parts of the code.
#
#       Second, as the size of the board is small, initializing the table with loops would not make the code shorter or
#       more efficient, but would make it more complicated, as the fillowing different would be needed (as per one of
#       the possible solutions);
#
#       One loop would be needed for the header (the list starts with " ", follows by "1", and increments by 1 until the
#       end), one for the list for the key "a" (the list starts with "a", all others to be filled with "R", one for
#       the list for the key "i" which would be similar to the key "a", but filled with "B" instead of "R", and all the
#       remaining lists would start with the key as their first data, and all others be filled with "." to show that
#       the squares are empty.
#
#
# 3) Determining how to track which player's turn it is to play right now
#       The Player class is a class under the HasamiShogiGame class, which has attributes; _active_player,
#       _inactive_player, _player_red and _player_black. Initially, the _active_player is set to _player_black, and
#       _inactive_player is set to _player_red. Everytime the make_move() method is called, after the move is validated
#       and the required captures are done, the set_active_player() method is called, which takes no parameters, ans
#       switches the active and inactive players (the active player becomes inactive and the inactive player becomes
#       active).
#
#       As a seprate note, if the intention was to create a platform with different games, this game being one of
#       them, then another class named Person could be created outside of this game, and the Player class under the
#       HasamiShogiGame class could be inherited from the Person class. However, as there is no indication that there
#       will be a platform, and there will other games within the platform, or there will be other similar reasons, I
#       did not create any other class outside the HasamiShogiGame class.
#
#
# 4) Determining how to validate piece movement
#       When called, the he make_move() first calls alidate_move() method, to validate piece movement, which takes
#       from_square and to_square parameters, and checks the following;
#         -	the get_game_state() method should return ‘UNFINISHED’
#         -	active_player has a piece on from_square
#         - the from_square and to_square parameter length are 2
#         -	to_square is a valid location (not out of the board)
#         - from_square and to_square have to be different
#         -	from_square and to_square have to be on the same line (horizontal or vertical)
#         -	get_square_occupant() is NONE for to_square, and any square between from_square and to_square. For
#         this, there will be two loops; to check either horizontal (if the _from_square and to_square are aligned
#         horizontally), or vertical (if aligned vertically). For horizontal, the column number should be incremented in
#         a loop from from_square (+1 or -1, starting from next column) to to_square. For vertical, the row name should
#         be incremented in a loop from from_square (+1 or -1, starting from next column) to to_square. For this, ord()
#         will be used to retrieve the ASCI code of the letter, to be able to increment/decrement the letter, and chr()
#         will be used to convert it back to a letter before concatenating the letter with the number to form the square
#         address to be checked using get_square_occupant() method whether the square is occupied (method should
#         return "NONE").
#       After making each of the the above checks, if any check fails, the validate_move() method returns true. If after
#       completing all the checks, False is still not returned, it means all the checks are passed, and the method will
#       return True.
#
#
# 5) Determining when pieces have been captured
#       After validating the to_square and from_square parameters, the make_move method will move the piece, by
#       calling the set_status_matrix() method of the Board, to set the from_square to ".", and to_square to the first
#       letter of the color of the self._active_player.
#       Once the piece is moved, the make_move method will continue and call the check_and_capture() method to check
#       whether any pieces of the inactive player should be captured, and will capture and remove if it should.
#       check_and_capture() method will take one parameter, to_square, and will make two sets of checks; first checking
#       corner captures, then checking horizontal and vertical captures as outlined below;
#
#       Group 1 checks - corner captures:
#       -   check each of the four corners if there is any inactive player's piece
#       -   for each of the corner that has inactive player's piece, check if the to_square is adjacent to it
#       -   if the to_square is a square adjacent to a corner that is occupied with inactive player's piece, check if
#           the other square adjacent to the corner has the active player’s piece.
#       If true:
#       -   call the inc_num_captured_pieces method of the self._inactive_player, which will increase the
#           self._captured_pieces by 1, and decrease the self._on_board_pieces by 1,
#       -   remove the piece from the board by calling set_status_matrix() and setting the square to ".".

#       Group 2 checks, horizontal and vertical captures - Checks in each direction (right, left, up, down) one by one:
#       -   Independent of Group 1 checks,
#       -   choses each direction with (right, left, up, left) using for loop
#       -   for each direction independently, checks if;
#       -     there is an inactive player’s piece next to the to_square
#       -     if yes, check one square next, towards the same direction, whether there is any black or red piece
#       -     If there is another inactive player’s piece, repeat checking the next square on the same direction, until
#             either an empty square, or a square with the active player’s piece, or the end of the board is reached,
#             and each time increment a counter representing pieces to capture, while iterating.
#       If in the end, the active player’s piece is reached,
#       -   call inc_num_captured_pieces() method for the inactive player, passing the counter (as pieces to capture
#           from the inactive player), which will increase the self._captured_pieces by counter, and decrease the
#           self._on_board_pieces by counter.
#       -   remove the piece(s) from the board by calling set_status_matrix() and setting the square(s) to ".".
#
#
# 6) Determining when the game has ended
#       After calling the check_and_capture() method (to check if any piece should be captured and capture the required
#       piece(s)), the make_move method will call self._inactive_player.get_on_board_pieces() method to obtain the
#       remaining number of pieces the inactive player has on board, after any potential captures.
#       If the number of pieces on board <= 1;
#           the inactive player has lost, the active player has won. In this case the make_move method will call the
#           self.set_game_state() method, which will set the self._game_state to "BLACK_WON" if the active player is
#           player_black, and will set the self._game_state to "RED_WON" if the active player is player_red, and
#           afterwards the self.set_game_state() method will continue by printing the self._game_state to the screen.
#       If the number of pieces on board > 1;
#           the game continues.
#       In the end, in both cases explained above, the make_move method returns True, meaning that the move could be
#       made without any issue.
#       The make_move method will switch the active player by calling self.set_active_player() method.

