# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/administrator/gsoc-AndroidGui/UI/ConfigurationDialog.ui'
#
# Created: Mon Aug 22 00:40:54 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ConfigurationDialog(object):
    def setupUi(self, ConfigurationDialog):
        ConfigurationDialog.setObjectName(_fromUtf8("ConfigurationDialog"))
        ConfigurationDialog.resize(422, 431)
        self.layoutWidget = QtGui.QWidget(ConfigurationDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 370, 331, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_ok = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_ok.setMaximumSize(QtCore.QSize(85, 27))
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(85, 27))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.widget = QtGui.QWidget(ConfigurationDialog)
        self.widget.setGeometry(QtCore.QRect(77, 31, 271, 311))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox_cfg = QtGui.QCheckBox(self.widget)
        self.checkBox_cfg.setChecked(True)
        self.checkBox_cfg.setObjectName(_fromUtf8("checkBox_cfg"))
        self.gridLayout.addWidget(self.checkBox_cfg, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.checkBox_dalvik = QtGui.QCheckBox(self.widget)
        self.checkBox_dalvik.setChecked(True)
        self.checkBox_dalvik.setObjectName(_fromUtf8("checkBox_dalvik"))
        self.gridLayout.addWidget(self.checkBox_dalvik, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.checkBox_javacode = QtGui.QCheckBox(self.widget)
        self.checkBox_javacode.setChecked(True)
        self.checkBox_javacode.setObjectName(_fromUtf8("checkBox_javacode"))
        self.gridLayout.addWidget(self.checkBox_javacode, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.checkBox_bytecode = QtGui.QCheckBox(self.widget)
        self.checkBox_bytecode.setChecked(True)
        self.checkBox_bytecode.setObjectName(_fromUtf8("checkBox_bytecode"))
        self.gridLayout.addWidget(self.checkBox_bytecode, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.checkBox_smalicode = QtGui.QCheckBox(self.widget)
        self.checkBox_smalicode.setChecked(True)
        self.checkBox_smalicode.setObjectName(_fromUtf8("checkBox_smalicode"))
        self.gridLayout.addWidget(self.checkBox_smalicode, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.checkBox_callin = QtGui.QCheckBox(self.widget)
        self.checkBox_callin.setChecked(True)
        self.checkBox_callin.setObjectName(_fromUtf8("checkBox_callin"))
        self.gridLayout.addWidget(self.checkBox_callin, 5, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.checkBox_callout = QtGui.QCheckBox(self.widget)
        self.checkBox_callout.setChecked(True)
        self.checkBox_callout.setObjectName(_fromUtf8("checkBox_callout"))
        self.gridLayout.addWidget(self.checkBox_callout, 6, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.checkBox_permission = QtGui.QCheckBox(self.widget)
        self.checkBox_permission.setChecked(True)
        self.checkBox_permission.setObjectName(_fromUtf8("checkBox_permission"))
        self.gridLayout.addWidget(self.checkBox_permission, 7, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.checkBox_manifest = QtGui.QCheckBox(self.widget)
        self.checkBox_manifest.setChecked(True)
        self.checkBox_manifest.setObjectName(_fromUtf8("checkBox_manifest"))
        self.gridLayout.addWidget(self.checkBox_manifest, 8, 1, 1, 1)

        self.retranslateUi(ConfigurationDialog)
        QtCore.QObject.connect(self.pushButton_ok, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), ConfigurationDialog.close)
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), ConfigurationDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationDialog)

    def retranslateUi(self, ConfigurationDialog):
        ConfigurationDialog.setWindowTitle(QtGui.QApplication.translate("ConfigurationDialog", "Configuration Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ok.setText(QtGui.QApplication.translate("ConfigurationDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cancel.setText(QtGui.QApplication.translate("ConfigurationDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConfigurationDialog", "CFG", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_cfg.setText(QtGui.QApplication.translate("ConfigurationDialog", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ConfigurationDialog", "Dalvik code", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_dalvik.setText(QtGui.QApplication.translate("ConfigurationDialog", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ConfigurationDialog", "Java code", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_javacode.setText(QtGui.QApplication.translate("ConfigurationDialog", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ConfigurationDialog", "Bytecode", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_bytecode.setText(QtGui.QApplication.translate("ConfigurationDialog", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ConfigurationDialog", "Smali code", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_smalicode.setText(QtGui.QApplication.translate("ConfigurationDialog", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ConfigurationDialog", "Call in", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_callin.setText(QtGui.QApplication.translate("ConfigurationDialog", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ConfigurationDialog", "Call out", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_callout.setText(QtGui.QApplication.translate("ConfigurationDialog", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ConfigurationDialog", "Permission", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_permission.setText(QtGui.QApplication.translate("ConfigurationDialog", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ConfigurationDialog", "Manifest", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_manifest.setText(QtGui.QApplication.translate("ConfigurationDialog", "open", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ConfigurationDialog = QtGui.QDialog()
    ui = Ui_ConfigurationDialog()
    ui.setupUi(ConfigurationDialog)
    ConfigurationDialog.show()
    sys.exit(app.exec_())

