# Project Euler Solutions

Project Euler matematik ve algoritma problemleri için bağımsız Python 3 çözümleri deposu.

| Alan | Değer |
|---|---|
| **Kategori** | CLI / Algoritma |
| **Teknoloji** | Python 3 |
| **Port / URL** | — (Web sunucusu gerektirmez) |
| **Başlatıcı** | `python projectEuler<N>.py` |
| **Doğrulama** | `python -m py_compile projectEuler*.py` |

## Özellikler

- Sayı teorisi, kombinatorik, ızgara tarama ve diziler üzerine 20 bağımsız Python çözümü.
- Tutarlı dosya adlandırması: `projectEuler<ProblemNo>.py`.
- Problem metinleri için [Project Euler Arşivi](https://projecteuler.net/archives) referans alınır.

## Klasör Yapısı

```text
project-euler-solutions/
├── projectEuler1.py … projectEuler30.py   # Problem #1–#30 çözümleri
├── projectEuler836.py                     # Problem #836 çözümü
├── AGENTS.md                              # Mühendislik kuralları
├── .gitignore                             # Git yoksayma kuralları
└── README.md
```

## Kurulum ve Çalıştırma

Python 3 kurulu olmalıdır; harici paket gerekmez.

```sh
python projectEuler11.py
python projectEuler12.py
```

## Testler ve Doğrulama

```sh
python -m py_compile projectEuler*.py
```
