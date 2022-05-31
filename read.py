import sys
sys.path.insert(1,'./DST_DIR/')
import todolist_pb2 as TodoList

# Open the file and convert the serialized string to a regular human readable block of data
my_list = TodoList.TodoList()


with open("./serializedFile", "rb") as fd:
    my_list.ParseFromString(fd.read())

print(my_list)
