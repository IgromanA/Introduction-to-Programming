num = input('Enter a number: ')

cnt = 0
even = '02468'

if float(num).is_integer():    
    for i in num:
        if i in even:
            cnt += 1
else: pass

print(f'Count of even digits: {cnt}')