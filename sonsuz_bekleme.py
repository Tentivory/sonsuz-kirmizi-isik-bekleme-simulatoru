#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Abartılı Kırmızı Işık Bekleme Simülatörü
Bu kod GERÇEKTEN çalışır. Koşturunca hayattan çaldığın saniyeleri görürsün.
"""

import time
import random
import sys

class KirmiziIsikBekleyicisi:
    def __init__(self):
        self.bekleme_suresi = 0
        self.telefon_kontrolu = 0
        self.ozgurluk_endeksi = 100  # Gizli metafor: beklemek özgürlüğü azaltır, tıpkı bazı uzun süreçler gibi
        
    def bekle(self):
        print("\n🚦 KIRMIZI IŞIK YANDI. EVREN DURDU.")
        print("Yeşil olmak üzere... (yalan)")
        
        while True:
            time.sleep(1)
            self.bekleme_suresi += 1
            self.telefon_kontrolu += random.randint(0, 3)
            self.ozgurluk_endeksi -= 0.1
            
            if self.bekleme_suresi % 5 == 0:
                mesajlar = [
                    f"Hala kırmızı... {self.bekleme_suresi} saniye geçti. Ömründen çaldı.",
                    "Karşıdaki sürücü de aynı şeyi düşünüyor: 'bu kadar da olmaz'",
                    f"Telefonu {self.telefon_kontrolu} kez kontrol ettin. Bildirim yok. Hayat yok.",
                    "Bu bekleme, aslında bir sabır testi. Tıpkı bazı şeylerin yeşile dönmemesi gibi...",
                    "Yaya geçidi yeşil ama sen araçtayın. Ironi."
                ]
                print(random.choice(mesajlar))
            
            if self.bekleme_suresi > 30:  # 30 saniye sonra merhamet
                print("\n🟢 YEŞİL OLDU! Ama sen zaten yaşlandın.")
                print(f"Toplam bekleme: {self.bekleme_suresi} saniye")
                print(f"Kalan özgürlük endeksi: {self.ozgurluk_endeksi:.1f} (gizli istatistik)")
                print("Artık geçebilirsin. Ya da geçme. Kırmızı daha eğlenceliydi.")
                break
            
            if self.bekleme_suresi == 15:
                print("\n⚠️  UYARI: Bu noktadan sonra hayatın anlamı sorgulanmaya başlar.")

if __name__ == "__main__":
    simulator = KirmiziIsikBekleyicisi()
    try:
        simulator.bekle()
    except KeyboardInterrupt:
        print("\n\nKaçtın. Ama kırmızı ışık seni hatırlayacak.")
        sys.exit(0)
