# Rubrica Python
Lavoro di gruppo con obiettivo di creare una rubrica utilizzando solo python.

---

## 🚀 Demo

Link alla demo (se disponibile):
👉 [https://tuo-progetto-demo.com](https://tuo-progetto-demo.com)

---

## 📸 Screenshot

*Aggiungi immagini o GIF del progetto*

---

## ✨ Features

* Creazione, Modifica, Lettura  e eliminazione sul file rubrica.csv

---

## 🛠️ Tecnologie utilizzate

* Linguaggi: python3.12.10
* Framework: Tkinter
* Librerie: 
* Altro: 

---

## 📦 Installazione

```bash
# Clona il repository
git clone https://github.com/pianic2/its-python-rubrica.git

# Entra nella cartella
cd project

# Crea una virtual enviroment
python3 -m venv .venv
source ./.venv/bin/activate

# Installa le dipendenze
python3 install -r requirements.txt
```

---

## ▶️ Utilizzo

```bash
# Avvia il progetto
cd project
source ./.venv/bin/activate
python run.py
```
---

## ⚙️ Configurazione

Descrivi eventuali variabili d’ambiente:

```env
PROJECT_PATH=BASE_DIR/project
```

---

## 🧪 Test

```bash
python3 pytest
```

---

## 📁 Struttura del progetto

```
project/
│
├── data/
│   └── rubrica.csv          # File di database flat per i contatti
│
├── schemas/
│   └── rubrica_schema.py    # Definizione della struttura dati (es. classi Pydantic)
│
├── engine/
│   └── editor_rubrica.py    # Logica di elaborazione dati e interazione con il CSV
│
├── frames/
│   └── index.py             # Probabile interfaccia principale (GUI con Tkinter o simile)
│     ├── rubrica/             # Moduli per le operazioni CRUD (Create, Read, Update, Delete)
│     ├── add.py               # Funzione per aggiungere nuovi contatti
│     ├── delete.py            # Funzione per rimuovere contatti
│     ├── modify.py            # Funzione per aggiornare contatti esistenti
│     └── read.py   
│
└── run.py                   # Entry point del programma per avviare l'applicazione

```

---

## 🤝 Contribuire

I contributi sono benvenuti!

1. Fork del progetto
2. Crea un branch (`git checkout -b feature/nome-feature`)
3. Commit (`git commit -m 'Aggiunta feature'`)
4. Push (`git push origin feature/nome-feature`)
5. Apri una Pull Request

---

## 🐛 Segnalazione Bug

Apri una issue qui:
👉 [https://github.com/pianic2/its-python-rubrica/issues](https://github.com/pianic2/its-python-rubrica/issues)

---

## 📄 Licenza

Distribuito sotto licenza MIT. Vedi `LICENSE` per maggiori informazioni.

---

## 🙌 Autori

* Nome Autore – [@username](https://github.com/username)

---

## ⭐ Supporto

Se il progetto ti piace, lascia una ⭐ su GitHub!

---

Se vuoi, posso anche:

* adattarlo a un progetto specifico (es. Python, React, AI, ecc.)
* renderlo più “professionale” o più “minimal”
* aggiungere badge (build, coverage, versioni, ecc.)

Dimmi il tipo di progetto 👍
