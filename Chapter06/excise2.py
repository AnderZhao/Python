import easygui

questions = ["What's your name?", "Where's your street?", "Where's your city?"]
answers = ["", "", ""]
position = 0
for question in questions:
    answers[position] = easygui.enterbox(question)
    position = position + 1
for answer in answers:
    easygui.msgbox(answer)
