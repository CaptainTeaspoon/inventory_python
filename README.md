# inventory_python

# Python Inventarverwaltungssystem

Eine Django-basierte Inventarverwaltungsanwendung zur Verfolgung und Verwaltung von Inventargegenständen.

## Voraussetzungen

- Python 3.8 oder höher
- pip (Python Paket-Installer)
- Git (optional, zum Klonen des Repositories)

## Installation und Einrichtung

### 1. Repository klonen (optional, alternativ von USB-Stick) 

```bash
git clone https://github.com/CaptainTeaspoon/inventory_python.git
```

```bash
cd inventory_python
```

### 2. Virtuelle Umgebung erstellen

```bash
python -m venv venv
```

### 3. Virtuelle Umgebung aktivieren

**Unter Windows:**
```bash
venv\Scripts\activate
```

**Unter macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Django und Abhängigkeiten installieren

```bash
pip install django
```

Falls eine requirements.txt Datei vorhanden ist, alle Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

### 5. Datenbank einrichten

Die Anwendung ist aktuell für SQLite konfiguriert (Standard). Zur Einrichtung der Datenbank:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 6. Superuser erstellen (Admin-Konto)

```bash
python manage.py createsuperuser
```

Folgen Sie den Anweisungen, um ein Admin-Konto zu erstellen.

### 7. Entwicklungsserver starten

```bash
python manage.py runserver
```

Die Anwendung ist unter `http://127.0.0.1:8000/` erreichbar.

## Projektstruktur

```
inventory_python/
├── inventory_python/          # Hauptprojektverzeichnis
│   ├── __init__.py
│   ├── settings.py           # Django-Einstellungen
│   ├── urls.py              # URL-Konfiguration
│   └── wsgi.py              # WSGI-Konfiguration
├── mainapp/                 # Hauptanwendung
│   ├── middleware.py        # Benutzerdefinierte Middleware
│   └── auth_backends.py     # Benutzerdefinierte Authentifizierung
├── templates/               # HTML-Templates
├── manage.py               # Django-Verwaltungsskript
└── db.sqlite3             # SQLite-Datenbank (nach Migration erstellt)
```

## Funktionen

- Benutzerauthentifizierung mit benutzerdefiniertem Backend
- Login-erforderliche Middleware
- Admin-Interface für Inventarverwaltung
- Template-basiertes Frontend

## Zugriff auf die Anwendung

1. **Admin-Interface:** `http://127.0.0.1:8000/admin/`
   - Verwenden Sie die erstellten Superuser-Zugangsdaten

2. **Hauptanwendung:** `http://127.0.0.1:8000/`
   - Login ist aufgrund der LoginRequiredMiddleware erforderlich

## Fehlerbehebung

### Häufige Probleme

1. **Port bereits in Verwendung:**
```bash
python manage.py runserver 8001
```

2. **Datenbankfehler:**
   - Stellen Sie sicher, dass Sie Migrationen ausgeführt haben

3. **Modul nicht gefunden Fehler:**
   - Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist
   - Installieren Sie fehlende Pakete mit pip

### Hilfe erhalten

- Django-Dokumentation prüfen: https://docs.djangoproject.com/
- Fehlermeldungen im Terminal überprüfen
- Django-Debug-Seite prüfen
