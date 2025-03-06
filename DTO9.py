# -*- coding: cp1251 -*-

import dto9fptr
import os

DTO_LIB_NAME = r"C:\Program Files (x86)\ATOL\Drivers9\fptr.dll"
VERSION = 13
Driver = dto9fptr.Fptr(DTO_LIB_NAME, VERSION)

# Примеры работы с моделью АТОЛ 60Ф (Сертефицирована под 1.05)
# Примеры работы с моделью АТОЛ 60Ф (Сертефицирована под 1.05)

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# ------------------------------Подключение к устройству-----------------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //


# Номер модели,с числом в названии АТОЛ 60Ф общего ничего не имеет
Driver.put_DeviceSingleSetting("Model", 76)
# Пароль пользователя по умолчаниюю
Driver.put_DeviceSingleSetting("UserPassword", 30)
# Номер Virtual(Real)COM
Driver.put_DeviceSingleSetting("Port", 5)
# Скорость обмена
Driver.put_DeviceSingleSetting("BaudRate", 115200)
# Протокол обмена (2 = АТОЛ 3.0)
Driver.put_DeviceSingleSetting("Protocol", 2)
Driver.put_DeviceSingleSetting("SearchDir", os.path.dirname(DTO_LIB_NAME))
Driver.ApplySingleSettings()
# Показать окно свойств
Driver.ShowProperties()
# Флаг "Устройство включено"
Driver.put_DeviceEnabled(True)

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# -------------------------------------Открыть смену---------------------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //

# Mode - Режим:
# 0 - Выбора
# 1 - Регистрации
# 2 - Отчётов без гашения
# 3 - Отчётов с гашением
# 4 - Программирования
# 5 - Доступ к ФП/Ввода ЗН
# 6 - Доступ к ЭКЛЗ/ФН

# UserPassword (по умолчанию):
# 30 - Пароль доступа Системеного Администратора
# 29 - Пароль доступа Администратора
# 28 - 1 - Пароли Кассиров

Driver.put_Mode(1)
Driver.put_UserPassword(30)
Driver.SetMode()

# Записать тег 1021 "Кассир"

# Номер тега
# Флаг "Печатать тег" (Внимание! Круг тегов, на которые влияет данный флаг достаточно узок, так как для большинства тегов строго опредлено, должен он печаться или не должен.)
# Тип значения (Строковае, байты, целое и т.д.
# Значение
# Записать тег

Driver.put_FiscalPropertyNumber(1021)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("Старший кассир Иванов И. И.")
Driver.WriteFiscalProperty()

# Открыть смену

Driver.OpenSession()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# -----------------------------------Внесение----------------------------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //

# Размер внесения
# Режим проверки возможности выполнения операции (выключен)
# Выполнить внесение

Driver.put_Summ(5000.000000)
Driver.put_TestMode(0)
Driver.CashIncome()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# ---------------Чек прихода без отправки электронного чека покупателю---------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //

# CheckType - Тип чека:
# 	1 - Приход
# 	2 - Возврат прихода
# 	4 - Расход
# 5 - Возврат расхода
# 	7 - Коррекция прихода
# 	9 - Коррекция расхода

Driver.put_CheckType(1)

# TestMode - Режим проверки операции
# 	0 - операция будет выполнена
# 	1 - Будет проверена возможность выполнения данной операции

Driver.put_TestMode(0)

# PrintCheck - Режим формирования чека:
# 	0 - только в электронном виде без печати на чековой ленте
# 	1 - печатать на чековой ленте

Driver.put_PrintCheck(1)
Driver.OpenCheck()

# Записать имя и должность кассира

Driver.put_FiscalPropertyNumber(1021)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("Старший кассир Иванов И. И.")
Driver.WriteFiscalProperty()

# Применяемая система налогооблажения в чеке:
# 	ОСН - 1
# 	УСН доход - 2
# 	УСН доход-расход - 4
# 	ЕНВД - 8
# 	ЕСН - 16
# 	ПСН - 32

