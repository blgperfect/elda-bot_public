![Project Logo](https://cdn.discordapp.com/attachments/1102406059722801184/1387886546300043264/0C5431CA-4920-413C-BBC7-0F18DA8C3D15.png)

# Elda-Bot

Salut et bienvenue dans le projet **Elda-Bot** !

> ⚠️ **Deux points importants**  
> 1. Ce dépôt contient mes commandes jugées fonctionnelles. Ce n’est **pas** mon GitHub principal.  
> 2. Vous êtes libres de copier et reproduire ce code, **à condition** d’en garder la paternité (crédit à l’auteur).

---

## 📢 Inviter Elda  
Pour voir l’avancement des commandes et tester le bot sur votre serveur test, ajoutez **Elda** via ce lien :  
<https://discord.com/oauth2/authorize?client_id=1387873062841745479>  
> ❗ Elda n’étant pas encore terminée, elle n’est pas toujours en ligne.

---

## 🗂️ Structure du projet

- **`elda.py`**  
  Fichier principal (équivalent de `bot.py`)—lancez votre bot à partir d’ici.  
- **`.env`**  
  Renommez `example.env` en `.env`, et renseignez-y vos variables d’environnement (token, MongoDB URI, etc.).  
- **`config/params.py`**  
  Adaptez les constantes (couleurs, messages, emojis…) selon vos préférences.  
- **`requirements.txt`**  
  Liste des dépendances à installer avant de lancer le bot.  

---

## ⚙️ Installation

### Prérequis
- Python **3.10+**
- Git
- (Optionnel) Environnement virtuel (`venv`, `pyenv`, etc.)

### Sous macOS / Linux

```bash
# 1. Cloner le dépôt
git clone https://github.com/blgperfect/elda-bot_public.git
cd elda-bot_public


# 2. (Optionnel) Créer et activer un venv
python3 -m venv .venv
source .venv/bin/activate

# 3. Installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt

# 4. Configurer
cp example.env .env
# Éditez .env et config/params.py selon vos infos

# 5. Lancer le bot
python elda.py
````

### Sous Windows (PowerShell)

```powershell
# 1. Cloner le dépôt
git clone https://github.com/blgperfect/elda-bot_public.git
cd elda-bot_public


# 2. (Optionnel) Créer et activer un venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Installer les dépendances
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Configurer
copy example.env .env
# Éditez .env et config/params.py selon vos infos

# 5. Lancer le bot
python elda.py
```

---

## 🤝 Contribution

Les pull-requests sont les bienvenues !
Merci de respecter la licence informelle : conservez toujours un crédit à l’auteur original.

---

© 2025 Melodie(xxmissr) – Elda-Bot

```

