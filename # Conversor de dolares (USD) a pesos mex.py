# Conversor de dolares (USD) a pesos mexicanos (MXN)
cantidad_dolares = float(input("Ingrese la cantidad de dólares (USD): "))
tipo_cambio = float(input("Ingrese el tipo de cambio actual (MXN por USD): "))
cantidad_pesos = cantidad_dolares * tipo_cambio
print("dolares: ", cantidad_dolares, "USD")
print("pesos: ", cantidad_pesos, "MXN")