Driver.put_FiscalPropertyNumber(1055)
Driver.put_FiscalPropertyValue(8)
Driver.put_FiscalPropertyType(1)
Driver.WriteFiscalProperty()

# !!!Для ФФД 1.05 запишем электронный адрес покупателя!!!

Driver.put_FiscalPropertyNumber(1008)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("customer@shop.buy")
Driver.WriteFiscalProperty()

# Регистрация товара или услуги

Driver.put_Name("Молоко 3.2%")
Driver.put_Price(50.330000)
Driver.put_Quantity(2.000000)
Driver.put_Department(0)
Driver.put_PositionSum(100.660000)
Driver.put_Summ(0.000000)

# TaxTypeNumber - Номер налога:
# 	0 - Налог из секции
# 	1 - НДС 0%
# 	2 - НДС 10%
# 	3 - НДС 18%
# 	4 - НДС не облагается
# 	5 - НДС с расчётной ставкой 10%
# 	6 - НДС с расчётной ставкой 18%

Driver.put_TaxNumber(4)

# рекомендуется р ассчитывать в кассовом ПО цену со скидкой, а информацию по начисленным скидкам печатать нефискальной печатью и не передавать скидку в ККМ, поэтому код для начисления скидки закомментирован
# Driver.Put_DiscountValue = 10;
#       DiscountType - Тип скидки:
#   	0 - суммовая
#   	1 - процентная
# Driver.Put_DiscountType = 10;

Driver.Registration()
Driver.put_Caption("В том числе скидка: 4.67\nЦена без скидки: 55.00")
Driver.PrintString()

#  Отброс копеек (округление чека без распределения по позициям). Скидка на чек доступна только для его округления до рубля. Таким образом недоступны: надбавки, назначение "на позицию", процентные значения.  SummCharge(), PercentsCharge(), PercentsDiscount () и ResetChargeDiscount () более недоступны
#  Destination - Назначение скидки:
# 	0 - на чек
# 	1 - на позицию (недоступно)

Driver.put_Destination(0)
Driver.put_Summ(0.66)
Driver.Discount()

# Нефискальная печать с информацией по скидкам чека
Driver.put_Caption("--Скидки по чеку--")
Driver.PrintString()
Driver.put_Caption("Сумма чека без скидок 110.00")
Driver.PrintString()
Driver.put_Caption("Скидки по карте: 9.34")
Driver.PrintString()
Driver.put_Caption("Округление: 0.66")
Driver.PrintString()

# Оплата и закрытие чека
# TypeClose - Тип оплаты:
# 	0 - Наличными
# 	1 - Электронными средствами платежа

Driver.put_TypeClose(0)
Driver.put_Summ(500.000000)
Driver.Payment()
Driver.CloseCheck()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# -----------Чек возврата прихода без отправки электронного чека покупателю----------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //

Driver.put_CheckType(2)
Driver.put_TestMode(0)
Driver.put_PrintCheck(1)
Driver.OpenCheck()

Driver.put_FiscalPropertyNumber(1021)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("Старший кассир Иванов И. И.")

Driver.WriteFiscalProperty()
Driver.put_FiscalPropertyNumber(1055)
Driver.put_FiscalPropertyValue(8)
Driver.put_FiscalPropertyType(1)
Driver.WriteFiscalProperty()

# !!!Для ФФД 1.05 запишем электронный адрес покупателя!!!

Driver.put_FiscalPropertyNumber(1008)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("customer@shop.buy")
Driver.WriteFiscalProperty()


