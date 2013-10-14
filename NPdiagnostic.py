from numpuzz import NumPuzz

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
