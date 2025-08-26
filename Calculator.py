from tkinter import *

from calculator_functions import clear, back, press, reciprocal, square, equal

root = Tk()
root.geometry("383x630")
root.title("Scientific Calculator")
root.config(bg="gray11")

e_string = StringVar()
e = Entry(root, textvariable=e_string, fg="white", bg="gray20", border=0, font=("Bahnschrift SemiBold", 26))
e.grid(columnspan=4, ipady=15)

font_value = ("Calibri", 18)

btn_tan = Button(root, text="tan", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                 command=lambda: press(e, "tan("))
btn_tan.grid(row=1, column=0, sticky=E+W, ipady=5)

btn_cos = Button(root, text="cos", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                 command=lambda: press(e, "cos("))
btn_cos.grid(row=1, column=1, sticky=E+W, ipady=5)

btn_sin = Button(root, text="sin", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                 command=lambda: press(e, "sin("))
btn_sin.grid(row=1, column=2, sticky=E+W, ipady=5)

btn_sqrt = Button(root, text="sqrt", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                  command=lambda: press(e, "sqrt("))
btn_sqrt.grid(row=1, column=3, sticky=E+W, ipady=5)

btn_log = Button(root, text="log", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                 command=lambda: press(e, "log("))
btn_log.grid(row=2, column=0, sticky=E+W, ipady=5)

btn_ln = Button(root, text="ln", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                command=lambda: press(e, "ln("))
btn_ln.grid(row=2, column=1, sticky=E+W, ipady=5)

btn_deg = Button(root, text="deg", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                 command=lambda: press(e, "deg("))
btn_deg.grid(row=2, column=2, sticky=E+W, ipady=5)

btn_reciprocal = Button(root, text="1/x", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                        command=lambda: reciprocal(e))
btn_reciprocal.grid(row=2, column=3, sticky=E+W, ipady=5)

btn_square = Button(root, text="x²", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                    command=lambda: square(e))
btn_square.grid(row=3, column=0, sticky=E+W, ipady=5)

btn_pow = Button(root, text="pow", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                 command=lambda: press(e, "pow"))
btn_pow.grid(row=3, column=1, sticky=E+W, ipady=5)

btn_rem = Button(root, text="rem", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                 command=lambda: press(e, "rem"))
btn_rem.grid(row=3, column=2, sticky=E+W, ipady=5)

btn_pi = Button(root, text="pi", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                command=lambda: press(e, "3.141592"))
btn_pi.grid(row=3, column=3, sticky=E+W, ipady=5)

btn_clear = Button(root, text="C", bg="gray5", fg="DarkOrange1", font=font_value, relief=SOLID,
                   command=lambda: clear(e))
btn_clear.grid(row=4, column=0, columnspan=2, sticky=E+W, ipady=5)

btn_backspace = Button(root, text="back", bg="gray5", fg="DarkOrange1", font=font_value, relief=SOLID,
                       command=lambda: back(e))
btn_backspace.grid(row=4, column=2, columnspan=2, sticky=E+W, ipady=5)

btn_7 = Button(root, text="7", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
               command=lambda: press(e, "7"))
btn_7.grid(row=5, column=0, sticky=E+W, ipady=5)

btn_8 = Button(root, text="8", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
               command=lambda: press(e, "8"))
btn_8.grid(row=5, column=1, sticky=E+W, ipady=5)

btn_9 = Button(root, text="9", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
               command=lambda: press(e, "9"))
btn_9.grid(row=5, column=2, sticky=E+W, ipady=5)

btn_divide = Button(root, text="/", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                    command=lambda: press(e, "/"))
btn_divide.grid(row=5, column=3, sticky=E+W, ipady=5)

btn_4 = Button(root, text="4", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
               command=lambda: press(e, "4"))
btn_4.grid(row=6, column=0, sticky=E+W, ipady=5)

btn_5 = Button(root, text="5", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
               command=lambda: press(e, "5"))
btn_5.grid(row=6, column=1, sticky=E+W, ipady=5)

btn_6 = Button(root, text="6", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
               command=lambda: press(e, "6"))
btn_6.grid(row=6, column=2, sticky=E+W, ipady=5)

btn_multiply = Button(root, text="*", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                      command=lambda: press(e, "*"))
btn_multiply.grid(row=6, column=3, sticky=E+W, ipady=5)

btn_1 = Button(root, text="1", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
               command=lambda: press(e, "1"))
btn_1.grid(row=7, column=0, sticky=E+W, ipady=5)

btn_2 = Button(root, text="2", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
               command=lambda: press(e, "2"))
btn_2.grid(row=7, column=1, sticky=E+W, ipady=5)

btn_3 = Button(root, text="3", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
               command=lambda: press(e, "3"))
btn_3.grid(row=7, column=2, sticky=E+W, ipady=5)

btn_subtract = Button(root, text="-", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                      command=lambda: press(e, "-"))
btn_subtract.grid(row=7, column=3, sticky=E+W, ipady=5)

btn_dot = Button(root, text=".", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                 command=lambda: press(e, "."))
btn_dot.grid(row=8, column=0, sticky=E+W, ipady=5)

btn_0 = Button(root, text="0", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
               command=lambda: press(e, "0"))
btn_0.grid(row=8, column=1, sticky=E+W, ipady=5)

btn_e = Button(root, text="e", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
               command=lambda: press(e, "2.71828"))
btn_e.grid(row=8, column=2, sticky=E+W, ipady=5)

btn_add = Button(root, text="+", bg="gray11", fg="DarkOrange1", font=font_value, relief=SOLID,
                 command=lambda: press(e, "+"))
btn_add.grid(row=8, column=3, sticky=E+W, ipady=5)

btn_equal = Button(root, text="=", bg="DarkOrange1", fg="gray11", font=font_value, relief=SOLID,
                   command=lambda: equal(e))
btn_equal.grid(row=9, column=0, columnspan=4, sticky=E+W, ipady=5)

root.mainloop()
