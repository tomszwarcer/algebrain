import block

class Expression():
    def __init__(self, content):
        #define expression content for later use in sympify
        self.content = content

        #initialise other attributes
        self.blocks = []
        self.create_blocks_signs()

    def create_blocks_signs(self):
        #add space after 1st minus:
        if self.content[0] == "-" and self.content[1] != " ":
            self.content = "- " + self.content[1:]

        #create combined blocks and signs: (signs removed later)
        blocks_temp = self.content.split(" ")

        #special behaviour for 1st element:
        #if no sign on 1st element, default to plus
        if blocks_temp[0] != "-" and blocks_temp[0] != "+":
            blocks_temp.insert(0, "+")

        #pre-populate self.blocks to avoid index error:
        self.blocks = [None] * int(len(blocks_temp)/2)

        #assign signs and content to self.block elements:
        for i in range(1,len(blocks_temp),2):
            self.blocks[int((i-1)/2)] = block.Block(blocks_temp[i-1], blocks_temp[i])

    def update(self):
        #update content from blocks.
        #construct content from blocks using signs:
        content_temp = []
        for index in range(len(self.blocks)):
            content_temp.append(self.blocks[index].sign)
            content_temp.append(self.blocks[index].content)
        
        #case of an empty expression (all blocks were removed):
        if len(content_temp) == 0:
            self.content = "0"
        #remove any +'s from the start:
        else:
            if content_temp[0] == "+":
                del content_temp[0]
            self.content = " ".join(content_temp)