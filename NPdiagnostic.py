from NPTree import *

tester=NumPuzz(3, ['B', 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 8, 'B', 4, 7, 6, 5])

tests=list()

def testDirs(test):
    print(test.moves)

def testB(test):
    print(test.B)

def defineMoves(test):
    result=list()
    if test.moves["L"]: result.append(test.left())
    if test.moves["R"]: result.append(test.right())
    if test.moves["U"]: result.append(test.up())
    if test.moves["D"]: result.append(test.down())

    for move in result:
        print(str(move))
        print("B is located at " + str(move.B))
        print("Path to this state is " + str(move.G))
        print("Manhattan distance to goal is " + str(move.H))
        print("Potential moves: " + str(move.moves))
        print("Is the move the goal state? " + str(move.isGoal()))
        print("\n")

    return result

def TestAllSearches(startV, stopV):
    start=NumPuzz(4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'B'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'B'])
    with open('Testing'+str(startV)+'-'+str(stopV)+'.txt', 'w') as f:
        f.write(str(start)+"\n")
        f.close()
    for testnum in range(startV,stopV+1):
        with open('Testing'+str(startV)+'-'+str(stopV)+'.txt', 'a') as f:
            f.write("\nGoal is:\n")
            f.write(start.goalString())
            print("Randomizing for " +str(testnum)+"-move solution...")
            start=Randomize(testnum, start)
            f.write("Testing all searches for randomized "+str(testnum)+"-move solution.\n")
            f.write(str(start))
            print("Testing all searches.\n")
            #print("Testing DFS for "+str(testnum)+"-move.")
            #f.write(search(depthselect, start)[0]+"\n") #Tests standard DFS w/ cycle checking
            print("Testing BFS for "+str(testnum)+"-move.")
            f.write(search(breadthselect, start)[0]+"\n") #Tests standard BFS w/ cycle checking
            print("Testing UCS for "+str(testnum)+"-move.")
            f.write(search(uniformselect, start)[0]+"\n") #Tests uniform cost search w/ cycle checking
            print("Testing DLS for "+str(testnum)+"-move.")
            f.write(search(depthselect, start, depth=testnum)[0]+"\n") #Tests depth-limited search w/ cycle checking
            print("Testing IDS for "+str(testnum)+"-move.")
            f.write(search(depthselect, start, it=True)[0]+"\n") #Tests iterative-deepning with cycle checking
            print("Testing A* for "+str(testnum)+"-move.")
            f.write(search(astarselect, start)[0]+"\n") #Tests A* search with cycle checking
            f.write("Searches for "+str(testnum)+" move solutions complete. Resetting board.\n")
            start.reset()
            f.close()

    print("Testing for " +str(startV)+" through "+str(stopV)+" has been completed.")
    print("Look for a file named 'Testing "+str(startV)+"-"+str(stopV)+".txt' in this program's"+
        " home directory.")