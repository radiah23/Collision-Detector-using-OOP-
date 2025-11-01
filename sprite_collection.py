from my_sprite import my_sprite
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class sprite_collection:
    def __init__(self) :
        self.lst_of_collection = [] 

    def add (self, to_add:my_sprite): #ok i got this right 
        if not isinstance(to_add, my_sprite): 
            raise TypeError 
        self.lst_of_collection.append(to_add)

    def get_collection(self):
        return self.lst_of_collection
    
    def __getitem__(self, key:int):
        if not isinstance(key,int):
            raise TypeError ("Key is not an integer") 
        if key <0 : 
            key = len(self.lst_of_collection) + key 
        if key <0 or key >=len(self.lst_of_collection):
            raise IndexError("Key is out of bound")
    
        return self.lst_of_collection[key]
    
 
    def __setitem__(self, key:int, value:my_sprite):
         if not isinstance(key,int):
            raise TypeError ("Key is not an integer") 
         if not isinstance(value, my_sprite):
             raise TypeError("Value not the same object as my_sprite")
         
         if key <0 : 
            key = len(self.lst_of_collection) + key 
         if key <0 or key >=len(self.lst_of_collection):
            raise IndexError("Key is out of bound")
      
         
         self.lst_of_collection[key] = value
   

    def __len__(self): 
        return len(self.lst_of_collection)
    
    def __str__(self): 
        p1 = []
        for s in self.lst_of_collection_: 
            p1.append(f"(loc = {s.loc},size = {(s.width)}x{s.height})")
        return "["+ ",".join(p1)+ "]"

        
           
    def search(self, target:my_sprite): 
        if not isinstance(target, my_sprite):
            raise TypeError ("Not the same object type as my_sprite")
        new_lst = []
        for i in self.lst_of_collection:  
            if i == target and all(i is not obj for obj  in new_lst):
                new_lst.append(i)
        return new_lst 
            


