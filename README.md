# spiderman-pdf-generator
Intern Project
🕷️ Spider-Man Hero Card PDF Generator

"With great power comes great responsibility — and great PDFs."
A Spider-Man themed web application that generates personalized Hero ID Card PDFs on the fly using Python, Flask, and ReportLab. Fill in your hero details and download a 2-page styled PDF instantly.

🌐 Live Demo

👉 View Live App
(Replace with your Render URL after deploying)

📸 What It Does

The user fills in a form on the website with:

Their hero name, alias, city, superpower, and personal quote
Strength, Agility, and Intelligence sliders (1–100)
They click Generate Hero Card PDF and instantly download a 2-page PDF that includes:

Page 1 — Hero ID Card

Spider-Man red/blue theme with web decorations
Hero name, alias, city, power, card number
Animated stat bars (Strength, Agility, Intelligence)
Custom hero quote with styled quote box
Official S.H.I.E.L.D. badge design
Page 2 — Hero Profile

Mission brief, psychological profile, and field notes
Auto-generated from user input
Spider silhouette and web corner decorations
🛠 Tech Stack

Tech	Purpose
Python 3.10+	Backend language
Flask	Web framework — handles the form and routes
ReportLab	PDF generation library
Gunicorn	Production web server
HTML + CSS + JS	Frontend form with Spider-Man theme

🔄 How It Works (Simple Explanation)

User fills form  →  Browser sends data to Flask  →  pdf_generator.py draws the PDF
→  Flask sends the PDF file back  →  Browser downloads it automatically
No database needed. Every PDF is generated fresh on request and deleted after download.

🎨 Customisation Ideas

What	Where
Change colours	pdf_generator.py → colour variables at the top
Add more stat bars	pdf_generator.py → draw_stat_bar() calls
Add more form fields	templates/index.html + app.py + pdf_generator.py
Change the theme	Replace red/blue with any hero's colours
Add a logo image	Use c.drawImage() in ReportLab
⚠️ Common Issues & Fixes

👤 Author
NAVIN E

Built as Task 4 of the Python Web Development curriculum.
Thwipped into existence with ❤️ and Python. 🕷️
