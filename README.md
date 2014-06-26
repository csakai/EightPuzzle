The Eight Puzzle in Python
Hi, if you're checking this out, this is a really simple implementation of the '8-puzzle' using
AI search algorithms such as Depth-First, Breadth-First, and A* Search. As of right now,
October 13, 2013, I have not implemented cycle checking on Depth-First Search, and as a result,
it will run wild very quickly if used.
A* search works pretty well, I am using the Manhattan Distance heuristic.
Breadth-First Search has been tested minimally.
This set of python modules was a test to see how much I have learned with Python and how well
I can use it.
Feel free to check it out and check back for updates!
-Chris Sakai

October 16: made the code more "pythonic" by defining one search function and instead passing the
selection type as a function to the "search" function.
A word of warning: If iterative deepning is used and there is no possible solution, the program will enter
into an infinite loop.

If you want to test the search functions, refer to NPdiagnostic.py and use the
"TestAllSearches(startV, stopV)" on line 31. It will write its results to a .txt file.

June 26, 2014: I should have mentioned in the readme that this was built using Python 3.3.2. It will not work
in Python 2.7 because Python 2.7's implementation of list does not have a copy function. I will be refactoring
this when I have time so that it can work on Python 2.7 since that is what I'm currently using.
