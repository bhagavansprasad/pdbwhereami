from whereami import whoami, whereami, whocalledme, calledtree, whosdaddy

def test_whoami():
    whoami()
    
    tstr = whoami(verbose=False)
    print(tstr)

    whoami("I am in test_whoami function")

def test_whereami():
    whereami()
    
    whereami("I am in test_whereami")
    
    tstr = whereami(verbose=False)
    print(tstr)

    whereami(obsolete_path = True)
    whereami(path_depth=1)
    whereami(path_depth=2)
    whereami(path_depth=3)
    whereami(path_depth=4)
    whereami(path_depth=5)
    whereami(path_depth=6)

def test_whocalledme():
    whocalledme()
    
    tstr = whocalledme(verbose=False)
    print(tstr)

    whocalledme(obsolete_path = True)
    whocalledme(path_depth=1)
    whocalledme(path_depth=2)
    whocalledme(path_depth=3)
    whocalledme(path_depth=4)
    whocalledme(path_depth=5)
    whocalledme(path_depth=6)
    pass
 
def test_calledtree():
    calledtree()
    
    tstr = calledtree(verbose=False)
    print(tstr)

    calledtree(tree_depth=1)
    calledtree(tree_depth=2)
    calledtree(tree_depth=3)
    calledtree(tree_depth=4)
    calledtree(tree_depth=5)
    calledtree(tree_depth=6)

def test_whosdaddy():
    whosdaddy()
    
    tstr = whosdaddy(versbose=False)
    print(tstr)

    whosdaddy("I am in test_whosdaddy")

from whereami import whoami, whereami, whocalledme, calledtree, whosdaddy

def debug_utility():
    whoami()
    whoami("I am in test_whoami function")

    print()
    
    whereami()
    whereami("I am in test_whereami")
    whereami(obsolete_path = True)
    whereami(path_depth=6)

    print()

    whocalledme()
    whocalledme(obsolete_path = True)
    whocalledme(path_depth=6)

    print()

    calledtree()
    tstr = calledtree(verbose=False)
    print(tstr)
    calledtree(tree_depth=1)
    calledtree(tree_depth=2)

    print()
    whosdaddy()
    
debug_utility()

def main():
    test_whereami()
    test_whoami()
    test_whocalledme()
    test_calledtree()
    test_whosdaddy()


if (__name__ == "__main__"):
    # main()
    pass
