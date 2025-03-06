import dto9base
import ctypes
import sys
import datetime

class Fptr(dto9base.DTO9Base):
	SET_TRIPLE_INT_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, \
												ctypes.c_void_p, \
												ctypes.c_int, \
												ctypes.c_int, \
												ctypes.c_int)
	GET_TRIPLE_INT_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, \
												ctypes.c_void_p, \
												ctypes.POINTER(ctypes.c_int), \
												ctypes.POINTER(ctypes.c_int), \
												ctypes.POINTER(ctypes.c_int))

	def _createInterface(self, version):
		return self.library.CreateFptrInterface(version)
	def _releaseInterface(self, interface):
		return self.library.ReleaseFptrInterface(ctypes.pointer(ctypes.c_void_p(interface)))
		
	def _settingsVersion(self):
		return 2

	def get_Caption(self):
		return self._getBuff('Caption')

	def put_Caption(self, value):
		if self._setBuff('Caption', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_CaptionPurpose(self):
		return self._getInt('CaptionPurpose')

	def put_CaptionPurpose(self, value):
		if self._setDouble('CaptionPurpose', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_CaptionIsSupported(self):
		return self._getBool('CaptionIsSupported')

	def get_CaptionName(self):
		return self._getBuff('CaptionName')

	def get_Value(self):
		return self._getDouble('Value')

	def put_Value(self, value):
		if self._setDouble('Value', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ValuePurpose(self):
		return self._getInt('ValuePurpose')

	def put_ValuePurpose(self, value):
		if self._setInt('ValuePurpose', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
			
	def get_ValueIsSupported(self):
		return self._getBool('ValueIsSupported')

	def get_ValueName(self):
		return self._getBuff('ValueName')

	def get_ValueMapping(self):
		value = self._getBuff('ValueMapping')
		if value is None:
			self._printResult(sys._getframe().f_code.co_name)
			return None
		else:
			result = dict()
			for pair in value.split(';'):
				if pair:
					[_key, _value] = pair.split(':', 1)
					result[_key] = _value
			return result

	def get_CharLineLength(self):
		return self._getInt('CharLineLength')

	def get_SerialNumber(self):
		return self._getBuff('SerialNumber')

	def put_SerialNumber(self, value):
		if self._setBuff('SerialNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Date(self):
		func = self.GET_TRIPLE_INT_PROTOTYPE((self._getterName('Date'), self.library))
		year = ctypes.c_int(0)
		month = ctypes.c_int(0)
		day = ctypes.c_int(0)
		func(self.interface, ctypes.pointer(day), ctypes.pointer(month), ctypes.pointer(year))
		return [day.value, month.value, year.value]

	def put_Date(self, date):
		func = self.SET_TRIPLE_INT_PROTOTYPE((self._setterName('Date'), self.library))
		func(self.interface, ctypes.c_int(date[0]), ctypes.c_int(date[1]), ctypes.c_int(date[2]))
		return self.get_Result()

	def get_Time(self):
		func = self.GET_TRIPLE_INT_PROTOTYPE((self._getterName('Time'), self.library))
		hour = ctypes.c_int(0)
		minute = ctypes.c_int(0)
		second = ctypes.c_int(0)
		func(self.interface, ctypes.pointer(hour), ctypes.pointer(minute), ctypes.pointer(second))
		return [hour.value, minute.value, second.value]

	def put_Time(self, time):
		func = self.SET_TRIPLE_INT_PROTOTYPE((self._setterName('Time'), self.library))
		if func(self.interface, ctypes.c_int(time[0]), ctypes.c_int(time[1]), ctypes.c_int(time[2])) < 0:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
			
	def get_Fiscal(self):
		return self._getBool('Fiscal')

	def get_TestMode(self):
		return self._getBool('TestMode')

	def put_TestMode(self, value):
		if self._setBool('TestMode', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_EnableCheckSumm(self):
		return self._getBool('EnableCheckSumm')

	def put_EnableCheckSumm(self, value):
		if self._setBool('EnableCheckSumm', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_UserPassword(self):
		return self._getBuff('UserPassword')

	def put_UserPassword(self, value):
		if self._setBuff('UserPassword', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Mode(self):
		return self._getInt('Mode')

	def put_Mode(self, value):
		if self._setInt('Mode', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
			
	def get_Alignment(self):
		return self._getInt('Alignment')

	def put_Alignment(self, value):
		if self._setInt('Alignment', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
			
	def get_TextWrap(self):
		return self._getInt('TextWrap')

	def put_TextWrap(self, value):
		if self._setInt('TextWrap', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
			
	def get_Barcode(self):
		return self._getBuff('Barcode')

	def put_Barcode(self, value):
		if self._setBuff('Barcode', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
			
	def get_BarcodeType(self):
		return self._getInt('BarcodeType')

	def put_BarcodeType(self, value):
		if self._setInt('BarcodeType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
			
	def get_PrintBarcodeText(self):
		return self._getBool('PrintBarcodeText')

	def put_PrintBarcodeText(self, value):
		if self._setBool('PrintBarcodeText', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
			
	def get_SlipDocOrientation(self):
		return self._getInt('SlipDocOrientation')

	def put_SlipDocOrientation(self, value):
		if self._setInt('SlipDocOrientation', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Scale(self):
		return self._getDouble('Scale')

	def put_Scale(self, value):
		if self._setDouble('Scale', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Height(self):
		return self._getInt('Height')

	def put_Height(self, value):
		if self._setInt('Height', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_TypeClose(self):
		return self._getInt('TypeClose')

	def put_TypeClose(self, value):
		if self._setInt('TypeClose', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Summ(self):
		return self._getDouble('Summ')

	def put_Summ(self, value):
		if self._setDouble('Summ', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_CheckType(self):
		return self._getInt('CheckType')

	def put_CheckType(self, value):
		if self._setInt('CheckType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_CheckState(self):
		return self._getInt('CheckState')

	def get_CheckNumber(self):
		return self._getInt('CheckNumber')

	def put_CheckNumber(self, value):
		if self._setInt('CheckNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_RegisterNumber(self):
		return self._getInt('RegisterNumber')

	def put_RegisterNumber(self, value):
		if self._setInt('RegisterNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_DocNumber(self):
		return self._getInt('DocNumber')

	def put_DocNumber(self, value):
		if self._setInt('DocNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
			
	def get_SessionOpened(self):
		return self._getBool('SessionOpened')

	def get_Session(self):
		return self._getInt('Session')

	def put_Session(self, value):
		if self._setInt('Session', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_CheckPaperPresent(self):
		return self._getBool('CheckPaperPresent')

	def get_ControlPaperPresent(self):
		return self._getBool('ControlPaperPresent')

	def get_PLUNumber(self):
		return self._getInt('PLUNumber')

	def put_PLUNumber(self, value):
		if self._setInt('PLUNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Name(self):
		return self._getBuff('Name')

	def put_Name(self, value):
		if self._setBuff('Name', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Price(self):
		return self._getDouble('Price')

	def put_Price(self, value):
		if self._setDouble('Price', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Quantity(self):
		return self._getDouble('Quantity')

	def put_Quantity(self, value):
		if self._setDouble('Quantity', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Department(self):
		return self._getInt('Department')

	def put_Department(self, value):
		if self._setInt('Department', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_DiscountType(self):
		return self._getInt('DiscountType')

	def put_DiscountType(self, value):
		if self._setInt('DiscountType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ReportType(self):
		return self._getInt('ReportType')

	def put_ReportType(self, value):
		if self._setInt('ReportType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BufferedPrint(self):
		return self._getBool('BufferedPrint')

	def put_BufferedPrint(self, value):
		if self._setBool('BufferedPrint', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_InfoLine(self):
		return self._getBuff('InfoLine')

	def get_Model(self):
		return self._getInt('Model')

	def get_ClearFlag(self):
		return self._getBool('ClearFlag')

	def put_ClearFlag(self, value):
		if self._setBool('ClearFlag', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FileName(self):
		return self._getBuff('FileName')

	def put_FileName(self, value):
		if self._setBuff('FileName', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_INN(self):
		return self._getBuff('INN')

	def put_INN(self, value):
		if self._setBuff('INN', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_MachineNumber(self):
		return self._getBuff('MachineNumber')

	def put_MachineNumber(self, value):
		if self._setBuff('MachineNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_License(self):
		return self._getBuff('License')

	def put_License(self, value):
		if self._setBuff('License', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_LicenseNumber(self):
		return self._getInt('LicenseNumber')

	def put_LicenseNumber(self, value):
		if self._setInt('LicenseNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Table(self):
		return self._getInt('Table')

	def put_Table(self, value):
		if self._setInt('Table', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Row(self):
		return self._getInt('Row')

	def put_Row(self, value):
		if self._setInt('Row', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Field(self):
		return self._getInt('Field')

	def put_Field(self, value):
		if self._setInt('Field', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FieldType(self):
		return self._getInt('FieldType')

	def put_FieldType(self, value):
		if self._setInt('FieldType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_CommandBuffer(self):
		return self._getBuff('CommandBuffer')

	def put_CommandBuffer(self, value):
		if self._setBuff('CommandBuffer', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_AnswerBuffer(self):
		return self._getBuff('AnswerBuffer')

	def get_DateEnd(self):
		func = self.GET_TRIPLE_INT_PROTOTYPE((self._getterName('DateEnd'), self.library))
		year = ctypes.c_int(0)
		month = ctypes.c_int(0)
		day = ctypes.c_int(0)
		func(self.interface, ctypes.pointer(day), ctypes.pointer(month), ctypes.pointer(year))
		return [year.value, month.value, day.value]

	def get_SessionEnd(self):
		return self._getInt('SessionEnd')

	def get_EKLZFlags(self):
		return self._getInt('EKLZFlags')

	def get_EKLZKPKNumber(self):
		return self._getInt('EKLZKPKNumber')

	def put_EKLZKPKNumber(self, value):
		if self._setInt('EKLZKPKNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_UnitType(self):
		return self._getInt('UnitType')

	def put_UnitType(self, value):
		if self._setInt('UnitType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_PictureNumber(self):
		return self._getInt('PictureNumber')

	def put_PictureNumber(self, value):
		if self._setInt('PictureNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_LeftMargin(self):
		return self._getInt('LeftMargin')

	def put_LeftMargin(self, value):
		if self._setInt('LeftMargin', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Memory(self):
		return self._getInt('Memory')

	def get_PictureState(self):
		return self._getInt('PictureState')

	def get_Width(self):
		return self._getInt('Width')

	def put_Width(self, value):
		if self._setInt('Width', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Operator(self):
		return self._getInt('Operator')

	def put_Operator(self, value):
		if self._setInt('Operator', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FontBold(self):
		return self._getBool('FontBold')

	def put_FontBold(self, value):
		if self._setBool('FontBold', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FontItalic(self):
		return self._getBool('FontItalic')

	def put_FontItalic(self, value):
		if self._setBool('FontItalic', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FontNegative(self):
		return self._getBool('FontNegative')

	def put_FontNegative(self, value):
		if self._setBool('FontNegative', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FontUnderline(self):
		return self._getBool('FontUnderline')

	def put_FontUnderline(self, value):
		if self._setBool('FontUnderline', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FontDblHeight(self):
		return self._getBool('FontDblHeight')

	def put_FontDblHeight(self, value):
		if self._setBool('FontDblHeight', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FontDblWidth(self):
		return self._getBool('FontDblWidth')

	def put_FontDblWidth(self, value):
		if self._setBool('FontDblWidth', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_PrintPurpose(self):
		return self._getInt('PrintPurpose')

	def put_PrintPurpose(self, value):
		if self._setInt('PrintPurpose', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ReceiptFont(self):
		return self._getInt('ReceiptFont')

	def put_ReceiptFont(self, value):
		if self._setInt('ReceiptFont', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ReceiptFontHeight(self):
		return self._getInt('ReceiptFontHeight')

	def put_ReceiptFontHeight(self, value):
		if self._setInt('ReceiptFontHeight', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ReceiptBrightness(self):
		return self._getInt('ReceiptBrightness')

	def put_ReceiptBrightness(self, value):
		if self._setInt('ReceiptBrightness', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ReceiptLinespacing(self):
		return self._getInt('ReceiptLinespacing')

	def put_ReceiptLinespacing(self, value):
		if self._setInt('ReceiptLinespacing', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_JournalFont(self):
		return self._getInt('JournalFont')

	def put_JournalFont(self, value):
		if self._setInt('JournalFont', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_JournalFontHeight(self):
		return self._getInt('JournalFontHeight')

	def put_JournalFontHeight(self, value):
		if self._setInt('JournalFontHeight', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_JournalBrightness(self):
		return self._getInt('JournalBrightness')

	def put_JournalBrightness(self, value):
		if self._setInt('JournalBrightness', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_JournalLinespacing(self):
		return self._getInt('JournalLinespacing')

	def put_JournalLinespacing(self, value):
		if self._setInt('JournalLinespacing', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_SummPointPosition(self):
		return self._getInt('SummPointPosition')

	def put_SummPointPosition(self, value):
		if self._setInt('SummPointPosition', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_QuantityPointPosition(self):
		return self._getInt('QuantityPointPosition')

	def put_QuantityPointPosition(self, value):
		if self._setInt('QuantityPointPosition', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Destination(self):
		return self._getInt('Destination')

	def put_Destination(self, value):
		if self._setInt('Destination', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_TaxNumber(self):
		return self._getInt('TaxNumber')

	def put_TaxNumber(self, value):
		if self._setInt('TaxNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodePrintType(self):
		return self._getInt('BarcodePrintType')

	def put_BarcodePrintType(self, value):
		if self._setInt('BarcodePrintType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeControlCode(self):
		return self._getBool('BarcodeControlCode')

	def put_BarcodeControlCode(self, value):
		if self._setBool('BarcodeControlCode', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeCorrection(self):
		return self._getInt('BarcodeCorrection')

	def put_BarcodeCorrection(self, value):
		if self._setInt('BarcodeCorrection', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeEncoding(self):
		return self._getInt('BarcodeEncoding')

	def put_BarcodeEncoding(self, value):
		if self._setInt('BarcodeEncoding', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeEncodingMode(self):
		return self._getInt('BarcodeEncodingMode')

	def put_BarcodeEncodingMode(self, value):
		if self._setInt('BarcodeEncodingMode', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FeedValue(self):
		return self._getInt('FeedValue')

	def put_FeedValue(self, value):
		if self._setInt('FeedValue', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ClsPtr(self):
		return self._getVoidPtr('ClsPtr')

	def get_PixelLineLength(self):
		return self._getInt('PixelLineLength')

	def get_RcpPixelLineLength(self):
		return self._getInt('RcpPixelLineLength')

	def get_JrnPixelLineLength(self):
		return self._getInt('JrnPixelLineLength')

	def get_SlipPixelLineLength(self):
		return self._getInt('SlipPixelLineLength')

	def get_RcpCharLineLength(self):
		return self._getInt('RcpCharLineLength')

	def get_JrnCharLineLength(self):
		return self._getInt('JrnCharLineLength')

	def get_SlipCharLineLength(self):
		return self._getInt('SlipCharLineLength')

	def get_Count(self):
		return self._getInt('Count')

	def put_Count(self, value):
		if self._setInt('Count', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_SlotNumber(self):
		return self._getInt('SlotNumber')

	def put_SlotNumber(self, value):
		if self._setInt('SlotNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_DrawerOpened(self):
		return self._getBool('DrawerOpened')

	def get_CoverOpened(self):
		return self._getBool('CoverOpened')

	def get_BatteryLow(self):
		return self._getBool('BatteryLow')

	def get_VerHi(self):
		return self._getBuff('VerHi')

	def get_VerLo(self):
		return self._getBuff('VerLo')

	def get_Build(self):
		return self._getBuff('Build')

	def get_Codepage(self):
		return self._getInt('Codepage')

	def get_LogicalNumber(self):
		return self._getInt('LogicalNumber')

	def put_LogicalNumber(self, value):
		if self._setInt('LogicalNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Remainder(self):
		return self._getDouble('Remainder')

	def get_Change(self):
		return self._getDouble('Change')

	def get_OperationType(self):
		return self._getInt('OperationType')

	def put_OperationType(self, value):
		if self._setInt('OperationType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_TaxTypeNumber(self):
		return self._getInt('TaxTypeNumber')

	def put_TaxTypeNumber(self, value):
		if self._setInt('TaxTypeNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_DiscountTypeNumber(self):
		return self._getInt('DiscountTypeNumber')

	def put_DiscountTypeNumber(self, value):
		if self._setInt('DiscountTypeNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_CounterType(self):
		return self._getInt('CounterType')

	def put_CounterType(self, value):
		if self._setInt('CounterType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_PowerSupplyValue(self):
		return self._getDouble('PowerSupplyValue')

	def get_PowerSupplyState(self):
		return self._getInt('PowerSupplyState')

	def get_StepCounterType(self):
		return self._getInt('StepCounterType')

	def put_StepCounterType(self, value):
		if self._setInt('StepCounterType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_PowerSupplyType(self):
		return self._getInt('PowerSupplyType')

	def put_PowerSupplyType(self, value):
		if self._setInt('PowerSupplyType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodePixelProportions(self):
		return self._getInt('BarcodePixelProportions')

	def put_BarcodePixelProportions(self, value):
		if self._setInt('BarcodePixelProportions', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeProportions(self):
		return self._getInt('BarcodeProportions')

	def put_BarcodeProportions(self, value):
		if self._setInt('BarcodeProportions', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeColumns(self):
		return self._getInt('BarcodeColumns')

	def put_BarcodeColumns(self, value):
		if self._setInt('BarcodeColumns', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeRows(self):
		return self._getInt('BarcodeRows')

	def put_BarcodeRows(self, value):
		if self._setInt('BarcodeRows', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodePackingMode(self):
		return self._getInt('BarcodePackingMode')

	def put_BarcodePackingMode(self, value):
		if self._setInt('BarcodePackingMode', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeUseProportions(self):
		return self._getBool('BarcodeUseProportions')

	def put_BarcodeUseProportions(self, value):
		if self._setBool('BarcodeUseProportions', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeUseRows(self):
		return self._getBool('BarcodeUseRows')

	def put_BarcodeUseRows(self, value):
		if self._setBool('BarcodeUseRows', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeUseColumns(self):
		return self._getBool('BarcodeUseColumns')

	def put_BarcodeUseColumns(self, value):
		if self._setBool('BarcodeUseColumns', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeUseCorrection(self):
		return self._getBool('BarcodeUseCorrection')

	def put_BarcodeUseCorrection(self, value):
		if self._setBool('BarcodeUseCorrection', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeUseCodeWords(self):
		return self._getBool('BarcodeUseCodeWords')

	def put_BarcodeUseCodeWords(self, value):
		if self._setBool('BarcodeUseCodeWords', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeInvert(self):
		return self._getBool('BarcodeInvert')

	def put_BarcodeInvert(self, value):
		if self._setBool('BarcodeInvert', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeSave(self):
		return self._getBool('BarcodeSave')

	def put_BarcodeSave(self, value):
		if self._setBool('BarcodeSave', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeDeferredPrint(self):
		return self._getBool('BarcodeDeferredPrint')

	def put_BarcodeDeferredPrint(self, value):
		if self._setBool('BarcodeDeferredPrint', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BarcodeNumber(self):
		return self._getInt('BarcodeNumber')

	def put_BarcodeNumber(self, value):
		if self._setInt('BarcodeNumber', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Frequency(self):
		return self._getInt('Frequency')

	def put_Frequency(self, value):
		if self._setInt('Frequency', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Duration(self):
		return self._getInt('Duration')

	def put_Duration(self, value):
		if self._setInt('Duration', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_DrawerOnTimeout(self):
		return self._getInt('DrawerOnTimeout')

	def put_DrawerOnTimeout(self, value):
		if self._setInt('DrawerOnTimeout', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_DrawerOffTimeout(self):
		return self._getInt('DrawerOffTimeout')

	def put_DrawerOffTimeout(self, value):
		if self._setInt('DrawerOffTimeout', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_DrawerOnQuantity(self):
		return self._getInt('DrawerOnQuantity')

	def put_DrawerOnQuantity(self, value):
		if self._setInt('DrawerOnQuantity', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Frequency(self):
		return self._getInt('Frequency')

	def put_Frequency(self, value):
		if self._setInt('Frequency', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Duration(self):
		return self._getInt('Duration')

	def put_Duration(self, value):
		if self._setInt('Duration', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_Directory(self):
		return self._getBuff('Directory')

	def put_Directory(self, value):
		if self._setBuff('Directory', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FileSize(self):
		return self._getInt('FileSize')

	def put_FileSize(self, value):
		if self._setInt('FileSize', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FileOpenType(self):
		return self._getInt('FileOpenType')

	def put_FileOpenType(self, value):
		if self._setInt('FileOpenType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FileOpenMode(self):
		return self._getInt('FileOpenMode')

	def put_FileOpenMode(self, value):
		if self._setInt('FileOpenMode', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FileOffset(self):
		return self._getInt('FileOffset')

	def put_FileOffset(self, value):
		if self._setInt('FileOffset', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_FileReadSize(self):
		return self._getInt('FileReadSize')

	def put_FileReadSize(self, value):
		if self._setInt('FileReadSize', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_NeedResultFlag(self):
		return self._getInt('NeedResultFlag')

	def put_NeedResultFlag(self, value):
		if self._setInt('NeedResultFlag', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()



	def SetMode(self):
		if self._execMethod('SetMode') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def ResetMode(self):
		if self._execMethod('ResetMode') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Beep(self):
		if self._execMethod('Beep') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def OpenDrawer(self):
		if self._execMethod('OpenDrawer') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def FullCut(self):
		if self._execMethod('FullCut') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PartialCut(self):
		if self._execMethod('PartialCut') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Feed(self):
		if self._execMethod('Feed') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetStatus(self):
		if self._execMethod('GetStatus') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetRegister(self):
		if self._execMethod('GetRegister') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetRange(self):
		if self._execMethod('GetRange') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetSumm(self):
		if self._execMethod('GetSumm') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def OpenSession(self):
		if self._execMethod('OpenSession') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def CashIncome(self):
		if self._execMethod('CashIncome') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def CashOutcome(self):
		if self._execMethod('CashOutcome') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Report(self):
		if self._execMethod('Report') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def NewDocument(self):
		if self._execMethod('NewDocument') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()


	def OpenCheck(self):
		if self._execMethod('OpenCheck') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Registration(self):
		if self._execMethod('Registration') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Annulate(self):
		if self._execMethod('Annulate') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Return(self):
		if self._execMethod('Return') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Buy(self):
		if self._execMethod('Buy') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def BuyReturn(self):
		if self._execMethod('BuyReturn') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def BuyAnnulate(self):
		if self._execMethod('BuyAnnulate') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Storno(self):
		if self._execMethod('Storno') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Discount(self):
		if self._execMethod('Discount') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Charge(self):
		if self._execMethod('Charge') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def ResetChargeDiscount(self):
		if self._execMethod('ResetChargeDiscount') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Payment(self):
		if self._execMethod('Payment') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def StornoPayment(self):
		if self._execMethod('StornoPayment') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def CancelCheck(self):
		if self._execMethod('CancelCheck') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def CloseCheck(self):
		if self._execMethod('CloseCheck') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def SummTax(self):
		if self._execMethod('SummTax') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def StornoTax(self):
		if self._execMethod('StornoTax') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PrintString(self):
		if self._execMethod('PrintString') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def AddTextField(self):
		if self._execMethod('AddTextField') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PrintFormattedText(self):
		if self._execMethod('PrintFormattedText') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PrintHeader(self):
		if self._execMethod('PrintHeader') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PrintFooter(self):
		if self._execMethod('PrintFooter') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def BeginDocument(self):
		if self._execMethod('BeginDocument') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def EndDocument(self):
		if self._execMethod('EndDocument') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PrintBarcode(self):
		if self._execMethod('PrintBarcode') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PrintPicture(self):
		if self._execMethod('PrintPicture') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetPictureArrayStatus(self):
		if self._execMethod('GetPictureArrayStatus') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetPictureStatus(self):
		if self._execMethod('GetPictureStatus') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PrintPictureByNumber(self):
		if self._execMethod('PrintPictureByNumber') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def AddPicture(self):
		if self._execMethod('AddPicture') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def AddPictureFromFile(self):
		if self._execMethod('AddPictureFromFile') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def DeleteLastPicture(self):
		if self._execMethod('DeleteLastPicture') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def ClearPictureArray(self):
		if self._execMethod('ClearPictureArray') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetPicture(self):
		if self._execMethod('GetPicture') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PrintBarcodeByNumber(self):
		if self._execMethod('PrintBarcodeByNumber') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def ClearBarcodeArray(self):
		if self._execMethod('ClearBarcodeArray') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def DeleteBarcode(self):
		if self._execMethod('DeleteBarcode') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetBarcode(self):
		if self._execMethod('GetBarcode') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def BeginReport(self):
		if self._execMethod('BeginReport') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetRecord(self):
		if self._execMethod('GetRecord') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def EndReport(self):
		if self._execMethod('EndReport') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def BeginAdd(self):
		if self._execMethod('BeginAdd') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def SetRecord(self):
		if self._execMethod('SetRecord') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def EndAdd(self):
		if self._execMethod('EndAdd') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def SetCaption(self):
		if self._execMethod('SetCaption') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetCaption(self):
		if self._execMethod('GetCaption') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def SetValue(self):
		if self._execMethod('SetValue') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetValue(self):
		if self._execMethod('GetValue') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def SetTableField(self):
		if self._execMethod('SetTableField') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetTableField(self):
		if self._execMethod('GetTableField') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Fiscalization(self):
		if self._execMethod('Fiscalization') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def ResetSummary(self):
		if self._execMethod('ResetSummary') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def SetDate(self):
		if self._execMethod('SetDate') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def SetTime(self):
		if self._execMethod('SetTime') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def GetLicense(self):
		if self._execMethod('GetLicense') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def SetLicense(self):
		if self._execMethod('SetLicense') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def SetSerialNumber(self):
		if self._execMethod('SetSerialNumber') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def InitTables(self):
		if self._execMethod('InitTables') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def TechZero(self):
		if self._execMethod('TechZero') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def RunCommand(self):
		if self._execMethod('RunCommand') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def FlushBuffer(self):
		if self._execMethod('FlushBuffer') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def ClearOutput(self):
		if self._execMethod('ClearOutput') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def EKLZActivate(self):
		if self._execMethod('EKLZActivate') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def EKLZCloseArchive(self):
		if self._execMethod('EKLZCloseArchive') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def EKLZGetStatus(self):
		if self._execMethod('EKLZGetStatus') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()


	def WriteData(self):
		if self._execMethod('WriteData') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PowerOff(self):
		if self._execMethod('PowerOff') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def DemoPrint(self):
		if self._execMethod('DemoPrint') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def TestConnector(self):
		if self._execMethod('TestConnector') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def Sound(self):
		if self._execMethod('Sound') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def AdvancedOpenDrawer(self):
		if self._execMethod('AdvancedOpenDrawer') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()


	def OpenDirectory(self):
		if self._execMethod('OpenDirectory') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def ReadDirectory(self):
		if self._execMethod('ReadDirectory') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def CloseDirectory(self):
		if self._execMethod('CloseDirectory') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def OpenFile(self):
		if self._execMethod('OpenFile') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def CloseFile(self):
		if self._execMethod('CloseFile') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def DeleteFileFromSD(self):
		if self._execMethod('DeleteFileFromSD') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def WriteFileToSD(self):
		if self._execMethod('WriteFileToSD') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def ReadFile(self):
		if self._execMethod('ReadFile') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PrintLastCheckCopy(self):
		if self._execMethod('PrintLastCheckCopy') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()



	def _doCallback(self, data, size):
		return self.callback(self, data, size)

	SCANER_EVENT_HANDLER_FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int)
	def InitScanerEventHandler(self):
		self._callback = self.SCANER_EVENT_HANDLER_FUNC(self._doCallback)
		self.library.put_ScannerEventHandlerFunc(self.interface, self._callback)

	def get_ScannerPortHandler(self):
		return self._getVoidPtr('ScannerPortHandler')

	def put_ScannerEventHandler(self, hndl):
		if self._setVoidPtr('ScannerEventHandler', hndl) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ScannerMode(self):
		return self._getInt('ScannerMode')

	def put_ScannerMode(self, value):
		if self._setInt('ScannerMode', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		


	def WritePinPad(self):
		if self._execMethod('WritePinPad') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def ReadPinPad(self):
		if self._execMethod('ReadPinPad') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()


	def WriteModem(self):
		if self._execMethod('WriteModem') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def ReadModem(self):
		if self._execMethod('ReadModem') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def OpenPinPad(self):
		if self._execMethod('OpenPinPad') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def ClosePinPad(self):
		if self._execMethod('ClosePinPad') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def OpenModem(self):
		if self._execMethod('OpenModem') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def CloseModem(self):
		if self._execMethod('CloseModem') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def GetModemStatus(self):
		if self._execMethod('GetModemStatus') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def GetPinPadStatus(self):
		if self._execMethod('GetPinPadStatus') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_PinPadDevice(self):
		return self._getVoidPtr('PinPadDevice')

	def get_PinPadMode(self):
		return self._getInt('PinPadMode')

	def put_PinPadMode(self, value):
		if self._setInt('PinPadMode', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PowerOnPinPad(self):
			if self._execMethod('PowerOnPinPad') is None:
					self._printResult(sys._getframe().f_code.co_name)
			return self.get_Result()

	def PowerOffPinPad(self):
			if self._execMethod('PowerOffPinPad') is None:
					self._printResult(sys._getframe().f_code.co_name)
			return self.get_Result()

	def get_ModemDevice(self):
		return self._getVoidPtr('ModemDevice')

	def get_ModemMode(self):
		return self._getInt('ModemMode')

	def put_ModemMode(self, value):
		if self._setInt('ModemMode', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def PowerOnModem(self):
			if self._execMethod('PowerOnModem') is None:
					self._printResult(sys._getframe().f_code.co_name)
			return self.get_Result()

	def PowerOffModem(self):
			if self._execMethod('PowerOffModem') is None:
					self._printResult(sys._getframe().f_code.co_name)
			return self.get_Result()

	def get_ReadSize(self):
		return self._getInt('ReadSize')

	def put_ReadSize(self, value):
		if self._setInt('ReadSize', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ModemConnectionType(self):
		return self._getInt('ModemConnectionType')

	def put_ModemConnectionType(self, value):
		if self._setInt('ModemConnectionType', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ModemPort(self):
		return self._getInt('ModemPort')

	def put_ModemPort(self, value):
		if self._setInt('ModemPort', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_WriteSize(self):
		return self._getInt('WriteSize')

	def get_ModemStatus(self):
		return self._getInt('ModemStatus')

	def put_ModemStatus(self, value):
		if self._setInt('ModemStatus', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ModemSignal(self):
		return self._getInt('ModemSignal')

	def put_ModemSignal(self, value):
		if self._setInt('ModemSignal', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_OutOfPaper(self):
		return self._getBool('OutOfPaper')

	def get_PrinterConnectionFailed(self):
		return self._getBool('PrinterConnectionFailed')

	def get_PrinterMechanismError(self):
		return self._getBool('PrinterMechanismError')

	def get_PrinterCutMechanismError(self):
		return self._getBool('PrinterCutMechanismError')

	def get_PrinterOverheatError(self):
		return self._getBool('PrinterOverheatError')

		
	def GetDeviceMetrics(self):
		if self._execMethod('GetDeviceMetrics') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def GetCurrentMode(self):
		if self._execMethod('GetCurrentMode') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def GetCurrentStatus(self):
		if self._execMethod('GetCurrentStatus') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def GetLastSummary(self):
		if self._execMethod('GetLastSummary') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()



	def get_ModemAddress(self):
		return self._getBuff('ModemAddress')

	def put_ModemAddress(self, value):
		if self._setBuff('ModemAddress', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
			
	def get_ModemOperator(self):
		return self._getBuff('ModemOperator')
		
	def get_ModemError(self):
		return self._getBuff('ModemError')

	def get_AdvancedMode(self):
		return self._getInt('AdvancedMode')

	def get_AutoCheckOpen(self):
		return self._getBool('AutoCheckOpen')
		
	def put_AutoCheckOpen(self, value):
		if self._setBool('AutoCheckOpen', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_BottomMargin(self):
		return self._getBool('BottomMargin')

	def put_BottomMargin(self, value):
		if self._setBool('BottomMargin', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_DeviceDescription(self):
		return self._getBuff('DeviceDescription')

	def get_EKLZKPK(self):
		return self._getInt('EKLZKPK')

	def EKLZGetKPK(self):
		if self._execMethod('EKLZGetKPK') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
