class Todo:
    NOT_DONE = ' '
    DONE = 'X'

    def __init__(self, title):
        self._title = title
        self.done = False
        self._mark = self.insert_mark()

    @property
    def title(self):
        return self._title
    
    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, boolian):
        self._done = boolian
    
    def insert_mark(self):
        if self.done:
            return Todo.DONE

        return Todo.NOT_DONE

    def __str__(self):
        return f"[{self.insert_mark()}] {self.title}"
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        
        return (self.title == other.title and self.done == other.done)

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

    def __len__(self):
        return len(self._todos)
    
    def first(self):
        return self._todos[0]
    
    def last(self):
        return self._todos[-1]

    def to_list(self):
        return self._todos.copy()
    
    def todo_at(self, index):
        return self._todos[index]
    
    def mark_done_at(self, index):
        self._todos[index].done = True
    
    def mark_undone_at(self, index):
        self._todos[index].done = False
    
    def mark_all_done(self):
        def mark_done(todo):
            todo.done = True

        self.each(mark_done)
    
    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False

        self.each(mark_undone)
    
    def all_done(self):
        return all([todo.done for todo in self._todos])
    
    def remove_at(self, index):
        self._todos.pop(index)

    def each(self, callback):
        for todo in self._todos:
            callback(todo)
    
    def select(self, callback):
        new_list = TodoList(self.title)
        for todo in filter(callback, self._todos):
            # print(todo.title)
            new_list.add(todo)

        # def choose(todo):
        #     if callback(todo):
        #         new_list.add(todo)
        
        # self.each(choose)
        return new_list
        
    def find_by_title(self, title):
        found = self.select(lambda todo: todo.title == title)

        return found.todo_at(0)

    def done_todos(self):
        return self.select(lambda todo: todo.done)
    
    def undone_todos(self):
        return self.select(lambda todo: not todo.done)
    
    def mark_done(self, title):
        found = self.find_by_title(title)
        found.done = True

#########

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



## def step_11():
#     print('--------------------------------- Step 11')
#     todo_list = setup()

#     todo_list.mark_all_undone()
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Clean room
#     # [ ] Go to gym

#     def done_if_y_in_title(todo):
#         if 'y' in todo.title:
#             todo.done = True

#     todo_list.each(done_if_y_in_title)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [X] Buy milk
#     # [ ] Clean room
#     # [X] Go to gym

#     todo_list.each(lambda todo: print('>>>', todo))
#     # >>> [X] Buy milk
#     # >>> [ ] Clean room
#     # >>> [X] Go to gym

# step_11()

# def step_12():
#     print('--------------------------------- Step 12')
#     todo_list = setup()

#     def y_in_title(todo):
#         return 'y' in todo.title

#     print(todo_list.select(lambda todo: y_in_title(todo)))
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Go to gym

#     print(todo_list.select(lambda todo: todo.done))
#     # ---- Today's Todos -----
#     # [X] Clean room

    
#     # print()
#     # print('y' in todo_list.todo_at(1).title)
#     print(y_in_title(todo_list.todo_at(1)))

# step_12()

# def step_13():
#     print('--------------------------------- Step 13')
#     todo_list = setup()

#     todo_list.add(Todo('Clean room'))
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [X] Clean room
#     # [ ] Go to gym
#     # [ ] Clean room
#     print()
#     found = todo_list.find_by_title('Go to gym')
#     print(found)
#     # [ ] Go to gym
#     print()
#     found = todo_list.find_by_title('Clean room')
#     print(found)
#     # [X] Clean room

#     try:
#         todo_list.find_by_title('Feed cat')
#     except IndexError:
#         print('Expected IndexError: Got it!')

# step_13()

# def step_14():
#     print('--------------------------------- Step 14')
#     todo_list = setup()

#     done = todo_list.done_todos()
#     print(done)
#     # ----- Today's Todos -----
#     # [X] Clean room

#     undone = todo_list.undone_todos()
#     print(undone)
#     # ----- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Go to gym

#     done = empty_todo_list.done_todos()
#     print(done)
#     # ----- Nothing Doing -----

#     undone = empty_todo_list.undone_todos()
#     print(undone)
#     # ----- Nothing Doing -----

# step_14()

# def step_15():
#     print('--------------------------------- Step 15')
#     todo_list = setup()

#     todo_list.mark_done('Go to gym')
#     print(todo_list)
#     # ----- Today's Todos -----
#     # [ ] Buy milk
#     # [X] Clean room
#     # [X] Go to gym

#     try:
#         todo_list.mark_done('Feed cat')
#     except IndexError:
#         print('Expected IndexError: Got it!')

# step_15()