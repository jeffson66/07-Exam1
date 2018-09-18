"""
Exam 1, problem 1.

Authors: David Mutchler, Vibha Alangar, Valerie Galluzzi, Mark Hays,
         Amanda Stouder, their colleagues and PUT_YOUR_NAME_HERE.
"""  # Lin Jiafan.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1a()
    run_test_problem1b()


def run_test_problem1a():
    """ Tests the   problem1a  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem1a  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of problem1a: '
    title += 'red & blue, then black & magenta'
    window = rg.RoseWindow(450, 250, title)

    rectangle = rg.Rectangle(rg.Point(100, 120), rg.Point(200, 170))
    rectangle.outline_color = 'blue'
    square = rg.Square(rg.Point(125, 50), 30)
    square.fill_color = 'red'

    problem1a(rectangle, square, 5, window)
    line = rg.Line(rg.Point(125, 50), rg.Point(150, 120))
    line.thickness = 5
    line.color = 'blue'
    line.attach_to(window)
    window.continue_on_mouse_click()

    rectangle = rg.Rectangle(rg.Point(300, 70), rg.Point(400, 20))
    rectangle.outline_color = 'magenta'
    rectangle.outline_thickness = 5
    square = rg.Square(rg.Point(250, 100), 50)

    problem1a(rectangle, square, 10, window)
    line = rg.Line(rg.Point(350, 20), rg.Point(250, 100))
    line.thickness = 8
    line.color = 'magenta'
    line.attach_to(window)
    window.render()
    window.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of problem1a: yellow & black'
    window = rg.RoseWindow(400, 300, title)

    rectangle = rg.Rectangle(rg.Point(100, 100), rg.Point(50, 250))
    rectangle.outline_color = 'black'
    rectangle.outline_thickness = 5
    square = rg.Square(rg.Point(300, 50), 80)
    square.fill_color = 'yellow'

    problem1a(rectangle, square, 15, window)
    line = rg.Line(rg.Point(70, 100), rg.Point(300, 50))
    line.thickness = 12
    line.color = 'black'
    line.attach_to(window)
    window.render()
    window.close_on_mouse_click()


def problem1a(rectangle, square, thickness, window):
    square.attach_to(window)
    rectangle.attach_to(window)
    window.render()
    window.continue_on_mouse_click()
    thickness
    rg.Point(100, 100)
    rg.Point(50, 250)
    window.render()
    window.continue_on_mouse_click()
    window.render()
    # --------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.  SEE THE PICTURES in the PDF!
    #          Tests have been written for you (above).
    # --------------------------------------------------------------------------


def run_test_problem1b():
    """ Tests the  problem1b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Test 1, followed by Test 2, of problem1b'
    window = rg.RoseWindow(300, 300, title)

    p = rg.Point(60, 50)
    problem1b(p, window, 100, 150, 'pink')
    window.continue_on_mouse_click()

    p = rg.Point(200, 100)
    problem1b(p, window, 200, 100, 'black')
    window.close_on_mouse_click()

    title = 'Test 3 of problem1b'
    window = rg.RoseWindow(300, 200, title)

    p = rg.Point(100, 50)
    problem1b(p, window, 150, 150, 'purple')
    window.close_on_mouse_click()


def problem1b(point, win, width, height, color):
    ellipse = rg.Ellipse(point, width, height)
    ellipse.attach_to(win)
    ellipse.fill_color = color
    win.render()
    win.close_on_mouse_click
    """
    See   problem1b_picture.pdf   in this project for pictures
    that may help you better understand the following specification:
    
    What comes in:
      -- An rg.Point.
      -- An rg.RoseWindow.
      -- Two positive integers.
      -- A string suitable for a color in RoseGraphics.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws an rg.Ellipse for which:
        -- The topmost point of the rg.Ellipse is the given rg.Point.
        -- The width of the rg.Ellipse is the given width.
        -- The height of the rg.Ellipse is the given width.
        -- The fill color of the rg.Ellipse is the given color.
      Must render but   ** NOT close **   the window.

    Type hints:
      :type point:  rg.Point
      :type win:    rg.RoseWindow
      :type width:  int
      :type height: int
      :type color:  str
    """
    # --------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.  SEE THE PICTURES in the PDF!
    #          Tests have been written for you (above).
    # --------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ------------------------------------------------------------------------------
main()
