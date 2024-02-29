# Password Manager

This Password Manager is a simple yet powerful Python application designed to help users generate, store, and retrieve their passwords securely. Built with Tkinter for the GUI, it provides an easy-to-use interface for managing website credentials.

## Features

- **Password Generation**: Automatically generate strong, random passwords to enhance security.
- **Secure Storage**: Save website, email, and password combinations in a local JSON file for later access.
- **Password Retrieval**: Quickly search for and retrieve stored passwords based on the website name.
- **Clipboard Support**: Automatically copy generated passwords to the clipboard for easy pasting.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher installed on your machine.
- Tkinter installed (comes with Python for Windows; may need separate installation on Linux/MacOS).

## Setup and Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Mas73rs/password-manager
cd password-manager
```

Ensure you have `pyperclip` installed for clipboard operations:

```bash
pip install pyperclip
```

## Usage

To start the application, run:

```bash
python main.py
```

1. **Generate Password**: Click on the "Generate Password" button to create a new, strong password.
2. **Add Password**: Enter the website, your email/username, and password. Press "Add" to save the credentials.
3. **Find Password**: Enter a website name and click "Search" to retrieve stored credentials.

## Contributing

Contributions to the Password Manager project are welcome! Here are a few ways you can help:

- Report bugs and suggest enhancements.
- Submit pull requests with bug fixes or new features.

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgements

- This project uses [Pyperclip](https://github.com/asweigart/pyperclip) for clipboard operations.