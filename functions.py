FILEPATH = "todo.txt"


def get_todo(filepath=FILEPATH):
    """
    this function will the data from the file and return the data
    """
    with open(filepath, 'r') as file:
        todo = file.readlines()
    return todo


def write_todo(todo, filepath=FILEPATH):
    """
    this function will write the  data to the file

    """
    with open(filepath, 'w') as file:
        file.writelines(todo)




if __name__ == "__main__":
    print("hello from functions")
