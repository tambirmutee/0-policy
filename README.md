# 🛡️ 0-Policy – CSP Security Scanner 🕵️‍♂️

**0-Policy** is a terminal-based tool for analyzing [Content-Security-Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) headers.  
It helps identify weak or misconfigured CSP directives, dangerous sources, and known bypass patterns.

---

## 🔍 Features

- 🚀 Scan single or multiple URLs
- 🧩 Parse and highlight insecure CSP directives
- 🔓 Detect bypass patterns using custom JSON database
- 📄 Export results as JSON or TXT reports
- 🌐 Multilingual support (English 🇬🇧 & Turkish 🇹🇷)
- ⚙️ Custom timeout, user-agent and output directory settings

---

## 📦 Installation

```bash
git clone https://github.com/tambirmutee/0-policy.git
cd 0-policy
pip install .
```

Or if you want to install requirements manually:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### ▶️ Run from terminal

```bash
python run.py
```

### 🛠️ Entry point (after install)

```bash
0-policy
```

Then follow the interactive menu to:
- Scan a single URL
- Scan a file of URLs
- Generate reports
- Change configuration

---

## 📁 Directory Structure

```
0-policy/
├── data/                    # CSP bypass patterns and config file
│   ├── bypass_patterns.json
│   └── config.json
├── zeropolicy/              # Main Python package
│   ├── main.py
│   ├── fetcher.py
│   ├── analyzer.py
│   ├── bypass_checker.py
│   ├── parser.py
│   ├── config.py
│   └── langs/
│       ├── tr.py
│       └── en.py
├── run.py
├── setup.py
├── requirements.txt
└── LICENSE
```

---

## 🧪 Example Output

![Terminal Screenshot](docs/screenshot.png)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

PRs welcome! Open an issue or fork the project and improve it.
