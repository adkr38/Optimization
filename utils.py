from typing import Callable,Any
import time

def timer(func:Callable[...,Any])  -> Callable[...,Any]:

    def wrapper(*args,**kwargs) -> Any:
        now = time.time()
        result = func(*args,**kwargs)
        elapsed = time.time() - now
        print(func.__name__, " took ",round(elapsed,6), " seconds.")
        return result

    return wrapper
