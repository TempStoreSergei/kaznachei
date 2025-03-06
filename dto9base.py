# -*- coding: utf-8 -*-

import sys
import ctypes
import xml.dom.minidom

class DTO9Base(object):
	DEFAULT_BUFF_SIZE = 4096

	SET_INT_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)
	GET_INT_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int))
	SET_DOUBLE_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_double)
	GET_DOUBLE_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double))
	SET_BUFF_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_wchar_p)
	GET_BUFF_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int)
	SET_BUFF_BY_KEY_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p)
	GET_BUFF_BY_KEY_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_int)
	SET_VOIDPTR_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
	GET_VOIDPTR_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
	METHOD_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

	def __init__(self, libraryName, version):
		self.library = ctypes.CDLL(libraryName, mode=ctypes.RTLD_LOCAL)
		self.interface = self._createInterface(version)
		
	def __del__(self):
		self._releaseInterface(self.interface)
		
	def _settingsVersion(self):
		return 1
		
	def _printResult(self, name):
		str = '%s: [%d]' % (name, self.get_ResultCode())
		print(str)


	def _getterName(self, prop):
		return 'get_%s' % prop

	def _setterName(self, prop):
		return 'put_%s' % prop

	def _getInt(self, prop):
		func = self.GET_INT_PROTOTYPE((self._getterName(prop), self.library))
		value = ctypes.c_int(0)
		func(self.interface, ctypes.pointer(value))
		return value.value;

	def _setInt(self, prop, value):
		func = self.SET_INT_PROTOTYPE((self._setterName(prop), self.library))
		if func(self.interface, ctypes.c_int(int(value))) < 0:
			return None
		return 0

	def _getDouble(self, prop):
		func = self.GET_DOUBLE_PROTOTYPE((self._getterName(prop), self.library))
		value = ctypes.c_double(0.0)
		func(self.interface, ctypes.pointer(value))
		return value.value;

	def _setDouble(self, prop, value):
		func = self.SET_DOUBLE_PROTOTYPE((self._setterName(prop), self.library))
		if func(self.interface, ctypes.c_double(float(value))) < 0:
			return None
		return 0
		
	def _getBool(self, prop):
		func = self.GET_INT_PROTOTYPE((self._getterName(prop), self.library))
		value = ctypes.c_int(0)
		func(self.interface, ctypes.pointer(value))
		return False if not value.value else True

	def _setBool(self, prop, value):
		func = self.SET_INT_PROTOTYPE((self._setterName(prop), self.library))
		if func(self.interface, ctypes.c_int(1 if value == True else 0)) < 0:
			return None
		return 0

	def _getVoidPtr(self, prop):
		func = self.GET_VOIDPTR_PROTOTYPE((self._getterName(prop), self.library))
		ptr = ctypes.c_void_p(0)
		func(self.interface, ctypes.pointer(ptr))
		return ptr.value;

	def _setVoidPtr(self, prop, ptr):
		func = self.SET_VOIDPTR_PROTOTYPE((self._setterName(prop), self.library))
		if func(self.interface, ctypes.c_void_p(ptr)) < 0:
			return None
		return 0

	def _getBuff(self, prop):
		func = self.GET_BUFF_PROTOTYPE((self._getterName(prop), self.library))
		buff = ctypes.create_unicode_buffer(self.DEFAULT_BUFF_SIZE)
		size = func(self.interface, buff, self.DEFAULT_BUFF_SIZE)
		if(size > self.DEFAULT_BUFF_SIZE):
			buff = ctypes.create_unicode_buffer(size)
			size = func(self.interface, buff, size)
		if size < 0:
			return None
					
		return buff.value;

	def _setBuff(self, prop, buff):
		func = self.SET_BUFF_PROTOTYPE((self._setterName(prop), self.library))
		if func(self.interface, ctypes.c_wchar_p(str(buff))) < 0:
			return None
		return 0

	def _getBuffByKey(self, prop, name):
		func = self.GET_BUFF_BY_KEY_PROTOTYPE((self._getterName(prop), self.library))
		buff = ctypes.create_unicode_buffer(self.DEFAULT_BUFF_SIZE)
		size = func(self.interface, ctypes.c_wchar_p(name), buff, self.DEFAULT_BUFF_SIZE)
		if(size > self.DEFAULT_BUFF_SIZE):
			buff = ctypes.create_unicode_buffer(size)
			size = func(self.interface, ctypes.c_wchar_p(name), buff, size)
		if size < 0:
			return None
					
		return buff.value;

	def _setBuffByKey(self, prop, name, buff):
		func = self.SET_BUFF_BY_KEY_PROTOTYPE((self._setterName(prop), self.library))
		if func(self.interface, ctypes.c_wchar_p(str(name)), ctypes.c_wchar_p(str(buff))) < 0:
			return None
		return 0

	def _execMethod(self, name):
		func = self.METHOD_PROTOTYPE((name, self.library))
		if func(self.interface) < 0:
			return None
		return 0

	def get_Result(self):
		return self.get_ResultCode(), self.get_ResultDescription(), self.get_BadParam(), self.get_BadParamDescription()

	def get_LicenseValid(self):
		return self._getInt('LicenseValid')

	def get_LicenseExpiredDate(self):
		return self._getBuff('LicenseExpiredDate')

	def get_Version(self):
		return self._getBuff('Version')

	def get_DriverName(self):
		return self._getBuff('DriverName')

	def get_ResultCode(self):
		return self._getInt('ResultCode')

	def get_ResultDescription(self):
		return self._getBuff('ResultDescription')

	def get_BadParam(self):
		return self._getInt('BadParam')

	def get_BadParamDescription(self):
		return self._getBuff('BadParamDescription')

	def get_DeviceEnabled(self):
		return self._getBool('DeviceEnabled')

	def put_DeviceEnabled(self, value):
		if self._setBool('DeviceEnabled', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_ApplicationHandle(self):
		return self._getVoidPtr('ApplicationHandle')

	def put_ApplicationHandle(self, value):
		if self._setVoidPtr('ApplicationHandle', value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_DeviceSettings(self):
		settings = self._getBuff('DeviceSettings')
		if settings is None:
			self._printResult(sys._getframe().f_code.co_name)
			return None
		else:
			result = dict()
			for el in xml.dom.minidom.parseString(settings).getElementsByTagName('value'):
				settingName = el.getAttribute('name')
				settingValue = []
				for child in el.childNodes:
					if child.nodeType == child.TEXT_NODE:
						settingValue.append(child.data)
				settingValue = ''.join(settingValue)
				result[settingName] = settingValue
			return result        
		
	def put_DeviceSettings(self, settings):
		settingsXml = xml.dom.minidom.Document()
		version = self._settingsVersion()
		root = settingsXml.createElement('settings')
		root.setAttribute('version', str(version))
		settingsXml.appendChild(root)
		for name, value in settings.items():
			settingNode = settingsXml.createElement('value')
			settingNode.setAttribute('name', name)
			settingNode.appendChild(settingsXml.createTextNode(str(value)))
			root.appendChild(settingNode)
		if self._setBuff('DeviceSettings', settingsXml.toxml()) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_DeviceSingleSetting(self, name):
		return self._getBuffByKey('DeviceSingleSettingAsBuff', name)
		
	def put_DeviceSingleSetting(self, name, value):
		if self._setBuffByKey('DeviceSingleSettingAsBuff', name, value) is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()

	def get_DeviceSingleSettingMapping(self, name):
		value = self._getBuffByKey('DeviceSingleSettingMapping', name)
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
		
	def ApplySingleSettings(self):
		if self._execMethod('ApplySingleSettings') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def ResetSingleSettings(self):
		if self._execMethod('ResetSingleSettings') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
		
	def ShowProperties(self):
		if self._execMethod('ShowProperties') is None:
			self._printResult(sys._getframe().f_code.co_name)
		return self.get_Result()
