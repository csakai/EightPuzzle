class NPnode:
    
    def __init__(self, numpuzz, name):
        self.data=numpuzz
        self.name=name
        self.left=None
        self.right=None
        self.up=None
        self.down=None

    def next(self):
        if self.data.moves["L"]: self.left=NPnode(self.data.left(), self.name+", L")
        if self.data.moves["U"]: self.up=NPnode(self.data.up(), self.name+", U")
        if self.data.moves["D"]: self.down=NPnode(self.data.down(), self.name+", D")
        if self.data.moves["R"]: self.right=NPnode(self.data.right(), self.name+", R")

    def isGoal(self):
        return self.data.isGoal()
        
    # a note: These comparison operators are for comparing HEURISTICS, not actual state.
    def __lt__(self, other):
        if isinstance(other, NPnode):
            return self.data<other.data
        else: return NotImplemented

    def __le__(self, other):
        if isinstance(other, NPnode):
            return self.data<=other.data
        else: return NotImplemented

    def __eq__(self, other):
        if isinstance(other, NPnode):
            return self.data==other.data
        else: return NotImplemented

    def __ne__(self, other):
        if isinstance(other, NPnode):
            return self.data!=other.data
        else: return NotImplemented

    def __ge__(self, other):
        if isinstance(other, NPnode):
            return self.data>=other.data
        else: return NotImplemented

    def __gt__(self, other):
        if isinstance(other, NPnode):
            return self.data>other.data
        else: return NotImplemented

    def __str__(self):
        return self.name+"\n"+str(self.data)