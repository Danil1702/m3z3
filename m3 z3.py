def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print("1. Вызовы:")
print_params()
print_params(10)
print_params(10, "другая")
print_params(b=25)
print_params(c=[1,2,3])

print("\n2. Распаковка:")
vals = [100, "список", False]
dict_vals = {"a": 200, "b": "словарь", "c": True}
print_params(*vals)
print_params(**dict_vals)

print("\n3. Распаковка + доп.:")
vals2 = [54.32, 'Строка']
print_params(*vals2, 42)