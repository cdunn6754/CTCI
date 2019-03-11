import unittest

class LinkedList:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


class MyDict:
    def __init__(self):
        self._arr = [None]*20

    def key_to_idx(self,key):
        return hash(key) % len(self._arr)

    def __getitem__(self, key):
        ll = self._arr[self.key_to_idx(key)]

        if ll == None:
            raise KeyError("That key is not defined")

        while ll.val[0] != key:
            if ll.next == None:
                raise KeyError("That key is not defined")
            ll = ll.next

        return ll.val[1]
    
    def __setitem__(self, key, value):
        idx = self.key_to_idx(key)
        ll = self._arr[idx]

        if ll == None:
            self._arr[idx] = LinkedList((key, value))

        else: 
            while ll.next != None and ll.val[0] != key:
                ll = ll.next

            if ll.next == None:
                ll.next = LinkedList((key, value))

            if ll.val[0] == key:
                ll.val = (key, value)

    def __delitem__(self, key):
        idx = self.key_to_idx(key)
        ll = self._arr[idx]

        if ll == None:
            raise KeyError("That key doesn't exist")

        if ll.val[0] == key:
            self._arr[idx] = ll.next
            return

        while ll.next != None:
            if ll.next.val[0] == key:
                ll.next = ll.next.next
                return
            ll = ll.next

        raise KeyError("That key doesn't exist")

class MyDictTest(unittest.TestCase):

    def setUp(self):
        self.d = MyDict()

    def test_insertion_and_get(self):
        self.d['hiya'] = 34
        self.assertEqual(self.d['hiya'], 34)

    def test_collision(self):
        """With an initial size of 20 we can create a collision on purpose"""       
        self.d[0] = 23
        self.d[20] = 24
        self.d[40] = 25

        self.assertEqual(self.d[0], 23)
        self.assertEqual(self.d[20], 24)
        self.assertEqual(self.d[40], 25)

    def test_deletion(self):
        self.d[2] = 23
        self.d[22] = 24

        del self.d[22];
        with self.assertRaises(KeyError):
            self.d[22]
            del self.d[22]
            
        self.assertEqual(self.d[2], 23)
        
if __name__ == '__main__':
    unittest.main()
