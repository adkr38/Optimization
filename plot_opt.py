import linear_opt
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable,List,Tuple,Dict,Union,Any


def plot_linear_optimization(
        constraints:List[Tuple[Callable[[np.ndarray],np.ndarray],str]],
        solution:Tuple[float,float],
        xlim:Tuple[float,float],
        ylim: Tuple[float,float],
        file_name:str) -> None:

    print(xlim,ylim)
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




def plot_setup(question:Any) -> Dict[str,Union[Tuple[float,float],float,List[Tuple[Callable,str]]]]:
    solution = question.opt()
    constraints =  question.get_plotting_constraints()
    corner_points = question.get_corner_points()
    xmax = 1.1 * max(solution[1],max(map(lambda x:x[0],corner_points)))
    ymax = 1.1 * max(solution[2],max(map(lambda x:x[1],corner_points)))

    return {
            "solution":solution,
            "constraints":constraints,
            "corner_points":corner_points,
            "xmax":xmax,
            "ymax":ymax
            }

def main() -> None:

    setup = plot_setup(linear_opt.Q3)
    print(setup)

    plot_linear_optimization(
            constraints = setup.get("constraints"),
            solution = (setup.get("solution")[1],setup.get("solution")[2]),
            xlim = (0,setup.get("xmax")),
            ylim =(0,setup.get("ymax")),
            file_name ="./images/q3_plot.png"
            )

if __name__ == "__main__":
    main()
