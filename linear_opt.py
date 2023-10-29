import numpy as np
from typing import List, Optional, Tuple
import sympy

# Optimization workbook
# Linear optimization

def q1(array:np.ndarray) -> Tuple[Optional[int],Optional[int]]:
    """
    Find max and min in array
    """

    if not len(array):
        return (None,None)

    current_max,current_min = array[0], array[0]

    for item in array:
        if item >= current_max:
            current_max = item

        if item <= current_min:
            current_min = item

    return (current_max,current_min)

def q2() :
    """
    Maximize Z = 3x + 4y subject to x + y <= 10 and x,y >= 0;
    """
    def objective_func(x:int,y:int) -> float:
        return 3*x + 4*y

    def is_feasible(x:int,y:int):
        return x+y <= 10 and x >=0 and y>= 0

    def opt() -> Tuple[float,int,int]:
        corner_points = [(0,0),(10,0),(0,10)]
        feasible_points = filter(lambda point: is_feasible(*point), corner_points)

        current_res = float("-inf")
        optimal_point_x = None
        optimal_point_y = None

        for x,y in feasible_points:
            res = objective_func(x,y)

            if res >= current_res:
                current_res = res
                optimal_point_x = x
                optimal_point_y = y

        return current_res,optimal_point_x,optimal_point_y


    return opt()

def q3():

    """
    Maximize Z = 2x + 3y subject to:
        x + 2y < 8
        3x + y <= 9
        x,y >= 0
    """


    def objective_function(x:int,y:int) -> float:
        return 2*x + 3*y

    def is_feasible(x:int,y:int) -> bool:
        return x+2*y <= 8 and 3*x + y < 9 and x >= 0 and y >= 0

    def get_corner_points() -> List[Tuple[int,int]]:
        x,y = sympy.symbols("x y")
        eq1 = sympy.Eq(x + 2*y,8)
        eq2 = sympy.Eq(3*x + y,9)
        intersection_point = sympy.solve((eq1,eq2),(x,y))
        intersection_x_axis_1 = sympy.solve(eq1.subs(y, 0), x)
        intersection_x_axis_2 = sympy.solve(eq2.subs(y, 0), x)
        intersection_y_axis_1 = sympy.solve(eq1.subs(x, 0), y)
        intersection_y_axis_2 = sympy.solve(eq2.subs(x, 0), y)

        return [
                (0,0),
                (intersection_x_axis_1[0],0),
                (intersection_x_axis_2[0],0),
                (0,intersection_y_axis_1[0]),
                (0,intersection_y_axis_2[0]),
                (intersection_point[x], intersection_point[y])
                ]

    def opt() -> Tuple[float,int,int]:
        corner_points = get_corner_points()
        feasible_points = filter(lambda x: is_feasible(*x),corner_points)
        current_res = float('-inf')
        optimal_point_x = None
        optimal_point_y = None

        for x, y in feasible_points:
            res = objective_function(x, y)
            if res > current_res:
                current_res = res
                optimal_point_x = x
                optimal_point_y = y

        return current_res, optimal_point_x, optimal_point_y

    return opt()


if __name__ == "__main__":
    print(q3())
