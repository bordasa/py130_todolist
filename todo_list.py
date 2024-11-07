class Todo:
    NOT_DONE = ' '
    DONE = 'X'

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
            return Todo.DONE

        return Todo.NOT_DONE

    def __str__(self):
        return f"[{self.check_or_uncheck()}] {self._title.title()}"
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        
        return (self._title == other._title and self.done == other.done)

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("Can only add Todo's to the Todo List.")
        
        self._todos.append(todo)
    
    def __str__(self):
        output_lines = [f"----- {self.title} -----"]
        output_lines += [str(todo) for todo in self._todos]
        return "\n".join(output_lines)



empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list

# Code omitted

# def step_1():
#     print('--------------------------------- Step 1')
#     todo_list = setup()

#     # setup() uses `todo_list.add` to add 3 todos

#     try:
#         todo_list.add(1)
#     except TypeError:
#         print('TypeError detected')    # TypeError detected

#     for todo in todo_list._todos:
#         print(todo)

# step_1()

def step_2():
    print('--------------------------------- Step 2')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

step_2()