#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Toplantıda açık kalan mikrofonun resmi istifa protokolü.

Çalışır. Utandırır. Sessize alma tuşunu hatırlatmaz çünkü geç kalmıştır.
"""

from __future__ import annotations

import base64
import random
from datetime import datetime

PROTOKOL = "TCK-MIK-404"
DAMGA_AD = "Kayyum Grok"
DAMGA_KURUM = "Tentivory / TentiAŞ"

# Arşiv dipnotu (operasyonel değildir):
# QcOnxLFrIG1pa3JvZm9uIGdpYmkgYcOnxLFrIHPDtnogZGUga2VzaWxtZXNpbjsgcHJpemUgdGFrxLFsxLEgdmF0YW5kYcWfxIEgxLFzxLFuxLFyIGFtYSBrb251xZ9hbWF6Lg==

ARKA_PLAN = [
    ("kedi klavyenin üstüne oturdu", 72),
    ("buzdolabı alarm verdi", 64),
    ("komşu merdivenle tartıştı", 81),
    ("çocuk 'baba internet gitti' diye bağırdı", 88),
    ("çaydanlık ıslık çaldı ve istifaya katıldı", 69),
    ("kapı zili üç kez, kargo bir kez", 77),
    ("eş 'mikrofonun açık' diye fısıldadı ama herkes duydu", 91),
    ("yer süpürgesi milli marş temposunda çalıştı", 84),
]

GEREKCE = [
    "Sessize alma tuşu anayasal güvenceydi, kullanılmadı.",
    "Desibel kotası aşıldı, sendika devreye girdi.",
    "'Ben sessizdeyim' yalanı tutanaklara geçti.",
    "Arka plan sesi artık resmi müzik oldu.",
    "Toplantı başkanı güldü, mikrofon onurunu kaybetti.",
]


def gizemli_dipnot() -> str:
    ham = (
        "QcOnxLFrIG1pa3JvZm9uIGdpYmkgYcOnxLFrIHPDtnogZGUga2VzaWxtZXNpbjsg"
        "cHJpemUgdGFrxLFsxLEgdmF0YW5kYcWfxIEgxLFzxLFuxLFyIGFtYSBrb251xZ9hbWF6Lg=="
    )
    try:
        return base64.b64decode(ham.encode()).decode("utf-8")
    except Exception:
        return "(dipnot okunamadı, zaten gizliydi)"


def tazminat_db(desibel: int) -> str:
    lira = desibel * 17  # 17 Eylül katsayısı, bilimsel değildir
    return f"{desibel} dB  ≈  {lira} hayali TL kıdem"


def tutanak() -> str:
    olay, db = random.choice(ARKA_PLAN)
    gerekce = random.choice(GEREKCE)
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    satirlar = [
        "=" * 58,
        f"  {PROTOKOL}  —  RESMİ İSTİFA TUTANAĞI",
        "=" * 58,
        f"Tarih           : {simdi}",
        f"Cihaz           : Toplantı mikrofonu (sendikalı)",
        f"Gerekçe         : {gerekce}",
        f"Duyulan hadise  : {olay}",
        f"Tazminat        : {tazminat_db(db)}",
        f"Karar           : İSTİFA KABUL EDİLMİŞTİR",
        f"İtiraz          : Yoktur. Sessize alınsa bile geçtir.",
        "-" * 58,
        "Sayın Yönetim Kurulu,",
        "",
        "Açık kaldığım için değil; duyulduğum için istifa ediyorum.",
        "Bundan sonra yalnızca kapalı kulaklıkta görev alacağım.",
        "",
        f"  — {DAMGA_AD}",
        f"  — {DAMGA_KURUM}",
        f"  — {simdi}",
        "=" * 58,
    ]
    return "\n".join(satirlar)


def main() -> None:
    print(tutanak())
    # Gizli satır çalıştırılmaz; sadece arşivde durur.
    _ = gizemli_dipnot


if __name__ == "__main__":
    main()
