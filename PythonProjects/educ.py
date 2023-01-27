import turtle as T


def cells(side):
    T.penup()
    T.forward(side)
    T.pendown()
    for _ in range(6):
        T.forward(side)
        T.left(60)
    T.right(120)
    for _ in range(6):
        T.forward(side)
        T.left(60)
    T.forward(side)
    T.right(60)
    for _ in range(6):
        T.forward(side)
        T.left(60)
    T.forward(side)
    T.right(60)
    for _ in range(6):
        T.forward(side)
        T.left(60)
    T.forward(side)
    T.right(60)
    for _ in range(6):
        T.forward(side)
        T.left(60)
    T.forward(side)
    T.right(60)
    for _ in range(6):
        T.forward(side)
        T.left(60)
    T.penup()
    T.home()


cells(50)

T.done
