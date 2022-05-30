import sys
sys.path.insert(1,'./DST_DIR/')
import todolist_pb2 as TodoList


my_list = TodoList.TodoList()
my_list.owner_id = 1234
my_list.owner_name = "Tim"

first_item = my_list.todos.add()
first_item.state = TodoList.TaskState.Value("TASK_DONE")
first_item.task = "Test ProtoBuf for Python"
first_item.due_date = "31.10.2019"

second_item = my_list.todos.add()
second_item.state = TodoList.TaskState.Value("TASK_IN_PROGRESS")
second_item.task = "The development of ProtoBuf using Python"
second_item.due_date = "05.06.2022"

# Write the data in a serialzed form in a file 
with open("./serializedFile", "wb") as fd:
    fd.write(my_list.SerializeToString())

