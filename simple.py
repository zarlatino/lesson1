# a = 2
# b = 0.5
# print(a + b)
#
# name ='augusto'
# print('hello', name )
#
# v= input('Type number: ')
# print(v)

numbers= ['2','5','7','9','10.5']
print(numbers[0:4])
numbers.append('python')
print(numbers)
print(numbers[1:4])
print(numbers[-1])
numbers.remove('python')
print(numbers)

russia = {'city':'moscow','temperature': '20'}
print(russia.get('city'))
russia['temperature'] = int(russia['temperature'])-5
print(russia)

def get_summ(one, two, delimiter='&'):
    x = str(one) + delimiter + str(two)
    return x

print(get_summ('learn','python'))






















