pi = 0

while pi <= 360:
    if pi == 90:
        print(f'{pi}º: A quarter of the unic circle has been covered. ')
    elif pi == 180:
        print(f'{pi}º: Half of the unic circle has been covered')
    elif pi == 270:
        print(f'{pi}º: Three quarters of the unic circle has been covered')
    else:print(f'{pi}º')
    pi = pi + 45
print('A complete turn on the unic circle has been done.')
