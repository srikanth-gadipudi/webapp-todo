import streamlit as st
import functions

todos = functions.get_todo()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todo(todos)


st.title("My Todo Webapp")
st.subheader("this will help you to plan your day")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    print(checkbox)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="add a new todo..", on_change=add_todo, key="new_todo", )
