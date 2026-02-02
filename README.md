# AI Password Strength Analyzer

A smart and interactive Python application that evaluates password strength using both **rule-based checks** and **AI-enhanced scoring**, helping users understand how secure their passwords are and how to improve them.

This tool combines **regular security metrics** with **AI/text analysis** to provide a more meaningful and user-friendly assessment of password quality.

---

## Project Overview

Choosing a strong password is one of the simplest yet most important steps in securing online accounts.  

This project detects weak passwords, scores them, and provides actionable feedback using **natural language analysis** and **security heuristics**.

With AI-powered suggestions, users gain insight into what makes a password strong **beyond traditional scoring systems**.

---

## Features

- **AI-based evaluation** using OpenAI (optional)
- Checks for:
  - Length
  - Uppercase & lowercase letters
  - Numbers
  - Special characters
  - Common patterns
  - Dictionary words
- Password strength score (Weak, Medium, Strong)
- Clear improvement suggestions
- Fully customizable and extendable

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| OpenAI API | AI-powered analysis (optional) |
| Regex | Pattern matching |
| CLI interface | Easy user interaction |

---

## Project Structure

AI-Password-Strength-Analyzer/  
│  
├── main.py - Main application script  
├── password_utils.py - Evaluation logic  
├── requirements.txt - Python dependencies  
├── README.md - Project documentation  
└── LICENSE - MIT License  

---

## Installation & Setup

### 1. Clone the Repository

    git clone https://github.com/Vaishuu-creator/AI-Password-Strength-Analyzer
    cd AI-Password-Strength-Analyzer

### 2. Create a Virtual Environment (optional)

    python -m venv venv
    source venv/bin/activate   # Linux / Mac
    venv\Scripts\activate      # Windows

### 3. Install Dependencies

    pip install -r requirements.txt

---

## How to Use

1. **Run the analyzer**
   ```bash
   python main.py
2. Then enter your password when prompted.
3. You will receive:
    - A **strength score**
    - Breakdown of detected issues
    - **AI-enhanced suggestions** (if enabled)

---

## What Makes It Unique

- Combines traditional password checks and AI evaluation
- Human-readable feedback
- Extensible and customizable
- Helpful for both beginners and power users

---

## Optional: AI Integration

You can integrate OpenAI to generate improved password suggestions:

1. Create an .env file
2. Add your OpenAI API key:
   ```bash
   OPENAI_API_KEY="your_api_key_here"
3. Run with AI enabled:
   ```bash
   python main.py --ai

---

## Use Cases

- Educational tools and workshops
- Security awareness programs
- Club/college projects
- Portfolio project showcasing Python & AI

---

## Future Enhancements

- GUI (Tkinter / CustomTkinter)
- Web version (Flask/Django)
- Integration with password managers
- Real-time API service

---

## License

This project is licensed under the MIT License — see the LICENSE file for details.

---

## Author

### Vaishali Murugesan
Final Year Computer Technology Student  
Aspiring Software & AI Engineer  

If you find this project helpful, please give it a star!