Driver.put_Name("Молоко 3.2%")
Driver.put_Price(50.330000)
Driver.put_Quantity(2.000000)
Driver.put_Department(0)
Driver.put_PositionSum(100.660000)
Driver.put_Summ(0.000000)
# рекомендуется рассчитывать в кассовом ПО цену со скидкой, а информацию по начисленным скидкам печатать нефискальной печатью и не передавать скидку в ККМ, поэтому код для начисления скидки закомментирован
# driver.DiscountValue = 10;
#    DiscountType - Тип скидки:
#    	0 - суммовая
#   	1 - процентная
# driver.DiscountType = 0;
Driver.put_TaxNumber(4)
Driver.Registration()
Driver.put_Caption("В том числе скидка: 4.67\nЦена без скидки: 55.00")
Driver.PrintString()
Driver.put_Destination(0)
Driver.put_Summ(0.66)
Driver.Discount()
Driver.put_Caption("--Скидки по чеку--")
Driver.PrintString()
Driver.put_Caption("Сумма чека без скидок 110.00")
Driver.PrintString()
Driver.put_Caption("Скидки по карте: 9.34")
Driver.PrintString()
Driver.put_Caption("Округление: 0.66")
Driver.PrintString()
Driver.put_TypeClose(0)
Driver.put_Summ(100.000000)
Driver.Payment()
Driver.CloseCheck()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# ----------------Чек прихода с отправкой электронного чека покупателю---------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //

Driver.put_CheckType(1)
Driver.put_TestMode(0)
Driver.put_PrintCheck(1)
Driver.OpenCheck()

Driver.put_FiscalPropertyNumber(1021)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("Старший кассир Иванов И. И.")

Driver.WriteFiscalProperty()
Driver.put_FiscalPropertyNumber(1055)
Driver.put_FiscalPropertyValue(1)
Driver.put_FiscalPropertyType(1)
Driver.WriteFiscalProperty()

# !!!Для ФФД 1.05 запишем электронный адрес покупателя!!!

Driver.put_FiscalPropertyNumber(1008)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("customer@shop.buy")
Driver.WriteFiscalProperty()

# Запись электронного адреса покупателя длдя отправки

Driver.put_FiscalPropertyNumber(1008)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("+79091235566")
Driver.WriteFiscalProperty()

Driver.put_Name("Детское питание Тёма")
Driver.put_Price(47.700000)
Driver.put_Quantity(6.000000)
Driver.put_Department(0)
Driver.put_PositionSum(286.200000)
Driver.put_Summ(0.000000)
Driver.put_TaxNumber(4)
# рекомендуется рассчитывать в кассовом ПО цену со скидкой, а информацию по начисленным скидкам печатать нефискальной печатью и не передавать скидку в ККМ, поэтому код для начисления скидки закомментирован
# driver.DiscountValue = 10;
#    DiscountType - Тип скидки:
#    	0 - суммовая
#   	1 - процентная
# driver.DiscountType = 0;
Driver.Registration()

Driver.put_Caption("В том числе скидка: 10%: 5.30 \nЦена без скидки: 53.00")
Driver.PrintString()

Driver.put_Name("Коньяк Победа 0,5")
Driver.put_Price(813.500000)
Driver.put_Quantity(1.000000)
Driver.put_PositionSum(813.500000)
Driver.put_Summ(0.000000)
Driver.put_Department(0)
# рекомендуется рассчитывать в кассовом ПО цену со скидкой, а информацию по начисленным скидкам печатать нефискальной печатью и не передавать скидку в ККМ, поэтому код для начисления скидки закомментирован
# driver.DiscountValue = 10;
#    DiscountType - Тип скидки:
#    	0 - суммовая
#   	1 - процентная
# driver.DiscountType = 0;
Driver.put_TaxNumber(3)
Driver.Registration()
Driver.put_Destination(0)
Driver.put_Summ(0.70)
Driver.Discount()
Driver.put_Caption("--Скидки по чеку--")
Driver.PrintString()
Driver.put_Caption("Сумма чека без скидок 1131.50")
Driver.PrintString()
Driver.put_Caption("Скидки по карте: 31.80")
Driver.PrintString()
Driver.put_Caption("Округление: 0.70")
Driver.PrintString()

Driver.put_TypeClose(0)
Driver.put_Summ(1500.000000)
Driver.Payment()
Driver.CloseCheck()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# ----------------Чек прихода с отправкой электронного чека покупателю---------------
# ----------------------------без печати на чековой ленте----------------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //

Driver.put_CheckType(1)
Driver.put_TestMode(0)
Driver.put_PrintCheck(0)
Driver.OpenCheck()

