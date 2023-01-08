import pyglet

width, height = 1080 / 2, 1920 / 2
font_size = 24
side_squares = 8
border = width / 20


def run_chess_mini():
    window = pyglet.window.Window(width=width, height=height)

    label = pyglet.text.Label('Chess Mini', font_name='JetBrains Mono', font_size=font_size, x=window.width // 2,
                              y=window.height - font_size, anchor_x='center', anchor_y='center')

    board_pos = [border, 100]
    square_width = (width - 2 * border) / side_squares

    squares = []
    for x in range(side_squares):
        for y in range(side_squares):
            squares.append(pyglet.shapes.Rectangle(x=board_pos[0] + x * square_width, y=board_pos[1] + y * square_width,
                                                   width=square_width, height=square_width,
                                                   color=(40, 0, 0) if (x + y) % 2 == 0 else (255, 255, 255)))

    @window.event
    def on_draw():
        window.clear()
        label.draw()

        for square in squares:
            square.draw()

    pyglet.app.run()


if __name__ == '__main__':
    run_chess_mini()
