# nuovamoschealugano.ch

Landing campagna fundraising **Dar al-Salam** — Lega dei Musulmani in Ticino.

## Stack

- **Hugo extended** (≥ 0.160) come static site generator
- **Cloudflare Pages** come hosting (repo privato post-lancio)
- **i18n**: IT (master, default a root), AR (RTL), EN, SQ — DE/FR in V1.5
- **CSS** vanilla con design tokens, no framework
- **Google Fonts**: Philosopher (display), Inter (body), Montserrat (UI), Amiri+Tajawal (arabo)

## Struttura

```
.
├── hugo.toml                # config principale + params brand
├── data/counter.toml        # counter raccolta (aggiornato manualmente)
├── content/
│   ├── _index.md            # home IT (master)
│   ├── _index.ar.md         # home AR
│   ├── _index.en.md         # home EN
│   └── _index.sq.md         # home SQ
├── i18n/                    # stringhe UI per lingua
├── layouts/
│   ├── _default/baseof.html # template base
│   ├── index.html           # home one-pager
│   └── partials/            # nav, footer, sezioni
├── assets/css/              # tokens.css + main.css
└── static/CNAME             # custom domain GH Pages legacy
```

## Sviluppo locale

```sh
hugo serve --buildDrafts --bind 0.0.0.0
# apri http://localhost:1313
```

## Build produzione

```sh
hugo --gc --minify
# output in ./public/
```

## Aggiornare il counter

Edita `data/counter.toml`, aggiorna `raised`, `raised_formatted` e `updated`. Commit + push. Cloudflare Pages ricostruisce in ~30s.

```toml
raised = 500000              # numero
raised_formatted = "500'000" # versione visibile (formato CH)
updated = "10 maggio 2026 alle 19:00"
```

## Branch strategy

- `main` → lancio pubblico (placeholder finché non finalizziamo)
- `develop` → lavoro in corso; Cloudflare Pages serve preview su `develop.moschealugano-website.pages.dev`

## Deploy Cloudflare Pages — config richiesta

| Campo | Valore |
|---|---|
| Framework preset | **Hugo** |
| Build command | `hugo --gc --minify` |
| Build output directory | `public` |
| Environment variable | `HUGO_VERSION` = `0.160.1` |

## Stato corrente (V0.4)

- ✅ TOP NAV con language switcher
- ✅ Hero con counter inline
- ✅ Footer con lockup + IBAN + lingue
- ⏳ § 2 Progetto — scaffold (gallery, donut budget, callout Fase 1, callout 6 appartamenti)
- ⏳ § 3 Donare — scaffold (tab matrix Carta/Bonifico/TWINT/Altre piattaforme)
- ⏳ § 4 Perché ora — scaffold (storytelling Voce A)
- ⏳ § 5 Voci — scaffold (carousel testimonianze)
- ⏳ § 6 FAQ — scaffold (accordion 8 domande)
- ⏳ § 7 Trasparenza — scaffold parziale
