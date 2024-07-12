# whereami (Python Module)

## Purpose
This is an utility module which helps in debugging python sources.

## Where is it used?
As part of debugging manier times developers wants to print the 'line number' and 'function name' which is under execution.
I have not found any function which provides the above functionality.

## How to use it?
``` Py {.numberLines .lineAnchors}
from whereami import whoami, whereami, whocalledme, calledtree

def factorial():
    print("I am in factorial")
    print(f"whoami      :{whoami()}")
    print(f"whereami    :{whereami()}")
    print(f"whereami    :{whereami('Hello')}")
    print(f"whocalledme :{whocalledme()}")

    print()
    print(f"calledtree  :\n{calledtree()}")

def test1():
    factorial()

def main():
    test1()

if (__name__ == "__main__"):
    main()
```

### output
```text
I am in factorial
whoami      :factorial
whereami    :[/home/bhagavan/whereami/main.py:6]:factorial ->
whereami    :[/home/bhagavan/whereami/main.py:7]:factorial ->Hello
whocalledme :[/home/bhagavan/whereami/main.py:14]:test1 ->

calledtree  :
#2[/home/bhagavan/whereami/main.py:11]:factorial <--
#1[/home/bhagavan/whereami/main.py:14]:test1 <--
#0[/home/bhagavan/whereami/main.py:17]:main <--
```