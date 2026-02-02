 # --------------------------------------------------------
    # Get terminal size (used for relative layouts)
    # h = terminal rows
    # w = terminal columns
    # --------------------------------------------------------
    h, w = stdscr.getmaxyx()

    # ========================================================
    # TOP ROW - Options To Send / Receive File
    # ========================================================

    # Send window
    # newwin(height, width, start_y, start_x)
    #
    # HOW TO ADJUST:
    #   - height: change 3
    #   - width : change 20
    #   - move  : change start_y (1) or start_x (2)
    Send = curses.newwin(
        3,      # height
        20,     # width
        1,      # y position (row)
        2       # x position (column)
    )
    draw_box(Send, "Send")

    # Receive window
    Receive = curses.newwin(
        3,      # height
        20,     # width
        1,      # y
        24      # x
    )
    draw_box(Receive, "Receive")

    # ========================================================
    # SECOND ROW - Navigation / File Browsing
    # ========================================================

    FileLocation = curses.newwin(
        3,      # height
        50,     # width
        5,      # y
        2       # x
    )
    draw_box(FileLocation, "FileLocation")

    temp4 = curses.newwin(
        3,      # height
        15,     # width
        5,      # y
        54      # x
    )
    draw_box(temp4, "Temp4")

    # ========================================================
    # MAIN CONTAINER (large bordered area)
    #
    # This box scales with terminal size
    # ========================================================

    container_height = h - 10   # CHANGE padding from bottom
    container_width  = w - 4    # CHANGE side padding

    container = curses.newwin(
        container_height,
        container_width,
        9,      # start below top sections
        2
    )
    draw_box(container, "Container")

    # ========================================================
    # INSIDE CONTAINER (top row inside)
    # ========================================================

    temp5 = curses.newwin(
        3,      # height
        12,     # width
        11,     # y (inside container area)
        4       # x
    )
    draw_box(temp5, "Temp5")

    temp6 = curses.newwin(
        3,
        w - 26, # spans most of container width
        11,
        18
    )
    draw_box(temp6, "Temp6")

    temp7 = curses.newwin(
        3,
        12,
        11,
        w - 16  # right-aligned
    )
    draw_box(temp7, "Temp7")

    # ========================================================
    # LARGE BOTTOM BOX
    # ========================================================

    temp8 = curses.newwin(
        h - 16, # height grows with terminal
        w - 8,  # width grows with terminal
        15,     # y
        4       # x
    )
    draw_box(temp8, "Temp8")

    # ========================================================
    # WAIT FOR KEY PRESS (prevents exit)
    # ========================================================
    stdscr.getch()


# ------------------------------------------------------------
# Safely start curses
# ------------------------------------------------------------
curses.wrapper(main
