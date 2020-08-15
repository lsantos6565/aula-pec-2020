print('REFORME SUA SALA')

print('='*20)
pisoSala_largura = float(input('Digite a largura do piso da sua casa: '))
pisoSala_comprimento = float(input('Digite o comprimento do piso da sua casa:'))

print('='*20)
volumeSala_largura = float(input('Digite a largura da sua sala: '))
volumeSala_comprimento = float(input('Digite o comprimento da sua sala: '))
volumeSala_altura = float(input('Digite a altura da sua sala: '))

print('='*20)
areaParede_altura = float(input('Digite a altura da parede: '))
areaParede_largura = float(input('Digite a largura da parede: '))
areaParede_comprimento = float(input('Digite o comprimento da parede: '))

areaPisoTotal = pisoSala_largura * pisoSala_comprimento

volumeTotal = volumeSala_largura * volumeSala_comprimento * volumeSala_altura

areaParedeTotal = (2 * areaParede_altura * areaParede_largura) + (2 * areaParede_altura * areaParede_comprimento)

print('='*20)
print(f'Você vai precisar de piso para cobrir uma área de {areaPisoTotal}m². ')
print(f'Você vai precisar de tinta para pintar uma área de {areaParedeTotal}m².')
print(f'Seu ar condicionado deve ter potência mínima para cobrir uma sala com volume total de  {volumeTotal}m³.')
print('Obrigado por utlizar nosso programa.')
