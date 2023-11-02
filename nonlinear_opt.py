import sympy
import numpy as np
from typing import Callable, List, Optional,Tuple


class Q1():
    """
    Maximize Z = x**2 + y**2
    subject to the constraint x**2 + y**2 <= 10;
    Steps:
        ```
            1 - Define the objective func
            2 - Define the constaint
            3 - Find the corner points
            4 - Evaluate the objective func at the corner points to find the max
        ```
    """

    @staticmethod
    def objective_function(x:float,y:float) -> float:
        return x**2 + y **2


    @staticmethod
    def get_plotting_constraints() -> List[Tuple[Callable[[float,float],float],str]]:
        return [
                (lambda x,y: 10 -  x**2+y**2,"x**2 + y**2 <= 10")
                ]

    @staticmethod
    def get_constraints() -> List[Tuple[Callable[[float,float],bool],str]]:
        return [
                (lambda x,y: x**2+y**2 <= 10,"x**2 + y**2 <= 10")
                ]

    @staticmethod
    def get_feasible_points() -> List[Tuple[float,float]]:
        feasible_points = list()
        constraints = Q1.get_constraints()
        for x in range(-10,11):
            for y in range(-10,11):
                if all(list(map(lambda constraint: constraint[0](x,y),constraints))):
                    feasible_points.append((x,y))

        return feasible_points

    @staticmethod
    def opt() -> Tuple[float,float,float]:
        feasible_points, objective_func = Q1.get_feasible_points(), Q1.objective_function
        max_res,best_x,best_y = objective_func(feasible_points[0][0],feasible_points[0][1]),feasible_points[0][0],feasible_points[0][1]
        for x,y in feasible_points[1:]:
            result = objective_func(x,y)
            if result >= max_res:
                max_res = result
                best_x = x
                best_y = y

        return (max_res,best_x,best_y)

