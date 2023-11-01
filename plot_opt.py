import linear_opt
import nonlinear_opt
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable,List,Tuple,Dict,Union,Any,Optional
import inspect


def plot_nonlinear_optimization(
        constraints:List[Tuple[Callable[[np.ndarray,np.ndarray],np.ndarray],str]],
        solution:Tuple[float,float],
        xlim:Tuple[float,float],
        ylim: Tuple[float,float],
        file_name:str) -> None:

        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111,projection= "3d")
        x,y = np.linspace(xlim[0],xlim[1],100), np.linspace(ylim[0],ylim[1],100)

        # Here we're meshing x and y to represent all coordinates where x and y could intersect
        ## when you do np.repeat(x[:,np.newaxis],len(y),axis=0) I'm saying, create a new row vector, creating a new col per value
        ## when you do np.repeat(x[np.newaxis,:],len(x),axis=1) I'm saying, create a new column vector, creating a new row per value
        X,Y = np.repeat(x[np.newaxis,:],len(y),axis=0), np.repeat(y[:,np.newaxis],len(x),axis=1)

        for constraint_callable,description in constraints:
            Z = constraint_callable(X,Y)

        return

def plot_linear_optimization(
        constraints:List[Tuple[Callable[[np.ndarray],np.ndarray],str]],
        solution:Tuple[float,float],
        xlim:Tuple[float,float],
        ylim: Tuple[float,float],
        file_name:str) -> None:

    fig, ax = plt.subplots(figsize=(6,6))
    x = np.linspace(xlim[0],xlim[1],400)

    for constraint,label in constraints:
        y = constraint(x)
        ax.fill_between(x,ylim[0],y,alpha = 0.3,color="gray")
        ax.plot(x,y,label=label)

    ax.plot(*solution,"ro")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.savefig(file_name)




def plot_setup(question:Any) -> Dict[str,Optional[Union[Tuple[float,float],float,List[Tuple[Callable,str]]]]]:
    solution = question.opt()
    constraints =  question.get_plotting_constraints()
    corner_points = question.get_corner_points() if hasattr(question,"get_corner_points") else None
    xmax = 1.1 * max(solution[1],max(map(lambda x:x[0],corner_points))) if corner_points else 1.1 * solution[1]
    ymax = 1.1 * max(solution[2],max(map(lambda x:x[1],corner_points))) if corner_points else 1.1* solution[2]

    return {
            "solution":solution,
            "constraints":constraints,
            "corner_points":corner_points,
            "xmax":xmax,
            "ymax":ymax
            }

def main() -> None:

    setup = plot_setup(nonlinear_opt.Q1)

    plot_linear_optimization(
            constraints = setup.get("constraints"),
            solution = (setup.get("solution")[1],setup.get("solution")[2]),
            xlim = (0,setup.get("xmax")),
            ylim =(0,setup.get("ymax")),
            file_name ="./images/nonlin_q1.png"
            )

if __name__ == "__main__":
    main()
