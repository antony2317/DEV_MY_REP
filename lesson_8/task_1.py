"""Задача по вычислению индекса массы тела"""
try:
    m = int(input('введите массу тела в килограммах: '))
    h = float(input('введите рост в метрах: '))
except(ValueError, TypeError):
    print('вы ввели не верные данные')
imt = m / h ** 2
if imt <= 16:
    print('Выраженный дефицит массы тела')
elif imt > 16 and imt < 18.5:
    print('Недостаточная масса тела (дефицит)')
elif imt > 18.5 and imt < 25:
    print('Норма')
elif imt > 25 and imt < 30:
    print('Избыточная масса тела (состояние, предшествующее ожирению)')
elif imt > 30 and imt < 35:
    print('Ожирение 1-й степени')
elif imt > 35 and imt < 40:
    print('Ожирение 2-й степени')
elif imt > 40:
    print('Ожирение 3-й степени')
