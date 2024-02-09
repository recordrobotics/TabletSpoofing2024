# Imports
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Imports screeninfo and gets information about screen dimensions
from screeninfo import get_monitors
screen_info = get_monitors()[0] # screen_info.width for width and screen_info.height for height

# Python Imports
from gamepad_spoofer import setLeftJoystickXY, press_A, release_A

RESOLUTION = {"x": 2880, "y": 1800}


# Creates tablet class
class TabletSampleWindow(QWidget):
    def __init__(self, parent=None):
        super(TabletSampleWindow, self).__init__(parent)
        self.pen_is_down = False
        self.pen_x = 0
        self.pen_y = 0
        self.pen_pressure = 0
        self.text = ""
        # Resizing the sample window to full desktop size:
        frame_rect = app.desktop().frameGeometry()
        width, height = screen_info.width, screen_info.height
        self.resize(width, height)
        self.move(-9, 0)
        self.setWindowTitle("Sample Tablet Event Handling")

    def tabletEvent(self, tabletEvent):
        self.pen_x = tabletEvent.globalX()
        self.pen_y = tabletEvent.globalY()
        self.pen_pressure = int(tabletEvent.pressure() * 100)

        if tabletEvent.type() == QTabletEvent.TabletPress:
            self.pen_is_down = True
            self.text = "TabletPress event"

        elif tabletEvent.type() == QTabletEvent.TabletMove:
            self.pen_is_down = True
            self.text = "TabletMove event"

            # Makes them between -1 and 1
            x = (self.pen_x / RESOLUTION["x"]) * 2 - 1
            y = (self.pen_y / RESOLUTION["y"]) * 2 - 1

            setLeftJoystickXY(x, y)

        elif tabletEvent.type() == QTabletEvent.TabletRelease:
            self.pen_is_down = False
            self.text = "TabletRelease event"
        self.text += " at x={0}, y={1}, pressure={2}%,".format(self.pen_x, self.pen_y, self.pen_pressure)
        
        if self.pen_is_down:
            self.text += " Pen is down."
            press_A()
        else:
            self.text += " Pen is up."
            release_A()
        tabletEvent.accept()
        self.update()

    def paintEvent(self, event):
        text = self.text
        i = text.find("\n\n")
        if i >= 0:
            text = text.left(i)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.drawText(self.rect(), Qt.AlignTop | Qt.AlignLeft , text)

app = QApplication(sys.argv)
# Creates cursor thing
QApplication.setOverrideCursor(QCursor(Qt.CrossCursor))

mainform = TabletSampleWindow()
mainform.show()
app.exec_()