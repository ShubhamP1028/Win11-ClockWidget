import sys
import time
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer


class DesktopClock(QWidget):
    def __init__(self):
        super().__init__()

        # Remove window borders and keep it below other windows (like an icon)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.Tool |
                            Qt.WindowType.WindowStaysOnBottomHint)

        # Make background transparent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Create a layout to hold both clock and date labels
        layout = QVBoxLayout(self)

        # Create a clock label
        self.clock_label = QLabel(self)
        self.clock_label.setFont(QFont("OCR A Extended", 45, QFont.Weight.Bold))
        self.clock_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a date label
        self.date_label = QLabel(self)
        self.date_label.setFont(QFont("OCR A Extended", 20, QFont.Weight.Normal))  # Smaller font size
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the labels to the layout
        layout.addWidget(self.clock_label)
        layout.addWidget(self.date_label)

        # Set layout properties
        self.setLayout(layout)

        # Apply stylesheet to the main widget->
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 0.5);  /* Semi-transparent black background */
                border-radius: 20px;  /* Rounded corners */
                border: 2px solid rgba(255, 255, 255, 100);  /* Light border */
            }
            QLabel {
                background: transparent;  /* Ensure labels have transparent backgrounds */
                color: white;  /* White text color */
            }
        """)

        # Set window size and position (adjust as needed)->
        self.setGeometry(1250, 30, 250, 150)

        # Start the timer to update the clock every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        # Update every minute ->
        self.timer.start(60000)

        # Initial update->
        self.update_time()
        # Display Date time ->
        # self.display()

    def update_time(self):
        # Update the clock display with the current time
        current_time = time.strftime("%H:%M")  # Get time in HH:MM format
        current_date = time.strftime("%d %B")  # Get the current date in readable format

        self.clock_label.setText(current_time)
        self.date_label.setText(current_date)

    def display(self):
        self.showNormal()  # Ensures the window is not minimized
        self.raise_()  # Brings the window to the foreground
        self.activateWindow()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DesktopClock()
    clock.display()
    sys.exit(app.exec())