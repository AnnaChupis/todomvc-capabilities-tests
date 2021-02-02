from todomvc_poc_test.pages import todomvc


def test_CRUD():
    todomvc.open()

    todomvc.add('a','b','c')
    todomvc.active_todos_should_be('a','b','c')

    todomvc.edit('b')

    todomvc.toggle_received_result('b edited')
    todomvc.clear_completed()
    todomvc.active_todos_should_be('a', 'c')

    todomvc.cancel_edit('c')

    todomvc.delete('c')
    todomvc.active_todos_should_be('a')
