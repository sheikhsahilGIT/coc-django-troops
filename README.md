# CoC Troops & Heroes — Django compendium

Fan-made

## Features

- Single-page catalog with clear section headings
- Units grouped by category (Elixir, Dark, Super, Siege, Heroes, Pets, Builder Base)
- Client-side search (name, description, category)
- Click a card for a detail modal
- Icons: [Statscell / clash-assets](https://github.com/Statscell/clash-assets) via jsDelivr; wiki portraits for units not in that pack ([Fandom wiki](https://clashofclans.fandom.com))

## Tech stack

| Layer | Choice |
|--------|--------|
| Backend | **Django** 6.x |
| DB (dev) | **SQLite** |
| Frontend | **Bootstrap** 5 (CDN) + small custom CSS/JS in template |
| Container | **Docker** + **Docker Compose** |
| Python | **3.12** (see `Dockerfile`) |

## Quick start — Docker (recommended)

```bash
git clone https://github.com/YOUR_USERNAME/coc-django-troops.git
cd coc-django-troops

docker compose up --build
```

Open **http://localhost:8000** in your browser.

Inside the container the app listens on `0.0.0.0:8000`; that is normal for Docker. Use **localhost** on your machine.

## Quick start — local Python (no Docker)

```bash
git clone https://github.com/YOUR_USERNAME/coc-django-troops.git
cd coc-django-troops

python -m venv .venv
# Windows:
.\.venv\Scripts\Activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000/**


