import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSpinBox
from design import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.plainTextEdit.setPlainText("")
        if self.radioButton.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(-int(self.spinBox.text()), int(self.spinBox.text()) + 1)],
                                   [i for i in range(-int(self.spinBox.text()), int(self.spinBox.text()) + 1)], pen='r')
            self.plainTextEdit.setPlainText("График функции - Прямая")
            self.plainTextEdit.appendPlainText("Функция возрастает при x(-∞; +∞)")
            self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
            self.plainTextEdit.appendPlainText("y = 0, при x = 0")
            self.plainTextEdit.appendPlainText("Функция является нечётной")
            self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим - не существует")
        elif self.radioButton_2.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(-int(self.spinBox.text()), int(self.spinBox.text()) + 1)],
                                   [i ** 2 for i in range(-int(self.spinBox.text()),
                                                          int(self.spinBox.text()) + 1)], pen='g')
            self.plainTextEdit.setPlainText("График функции - парабола\nВетви направлены вверх")
            self.plainTextEdit.appendPlainText("Функция убывает при x(-∞; 0)\nФункция возрастает при x(0; +∞)")
            self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
            self.plainTextEdit.appendPlainText("y = 0, при x = 0")
            self.plainTextEdit.appendPlainText("Функция является чётной")
            self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим = 0")
        elif self.radioButton_3.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(-int(self.spinBox.text()), int(self.spinBox.text()) + 1)],
                                   [i ** 3 for i in range(-int(self.spinBox.text()),
                                                          int(self.spinBox.text()) + 1)], pen='b')
            self.plainTextEdit.setPlainText("График функции - кубическая парабола")
            self.plainTextEdit.appendPlainText("Функция возрастает при x(-∞; +∞)")
            self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
            self.plainTextEdit.appendPlainText("y = 0, при x = 0")
            self.plainTextEdit.appendPlainText("Функция является нечётной")
            self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим - не существует")
        elif self.radioButton_4.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i ** 2 for i in range(int(self.spinBox.text()) + 1)],
                                   [i for i in range(int(self.spinBox.text()) + 1)], pen='b')
            self.plainTextEdit.setPlainText("График функции")
            self.plainTextEdit.appendPlainText("Функция возрастает при x(0; +∞)")
            self.plainTextEdit.appendPlainText("D(f) = (0; +∞) \nE(f) = (0; +∞)")
            self.plainTextEdit.appendPlainText("y = 0, при x = 0")
            self.plainTextEdit.appendPlainText("Функция является ни нечётной, ни чётной")
            self.plainTextEdit.appendPlainText("y наиб = не существует \ny наим = 0")
        elif self.radioButton_5.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(-int(self.spinBox.text()), int(self.spinBox.text()) + 1)],
                                   [-i for i in range(-int(self.spinBox.text()), int(self.spinBox.text()) + 1)],
                                   pen='r')
            self.plainTextEdit.setPlainText("График функции - Прямая")
            self.plainTextEdit.appendPlainText("Функция убывает при x(-∞; +∞)")
            self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
            self.plainTextEdit.appendPlainText("y = 0, при x = 0")
            self.plainTextEdit.appendPlainText("Функция является нечётной")
            self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим - не существует")
        elif self.radioButton_6.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(-int(self.spinBox.text()), int(self.spinBox.text()) + 1)],
                                   [-(i ** 2) for i in range(-int(self.spinBox.text()),
                                                             int(self.spinBox.text()) + 1)], pen='g')
            self.plainTextEdit.setPlainText("График функции - парабола\nВетви направлены вниз")
            self.plainTextEdit.appendPlainText("Функция возрастает при x(-∞; 0)\nФункция убывает при x(0; +∞)")
            self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
            self.plainTextEdit.appendPlainText("y = 0, при x = 0")
            self.plainTextEdit.appendPlainText("Функция является чётной")
            self.plainTextEdit.appendPlainText("y наиб = 0 \ny наим - не существует")
        elif self.radioButton_7.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(-int(self.spinBox.text()), int(self.spinBox.text()) + 1)],
                                   [-(i ** 3) for i in range(-int(self.spinBox.text()),
                                                             int(self.spinBox.text()) + 1)], pen='b')
            self.plainTextEdit.setPlainText("График функции - кубическая парабола")
            self.plainTextEdit.appendPlainText("Функция убывает при x(-∞; +∞)")
            self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
            self.plainTextEdit.appendPlainText("y = 0, при x = 0")
            self.plainTextEdit.appendPlainText("Функция является нечётной")
            self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим - не существует")
        elif self.radioButton_8.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([-(i ** 2) for i in range(int(self.spinBox.text()) + 1)],
                                   [i for i in range(int(self.spinBox.text()) + 1)], pen='b')
            self.plainTextEdit.setPlainText("График функции")
            self.plainTextEdit.appendPlainText("Функция убывает при x(-∞; 0)")
            self.plainTextEdit.appendPlainText("D(f) = (-∞; 0) \nE(f) = (-∞; 0)")
            self.plainTextEdit.appendPlainText("y = 0, при x = 0")
            self.plainTextEdit.appendPlainText("Функция является ни нечётной, ни чётной")
            self.plainTextEdit.appendPlainText("y наиб = не существует \ny наим = 0")
        elif self.radioButton_9.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(-int(self.spinBox.text()), int(self.spinBox.text()) + 1)],
                                   [int(self.spinBox_3.text()) * i for i in
                                    range(-int(self.spinBox.text()), int(self.spinBox.text()) + 1)], pen='r')
            b = int(self.spinBox_3.text())
            if b > 0:
                self.plainTextEdit.setPlainText("График функции - Прямая")
                self.plainTextEdit.appendPlainText("Функция возрастает при x(-∞; +∞)")
                self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
                self.plainTextEdit.appendPlainText("y = 0, при x = 0")
                self.plainTextEdit.appendPlainText("Функция является нечётной")
                self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим - не существует")
            elif b < 0:
                self.plainTextEdit.setPlainText("График функции - Прямая")
                self.plainTextEdit.appendPlainText("Функция убывает при x(-∞; +∞)")
                self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
                self.plainTextEdit.appendPlainText("y = 0, при x = 0")
                self.plainTextEdit.appendPlainText("Функция является нечётной")
                self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим - не существует")
            else:
                self.plainTextEdit.setPlainText("График функции - Прямая")
                self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
                self.plainTextEdit.appendPlainText("y = 0, при любом значении x")
                self.plainTextEdit.appendPlainText("Функция является нечётной")
                self.plainTextEdit.appendPlainText("y наиб = 0 \ny наим = 0")
        elif self.radioButton_10.isChecked():
            self.graphicsView.clear()
            if int(self.spinBox_3.text()) != 0:
                self.graphicsView.plot([i for i in range(-int(self.spinBox.text()), int(self.spinBox.text()) + 1)],
                                       [int(self.spinBox_3.text()) * i ** int(self.spinBox_2.text()) for i in
                                        range(-int(self.spinBox.text()),
                                              int(self.spinBox.text()) + 1)], pen='g')
                b = int(self.spinBox_3.text())
                n = int(self.spinBox_2.text())
                if b > 0 and n % 2 == 0 and n > 1:
                    self.plainTextEdit.setPlainText("График функции - парабола\nВетви направлены вверх")
                    self.plainTextEdit.appendPlainText("Функция убывает при x(-∞; 0)\nФункция возрастает при x(0; +∞)")
                    self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
                    self.plainTextEdit.appendPlainText("y = 0, при x = 0")
                    self.plainTextEdit.appendPlainText("Функция является чётной")
                    self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим = 0")
                elif b > 0 and n % 2 == 1 and n > 1:
                    self.plainTextEdit.setPlainText("График функции - кубическая парабола")
                    self.plainTextEdit.appendPlainText("Функция возрастает при x(-∞; +∞)")
                    self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
                    self.plainTextEdit.appendPlainText("y = 0, при x = 0")
                    self.plainTextEdit.appendPlainText("Функция является нечётной")
                    self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим - не существует")
                elif b < 0 and n % 2 == 0 and n > 1:
                    self.plainTextEdit.setPlainText("График функции - парабола\nВетви направлены вниз")
                    self.plainTextEdit.appendPlainText("Функция возрастает при x(-∞; 0)\nФункция убывает при x(0; +∞)")
                    self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
                    self.plainTextEdit.appendPlainText("y = 0, при x = 0")
                    self.plainTextEdit.appendPlainText("Функция является чётной")
                    self.plainTextEdit.appendPlainText("y наиб = 0 \ny наим - не существует")
                elif b < 0 and n % 2 == 1 and n > 1:
                    self.plainTextEdit.setPlainText("График функции - кубическая парабола")
                    self.plainTextEdit.appendPlainText("Функция убывает при x(-∞; +∞)")
                    self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
                    self.plainTextEdit.appendPlainText("y = 0, при x = 0")
                    self.plainTextEdit.appendPlainText("Функция является нечётной")
                    self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим - не существует")
                elif b > 0 and n == 1:
                    self.plainTextEdit.setPlainText("График функции - Прямая")
                    self.plainTextEdit.appendPlainText("Функция возрастает при x(-∞; +∞)")
                    self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
                    self.plainTextEdit.appendPlainText("y = 0, при x = 0")
                    self.plainTextEdit.appendPlainText("Функция является нечётной")
                    self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим - не существует")
                elif b < 0 and n == 1:
                    self.plainTextEdit.setPlainText("График функции - Прямая")
                    self.plainTextEdit.appendPlainText("Функция убывает при x(-∞; +∞)")
                    self.plainTextEdit.appendPlainText("D(f) = (-∞; +∞) \nE(f) = (-∞; +∞)")
                    self.plainTextEdit.appendPlainText("y = 0, при x = 0")
                    self.plainTextEdit.appendPlainText("Функция является нечётной")
                    self.plainTextEdit.appendPlainText("y наиб - не существует \ny наим - не существует")

        elif self.radioButton_11.isChecked():
            self.graphicsView.clear()
            if int(self.spinBox_3.text()) != 0:
                self.graphicsView.plot(
                    [int(self.spinBox_3.text()) * (i ** 2) for i in range(int(self.spinBox.text()) + 1)],
                    [i for i in range(int(self.spinBox.text()) + 1)], pen='b')
                b = int(self.spinBox_3.text())
                if b > 0:
                    self.plainTextEdit.setPlainText("График функции")
                    self.plainTextEdit.appendPlainText("Функция возрастает при x(0; +∞)")
                    self.plainTextEdit.appendPlainText("D(f) = (0; +∞) \nE(f) = (0; +∞)")
                    self.plainTextEdit.appendPlainText("y = 0, при x = 0")
                    self.plainTextEdit.appendPlainText("Функция является ни нечётной, ни чётной")
                    self.plainTextEdit.appendPlainText("y наиб = не существует \ny наим = 0")
                elif b < 0:
                    self.plainTextEdit.setPlainText("График функции")
                    self.plainTextEdit.appendPlainText("Функция убывает при x(-∞; 0)")
                    self.plainTextEdit.appendPlainText("D(f) = (-∞; 0) \nE(f) = (-∞; 0)")
                    self.plainTextEdit.appendPlainText("y = 0, при x = 0")
                    self.plainTextEdit.appendPlainText("Функция является ни нечётной, ни чётной")
                    self.plainTextEdit.appendPlainText("y наиб = не существует \ny наим = 0")


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())