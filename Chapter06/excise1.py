import easygui

fahrenheit = float(easygui.enterbox("Type in a temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5.0 / 9
easygui.msgbox("This is " + str(celsius) + " degrees Celsius.")
