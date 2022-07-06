# Simple desktop app to translate words and score points.

import sys
from PySide2 import QtCore, QtGui, QtWidgets

""" Create a class that inherits from QtWidget so that it can be displayed.
    Use super().__init__() to call from parent class QtWidget, but so that we can add something to init
    without overwriting what is in parent.
    Create a variable 'label' with which we can create a label with the text to be displayed in the argument.
    Create a layout (layout, template, publication page template) in which the view (label) is to be displayed.
    Set layout so that the widget is made on this layout.
"""


class InlineTranslation:
    def __init__(self, to_translate, input_form, translated, correct_translation):
        self.to_translate = to_translate
        self.input_form = input_form
        self.translated = translated
        self.correct_translation = correct_translation


class AppWidget(QtWidgets.QWidget):
    def __init__(self, translate):
        super().__init__()
        self.translate = translate
        self.state = []  # list to store objects
        self.layout = self.initialize_layout()
        self.setLayout(self.layout)

    def on_submit(self):
        self.points = 0
        for line in self.state:
            print(f'Word to translate: {line.to_translate}')
            print(f'Your answer is: {line.input_form.text()}')
            print(f'The correct answer is: {line.correct_translation}')
            print('\n')
            if line.correct_translation == line.input_form.text():
                self.points += 1
        print(f'You got {self.points} points.')
        msg = QtWidgets.QMessageBox()
        msg.setText(f'You got {self.points} points.')
        msg.exec_()

    def initialize_layout(self):
        self.setWindowTitle('Translate to Spanish')
        # self.setGeometry(300, 300, 500, 400)
        self.setWindowIcon(QtGui.QIcon(
            'icon.png'))  # Window icon setting: the icon must be in the same folder as the project and have the same
        # name as used in the program.
        row = 0
        grid = QtWidgets.QGridLayout()  # setting elements in specific rows and columns
        for key, correct_translation in self.translate.items():
            to_translate = QtWidgets.QLabel(key)
            input_form = QtWidgets.QLineEdit()
            self.state.append(InlineTranslation(key, input_form, '', correct_translation))
            grid.addWidget(to_translate, row, 0)
            grid.addWidget(input_form, row, 1)
            row += 1

        # label.setFont(QtGui.QFont('Sanserif', 20)) # setting the size and font of the text

        # layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(label)  # # adding a widget to the layout
        # return layout

        # create a button to check if a word was translated correctly
        submit = QtWidgets.QPushButton("Submit")
        submit.clicked.connect(self.on_submit)
        grid.addWidget(submit, row, 1)
        # 1 means that it should be on the right side, but in this case the button has a width like the lines above.

        return grid


if __name__ == "__main__":
    translate = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miercoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sabado',
        'Sunday': 'Domingo'
    }
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName('Test window')  # window name setting
    # appWidget = AppWidget()
    appWidget = AppWidget(translate)  # transfer of the created dictionary to the widget
    appWidget.resize(400, 600)
    appWidget.show()  # show widget

    sys.exit(app.exec_())
