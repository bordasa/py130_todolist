class Todo:
    INC_MARK = ' '
    COMP_MARK = 'X'

    def __init__(self, title):
        self._title = title
        self.done = False
        self._mark = self.check_or_uncheck()

    @property
    def title(self):
        return self._title
    
    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, boolian):
        self._done = boolian
    
    def check_or_uncheck(self):
        if self.done:
            return Todo.COMP_MARK

        return Todo.INC_MARK

    def __str__(self):
        return f"[{self.check_or_uncheck()}] {self._title.title()}"
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        
        return (self._title == other._title and self.done == other.done)
    
def test_todo():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')
    todo4 = Todo('Clean room')

    print(todo1)                  # [ ] Buy milk
    print(todo2)                  # [ ] Clean room
    print(todo3)                  # [ ] Go to gym
    print(todo4)                  # [ ] Clean room

    print(todo2 == todo4)         # True
    print(todo1 == todo2)         # False
    print(todo4.done)             # False

    todo1.done = True
    todo4.done = True
    print(todo4.done)             # True

    print(todo1)                  # [X] Buy milk
    print(todo2)                  # [ ] Clean room
    print(todo3)                  # [ ] Go to gym
    print(todo4)                  # [X] Clean room

    print(todo2 == todo4)         # False

    todo4.done = False
    print(todo4.done)             # False
    print(todo4)                  # [ ] Clean room

test_todo()