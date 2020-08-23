def func_numeros():
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    numero3 = int(input('Digite outro número: '))
    numero4 = int(input('Digite outro número: '))
    numero5 = int(input('Digite mais um número: '))

    print(max(numero1, numero2, numero3, numero4, numero5))
    print(min(numero1, numero2, numero3, numero4, numero5))
    print((numero1 + numero2 + numero3 + numero4 + numero5) // 5)
func_numeros()
