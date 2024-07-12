import datetime
import json
import sys
import inspect

def whereami(msg=""):
    data = inspect.stack()
    myself = data[1]

    return(f"[{myself[1]}:{myself[2]}]:{myself[3]} ->{msg}")

def whocalledme():
    data = inspect.stack()
    parent = data[2]

    return(f"[{parent[1]}:{parent[2]}]:{parent[3]} ->")

def calledtree(tree_depth=3, verbose=False):
    data = inspect.stack()
    tree = ""
    
    stack_len = len(data)
    
    if (verbose):
        print(f"stack_len :{stack_len}")
        
    for (i, sf) in enumerate(data):
        if (i == 0):
            continue
        if (i > tree_depth):
            break
        tree = tree + f"#{tree_depth-i}[{data[i][1]}:{data[i][2]}]:{data[i][3]} <-- \n"

    return tree

def whoami():
    return inspect.stack()[1][3]

def whosdaddy():
    return inspect.stack()[2][3]

def factorial():
    print("I am in factorial")
    print(f"whoami      :{whoami()}")
    print(f"whereami    :{whereami()}")
    print(f"whereami    :{whereami('Hello')}")
    print(f"whocalledme :{whocalledme()}")
    print(f"calledtree  :\n{calledtree()}")

def test1():
    factorial()

def main():
    # utility_fun()
    print(f"whoami      :{whoami()}")
    print(f"whereami    :{whereami()}")
    print(f"whereami    :{whereami('Hello')}")
    print(f"whocalledme :{whocalledme()}")
    print(f"calledtree  :\n{calledtree()}")
    test1()
    return

if (__name__ == "__main__"):
    main()
