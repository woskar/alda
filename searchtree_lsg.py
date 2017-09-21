#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:38:49 2017

@author: christopher
"""

class Node:
    
    def __init__ (self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None
        
    """
        Additional helper method for __repr__
        This was not demanded by the excercise
    """
    def __strSubTree (self, subTree):
        head = '|\n+--'
        lines = (repr(subTree) + '\n').split('\n')[:-1]
        head += lines[0] + '\n'
        
        for line in lines[1:-1]:
            head += '|  ' + line + '\n'
        
        return head
        
    """
        Additional method to get a string only containing key, value of 
        the node
        This was not demanded by the excercise
    """
    def __str__ (self):
        return '[%s : %s]' % (self.key, self.value)
        
    """
        Additional method to get a complete representation of this node and its
        children.
        This was not demanded by the excercise
    """
    def __repr__ (self):
        head = '[%s : %s]\n' % (self.key, self.value)
        head += self.__strSubTree(self.left)
        head += self.__strSubTree(self.right)
        
        return head
                
    def depth(self, curVal = 0):
        leftV, rightV = curVal, curVal
        if self.left != None:
            leftV = self.left.depth(leftV + 1)
            
        if self.right != None:
            rightV  = self.right.depth(rightV + 1)
            
        return max(leftV, rightV)

#==============================================================================        
                    
"""
    Tree = Node with subtrees

    [key : value]
    |
    +-[key : value]
    | |
    | +- (...)
    | |
    | +- (...)
    |
    +-[key : value]
    | |
    | +- (...)
    | |
    | +- (...)
"""
        
class SearchTree:
    
    def __init__ (self):
        self.__root = None
        self.__size = 0
        
    def __len__ (self):
        return self.__size
    
    #--------------------------------------------------------------------------
    
    def __treeInsert (self, parent, node):
        if parent == None:
            self.__size += 1 # only case when size increases
            return node
        
        if parent.key == node.key:
            parent.value = node.value
            return parent
        
        elif node.key < parent.key:
            parent.left = self.__treeInsert(parent.left, node)
        
        else:
            parent.right = self.__treeInsert(parent.right, node)
            
        return parent
    
    def insert(self, key, value):
        self.__root = self.__treeInsert(self.__root, Node(key, value))
        
    #--------------------------------------------------------------------------    
    
    def __treePredecessor(self, node):
        node = node.left
        
        while node.right is not None:
            node = node.right
            
        return node
    
    def __treeRemove(self, node, key):
        if node is None:
            raise KeyError("Didn't find '%s' in tree" % str(key))
        
        if key < node.key: 
            node.left = self.__treeRemove(node.left, key)
            
        elif key > node.key:
            node.right = self.__treeRemove(node.right, key)
            
        else:
            self.__size -= 1
            if node.left is None and node.right is None:
                node = None
                
            elif node.left is None:
                node = node.right
                
            elif node.right is None:
                node = node.left
                
            else:
                pred = self.__treePredecessor(node)
                node.key = pred.key
                node.value = pred.value
                node.left = self.__treeRemove(node.left, pred.key)
                
        return node
        
    def remove(self, key):
        self.__treeRemove(self.__root, key)
        
    #--------------------------------------------------------------------------
    
    def __treeSearch(self, node, key):
        if node is None:
            return None
        
        elif node.key == key:
            return node
        
        elif key < node.key:
            return self.__treeSearch(node.left, key)
        
        else:            
            return self.__treeSearch(node.right, key)
    
    def find(self, key):
        return self.__treeSearch(self.__root, key)
    
    #--------------------------------------------------------------------------
    
    
    """
        Additional method to get a string representation of the root
        This was not demanded by the excercise
    """
    def __str__ (self):
        return repr(self.__root)
    
    """
        Additional static method to create a tree from tuples
        This was not demanded by the excercise
    """
    @staticmethod
    def createFromTuples(tups):
        st = SearchTree()
        
        for key, value in tups:
            st.insert(key, value)
            
        return st
    
    def depth(self):
        if self.__root == None:
            return -1
        
        return self.__root.depth()
            
#==============================================================================
