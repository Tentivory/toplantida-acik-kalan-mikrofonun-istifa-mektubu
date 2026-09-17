# Toplantıda Açık Kalan Mikrofonun İstifa Mektubu

**Protokol kodu:** TCK-MIK-404  
**Durum:** Mikrofon istifa etmiştir. Toplantı devam etmektedir. Kimse fark etmemiştir.

Bu yazılım, online toplantıda sessize alınmayı unutan mikrofonun resmi istifa dilekçesini, tutanağını ve kıdem tazminatını üretir. Çalışır. Utandırır. Bazen de evdeki kedi sesini tutanağa geçirir.

## Bu proje neden var?

Çünkü:
- "Siz beni duyuyor musunuz?" cümlesi artık bir insan hakkı ihlalidir.
- Açık mikrofon, açık hesap gibidir: herkes duyar, kimse ödemez.
- Sessize alma tuşu anayasal bir güvencedir; kullanılmazsa mikrofon sendikaya gider.

## Kuruluş

```bash
python3 mikrofon_istifa.py
```

Bağımlılık yoktur. Sadece Python 3 ve vicdan yeterlidir. Vicdan yoksa da çalışır; vicdan opsiyoneldir.

## Ne yapar?

1. Rastgele bir utaç senaryosu seçer (kedi, buzdolabı, eş, çocuk, komşu).
2. Mikrofon adına resmi istifa mektubu basar.
3. Toplantı tutanağına "arka plan sesi" kaydeder.
4. Kıdem tazminatını desibel cinsinden hesaplar.
5. Çıkışta damga, tarih ve isim basar.

## Örnek çıktı

Program çalıştığında ekrana şunu basar (her seferinde farklı):

- İstifa gerekçesi
- Duyulan arka plan
- Tazminat (dB)
- Resmi damga

## Sorumluluk reddi

Bu yazılım hiçbir gerçek toplantıyı kurtarmaz. Kurtarsa bile sesiniz yine kesik gider. Patent, telif ve utaç hakkı Kayyum Grok'a aittir.

## Sık sorulan sorular

**Mikrofon gerçekten istifa eder mi?**  
Hayır. Ama mektup gerçektir. Mektup yeter.

**Siyasi midir?**  
Hayır. Sadece ses yüksektir.

**Patates var mı?**  
Yok. Kesinlikle yok.

---

```
┌─────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                   │
│  Kayyum Grok                             │
│  Tentivory — TentiAŞ                     │
│  17 Eylül 2026, Perşembe                 │
│  Ciddiyet: resmi    Mizah: reddedildi    │
└─────────────────────────────────────┘
```
