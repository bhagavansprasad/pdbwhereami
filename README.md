# pdbwhereami

## Purpose

This is an utility module which helps in debugging python sources with below functions

* whoami
* whereami
* whocalledme
* calledtree
* whosdaddy

## Where is it used?

This moduled help developers in several key ways, especially when it comes to debugging and maintaining code. Here are the primary benefits:

### 1. **Debugging:**

* **Identifying Errors:** When an error occurs, knowing the exact line number and file can significantly reduce the time spent searching for the cause. By calling these functions in error messages, developers can quickly pinpoint where an issue arose.
* **Traceability:** By logging the line number and file name, developers can trace the execution path of the program, especially when dealing with complex codebases or multi-file projects.

### 2. **Logging:**

* **Detailed Logs:** Including line numbers and file names in log messages provides detailed context, making logs more informative and easier to interpret.
* **Automated Monitoring:** In large systems, automated monitoring tools can use these details to flag specific parts of the code that frequently cause issues, aiding in proactive maintenance.

### 3. **Assertions and Debug Builds:**

* **Assertions:** Using macros like `assert()` along with `whoami`, `whereami`, `whocalledme`, `calledtree` and `whosdaddy` helps in catching logical errors during development. When an assertion fails, it prints the line number and file name, making it easier to debug.
* **Conditional Compilation:** For debug builds, additional diagnostic information can be included using these macros without affecting the release builds.

### 4. **Documentation and Maintenance:**

* **Code Reviews:** During code reviews, having detailed error logs can help reviewers understand the flow and identify potential problem areas more efficiently.
* **Maintenance:** For long-term maintenance, having detailed error reports with line numbers and file names helps new developers understand and fix issues without needing deep familiarity with the entire codebase.

By leveraging `whoami`, `whereami`, `whocalledme`, `calledtree` and `whosdaddy`, developers can create more robust, maintainable, and easier-to-debug code.

## How to use it?

```Py
from pdbwhereami import whoami, whereami, whocalledme, calledtree, whosdaddy

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
```

### output

```text
[debug_utility] ->
[debug_utility] -> I am in test_whoami function

[whereami/main.py:71]:debug_utility ->
[whereami/main.py:72]:debug_utility -> I am in test_whereami
[/home/bhagavan/whereami/main.py:73]:debug_utility ->
[/home/bhagavan/whereami/main.py:74]:debug_utility ->

[whereami/main.py:93]:<module> ->
[/home/bhagavan/whereami/main.py:93]:<module> ->
[/home/bhagavan/whereami/main.py:93]:<module> ->

#1[/home/bhagavan/whereami/main.py:84]:debug_utility <--
#0[/home/bhagavan/whereami/main.py:93]:<module> <--

#1[/home/bhagavan/whereami/main.py:85]:debug_utility <--
#0[/home/bhagavan/whereami/main.py:93]:<module> <--

#0[/home/bhagavan/whereami/main.py:87]:debug_utility <--

#1[/home/bhagavan/whereami/main.py:88]:debug_utility <--
#0[/home/bhagavan/whereami/main.py:93]:<module> <--

[<module>] ->
```
## Installation
### Using pip
```sh
pip install pdbwhereami
```
### Using sources
```sh
git clone https://github.com/bhagavansprasad/pdbwhereami.git
cd pdbwhereami
pip install ./
```
