from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize, Qt, QCoreApplication, QMetaObject
from PyQt5.QtWidgets import (
    QLabel,
    QPushButton,
    QFrame,
    QTextEdit,
    QStackedWidget,
    QWidget,
    QListView,
    QSlider,
    QStatusBar,
    QMenuBar,
    QApplication,
    QLineEdit,
    QMessageBox,
)
from PyQt5.QtGui import QIcon, QPixmap
import sys
import requests


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Login page")
        Form.resize(837, 552)
        Form.setMaximumSize(QSize(837, 552))
        icon = QIcon("assets/Catering service-pana.png")  # Adjust the path to your icon file
        Form.setWindowIcon(icon)
        self.frame = QFrame(Form)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(-50, 0, 881, 541))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setGeometry(QRect(0, 30, 861, 471))
        self.frame_2.setStyleSheet(
            "QFrame {\n"
            " /* Slight orange background */\n"
            "    border: 2px solid #402A12 ; /* Border color */\n"
            "    border-radius: 50px;       /* Rounded corners */\n"
            "}\n"
            ""
        )
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(610, 60, 101, 91))
        self.label.setStyleSheet(
            "QLabel{\n"
            "    border: 5x solid #403A12 ; /* Border color */\n"
            "    border-radius: 50px;       /* Rounded corners */\n"
            "}\n"
            ""
        )
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label.setPixmap(QPixmap("assets/room-service.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(110, 30, 341, 271))
        self.label_2.setStyleSheet("border:none")
        self.label_2.setPixmap(QPixmap("assets/Catering service-pana.png"))
        self.label_2.setScaledContents(True)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(562, 201, 211, 31))
        self.lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "  border: none;\n"
            "  border-bottom: 2.5px solid ;  /* Deep brown color code */\n"
            "}\n"
            "QLineEdit {\n"
            "  padding-top: 5px; /* Adjust padding to accommodate placeholder text */\n"
            "}\n"
            "\n"
            "QLineEdit::placeholder {\n"
            "  color: #A52A2A; /* Adjust placeholder color (optional) */\n"
            "  opacity: 1; /* Ensure placeholder is fully visible */\n"
            "}\n"
            "\n"
            "QLineEdit::before {\n"
            "  content: attr(placeholder); /* Inherit content from placeholder */\n"
            "  position: absolute;\n"
            "  top: 1; /* Position on top of the input field */\n"
            "  left: 5px; /* Adjust horizontal positioning */\n"
            "  font-size: 0.8em; /* Adjust font size (optional) */\n"
            "  color: #C0C0C0; /* Match placeholder color (optional) */\n"
            "  transition: opacity 0.7s ease-in-out; /* Add smooth opacity transition */\n"
            "}\n"
            "\n"
            '/* Hide the "before" element when text is entered */\n'
            'QLineEdit:not([placeholderText=""])::before {\n'
            "  opacity: 0;\n"
            "}"
        )
        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(560, 270, 211, 31))
        self.lineEdit_2.setStyleSheet(
            "QLineEdit {\n"
            "  border: none;\n"
            "  border-bottom: 2.5px solid #592007;  /* Deep brown color code */\n"
            "}\n"
            ""
        )
        self.lineEdit_2.setMaxLength(30)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.login = QPushButton(self.frame_2)
        self.login.setObjectName("login")
        self.login.setGeometry(QRect(630, 330, 71, 31))
        self.login.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: transparent;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #EBDEDE;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: #d0d0d0;\n"
            "}\n"
            "\n"
            "QPushButton:flat {\n"
            "    border: none;\n"
            "	color: rgb(0, 0, 0);\n"
            "}\n"
            ""
        )
        icon = QIcon()
        icon.addFile(
            "../../desktop-application-for-student-based-management-system/icons8-login-rounded-up-24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.login.setIcon(icon)
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QRect(610, 380, 121, 31))
        self.pushButton_3.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: transparent;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #EBDEDE;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: #d0d0d0;\n"
            "}\n"
            "\n"
            "QPushButton:flat {\n"
            "    border: none;\n"
            "	color: rgb(0, 0, 0);\n"
            "}\n"
            ""
        )
        icon1 = QIcon()
        icon1.addFile(
            "../../desktop-application-for-student-based-management-system/icons8-forgot-password-16.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.pushButton_3.setIcon(icon1)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(110, 310, 381, 41))
        self.label_3.setMouseTracking(True)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet('font: 700 italic 9pt "Segoe UI";')
        self.label_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(250, 430, 381, 41))
        self.label_4.setMouseTracking(True)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet('font: 700 italic 9pt "Segoe UI";')
        self.label_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        self.login.clicked.connect(self.handle_register)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Login Page", "Login Page", None))
        self.label.setText("")
        self.label_2.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("Form", "Staff ID", None)
        )
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("Form", "Password", None)
        )
        self.login.setText(QCoreApplication.translate("Form", " Login", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("Form", "  forgot Password", None)
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "Form", "please keep your information safe", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate("Form", "copyright of codeironside\u00a9", None)
        )

    def handle_register(self):
        staff_id = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # Prepare the payload for the POST request
        payload = {
            "staffID": staff_id,
            "password": password,
        }

        url = "http://localhost:1234/api/v1/staff/login"  # Replace with your actual URL

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                QMessageBox.information(None, "Success", "Login successful!")
            else:
                # Extract the message from the JSON response
                response_json = response.json()
                error_message = response_json.get('Message', 'Unknown error')  # Fallback if 'Message' key is missing
                QMessageBox.warning(None, 'Error', f"Login failed: {error_message}") 
        except requests.exceptions.RequestException as e:
            # Handle network-related errors
            QMessageBox.critical(None, "Error", f"Request failed: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