Driver.put_FiscalPropertyNumber(1021)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("Старший кассир Иванов И. И.")
Driver.WriteFiscalProperty()

Driver.put_FiscalPropertyNumber(1055)
Driver.put_FiscalPropertyValue(1)
Driver.put_FiscalPropertyType(1)
Driver.WriteFiscalProperty()

# Запись электронного адреса покупателя для отправки

Driver.put_FiscalPropertyNumber(1008)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("+79091235566")
Driver.WriteFiscalProperty()

Driver.put_Name("Детское питание Тёма")
Driver.put_Price(47.700000)
Driver.put_Quantity(6.000000)
Driver.put_Department(0)
Driver.put_PositionSum(286.200000)
Driver.put_Summ(0.000000)
Driver.put_TaxNumber(4)
# рекомендуется рассчитывать в кассовом ПО цену со скидкой, а информацию по начисленным скидкам печатать нефискальной печатью и не передавать скидку в ККМ, поэтому код для начисления скидки закомментирован
# driver.DiscountValue = 10;
#    DiscountType - Тип скидки:
#    	0 - суммовая
#   	1 - процентная
# driver.DiscountType = 0;
Driver.Registration()

Driver.put_Caption("В том числе скидка: 10%: 5.30 \nЦена без скидки: 53.00")
Driver.PrintString()

Driver.put_Name("Коньяк Победа 0,5")
Driver.put_Price(813.500000)
Driver.put_Quantity(1.000000)
Driver.put_PositionSum(813.500000)
Driver.put_Summ(0.000000)
Driver.put_Department(0)
# рекомендуется рассчитывать в кассовом ПО цену со скидкой, а информацию по начисленным скидкам печатать нефискальной печатью и не передавать скидку в ККМ, поэтому код для начисления скидки закомментирован
# driver.DiscountValue = 10;
#    DiscountType - Тип скидки:
#    	0 - суммовая
#   	1 - процентная
# driver.DiscountType = 0;
Driver.put_TaxNumber(3)
Driver.Registration()
Driver.put_Destination(0)
Driver.put_Summ(0.70)
Driver.Discount()
Driver.put_Caption("--Скидки по чеку--")
Driver.PrintString()
Driver.put_Caption("Сумма чека без скидок 1131.50")
Driver.PrintString()
Driver.put_Caption("Скидки по карте: 31.80")
Driver.PrintString()
Driver.put_Caption("Округление: 0.70")
Driver.PrintString()

Driver.put_TypeClose(0)
Driver.put_Summ(1500.000000)
Driver.Payment()
Driver.CloseCheck()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# -------------------------------Чек коррекции прихода-------------------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //


Driver.put_CheckType(7)
Driver.put_TestMode(0)
Driver.put_PrintCheck(1)
Driver.OpenCheck()

Driver.put_FiscalPropertyNumber(1021)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("Старший кассир Иванов И. И.")

Driver.put_Name("Коррекция прихода")
Driver.put_Price(99.330000)
Driver.put_Quantity(1.000000)
Driver.put_PositionSum(99.330000)
Driver.put_Summ(0.000000)

# !!!Для ФФД 1.05 запишем ТИП КОРРЕКЦИИ!!!

Driver.put_FiscalPropertyNumber(1173)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(1)
Driver.put_FiscalPropertyValue(1)
Driver.WriteFiscalProperty()

# !!!Для ФФД 1.05 запишем ОСНОВАНИЕ ДЛЯ КОРРЕКЦИИ!!!
# !!! Составной тег

Driver.BeginFormFiscalProperty()

# Добавление тега 1177 к составному тегу

Driver.put_FiscalPropertyNumber(1177)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue(" ДОКУМЕНТ КОРРЕКЦИИ №517")
Driver.AddFiscalProperty()

# Добавление тега 1178 к составному тегу
# Обратить внимание, что форматами ФФД определено время в UnixTime

