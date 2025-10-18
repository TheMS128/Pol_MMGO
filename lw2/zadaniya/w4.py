x_coords = [9, 1, 9, 11, 8]
y_coords = [17, 10, 18, 5, 8]

M1 = ((x_coords[0] + x_coords[1]) / 2, (y_coords[0] + y_coords[1]) / 2)  # (5.0, 13.5)
M2 = ((x_coords[2] + x_coords[3]) / 2, (y_coords[2] + y_coords[3]) / 2)  # (10.0, 11.5)
M3 = ((x_coords[4] + x_coords[0]) / 2, (y_coords[4] + y_coords[0]) / 2)  # (8.5, 12.5)

sides = [
    ("m1m2", M1, M2),
    ("m2m3", M2, M3),
    ("m3m1", M3, M1)
]


def get_implicit_equation(P1, P2):
    x1, y1 = P1
    x2, y2 = P2

    A = y2 - y1
    B = -(x2 - x1)
    C = x2 * y1 - y2 * x1

    implicit_eq = f"{A}x"
    implicit_eq += f" + {B}y" if B > 0 else f" {B}y"
    implicit_eq += f" + {C} = 0" if C >= 0 else f" {C} = 0"

    return implicit_eq

def get_parametric_equation(P1, P2):
    x0, y0 = P1

    l = P2[0] - P1[0]
    m = P2[1] - P1[1]

    parametric_eq = (
        f"x = {x0:.1f} + {l}t\n"
        f"y = {y0:.1f} + {m}t"
    )
    return parametric_eq

for name, P1, P2 in sides:
    if name == "m1m2":
        x1, y1 = P1
        x2, y2 = P2

        print(f"  (x - {x1:.1f}) / ({x2:.1f} - {x1:.1f}) = (y - {y1:.1f}) / ({y2:.1f} - {y1:.1f})")
        print(f"  (x - {x1:.1f}) / {x2 - x1:.1f} = (y - {y1:.1f}) / {y2 - y1:.1f}")

    implicit = get_implicit_equation(P1, P2)
    parametric = get_parametric_equation(P1, P2)

    print(f"{name}")
    print(f"Неявное уравнение (Ax + By + C = 0):\n  {implicit}")
    print(f"Параметрическое уравнение (x = x0 + lt, y = y0 + mt):\n  {parametric}")
    print('\n\n')