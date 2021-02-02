from selene import have,be
from selene.support.shared import browser

todo_list = browser.all('#todo-list li')
editing_field = todo_list.element_by(have.css_class('editing')).element('.edit')

def open():
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.element('#new-todo').should(be.enabled).wait_until('')

#ADD
def add(*todos:str):
    for todo in todos:
        browser.element('#new-todo').type(todo).press_enter()

#EDIT
def edit(todo:str):
    todo_list.element_by(have.exact_text(todo)).double_click()
    editing_field.type(' edited').press_enter()

#COMPLETE AND CLEAR
def toggle_received_result(todo_edited:str):
    todo_list.element_by(have.exact_text(todo_edited)).element('.toggle').click()

def clear_completed():
    browser.element('#clear-completed').click()

#CANCEL EDIT
def cancel_edit(todo:str):
   todo_list.element_by(have.exact_text(todo)).double_click()
   editing_field.type(' to be canceled').press_escape()

#DELETE
def delete(todo:str):
    todo_list.element_by(have.exact_text(todo)).element('.destroy').click()

#ASSERTS
def active_todos_should_be(*todos:str):
        todo_list.should(have.exact_texts(*todos))


