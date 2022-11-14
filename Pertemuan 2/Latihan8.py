# latihan konversi satuan temperature
# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = int(input('Masukan suhu dalam celcius : '))
print("suhu adalah",celcius, "C")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur, "R")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "F")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, "K")