# 🤖 Instagram Automation using Python & Selenium

This project automates Instagram tasks using **Python** and **Selenium WebDriver**.

The script:
- Logs into Instagram using dummy credentials
- Navigates to the `@cbitosc` profile
- Clicks the **Follow** button (if not already following)
- Extracts the **profile name**
- Saves the output to a text file (`output.txt`)

> ⚠️ **Disclaimer**: This script is for **educational use only**. Do not use your real account. Instagram may restrict or block accounts for automated actions.

---

## 📁 Folder Structure

```plaintext
instagram-automation/
├── instagram_bot.py     # Automation script
├── output.txt           # Profile info output
└── README.md            # Project documentation
```

---

## 🛠️ Technologies Used

- Python 3
- Selenium
- WebDriver Manager
- Google Chrome + ChromeDriver

---

## 🚀 Features

- ✅ Automated Instagram login
- ✅ Navigate to a public profile (`@cbitosc`)
- ✅ Clicks **Follow** if not already followed
- ✅ Extracts **profile name**
- ✅ Writes output to `output.txt`

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/23241a6749/instagram-automation.git
cd instagram-automation
```

### 2. Install Python Dependencies

```bash
pip install selenium webdriver-manager
```

> If using a specific Python version:
```bash
python3 -m pip install selenium webdriver-manager
```

### 3. Set Your Dummy Credentials

Open `instagram_bot.py` and update these lines:

```python
USERNAME = "your_dummy_username"
PASSWORD = "your_dummy_password"
```

---

## ▶️ Running the Script

Simply run the following command in the terminal:

```bash
python instagram_bot.py
```

The script will:
- Open Chrome
- Log in to Instagram
- Visit the `@cbitosc` page
- Click follow (if needed)
- Save the following to `output.txt`

---

## 📄 Example Output (`output.txt`)

```plaintext
Profile: cbitosc
Name: CBIT OSC
```

---

## 💡 Notes

- Instagram's frontend may change — if the script fails, update XPath selectors accordingly.
- `time.sleep()` is used for simplicity. For production, consider using `WebDriverWait`.
- `webdriver-manager` auto-handles ChromeDriver installation and versioning.

---

## ⚠️ Disclaimer

This script is intended for **educational and non-commercial use only**.

Automating actions on Instagram may **violate their Terms of Service**. Use only with **dummy accounts**.  
Instagram may **block, restrict, or shadowban** accounts that use automation.

---

## 🙋 Author

**GitHub:** [23241a6749](https://github.com/23241a6749)

Contributions and feedback welcome!
