import unittest
import numpy as np
from typing import Tuple,List
import utils


class TestMeshGrid(unittest.TestCase):

    @utils.timer
    def custom_meshGrid(self,x:np.ndarray,y:np.ndarray) -> Tuple[np.ndarray,np.ndarray]:
        x_2d = np.array(list(map(lambda _: x,range(y.shape[0])))) # Repeat entire x for each y elem
        y_2d = np.array(list(map(lambda y_new: [y_new] * x.shape[0] , y)))
        return x_2d, y_2d

    @utils.timer
    def custom_numpy_meshGrid(self,x:np.ndarray,y:np.ndarray) -> Tuple[np.ndarray,np.ndarray]:
        x_2d = np.repeat(x[np.newaxis,:],len(y),axis=0)
        y_2d = np.repeat(y[:,np.newaxis],len(x),axis=1)
        return x_2d, y_2d

    @utils.timer
    def original_meshgrid(self,x:np.ndarray,y:np.ndarray) -> List[np.ndarray]:
        return np.meshgrid(x,y)

    def test_meshFormula(self):
        x,y = np.random.randn(1000), np.random.randn(1000)
        X,Y = self.original_meshgrid(x,y)
        cX, cY = self.custom_numpy_meshGrid(x,y)
        assert (np.array_equal(X,cX)) & (np.array_equal(Y,cY))




if __name__ == "__main__":
    unittest.main()
