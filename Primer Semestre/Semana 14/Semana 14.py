# Calculo de descuentos
if __name__ == "__main__":
# Primera factura
    monto_1 = 355
    descuento_1 = 25
    monto_final_1 = monto_1 - (monto_1 * descuento_1) / 100
    porcentaje_descuento_1 = (monto_1 * descuento_1) / 100
# Resultados del calculo factura numero 1
    print(f"Factura número 1 varlor total a pagar ${monto_1} descuento del {descuento_1}% ")
    print("")
    print(f"Monto total: ${monto_1:.2f}")
    print(f"Descuento del {descuento_1}%: ${porcentaje_descuento_1}")
    print(f"Monto final a pagar: ${monto_final_1:.2f}\n")

# Segunda factura
    monto_2 = 1230
    descuento_2 = 30
    monto_final_2 = monto_2 - (monto_2 * descuento_2) / 100
    porcentaje_descuento_2 = (monto_2 * descuento_2) / 100
# Resultados del calculo factura numero 2
    print(f"Factura número 2 varlor total a pagar ${monto_2} descuento del {descuento_2}% ")
    print("")
    print(f"Monto total: ${monto_2:.2f}")
    print(f"Descuento del {descuento_2}%: ${porcentaje_descuento_2}")
    print(f"Monto final a pagar: ${monto_final_2:.2f}")