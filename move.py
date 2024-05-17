#TODO: better system than labelling subj side "lhs" or "rhs".
#could make this wayyy more efficient (but I am short on time)

import sympy as sp
import block

def get_subj_block(eq,subject):
    for element in eq.lhs.blocks:
        if subject in element.content:
            return element, "lhs"
    for element in eq.rhs.blocks:
        if subject in element.content:
            return element, "rhs"

def is_subject_isolated(eq, subj_side):
    if subj_side == "lhs":
        if len(eq.lhs.blocks) == 1:
            return True
        else:
            return False
    else:
        if len(eq.rhs.blocks) == 1:
            return True
        else:
            return False

def is_subject_last(eq, subj_side, subj_block):
    if subj_side == "lhs":
        if subj_block == eq.lhs.blocks[-1]:
            return True
        else:
            return False
    else:
        if subj_block == eq.rhs.blocks[-1]:
            return True
        else:
            return False


def move(eq, subject):
    subj_block, subj_side = get_subj_block(eq,subject)
    if subj_block.sign == "-":
        if subj_side == "lhs":
            eq.lhs.blocks.remove(subj_block)
            subj_block.sign = "+"
            eq.rhs.blocks.append(subj_block)

            #record change in side
            subj_side = "rhs"

            #update:
            eq.lhs.update()
            eq.rhs.update()
            eq.update()
            
            return eq, subj_side, subj_block
        else:
            eq.rhs.blocks.remove(subj_block)
            subj_block.sign = "+"
            eq.lhs.blocks.append(subj_block)

            #record change in side
            subj_side = "lhs"

            #update:
            eq.lhs.update()
            eq.rhs.update()
            eq.update()

            return eq, subj_side, subj_block
    else:
        if is_subject_isolated(eq,subj_side) == True:
            #nothing to move
            return eq, subj_side, None
        else:#there are two copies of this code. Surely there's a better way than this...
            if subj_side == "lhs":
                if is_subject_last(eq,subj_side,subj_block) == True:
                    #make new 'symb subject' everything except the 1st block
                    symb_subj_blocks = eq.lhs.blocks[1:]
                    
                else:
                    #make new 'symb subject' everything except the last block
                    symb_subj_blocks = eq.lhs.blocks[:-1]

                #make this into an actual symbolic object:
                symb_subj_list = []
                for element in symb_subj_blocks:
                    symb_subj_list.append(element.sign + " " + element.content)
                symb_subj = " ".join(symb_subj_list)
                symb_subj = sp.sympify(symb_subj)
                symb_side = sp.sympify(eq.lhs.content)

                #identify the block to move:
                symb_block_to_move = str(sp.solve(symb_side, symb_subj)[0])
                #remove from lhs:
                for element in eq.lhs.blocks:
                    if symb_block_to_move[0] == "-":
                        if element.content == symb_block_to_move[1:]:
                            eq.lhs.blocks.remove(element)
                    else:
                        if element.content == symb_block_to_move:
                            eq.lhs.blocks.remove(element)
                    

                #add to rhs:
                symb_block_to_move = block.Block.str_to_block(symb_block_to_move)
                eq.rhs.blocks.append(symb_block_to_move)

                #update everything:
                eq.lhs.update()
                eq.rhs.update()
                eq.update()

                return eq, subj_side, symb_block_to_move
            else:
                if is_subject_last(eq,subj_side,subj_block) == True:
                    #make new 'symb subject' everything except the 1st block
                    symb_subj_blocks = eq.rhs.blocks[1:]
                    
                else:
                    #make new 'symb subject' everything except the last block
                    symb_subj_blocks = eq.rhs.blocks[:-1]

                #make this into an actual symbolic object:
                symb_subj_list = []
                for element in symb_subj_blocks:
                    symb_subj_list.append(element.sign + " " + element.content)
                symb_subj = " ".join(symb_subj_list)
                symb_subj = sp.sympify(symb_subj)
                symb_side = sp.sympify(eq.rhs.content)

                #identify the block to move:
                symb_block_to_move = str(sp.solve(symb_side, symb_subj)[0])

                #remove from rhs
                for element in eq.rhs.blocks:
                    if symb_block_to_move[0] == "-":
                        if element.content == symb_block_to_move[1:]:
                            eq.rhs.blocks.remove(element)
                    else:
                        if element.content == symb_block_to_move:
                            eq.rhs.blocks.remove(element)

                #add to lhs:
                symb_block_to_move = block.Block.str_to_block(symb_block_to_move)
                eq.lhs.blocks.append(symb_block_to_move)

                #update everything:
                eq.lhs.update()
                eq.rhs.update()
                eq.update()

                return eq, subj_side, symb_block_to_move

        