Driver.put_FiscalPropertyNumber(1178)
Driver.put_FiscalPropertyType(4)
Driver.put_FiscalPropertyValue("1491004800")  # 01.04.2017
Driver.AddFiscalProperty()

# Добавление тега 1079 к составному тегу

Driver.put_FiscalPropertyNumber(1179)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("4")
Driver.AddFiscalProperty()


Driver.EndFormFiscalProperty()

Value_of_1174 = Driver.get_FiscalPropertyValue()


# Запись тега 1174

Driver.put_FiscalPropertyNumber(1174)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(0)
Driver.put_FiscalPropertyValue(Value_of_1174)

Driver.WriteFiscalProperty()


Driver.put_Department(0)
Driver.put_TaxNumber(4)
Driver.Registration()

Driver.put_TypeClose(0)
Driver.put_Summ(99.330000)
Driver.CloseCheck()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# -----------------------------------Закрытие смены----------------------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //

Driver.put_Mode(3)
Driver.put_UserPassword(30)
Driver.SetMode()

Driver.put_FiscalPropertyNumber(1021)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("Старший кассир Иванов И. И.")
Driver.WriteFiscalProperty()

Driver.put_ReportType(1)
Driver.Report()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# -----------------------------Отчёт о состоянии расчетов----------------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //

Driver.put_Mode(2)
Driver.put_UserPassword(30)
Driver.SetMode()

Driver.put_FiscalPropertyNumber(1021)
Driver.put_FiscalPropertyPrint(1)
Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyValue("Старший кассир Иванов И. И.")
Driver.WriteFiscalProperty()

Driver.put_ReportType(42)
Driver.Report()

# Выйти из режима

Driver.ResetMode()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# ----------------Получение состояния связи фискального накопителя-------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //


# Запрашиваем регистр 43
# Получаем Код Ошибки ФН
# Получаем Код Ошибки ОФД
# Получаем Код Ошибки сети

Driver.put_RegisterNumber(43)
Driver.GetRegister()
Driver.get_FNError()
Driver.put_Caption("Код ошибки ФН: " + str(Driver.get_FNError()))
Driver.PrintString()
Driver.get_OFDError()
Driver.put_Caption("Код ошибки ОФД: " + str(Driver.get_FNError()))
Driver.PrintString()
Driver.get_NetworkError()
Driver.put_Caption("Код ошибки сети: " + str(Driver.get_FNError()))
Driver.PrintString()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# ------------------Получение количества неотправленных документов и-----------------
# ---------------------даты самого старого неотправленного ----------------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //


Driver.put_RegisterNumber(44)
Driver.GetRegister()
Driver.get_Count()
Driver.put_Caption(
    "Количество неотправленных документов в ФН: " + str(Driver.get_Count())
)
Driver.PrintString()
Driver.put_RegisterNumber(45)
Driver.GetRegister()
Driver.get_Time()
Driver.get_Date()
Driver.put_Caption(
    "Дата и время первого: "
    + str(Driver.get_Date()[0])
    + "."
    + str(Driver.get_Date()[1])
    + "."
    + str(Driver.get_Date()[2])
    + " "
    + str(Driver.get_Time()[0])
    + ":"
    + str(Driver.get_Time()[1])
)
Driver.PrintString()


# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# ----------------Получение регистрационных данных ККТ-------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //


# Наименование пользователя:

Driver.put_FiscalPropertyType(5)
Driver.put_FiscalPropertyNumber(1048)
Driver.ReadFiscalProperty()
Driver.get_FiscalPropertyValue()
Driver.put_Caption("Наименование пользователя: " + Driver.get_FiscalPropertyValue())
Driver.PrintString()

# ИНН пользователя

Driver.put_FiscalPropertyNumber(1018)
Driver.put_FiscalPropertyType(5)
Driver.ReadFiscalProperty()
Driver.get_FiscalPropertyValue()
Driver.put_Caption("ИНН пользователя: " + str(Driver.get_FiscalPropertyValue()))
Driver.PrintString()

# СНО, выбранное при регистрации ККТ

