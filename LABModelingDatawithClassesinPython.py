 class Todo:
  2     """
  3     Todo represents a task with a name, description, point value, and completed.
  4
  5     A new Todo should have a `completed` field that defaults to `False`.
  6     All other attributes must be provided.
  7
  8     >>> todo = Todo(name='Get Lunch', description='Need to eat.', points=0)
  9     >>> print(todo)
 10     Get Lunch (Incomplete - 0 points): Need to eat.
 11     >>> todo.completed = True
 12     >>> print(todo)
 13     Get Lunch (Complete - 0 points): Need to eat.
 14     >>> todo2 = Todo(name='Test', description='Another todo', points=1, completed=    True)
 15     """
         statuses = {False: '', True: 'Complete'}
 16     def __init__(self, name, description, points, completed = False):
            self.name = name
            self.description = description
            self.points = points
            self.completed = completed
        def __repr__(self):
            return f"{self.name}({self.statuses[self.completed]} - {self.points}): {self.description}"

 17
 18 class TodoList:
 19     """
 20     TodoList wraps a list of Todo objects and implements some functionality that
 21     utilize the information from the entire collection.
 22
 23     >>> todo = Todo(name='Get Lunch', description='Need to eat', points=0, complet    ed=True)
 24     >>> todo2 = Todo(name='Submit Talk Proposal', description='Write and submit ta    lk for PyCon', points=3)
 25     >>> todo_list = TodoList([todo, todo2])
 26     >>> todo_list.average_points()
 27     1.5
 28     >>> todo_list.completed()
 29     [Get Lunch (Complete - 0 points): Need to eat]
 30     >>> todo_list.incomplete()
 31     [Submit Talk Proposal (Incomplete - 3 points): Write and submit talk for PyCon    ]
 32     """
 33     pass
