# 🕷️ Spider-Man Hero Card PDF Generator

> *"With great power comes great responsibility — and great PDFs."*

A Spider-Man themed web application that generates **personalized Hero ID Card PDFs on the fly** using Python, Flask, and ReportLab. Fill in your hero details and download a 2-page styled PDF instantly.

---

## 🌐 Live Demo

👉 **[View Live App](https://YOUR-APP-NAME.onrender.com)**  
*(Replace with your Render URL after deploying)*

---

## 📸 What It Does

The user fills in a form on the website with:
- Their hero name, alias, city, superpower, and personal quote
- Strength, Agility, and Intelligence sliders (1–100)

They click **Generate Hero Card PDF** and instantly download a 2-page PDF that includes:

**Page 1 — Hero ID Card**
- Spider-Man red/blue theme with web decorations
- Hero name, alias, city, power, card number
- Animated stat bars (Strength, Agility, Intelligence)
- Custom hero quote with styled quote box
- Official S.H.I.E.L.D. badge design

**Page 2 — Hero Profile**
- Mission brief, psychological profile, and field notes
- Auto-generated from user input
- Spider silhouette and web corner decorations

---

## 🛠 Tech Stack

| Tech | Purpose |
|------|---------|
| Python 3.10+ | Backend language |
| Flask | Web framework — handles the form and routes |
| ReportLab | PDF generation library |
| Gunicorn | Production web server |
| HTML + CSS + JS | Frontend form with Spider-Man theme |

---

## 📁 Project Structure

```
spiderman-pdf/
│
├── app.py              ← Flask web server + routes
├── pdf_generator.py    ← All PDF drawing logic (ReportLab)
├── requirements.txt    ← Python dependencies
├── Procfile            ← Tells Render/Railway how to run the app
├── README.md           ← This file
│
└── templates/
    └── index.html      ← Spider-Man themed HTML form
```

---

## 🚀 Run Locally (On Your Computer)

### Step 1 — Make sure Python is installed
Open a terminal/command prompt and type:
```bash
python --version
```
You need Python 3.8 or higher. Download from [python.org](https://python.org) if needed.

### Step 2 — Install the dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Run the app
```bash
python app.py
```

### Step 4 — Open in browser
Go to 👉 **http://localhost:5000**

Fill in the form, click the button, and your PDF downloads automatically!

---

## ☁️ Deploy to Render (Free Live URL)

**What is Render?** It's a free cloud platform that hosts Python web apps. Perfect for Flask.

### Step 1 — Push to GitHub

1. Go to [github.com](https://github.com) → Sign Up (free)
2. Click **New Repository** → name it `spiderman-pdf-generator` → Public → Create
3. Click **"uploading an existing file"**
4. Upload ALL files (keep the `templates/` folder structure):
   - `app.py`
   - `pdf_generator.py`
   - `requirements.txt`
   - `Procfile`
   - `README.md`
   - `templates/index.html`
5. Click **Commit changes**

> ⚠️ Make sure `templates/index.html` is inside a folder called `templates` when uploading.

### Step 2 — Deploy on Render

1. Go to 👉 [render.com](https://render.com) → Sign Up with your GitHub account (free)
2. Click **New +** → **Web Service**
3. Click **Connect a repository** → select `spiderman-pdf-generator`
4. Fill in the settings:

| Setting | Value |
|---------|-------|
| Name | `spiderman-pdf-generator` |
| Environment | `Python 3` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

5. Click **Create Web Service**
6. Wait 2–3 minutes while it builds
7. Your live URL appears at the top:

```
https://spiderman-pdf-generator.onrender.com
```

✅ **Share this link — anyone can visit it and generate their own Hero Card PDF!**

---

## 🔄 How It Works (Simple Explanation)

```
User fills form  →  Browser sends data to Flask  →  pdf_generator.py draws the PDF
→  Flask sends the PDF file back  →  Browser downloads it automatically
```

No database needed. Every PDF is generated fresh on request and deleted after download.

---

## 🎨 Customisation Ideas

| What | Where |
|------|-------|
| Change colours | `pdf_generator.py` → colour variables at the top |
| Add more stat bars | `pdf_generator.py` → `draw_stat_bar()` calls |
| Add more form fields | `templates/index.html` + `app.py` + `pdf_generator.py` |
| Change the theme | Replace red/blue with any hero's colours |
| Add a logo image | Use `c.drawImage()` in ReportLab |

---

## ⚠️ Common Issues & Fixes

| Problem | Fix |
|---------|-----|
| `ModuleNotFoundError: flask` | Run `pip install -r requirements.txt` again |
| PDF doesn't download | Check browser pop-up settings; allow downloads |
| Render build fails | Make sure `requirements.txt` has correct package names |
| `templates/` not found | Keep the `templates/` folder — don't move `index.html` out |
| Render app sleeps after 15 min | Free tier sleeps when idle; first visit takes ~30 seconds to wake |

---

## 📜 License

MIT License — use freely, remix boldly.

---

## 👤 Author

Built as **Task 4** of the Python Web Development curriculum.  
Thwipped into existence with ❤️ and Python. 🕷️

---

> *"Anyone can wear the mask. Anyone can be a hero."*