Driver.put_FiscalPropertyNumber(1062)
Driver.put_FiscalPropertyType(1)
Driver.ReadFiscalProperty()
Driver.get_FiscalPropertyValue()
Driver.put_Caption("СНО: " + str(Driver.get_FiscalPropertyValue()))
Driver.PrintString()

# РНМ

Driver.put_FiscalPropertyNumber(1037)
Driver.put_FiscalPropertyType(5)
Driver.ReadFiscalProperty()
Driver.get_FiscalPropertyValue()
Driver.put_Caption("РН ККТ: " + str(Driver.get_FiscalPropertyValue()))
Driver.PrintString()

# Серийный номер ФН

Driver.put_RegisterNumber(47)
Driver.GetRegister()
Driver.get_SerialNumber()
Driver.put_Caption("Номер ФН: " + str(Driver.get_SerialNumber()))
Driver.PrintString()

# Дата/Время последнего неотправленного ОФД, Номер последнего ФД

Driver.put_RegisterNumber(48)
Driver.GetRegister()
Driver.get_Date()
Driver.get_Time()
Driver.put_Caption(
    "Дата и время регистрации/перегестрации: "
    + str(Driver.get_Date()[0])
    + "."
    + str(Driver.get_Date()[1])
    + "."
    + str(Driver.get_Date()[2])
    + " "
    + str(Driver.get_Time()[0])
    + ":"
    + str(Driver.get_Time()[1])
)
Driver.PrintString()
Driver.get_DocNumber()
Driver.put_Caption("Номер последнего ФД: " + str(Driver.get_DocNumber()))
Driver.PrintString()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# -----------------------------Данные последнего чека--------------------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //

# Дата/Время последнего чека, тип чека, номер ФД чека, сумма чека, ФП

Driver.put_RegisterNumber(51)
Driver.GetRegister()
Driver.get_Date()
Driver.get_Time()
Driver.put_Caption(
    "Дата и время последнего чека: "
    + str(Driver.get_Date()[0])
    + "."
    + str(Driver.get_Date()[1])
    + "."
    + str(Driver.get_Date()[2])
    + " "
    + str(Driver.get_Time()[0])
    + ":"
    + str(Driver.get_Time()[1])
)
Driver.PrintString()
Driver.get_CheckType()
Driver.put_Caption("Тип чека: " + str(Driver.get_CheckType()))
Driver.PrintString()
Driver.get_DocNumber()
Driver.put_Caption("Номер ФД последнего чека: " + str(Driver.get_DocNumber()))
Driver.PrintString()
Driver.get_Summ()
Driver.put_Caption("Итог: " + str(Driver.get_Summ()))
Driver.PrintString()
Driver.get_Value()
FP = int(Driver.get_Value())
Driver.put_Caption("Фискальный признак: " + str(FP))
Driver.PrintString()

# // // // // // // // // // // // // // // // // // // // // // // // // // // // //
# ------------------Данные последнего фискального документа--------------------------
# // // // // // // // // // // // // // // // // // // // // // // // // // // // //

# Дата/Время последнего фискального документа, его номер, ФП

Driver.put_RegisterNumber(52)
Driver.GetRegister()
Driver.get_Date()
Driver.get_Time()
Driver.put_Caption(
    "Дата и время последнего ФД: "
    + str(Driver.get_Date()[0])
    + "."
    + str(Driver.get_Date()[1])
    + "."
    + str(Driver.get_Date()[2])
    + " "
    + str(Driver.get_Time()[0])
    + ":"
    + str(Driver.get_Time()[1])
)
Driver.PrintString()
Driver.get_DocNumber()
Driver.put_Caption("Номер последнего ФД: " + str(Driver.get_DocNumber()))
Driver.PrintString()
Driver.get_Value()
FP = int(Driver.get_Value())
Driver.put_Caption("Фискальный признак: " + str(FP))
Driver.PrintString()

# Проматываем несколько строк
i = 0
while i < 10:
    Driver.put_Caption(" ")
    Driver.PrintString()
    i += 1
# И делаем полный отрез, (в 60Ф отрезчик нет)

Driver.FullCut()
