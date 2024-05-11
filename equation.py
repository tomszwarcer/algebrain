import side

class Equation:
    def __init__(self, content):
        self.content = content
        #separate eqn into sides
        self.lhs = side.Side(content.split(" = ")[0])
        self.rhs = side.Side(content.split(" = ")[1])

        #generate total blocks list
        self.all_blocks = [] 
        self.combine_blocks()
    
    def combine_blocks(self):
        self.all_blocks = self.lhs.blocks + self.rhs.blocks

    def update(self):
        # updates the written form of equation (for use with SymPy)
        self.content = self.lhs.content + " = " + self.rhs.content
        self.all_blocks = self.lhs.blocks + self.rhs.blocks