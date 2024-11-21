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

if __name__ == "__main__":
    unittest.main()