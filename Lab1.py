def task_7():
    # У Jupyter Notebook можна легко вводити дані через інтерактивні засоби, наприклад:
    inputs = [float(input("Введіть число: "))]  # Використовуємо для вводу числа
    
    results = []
    
    for num in inputs:
        if num < 0:
            sign = '1|'
            num = -num
        else:
            sign = '0|'
        
        # Розділяємо на цілу та дробову частини
        integer_part = int(num)
        fractional_part = num - integer_part
        
        # Конвертуємо цілу частину в двійкову систему
        binary_integer = bin(integer_part)[2:]
        
        # Конвертуємо дробову частину в двійкову систему
        binary_fraction = []
        while fractional_part and len(binary_fraction) < 10:  # Ліміт на 10 бітів
            fractional_part *= 2
            bit = int(fractional_part)
            binary_fraction.append(str(bit))
            fractional_part -= bit
        
        binary_fraction = ''.join(binary_fraction)
        
        # Формуємо фінальний результат
        binary_result = f"{sign}{binary_integer}" + (f".{binary_fraction}" if binary_fraction else "")
        results.append(binary_result)
    
    # Виводимо результат в Jupyter Notebook
    for result in results:
        print(f"{inputs[0]} у двійковій системі буде {result}")

task_7()

