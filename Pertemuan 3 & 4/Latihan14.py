data="ini adalah string"

print(data)
print(type(data))

#1. cara membuat string

# 1. dengan menggunakan single quote'...'
# 2. dengan menggunakan double quote "..."

data='Menggunakan single quote'
print(data)

data="Menggunakan double quote"
print(data)

print('''Halo, apa kabar?''')
print('''Halo, apa kabar?''')
print("ini adalah hari jum'at ")

#2. Menggunakan tanda \
#membuat tanda ' menjadi string

print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

#backlash 
print("C:\\user\\Ucup")

#tab
print("ucup\t\t\totong, semakin jauhan")

#backspace
print("ucup \botong, jadi deketan")

#newline
print("Baris pertama.\nBaris kedua.")#LF -> Line feed ->unix, macous, linux
print("Baris pertama.\rBaris kedua")#CR -> carriage return-> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows
#3. String literal atau raw
#hati-hati
print('C:\new folder') # akan salah pathnya
# menggunakan raw string
print(r'C:\new folder')

#multiline literal string
print("""
Nama : Raka
Kelas : A2 UNIVESITAS
""")
# multiline literal string dan RAW
print(r"""
Nama : Raka
Kelas : A2 UNIVERSITAS\new normal 
Website : www.raka.com/newID
""")