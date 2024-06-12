# Prodigy_CS_Task4

## ⌨️ Simple Keylogger
Internship Task 4 at Prodigy InfoTech

## Overview🧐
This repository contains a basic keylogger program implemented in Python. The keylogger records and logs keystrokes, saving them to a file. **Note**: Ethical considerations and permissions are crucial for projects involving keyloggers. Ensure you have explicit consent from users before deploying this tool.

## Theoretical Explanation🧠

### Cybersecurity Topics
#### ⌨ 🖲Keyloggers:
Keyloggers are tools that capture and log keystrokes made by a user. While they can be used for legitimate purposes, such as monitoring employee activity or recovering lost data, they are often associated with malicious activities, like stealing sensitive information. It is important to handle such tools responsibly and ethically.

### ⚖ Ethical Considerations:
- **Consent**: Always obtain explicit consent from users before deploying a keylogger.
- **Legality**: Ensure that the use of a keylogger complies with local laws and regulations.
- **Privacy**: Be transparent about the data being collected and how it will be used.

## 💎Features
- Logs keystrokes to a file named `keylogs.txt`.
- Captures regular keys, special keys (like space and enter), and handles special key events.
- Stops logging when the `ESC` key is pressed.

## 📌Requirements
### Software:
- Python 3.x
- PyCharm IDE (or any other Python-compatible IDE)
### Hardware:
- A computer with a working keyboard.
### Python Libraries:
- `pynput`: For capturing keyboard events.

## 🧩Installation
1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/yourusername/simple-keylogger.git](https://github.com/mrudula0003/Prodigy_CS_Task4)
   cd Prodigy_CS_Task4
   ```
2. **Install the Required Library**:
   ```bash
   pip install pynput
   ```

## ▶ Usage
1. **Open the Project in PyCharm**:
   - Open PyCharm and load the project directory.
2. **Run the Program**:
   - Execute the Python script from within PyCharm or from the command line:
     ```bash
     python keylogger.py
     ```
3. **Monitor Keylogs**:
   - The keystrokes will be logged into the `keylogs.txt` file located in the same directory as the script.
4. **Stop the Keylogger**:
   - Press the `ESC` key to stop the keylogger.

## 🧾Code Explanation
- **Importing Libraries**: The `pynput` library is imported to capture keyboard events.
- **Logging Keystrokes**: The `on_press` function logs regular keys and handles special keys (space, enter, etc.).
- **Stopping the Keylogger**: The `on_release` function stops the keylogger when the `ESC` key is pressed.
- **Listener**: The keyboard listener is set up to call the `on_press` and `on_release` functions accordingly.

## Thanks🙌
To the open-source community for providing the necessary tools and libraries.

## Contributing🤝
Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue.

---

⚠ *Disclaimer*: This tool is intended for educational purposes only. Always ensure you have proper authorization before using a keylogger.
