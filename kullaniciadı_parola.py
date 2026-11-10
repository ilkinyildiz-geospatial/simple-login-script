kullaniciadi = "harita"
parola = "1964"

girilen_kullaniciadi = input("Kullanıcı adınız: ").strip()
girilen_parola = input("Parolanız: ").strip()

if girilen_kullaniciadi == kullaniciadi and girilen_parola == parola:
    print("Hoş geldiniz")
elif girilen_kullaniciadi != kullaniciadi and girilen_parola == parola:
    print("Hatalı kullanıcı adı")
elif girilen_kullaniciadi == kullaniciadi and girilen_parola != parola:
    print("Hatalı parola")
else:
    print("Kullanıcı adı ve parola hatalı")