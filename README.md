# PIL Turtle

This module tries to emulate the standard `turtle` module on top of PIL, the Python Imaging Library.

# Demo

The output of this program

```python
from pilturtle import *

for i in range(8):
    circle(100)
    right(45)
dot(10, 'red')

done()
```

is a file `output.png` with this image:

![demo.png](demo.png)


# Important differences

`pilturtle` tries to emulate the standard `turtle`, but some differences exist:

- `pilturtle` does not work interactively. 

    There is no window and you cannot see the turtle moving.
    
    The image file is created with the `done()` operation. 

- Colors are specified in a slightly different way: Colors can be given by a string as described in https://pillow.readthedocs.io/en/stable/reference/ImageColor.html
or as an RBG tuple of integers in the 0-255 range. Here are some examples for the orange color:

    - `'Orange'`
    - `'#FFA500'`
    - `'rgb(255,165,0)'`
    - `'hsl(39,100%,150%)'`
    - `'hsv(39,100%,100%)'`
    - `(255,165,0)`

- Fillings are not implemented.

- The `pilturtle` offers type annotations.


# Operations

The following turtle operations have been implemented and behave as in the standard `turtle`, unless noted.

- `forward() | fd()`
- `backward() | bk() | back()`
- `right() | rt()`
- `left() | lt()`
- `goto() | setpos() | setposition()`
- `setx()`
- `sety()`
- `setheading() | seth()`
- `home()`
- `circle()`
- `dot()`
- `stamp()` ❌
- `clearstamp()` ❌
- `clearstamps()` ❌
- `undo()` ❌
- `speed()`

- `position() | pos()`
- `towards()` ⚒️
- `xcor()`
- `ycor()`
- `heading()`
- `distance()` ⚒️

- `degrees()` ⚒️
- `radians()` ⚒️

- `pendown() | pd() | down()`
- `penup() | pu() | up()`
- `pensize() | width()`
- `pen()`
- `isdown()`

- `color()`
- `pencolor()`
- `fillcolor()`

- `filling()` ❌
- `begin_fill()` ❌
- `end_fill()` ❌

- `reset()`
- `clear()`
- `write()` ⚒️

- `showturtle() | st()`
- `hideturtle() | ht()`
- `isvisible()`


- `window_height()`
- `window_width()`

- `done()`: saves the image. By default uses the `output.png` filename but you can provide your own filename.


# Credits

- [Jordi Petit](https://github.com/jordi-petit/)

Copyright 2022, Universitat Politècnica de Catalunya