import unittest
from my_sprite import my_sprite
from sprite_collection import sprite_collection
import pygame 

def example_sprite(width, height, loc=(0, 0)):
    surface = pygame.Surface((width, height))
    sprite = my_sprite.__new__(my_sprite)
    pygame.sprite.Sprite.__init__(sprite)
    sprite.image = surface
    sprite.width = width
    sprite.height = height
    sprite.loc = loc
    return sprite

class TestMySprite(unittest.TestCase):
    def test_isEqual(self):
        #my_sprite()
        p1 = example_sprite(100, 150, (10, 15))
        p2 = example_sprite(100, 150, (10, 15))
        self.assertTrue(p1 == p2)
    def test_isNotEqual(self): #Different locations
        p3 = example_sprite(100, 150, (10, 15))
        p4 = example_sprite(100, 150, (20, 15))
        self.assertFalse(p3 == p4)
    def test_isDifferentImage(self):
        p5 = example_sprite(340, 150, (20, 15))
        p6 = example_sprite(100, 150, (20, 15))
        self.assertFalse(p5==p6)
    def test_SameObject(self): 
        p1 = example_sprite(100, 150, (10, 15))
        self.assertTrue(p1==p1)


class TestSpriteCollection(unittest.TestCase):
    def setUp(self):
        self.c = sprite_collection()
        self.a1 = example_sprite(100, 150, (10, 15))
        self.a2 = example_sprite(100, 150, (10, 15))
        self.c.add(self.a1)
        self.c.add(self.a2)
        

    def test_add_getCollection(self):
        col = self.c.get_collection() 
        self.assertEqual(len(col),2) #checks if the length is equal to 2 and we gave 2 objects
        self.assertIn(self.a1, col) #we get a list of sprite collection, then we check if it added the right object in the list
        with self.assertRaises(TypeError):
            self.c.add("a-b-c-d-e-f")
    
    def test_getItem(self): 
        self.assertIs(self.c[0], self.a1) #Checking the memory address if it is actually a1
        with self.assertRaises(IndexError): 
            _ = self.c[20]
        with self.assertRaises(TypeError):
            _ = self.c["No"]



    def test_setItem(self): 
        a3 = example_sprite(130, 140, (70, 45))
        self.c[1] = a3
        self.assertIs(self.c[1], a3)
        with self.assertRaises(IndexError): 
             self.c[20] = a3
        with self.assertRaises(TypeError):
            self.c[1] = "Nooo"

    
    def test_len(self): 
        self.assertEqual(len(self.c),2)
        a3 = example_sprite(130, 140, (70, 45))
        self.c.add(a3)
        self.assertEqual(len(self.c),3)

    #Search function
    #Multiple equal sprites 
    def test_search_multiple_equal(self): 

        new_lst = self.c.search(self.a1)
        self.assertEqual(len(new_lst),2)
        #and then check the objects are actually a1 and a2)
        self.assertIn(self.a1, new_lst)
        self.assertIn(self.a2, new_lst)
        #then check if they are the same to avoid duplicate
        self.assertFalse(new_lst[0]is new_lst[1])

    #Single match 
    def test_search_single_equal(self): 
        a3 = example_sprite(130, 140, (70, 45))
        self.c.add(a3)
        new_lst = self.c.search(a3)
        self.assertEqual((new_lst), [a3])

    #No Match 
    def test_search_no_match(self): 
        target = example_sprite(130, 140, (70, 45))
        new_lst = self.c.search(target)
        self.assertEqual(new_lst, [])

    #Empty 
    def test_search_empty(self): 
        c2 = sprite_collection()
        target = example_sprite(130, 140, (70, 45))
        new_lst = c2.search(target)
        self.assertEqual(new_lst, [])

    #test duplicate 
    def test_search_identical(self): 
        #since our collection has two identical objects 
        self.c[1] = self.a1
        new_lst = self.c.search(self.a1)
        self.assertEqual(new_lst, [self.a1])

        #only returns the list that has one a1 object 

    #test error 
    def test_search_type(self):
        with self.assertRaises(TypeError):
            self.c.search("not a sprite object")
    
    


















        
        






        




if __name__=="__main__":
    unittest.main()




