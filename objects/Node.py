from typing import Type


class TreeNode:
    __slots__ = "Childs", "Value", "Parent"
    
    def __init__(self, Value) -> None:
        self.Childs = []
        self.Value = Value
        self.Parent = None

    def AddChild(self, Child):
        Child.Parent = self
        self.Childs.append(Child)


class TreeExplorer:
    def __init__(self, root) -> None:
        self.Current = root
    
    def __getitem__(self, key):
        if Type(key) is not int:
            raise TypeError("Expected int, not "+str(Type(key)) + " while trying to access tree's child indexes")
        return self.Current.Childs[key]

    def GetItemByValue(self, value):
        for child in self.Current.Childs:
            if (value.strip().lower() == child.Value.strip().lower()):
                return child
    
    def GoUp(self):
        """Go up of one node and return the current node"""
        if self.Current.Parent is not None:
            self.Current = self.Current.Parent
        else:
            raise Exception("Try to access root parent")
        
    def ListValues(self):
        """Makes a list of differents child"""
        res = []
        for child in self.Current.Childs:
            res.append(child.Value)
        return res

    def ListPath(self):
        """Generate a pile of the path of used value from root to current node"""
        c = self.Current
        res = []
        while c.Parent is not None:
            res.append(c.Value)
            c = c.Parent
        return res.reverse()

    def GoTo(self, value):
        c = False
        for child in self.Current.Childs:
            if (value.strip().lower() == child.Value.strip().lower()):
                c = True
                self.Current = child

        if not c:
            raise Exception("Value not found, could not move")
        return self.Current

    @property
    def CanGoLower(self):
        return len(self.ListValues()) != 0

    @property
    def CanGoUpper(self):
        return self.Current.Parent != None