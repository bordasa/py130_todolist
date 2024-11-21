import unittest
from todo_list import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_to_list(self):
        self.assertEqual([self.todo1, self.todo2, self.todo3], 
                         self.todos.to_list())

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())
    
    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())
    
    def test_all_done(self):
        self.todo1.done, self.todo2.done, self.todo3.done = (True, 
                                                             True, True)

        for todo in self.todos.to_list():
            self.assertTrue(todo.done)
    
    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add(5)
        
        with self.assertRaises(TypeError):
            self.todos.add('String')

        with self.assertRaises(TypeError):
            new_todos = TodoList('New Todos')
            self.todos.add(new_todos)

    def test_todo_at(self):
        with self.assertRaises(IndexError):
            self.todos.todo_at(100)
        
        self.assertEqual(self.todos.todo_at(0), self.todo1)
        self.assertEqual(self.todos.todo_at(1), self.todo2)
    
    def test_mark_done_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(100)
        
        self.todos.mark_done_at(0)
        self.assertTrue(self.todo1.done)
        self.assertFalse(self.todo2.done)
        self.assertFalse(self.todo3.done)
    
    def test_mark_undone_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(100)
        
        self.todo1.done = True
        self.todo2.done = True
        self.todo3.done = True

        self.todos.mark_undone_at(1)
        
        self.assertTrue(self.todo1.done)
        self.assertFalse(self.todo2.done)
        self.assertTrue(self.todo3.done)
    
    def test_mark_all_done(self):
        self.todos.mark_all_done()

        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)
        self.assertTrue(self.todos.all_done())
    
    def test_remove_at(self):
        with self.assertRaises(IndexError):
            self.todos.remove_at(100)
        
        self.todos.remove_at(1)
        
        self.assertEqual([self.todo1, self.todo3], self.todos.to_list())

if __name__ == "__main__":
    unittest.main()