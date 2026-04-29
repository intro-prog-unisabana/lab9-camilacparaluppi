from aircraft import Aircraft
modeloaeronave = input("Enter aircraft model: ")
plane = Aircraft(modeloaeronave)
while True:
    comando = input("Enter command (A for ascent, D for descent, X to exit): ")
    if comando == "X":
        break
    partes = comando.split()
    direccion = partes[0]
    pies = int(partes[1])
    if direccion == "A":
        plane.ascend(pies)
    elif direccion == "D":
        plane.descend(pies)
print(f"Final altitude: {plane.altitude} feet")