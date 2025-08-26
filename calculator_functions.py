def press(entry_widget, value):
    current_text = entry_widget.get()
    entry_widget.delete(0, "end")
    entry_widget.insert(0, current_text + value)

def clear(entry_widget):
    entry_widget.delete(0, "end")

def back(entry_widget):
    current_text = entry_widget.get()
    entry_widget.delete(0, "end")
    entry_widget.insert(0, current_text[:-1])

def reciprocal(entry_widget):
    try:
        current_value = float(entry_widget.get())
        result = 1 / current_value
        entry_widget.delete(0, "end")
        entry_widget.insert(0, str(result))
    except (ValueError, ZeroDivisionError):
        entry_widget.delete(0, "end")
        entry_widget.insert(0, "Error")

def square(entry_widget):
    try:
        current_value = float(entry_widget.get())
        result = current_value ** 2
        entry_widget.delete(0, "end")
        entry_widget.insert(0, str(result))
    except ValueError:
        entry_widget.delete(0, "end")
        entry_widget.insert(0, "Error")

def equal(entry_widget):
    try:
        expression = entry_widget.get()
        expression = expression.replace("sqrt", "math.sqrt")
        expression = expression.replace("log", "math.log10")
        expression = expression.replace("ln", "math.log")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("deg", "math.degrees")
        result = eval(expression)
        entry_widget.delete(0, "end")
        entry_widget.insert(0, str(result))
    except Exception as e:
        entry_widget.delete(0, "end")
        entry_widget.insert(0, "Error")
