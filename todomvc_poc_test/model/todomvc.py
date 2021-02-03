from selene import have, command
from selene.support.shared import browser

todo_list = browser.all('#todo-list li')

def edit_field(text):
    return todo_list.element_by(have.css_class('editing')).element('.edit').type(text)

def open():
    browser.open('https://todomvc4tasj.herokuapp.com').\
        should(have.js_returned(True, 'return Object.keys(require.s.contexts._.defined).length == 39'))


def add(*todos: str):
    for todo in todos:
        browser.element('#new-todo').type(todo).press_enter()

def edit(todo: str,new_text):
    todo_list.element_by(have.exact_text(todo)).double_click()
    edit_field(new_text).perform(command.js.set_value(new_text)).press_enter()

def toggle(todo: str):
    todo_list.element_by(have.exact_text(todo)).element('.toggle').click()

def clear_completed():
    browser.element('#clear-completed').click()

def cancel_edit(todo: str,new_text):
   todo_list.element_by(have.exact_text(todo)).double_click()
   edit_field(new_text).press_escape()

def delete(todo: str):
    todo_list.element_by(have.exact_text(todo)).hover().element('.destroy').click()

def should_have(*todos: str):
        todo_list.should(have.exact_texts(*todos))


