#!/usr/bin/python

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Float64
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):

        def button1_pressed():
            msg1 = 0.28
            msg2 = 0.28
            pubslide1.publish(msg1)
            pubslide2.publish(msg2)


        def button1_released():
            msg=False
            pub.publish(msg)

        def button2_pressed():
            msg1 = -1.0
            msg2 = -1.0
            pubslide1.publish(msg1)
            pubslide2.publish(msg2)

        def button2_released():
            msg=False
            pub.publish(msg)

        def valuechange():
            size = self.horizontalSlider.value()
            msg= size/1000.0
            pubslide1.publish(msg)

        def valuechange_2():
            size2 = self.horizontalSlider_2.value()
            msg2= size2/1000.0
            pubslide2.publish(msg2)

        Form.setObjectName("Form")
        Form.resize(403, 335)

        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 50, 301, 20))
        self.horizontalSlider.setMaximum(280)
        self.horizontalSlider.setMinimum(-1000)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(50, 140, 301, 20))
        self.horizontalSlider_2.setMaximum(280)
        self.horizontalSlider_2.setMinimum(-1000)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setProperty("value", 0)
        self.horizontalSlider_2.setSliderPosition(0)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickInterval(0)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 230, 101, 25))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(248, 230, 101, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 70, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 160, 91, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.pressed.connect(button1_pressed)
        self.pushButton.released.connect(button1_released)
        self.pushButton_2.pressed.connect(button2_pressed)
        self.pushButton_2.released.connect(button2_released)
        self.horizontalSlider.valueChanged.connect(valuechange)
        self.horizontalSlider_2.valueChanged.connect(valuechange_2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Turtlebot3 Gripper Controller"))
        self.pushButton.setText(_translate("Form", "Open Gripper"))
        self.pushButton_2.setText(_translate("Form", "Close Gripper"))
        self.label.setText(_translate("Form", "Left Gripper"))
        self.label_2.setText(_translate("Form", "Right Gripper"))

if __name__ == "__main__":
    
    import sys
    
    pub = rospy.Publisher('/button',Bool,queue_size=1)
    pubslide1 = rospy.Publisher('/turtlebot3/flapleft_joint_position_controller/command',Float64,queue_size=10)
    pubslide2 = rospy.Publisher('/turtlebot3/flapright_joint_position_controller/command',Float64,queue_size=10)
    rospy.init_node('turtlebot3_gripper_controller_gui', anonymous=True)
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

