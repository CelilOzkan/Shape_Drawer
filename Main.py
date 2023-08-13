
input_text = input()

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def dictionary_setter():
    # Firstly we convert input_txt into a list of strings
    list_of_rows = input_text.split(",N,")
    # At this stage we get a dict. of keys with strings like element_list_of_row1, ...2 and so on
    # as many as the number of the rows
    global dictionary_of_rows
    dictionary_of_rows = {}
    for i in range(1, len(list_of_rows) + 1):
        dictionary_of_rows["element_list_of_row{}".format(i)] = list_of_rows[i - 1]

def width_finder_of_shapes(string):  # If the input is "DL", "N" or "B", it will return width of 0
    starting_letter = string[0]
    if starting_letter == "T":
        height = int(string[1: len(string)])
        width = (height * 2) - 1
        return width
    if starting_letter == "V" or starting_letter == "S" or starting_letter == "O":
        width = int(string[1: len(string)])
        return width
    if starting_letter == "E" or starting_letter == "R":
        x_index = string.index("x")
        width = int(string[(x_index + 1): len(string)])
        return width
    else:
        return 0

def width_finder_of_rows(row_string):
    total_width = 0
    list_of_shapes_in_the_row = row_string.split(",")

    dl_counter = list_of_shapes_in_the_row.count("DL")
    n_counter = list_of_shapes_in_the_row.count("N")
    b_counter = list_of_shapes_in_the_row.count("B")

    for i in range(len(list_of_shapes_in_the_row) - 1): # Width coming from the space characters between any two shapes
        total_width += 1
    for i in range(dl_counter + n_counter + b_counter): # To avoid overcounting
        total_width -= 1
    for shape in list_of_shapes_in_the_row: # Width coming from the shapes' own widths
        width = width_finder_of_shapes(shape)
        total_width += width
    return total_width

def max_width_finder():
    max_width = 0
    for row in dictionary_of_rows.values():
        if width_finder_of_rows(row) > max_width:
            max_width = width_finder_of_rows(row)
    return max_width

def height_finder_of_shapes(string): # If the input is "DL", "N" or "B", it will return height of 0
    starting_letter = string[0]
    if starting_letter == "T" or starting_letter == "S":
        height = int(string[1: len(string)])
        return height
    if starting_letter == "V":
        width = int(string[1: len(string)])
        height = int((width + 1) / 2)
        return height
    if starting_letter == "E" or starting_letter == "R":
        x_index = string.index("x")
        height = int(string[1: x_index])
        return height
    else:
        return 0

def max_height_finder_of_rows(row_string):
    list_of_shapes_in_the_row = row_string.split(",")
    row_max_height = 0
    for shape in list_of_shapes_in_the_row:
        if height_finder_of_shapes(shape) > row_max_height:
            row_max_height = height_finder_of_shapes(shape)
    return row_max_height

def square_line_drawer(size, line, height_offset):
    if line <= height_offset:
        print(" " * size, end= " ")
    else:
        print("*" * size, end= " ")

def triange_line_drawer(height, line, height_offset):
    width = height * 2 - 1
    if line <= height_offset:
        print(" " * width, end= " ")
    else:
        line = line - height_offset
        print(" " * (height - line) + "*" * ((line * 2) - 1) + " " * (height - line), end= " ")

def inverted_triangle_line_drawer(width, line, height_offset, max_height):
    if line > max_height - height_offset: # If the shape has been drawn
        print(" " * width, end = " ")
    else:
        print(" " * (line - 1) + "*" * ((width + 2) - (2 * line)) + " " * (line - 1), end = " ")

def rectangle_line_drawer(width, line, height_offset):
    if line <= height_offset:
        print(" " * width, end = " ")
    else:
        print("*" * width, end = " ")

def empty_rectangle_line_drawer(width):
    print(" " * width, end = " ")

def shape_drawer(string, line, height_offset, rows_max_height):
    starting_letter = string[0]
    if starting_letter == "T":
        triange_line_drawer(height_finder_of_shapes(string), line, height_offset)
    if starting_letter == "V":
        inverted_triangle_line_drawer(width_finder_of_shapes(string), line, height_offset, rows_max_height)
    if starting_letter == "S":
        square_line_drawer(width_finder_of_shapes(string), line, height_offset)
    if starting_letter == "E" or starting_letter == "O":
        empty_rectangle_line_drawer(width_finder_of_shapes(string))
    if starting_letter == "R":
        rectangle_line_drawer(width_finder_of_shapes(string), line, height_offset)

def main():

    max_width = max_width_finder()  # Checks all the rows and returns the biggest width

    for row in dictionary_of_rows.values():

        # dictionary_of_rows.values() are something like ['T4,S4,DL,DL,T5', 'E1x4,R3x5,E1x7,T3,E1x4', 'B', 'DL,V3,T7,S3,R5x2']
        # row in the form of "T4,S4,DL,DL,T5"

        shapes_list_of_the_row = row.split(",")

        # shapes_list_of_the_row in the form of ['T4', 'S4', 'DL', 'DL', 'T5']

        rows_width = width_finder_of_rows(row)
        width_offset = int((max_width - rows_width) / 2)  # For any row finds the initial spacing
        rows_max_height = max_height_finder_of_rows(row)  # Works for only this row, not for all the rows

        if "DL" in shapes_list_of_the_row: # Delete all "DL"s in the row, if any exist in a row print dashed line
            print("-" * max_width)
            dl_count = shapes_list_of_the_row.count("DL")
            for i in range(dl_count):
                shapes_list_of_the_row.remove("DL")

        if "B" in shapes_list_of_the_row: # Print blank line as many as the "B" letter
            b_count = shapes_list_of_the_row.count("B")
            for i in range(b_count):
                print()

        for line in range(1, rows_max_height + 1):
            print(" " * width_offset, end= "")
            for row_shapes in shapes_list_of_the_row:
                height_offset = rows_max_height - height_finder_of_shapes(row_shapes)
                shape_drawer(row_shapes, line, height_offset, rows_max_height)
            print()

    print("-" * max_width)

dictionary_setter()
main()


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

