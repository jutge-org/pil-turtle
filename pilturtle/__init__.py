# pil-turtle 💊🐢

from PIL import Image, ImageDraw
import math
from typing import Optional, Any, Union
import atexit


class Vec2D(tuple):
    """
    Class copied from original turtle.py 
    (https://github.com/python/cpython/blob/3.10/Lib/turtle.py)
    """

    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))

    def __add__(self, other):
        return Vec2D(self[0]+other[0], self[1]+other[1])

    def __mul__(self, other):
        if isinstance(other, Vec2D):
            return self[0]*other[0]+self[1]*other[1]
        return Vec2D(self[0]*other, self[1]*other)

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2D(self[0]*other, self[1]*other)
        return NotImplemented

    def __sub__(self, other):
        return Vec2D(self[0]-other[0], self[1]-other[1])

    def __neg__(self):
        return Vec2D(-self[0], -self[1])

    def __abs__(self):
        return math.hypot(*self)

    def rotate(self, angle):
        """rotate self counterclockwise by angle"""
        perp = Vec2D(-self[1], self[0])
        angle = math.radians(angle)
        c, s = math.cos(angle), math.sin(angle)
        return Vec2D(self[0]*c+perp[0]*s, self[1]*c+perp[1]*s)

    def __getnewargs__(self):
        return (self[0], self[1])

    def __repr__(self):
        return "(%.2f,%.2f)" % self


"""
Colors can be given by a string as described in https://pillow.readthedocs.io/en/stable/reference/ImageColor.html
or as an RBG tuple of integers in the 0-255 range. Here are some examples for the orange color:

'Orange'
'#FFA500'
'rgb(255,165,0)'
'hsl(39,100%,150%)'
'hsv(39,100%,100%)'
(255,165,0)
"""

Color = Union[str, tuple[int, int, int]]


class Turtle:

    # horizontal and vertical size of the canvas
    _size: int

    # x and y position
    _xcor: float
    _ycor: float

    # heading
    _heading: float

    # pen size
    _pensize: float

    # pen color
    _pencolor: Color

    # pen down
    _pendown: bool

    # hide/show turtle (we do not show it but maintain its state)
    _isvisible: bool

    # PIL
    _img: Any
    _drw: Any

    def __init__(self, size: int = 500):
        self.reset()

    def __del__(self):
        pass
        # this does not work 😟:
        # self.save()

    def _draw_line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        if self._pendown:
            x1 += self._size/2
            x2 += self._size/2
            y1 += self._size/2
            y2 += self._size/2
            self._drw.line([(x1, y1), (x2, y2)], fill=self._pencolor, width=self._pensize)

    def reset(self, size: int = 500) -> None:
        assert size > 0
        self._size = size
        self._xcor = 0
        self._ycor = 0
        self._heading = 0
        self._pensize = 1
        self._pencolor = 'Black'
        self._pendown = True
        self._isvisible = False
        self.clear()

    def clear(self) -> None:
        # this could better be done by painting a rectangle on the current drawing
        self._img = Image.new('RGB', (self._size, self._size), color='White')
        self._drw = ImageDraw.Draw(self._img)

    def save(self, filename: str = 'output.png') -> None:
        self._img.save(filename)

    def forward(self, distance: float) -> None:
        x = self._xcor + distance * math.cos(math.radians(self._heading))
        y = self._ycor + distance * math.sin(math.radians(self._heading))
        self._draw_line(self._xcor, self._ycor, x, y)
        self._xcor, self._ycor = x, y

    def backward(self, distance: float) -> None:
        self.forward(-distance)

    def right(self, angle: float) -> None:
        self._heading += angle

    def left(self, angle: float) -> None:
        self._heading -= angle

    def goto(self, x: float, y: float) -> None:
        self._draw_line(self._xcor, self._ycor, x, y)
        self._xcor, self._ycor = x, y

    def setx(self, x: float) -> None:
        self._draw_line(self._xcor, self._ycor, x, self._ycor)
        self._xcor = x

    def sety(self, y: float) -> None:
        self._draw_line(self._xcor, self._ycor, self._xcor, y)
        self._ycor = y

    def setheading(self, to_angle: float) -> None:
        self._heading = to_angle

    def home(self) -> None:
        self.goto(0, 0)
        self.setheading(0)

    def pendown(self) -> None:
        self._pendown = True

    def penup(self) -> None:
        self._pendown = False

    def isdown(self) -> bool:
        return self._pendown

    def pensize(self, width: Optional[float] = None) -> float:
        if width is not None:
            assert width >= 0
            self._pensize = width
        return self._pensize

    def pencolor(self, color: Optional[Color] = None) -> Color:
        if color is not None:
            self._pencolor = color
        return self._pencolor

    def hideturtle(self) -> None:
        self._isvisible = False

    def showturtle(self) -> None:
        self._isvisible = True

    def isvisible(self) -> bool:
        return self._isvisible

    def position(self) -> Vec2D:
        return Vec2D(self._xcor, self._ycor)

    def xcor(self) -> float:
        return self._xcor

    def ycor(self) -> float:
        return self._ycor

    def heading(self) -> float:
        return self._heading

    fd = forward
    back = backward
    bk = backward
    rt = right
    lt = left
    setpos = goto
    setposition = goto
    seth = setheading
    pd = pendown
    down = pendown
    pu = penup
    up = penup
    ht = hideturtle
    st = showturtle
    pos = position


#########################################################################
# operations without turtle object
#########################################################################

_default_turtle: Optional[Turtle] = None


def _turtle() -> Turtle:
    global _default_turtle
    if _default_turtle is None:
        _default_turtle = Turtle()
    return _default_turtle


def _save(filename: str = 'output.png') -> None:
    global _default_turtle
    if _default_turtle is not None:
        _default_turtle.save(filename)


def reset(size: int = 500) -> None:
    return _turtle().reset(size)


def forward(distance: float) -> None:
    return _turtle().forward(distance)


def backward(distance: float) -> None:
    return _turtle().backward(distance)


def right(angle: float) -> None:
    return _turtle().right(angle)


def left(angle: float) -> None:
    return _turtle().left(angle)


def goto(x: float, y: float) -> None:
    return _turtle().goto(x, y)


def setx(x: float) -> None:
    return _turtle().setx(x)


def sety(y: float) -> None:
    return _turtle().sety(y)


def setheading(to_angle: float) -> None:
    return _turtle().setheading(to_angle)


def home() -> None:
    return _turtle().home()


def pendown() -> None:
    return _turtle().pendown()


def penup() -> None:
    return _turtle().penup()


def isdown() -> bool:
    return _turtle().isdown()


def pensize(width: Optional[float] = None) -> float:
    return _turtle().pensize(width)


def pencolor(color: Optional[Color] = None) -> Color:
    return _turtle().pencolor(color)


def hideturtle() -> None:
    return _turtle().hideturtle()


def showturtle() -> None:
    return _turtle().showturtle()


def isvisible() -> bool:
    return _turtle().isvisible()


def position() -> Vec2D:
    return _turtle().position()


def xcor() -> float:
    return _turtle().xcor()


def ycor() -> float:
    return _turtle().ycor()


def heading() -> float:
    return _turtle().heading()


def done() -> None:
    pass


fd = forward
back = backward
bk = backward
rt = right
lt = left
setpos = goto
setposition = goto
seth = setheading
pd = pendown
down = pendown
pu = penup
up = penup
ht = hideturtle
st = showturtle
pos = position


#########################################################################
# hack to save image at the end of the program
#########################################################################

atexit.register(lambda: _save())
