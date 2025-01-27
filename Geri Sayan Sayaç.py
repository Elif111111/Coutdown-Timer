import time

def geri_sayim(saniye):
    """
    Belirtilen saniye boyunca geri sayım yapar.
    :param saniye: Geri sayımın süresi (saniye)
    """
    while saniye:
        dakika, saniye_kalan = divmod(saniye, 60)
        zaman_format = f"{dakika:02d}:{saniye_kalan:02d}"
        print(zaman_format, end="\r")  # Aynı satırı günceller
        time.sleep(1)  # 1 saniye bekle
        saniye -= 1

    print("Süre doldu!")

# Kullanım
sure = int(input("Kaç saniye geri sayım yapmak istiyorsunuz?: "))
geri_sayim(sure)
