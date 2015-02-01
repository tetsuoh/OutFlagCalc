# -*- coding: utf-8 -*-

import sys
import re
from PySide import QtGui
from CalcDesigne import *

class CalcWindow(QtGui.QMainWindow, Ui_OutFlagCalc):

	def __init__(self, parent=None):
		super(CalcWindow, self).__init__(parent)
		self.setupUi(self)

	@QtCore.Slot()

	def calc(self):
		layout_OF1 = self.of1Layout
		layout_OF2 = self.of2Layout
		resultWidget_OF1 = self.of1_result	
		resultWidget_OF2 = self.of2_result	
		codePrefix_OF1 = 'out_data->out_flags = '
		codePrefix_OF2 = 'out_data->out_flags2 = '
		list_OF1 = self.__makeCheckedList(layout_OF1)
		list_OF2 = self.__makeCheckedList(layout_OF2)

		self.PF_GlobalCmd_code.setText('')

		result_OF1 = self.__calcOutFlag(list_OF1)
		resultWidget_OF1.setText(str(result_OF1))

		result_OF2 = self.__calcOutFlag(list_OF2)
		resultWidget_OF2.setText(str(result_OF2))

		if len(list_OF1) > 0:
			code_OF1 = codePrefix_OF1 + self.__genarateCode(list_OF1)
			self.PF_GlobalCmd_code.setText(code_OF1)
		else:
			self.PF_GlobalCmd_code.setText('')

		if len(list_OF2) > 0:
			code_OF2 = codePrefix_OF2 + self.__genarateCode(list_OF2)
			self.PF_GlobalCmd_code.append(code_OF2)

	def __genarateCode(self, checkBoxList):
		result = ''
		for index in xrange(len(checkBoxList)):
			result = result + checkBoxList[index].text() + ' |\r'
		result = re.sub(r'\|\r$', ';', result)
		return result

	def __makeCheckedList(self, targetLO):
		dst = []
		count = targetLO.count()
		for index in xrange(count):
			checkBox = targetLO.itemAt(index).widget()
			if checkBox.isChecked():
				dst.append(checkBox)
		return dst

	def __calcOutFlag(self, checkBoxList):
		result = 0
		for index in xrange(len(checkBoxList)):
			if checkBoxList[index].isChecked():
				result = result + ( 1 << checkBoxList[index].property('bit') )
		return result

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = CalcWindow()
	window.show()
	sys.exit(app.exec_())

