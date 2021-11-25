kalimatawal=input("Masukkan kalimat awal: ")
kalimatuntukdisisipan=input("Masukkan kata untuk disisipan: ")
kataindeks=int(input("Masukkan indeks: "))
hasil=f"{kalimatawal[:kataindeks]}{kalimatuntukdisisipan}{kalimatawal[kataindeks]}"

print(hasil)
