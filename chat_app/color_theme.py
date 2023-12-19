THEME = "light"
CANVAS = "#21252b"
BACKGROUND = "#282c34"
BUTTON = "#323844"
HOVER = "#4d78cc"
TEXT = "#FFFFFF"


def change_theme(self):
    global THEME, CANVAS, BACKGROUND, BUTTON, HOVER, TEXT
    if THEME == "dark":
        THEME = "light"
        CANVAS = "#21252b"
        BACKGROUND = "#282c34"
        BUTTON = "#323844"
        HOVER = "#4d78cc"
        TEXT = "#FFFFFF"
    elif THEME == "light":
        THEME = "dark"
        CANVAS = "red"
        BACKGROUND = "yellow"
        BUTTON = "orange"
        HOVER = "white"
        TEXT = "#FFFFFF"
