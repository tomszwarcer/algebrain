#TODO: add update() to update from content
#TODO: make blocks compatible with brackets

class Block():
    def __init__(self, sign, content):
        self.sign = sign
        self.content = content
        self.coeff = ""
        self.alg = ""
        self.get_coeff()
        self.bracketed = False
        self.is_bracketed()

    def get_coeff(self):
        #case of single factor:
        if "*" not in self.content:
            try:
                float(self.content)
            except:
                self.alg = self.content
                self.coeff = ""
            else:
                self.alg = ""
                self.coeff = self.content 
        else:
            #choose everything before 1st star:
            self.coeff = self.content[:self.content.index("*")]
            self.alg = self.content[self.content.index("*")+1:]

    def str_to_block(input):
    #converts str into Block object
        if input[0] == "-":
            sign = "-"
            input = input[1:]
        else:
            sign = "+"
        result = Block(sign,input)
        return result
            
    def blocks_to_str(block_list):
        #block_list is a list of block objects
        result_list = []
        for i in block_list:
            result_list.append(i.sign)
            result_list.append(i.content)
        #remove 1st sign if plus:
        if result_list[0] == "+":
            del result_list[0] 
        #make str:    
        result = " ".join(result_list)
        return result
    
    def is_bracketed(self):
        for char in self.content:
            if char == "(":
                self.bracketed = True
                break

    def flip_sign(self):
        if self.sign == "-":
            self.sign = "+"
        else:
            self.sign = "-"

