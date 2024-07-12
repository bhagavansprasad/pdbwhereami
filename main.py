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
