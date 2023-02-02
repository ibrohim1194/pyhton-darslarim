# Python programasida oddiy kankulyator yasahs
# calculator tkinter da qilinadi


from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
  # point out the global expression variable
  global expression

  # concatenation of string
  expression = expression + str(num)

  # update the expression by using set method
  equation.set(expression)


# Function to evaluate the final expression
def equalpress():
  # Try and except statement is used
  # for handling the errors like zero
  # division error etc.

  # Put that code inside the try block
  # which may generate the error
  try:

    global expression

    # eval function evaluate the expression
    # and str function convert the result
    # into string
    total = str(eval(expression))

    equation.set(total)

    # initialize the expression variable
    # by empty string
    expression = ""

  # if error is generate then handle
  # by the except block
  except:

    equation.set(" error ")
    expression = ""


# Function to clear the contents
# of text entry box
def clear():
  global expression
  expression = ""
  equation.set("")


# Driver code
if name == "main":
  # create a GUI window
  gui = Tk()

  # set the background colour of GUI window
  gui.configure(background="light green")

  # set the title of GUI window
  gui.title("Oddiy Kankulyator")

  # set the configuration of GUI window
  gui.geometry("600x600")

  # StringVar() is the variable class
  # we create an instance of this class
  equation = StringVar()

  # create the text entry box for
  # showing the expression .
  expression_field = Entry(gui, textvariable=equation)

  # grid method is used for placing
  # the widgets at respective positions
  # in table like structure .
  expression_field.grid(columnspan=4, ipadx=70)

  # create a Buttons and place at a particular
  # location inside the root window .
  # when user press the button, the command or
  # function affiliated to that button is executed .
  button1 = Button(gui, text=' 1 ', fg='white', bg='black',
          command=lambda: press(1), height=7, width=20)
  button1.grid(row=2, column=0)

  button2 = Button(gui, text=' 2 ', fg='red', bg='white',
          command=lambda: press(2), height=7, width=20)
  button2.grid(row=2, column=1)

  button3 = Button(gui, text=' 3 ', fg='white', bg='black',
          command=lambda: press(3), height=7, width=20)
  button3.grid(row=2, column=2)

  button4 = Button(gui, text=' 4 ', fg='white', bg='black',
          command=lambda: press(4), height=7, width=20)
  button4.grid(row=3, column=0)

  button5 = Button(gui, text=' 5 ', fg='white', bg='black',
          command=lambda: press(5), height=7, width=20)
  button5.grid(row=3, column=1)

  button6 = Button(gui, text=' 6 ', fg='white', bg='black',
          command=lambda: press(6), height=7, width=20)
  button6.grid(row=3, column=2)

  button7 = Button(gui, text=' 7 ', fg='white', bg='black',
          command=lambda: press(7), height=7, width=20)
  button7.grid(row=4, column=0)

  button8 = Button(gui, text=' 8 ', fg='white', bg='black',
          command=lambda: press(8), height=7, width=20)
  button8.grid(row=4, column=1)

  button9 = Button(gui, text=' 9 ', fg='white', bg='black',
          command=lambda: press(9), height=7, width=20)
  button9.grid(row=4, column=2)

  button0 = Button(gui, text=' 0 ', fg='white', bg='black',
          command=lambda: press(0), height=7, width=20)
  button0.grid(row=5, column=0)

  plus = Button(gui, text=' + ', fg='white', bg='black',
        command=lambda: press("+"), height=7, width=20)
  plus.grid(row=2, column=3)

  minus = Button(gui, text=' - ', fg='white', bg='black',
        command=lambda: press("-"), height=7, width=20)
  minus.grid(row=3, column=3)

  multiply = Button(gui, text=' * ', fg='white', bg='black',
          command=lambda: press("*"), height=7, width=20)
  multiply.grid(row=4, column=3)



divide = Button(gui, text=' / ', fg='white', bg='black',
          command=lambda: press("/"), height=7, width=20)
divide.grid(row=5, column=3)

equal = Button(gui, text=' = ', fg='white', bg='black',
        command=equalpress, height=7, width=20)
equal.grid(row=5, column=2)

clear = Button(gui, text='Tozalash', fg='white', bg='black',
        command=clear, height=7, width=20)
clear.grid(row=5, column='1')

Decimal= Button(gui, text='.', fg='white', bg='black',
          command=lambda: press('.'), height=7, width=20)
Decimal.grid(row=6, column=0)
  # start the GUI
gui.mainloop()