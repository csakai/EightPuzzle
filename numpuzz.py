class NumPuzz:
    #notes for instantiation: size is to be the dimension of the puzzle ie a 3x3 simply
    # calls for an input of 3. Order is an array for representing the state of the puzzle
    # I am trusting for now that one using this would give proper inputs as opposed to
    # trying to break my code. prev is a string to indicate which direction 
    # the past move was from i.e. "L" to indicate the last shift was a right
    # to indicate that one should not move backwards, thus negating the previous move.
    # prevdist is for using the heuristics, so this would be the combined weight of edges
    # traversed in the search tree to reach the curren state.
    # goal is a list to represent the goal state of the puzzle.
    # for cost purposes: self.F=total cost to get to this state,
    #   self.G=Manhatta Distance to Goal State from curren state, self.H=Total Heuristic Value (F+G)
    def __init__(self, size, order=['B'], goal=None, prev=None, prevdist=-1):
        self.size=size**2
        self.bound=size
        self.F=prevdist+1
        if len(order)!=self.size or order==['B']:
            self.order=['B'].extend([n for n in range(1,self.size)])
        else:
            self.order=order
        self.B=self.order.index('B')
        self.moves={"L": True, "U": True, "D": True, "R": True}
        self.possibleMoves()
        if prev: self.moves[prev]=False
        if goal:
            self.goal=goal
            self.manhattanDistance()
            self.H=self.F+self.G
        else:
            self.goal=None

    def possibleMoves(self): #the direction denoted is the direction that a piece would slide into the blank spot.
        if self.B%self.bound==0: self.moves["R"]=False
        if self.B<self.bound: self.moves["D"]=False
        if (self.B+1)%self.bound==0: self.moves["L"]=False
        if self.B//self.bound==self.bound-1: self.moves["U"]=False

# a note: These comparison operators are for comparing HEURISTICS, not actual state.
    def __lt__(self, other):
        if isinstance(other, NumPuzz):
            return self.H<other.H
        else: return NotImplemented

    def __le__(self, other):
        if isinstance(other, NumPuzz):
            return self.H<=other.H
        else: return NotImplemented

    def __eq__(self, other):
        if isinstance(other, NumPuzz):
            return self.H==other.H
        else: return NotImplemented

    def __ne__(self, other):
        if isinstance(other, NumPuzz):
            return self.H!=other.H
        else: return NotImplemented

    def __ge__(self, other):
        if isinstance(other, NumPuzz):
            return self.H>=other.H
        else: return NotImplemented

    def __gt__(self, other):
        if isinstance(other, NumPuzz):
            return self.H>other.H
        else: return NotImplemented


    def left(self):
        leftorder=self.order.copy()
        leftorder[self.B]=self.order[self.B+1]
        leftorder[self.B+1]='B'
        return NumPuzz(self.bound, leftorder, self.goal, "R", self.F)

    def right(self):
        rightorder=self.order.copy()
        rightorder[self.B]=self.order[self.B-1]
        rightorder[self.B-1]='B'
        return NumPuzz(self.bound, rightorder, self.goal, "L", self.F)

    def up(self):
        uporder=self.order.copy()
        uporder[self.B]=self.order[self.B+self.bound]
        uporder[self.B+self.bound]='B'
        return NumPuzz(self.bound, uporder, self.goal, "D", self.F)

    def down(self):
        downorder=self.order.copy()
        downorder[self.B]=self.order[self.B-self.bound]
        downorder[self.B-self.bound]='B'
        return NumPuzz(self.bound, downorder, self.goal, "U", self.F)

    def __str__(puzzle):
        s=str(puzzle.size-1)
        s+=("-Puzzle\n")
        s+='| '
        for n in range(puzzle.size):
            if puzzle.order[n]=='B' or puzzle.order[n]<10:
                s+=' '
            s+=str(puzzle.order[n])
            s+=' | '
            if (n+1)%puzzle.bound==0:
                if (n+1)<puzzle.size:
                    s+="\n| "
                else:
                    s+="\n"
        return s

    def goalString(self):
        s=str(self.size-1)
        s+=("-Puzzle Goal\n")
        s+='| '
        for n in range(self.size):
            if self.goal[n]=='B' or self.goal[n]<10:
                s+=' '
            s+=str(self.goal[n])
            s+=' | '
            if (n+1)%self.bound==0:
                if (n+1)<self.size:
                    s+="\n| "
                else:
                    s+="\n"
        return s

    def printGoal(self):
        s=str(self.size-1)
        s+=("-Puzzle Goal\n")
        s+='| '
        for n in range(self.size):
            if self.goal[n]=='B' or self.goal[n]<10:
                s+=' '
            s+=str(self.goal[n])
            s+=' | '
            if (n+1)%self.bound==0:
                if (n+1)<self.size:
                    s+="\n| "
                else:
                    s+="\n"
        print(s)

    # def validate(self):
    #     errors=dict()
    #     if self.order.count('B')!=1:
    #         errors.append('B':self.order.count('B'))
    #     for n in range(self.size):
    #         if self.order.count(n):
    #             errors.append(n:self.order.count(n))
    #     if errors is not empty:
    #         self.fix(errors)

    # def fix(errors):
    #     while errors is not empty:

    def manhattanDistance(self):
        self.G=0
        for n in range(len(self.order)):
            if self.order[n]!='B':
                self.G+=abs(self.vDist(n, self.goal.index(self.order[n])))
                self.G+=abs(self.hDist(n, self.goal.index(self.order[n])))

    def vDist(self, n, m):
        return (n//self.bound)-(m//self.bound)
    
    def hDist(self, n,m):
        return (n%self.bound)-(m%self.bound)
    
    def isGoal(self):
        return self.order==self.goal

    def reset(self):
        self.order=self.goal.copy()
        self.F=0
        self.B=self.order.index('B')
        self.moves={"L": True, "U": True, "D": True, "R": True}
        self.possibleMoves()
        self.manhattanDistance()
        self.H=self.F+self.G