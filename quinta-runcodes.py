
pisoSala_largura = float(input())
pisoSala_comprimento = float(input())

volumeSala_largura = float(input())
volumeSala_comprimento = float(input())
volumeSala_altura = float(input())

areaParede_altura = float(input())
areaParede_largura = float(input())
areaParede_comprimento = float(input())

areaPisoTotal = pisoSala_largura * pisoSala_comprimento

volumeTotal = volumeSala_largura * volumeSala_comprimento * volumeSala_altura

areaParedeTotal = (2 * areaParede_altura * areaParede_largura) + (2 * areaParede_altura * areaParede_comprimento)

print(f'{areaPisoTotal}m². ')
print(f'{areaParedeTotal}m².')
print(f'{volumeTotal}m³.')

