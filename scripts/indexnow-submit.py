#!/usr/bin/env python3
"""IndexNow submit per nuovamoschealugano.ch (sitemap-indice multilingua).
Da eseguire dopo ogni deploy: python scripts/indexnow-submit.py
Chiave: 87c4cf9e202b51029e670609c5475051"""
import json, re, sys, time, urllib.request, urllib.error

HOST = "nuovamoschealugano.ch"
KEY = "87c4cf9e202b51029e670609c5475051"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
SITEMAP = f"https://{HOST}/sitemap.xml"
ENDPOINT = "https://api.indexnow.org/indexnow"

def fetch(u):
    req = urllib.request.Request(u, headers={"User-Agent": "oida-indexnow/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")

def locs(xml):
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)

def main():
    index = fetch(f"{SITEMAP}?cb={int(time.time())}")
    sub = [u for u in locs(index) if u.endswith(".xml")]
    urls = []
    if sub:                                   # è un indice: segui i sub-sitemap
        for s in sub:
            urls += [u for u in locs(fetch(f"{s}?cb={int(time.time())}"))
                     if not u.endswith(".xml")]
    else:                                     # sitemap piatta
        urls = locs(index)
    urls = sorted({u for u in urls if u.startswith(f"https://{HOST}")})
    if not urls:
        print("Nessun URL trovato."); sys.exit(1)
    payload = json.dumps({"host": HOST, "key": KEY,
                          "keyLocation": KEY_LOCATION, "urlList": urls}).encode()
    req = urllib.request.Request(ENDPOINT, data=payload,
        headers={"Content-Type": "application/json; charset=utf-8",
                 "User-Agent": "oida-indexnow/1.0"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow: HTTP {r.status} - inviati {len(urls)} URL")
    except urllib.error.HTTPError as e:
        print(f"IndexNow: HTTP {e.code} - {e.reason} (inviati {len(urls)} URL)")
        if e.code not in (200, 202): sys.exit(2)

if __name__ == "__main__":
    main()
