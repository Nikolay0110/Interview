class Stack:
    def __init__(self):  # Наша строка
        self.items = []

    def is_empty(self):  # Проверка стека на пустоту
        return len(self.items) == 0

    def push(self, item):  # Добавление элемента в конец стека
        self.items.append(item)

    def pop(self):  # Удаляет последний элемент в стеке
        if not self.is_empty():
            return self.items.pop()

    def peek(self):  # Возвращает верхний элемент стека, но не удаляет его. Стек не меняется
        if not self.is_empty():
            return self.items[-1]

    def size(self):  # Возвращает количество элементов в стеке
        return len(self.items)


def check_balanced(expression):
    stack = Stack()
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for char in expression:  # Запускаем цикл по элементам списка
        if char in brackets.keys():  # Если элемент относится к открывающим скобкам
            stack.push(char)  # Тогда добавляет элемент итерации в stack
        elif char in brackets.values():  # В ином случае проверяем наличие элемента итерации в закрывающих скобках
            if stack.is_empty() or brackets[
                stack.pop()] != char:  # И если stack оказался пуст или значения не соответствуют друг другу
                return False  #

    return stack.is_empty()  # Если вернутся True тогда stack пуст, False - не пуст


# Проверка сбалансированности скобок
expressions = [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
    "}{",
    "{{[(])]}}",
    "[[{())}]"
]

for expression in expressions:
    if check_balanced(expression):
        print(f"Скобки в выражении {expression} сбалансированы.")
    else:
        print(f"Скобки в выражении {expression} несбалансированы.")
