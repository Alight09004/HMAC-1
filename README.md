# SecureMessage — HMAC Message Authentication Tool

**Course project:** NIST Cryptography & Vibe Coding  
**Topic:** HMAC (Keyed-Hash Message Authentication Code)  
**Primary standard:** NIST FIPS PUB 198-1  
**Implementation:** Python + Streamlit

## 1. Project overview

SecureMessage is an educational application that generates and verifies HMAC tags for messages. It also includes an optional file-authentication feature. The application demonstrates how a shared secret key and a cryptographic hash function can be used to verify message integrity and authenticate a message under the shared-key model.

## 2. Features

- Generate HMAC tags for text messages.
- Verify a received message against a supplied tag.
- Generate a random key for demonstration purposes.
- Detect message, key, or tag mismatches.
- Compute an HMAC for an uploaded file.
- Explain the security properties and limitations of HMAC.

## 3. Requirements

- Python 3.10 or newer recommended.
- Internet access is only needed to install Streamlit.
- The `hmac`, `hashlib`, and `secrets` modules are part of Python's standard library.

## 4. Run the application

Open a terminal in this project folder and run:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

Start the app:

```bash
streamlit run app.py
```

A browser tab should open automatically. If not, open the local URL printed in the terminal.

## 5. Run the tests

```bash
python -m unittest -v tests.py
```

The tests cover successful verification, message tampering, an incorrect key, a modified tag, and an empty message.

## 6. Suggested demo

1. Open **Generate HMAC**.
2. Enter a secret key such as `demo-key-please-change-123456`.
3. Enter `Transfer 100 USD to Bob`.
4. Generate and copy the tag.
5. Open **Verify HMAC** and enter the same key, message, and tag. Verification should pass.
6. Change the message to `Transfer 900 USD to Bob` while keeping the old tag. Verification should fail.
7. Restore the message but enter a different key. Verification should fail.
8. Optionally upload a file and generate its HMAC.

Use demonstration-only keys in class. Do not paste real passwords, API keys, or production secrets into the app.

## 7. Security notes and limitations

- HMAC does not encrypt messages.
- HMAC does not provide non-repudiation because multiple parties may know the shared key.
- Both parties must protect the shared secret key.
- The app uses Python's standard `hmac` implementation rather than implementing cryptographic primitives manually.
- The random-key button creates 32 random bytes represented as hexadecimal text. Because the current UI treats key input as UTF-8 text, this hexadecimal representation is used as the literal key text; it is still unpredictable, but its byte representation is ASCII hex characters.
- The app is a classroom prototype. It does not provide a secure key vault, user accounts, secure key exchange, or formal NIST module validation.

## 8. Standards reference

NIST, **FIPS PUB 198-1: The Keyed-Hash Message Authentication Code (HMAC)**, July 2008. See the official NIST Computer Security Resource Center for current publication status and related guidance before making claims about present-day compliance.

## 9. Deliverables checklist

- [ ] Source code (`app.py`)
- [ ] Test cases (`tests.py`)
- [ ] Test evidence/screenshots
- [ ] English report (`REPORT.md`)
- [ ] AI usage log (`AI_USAGE.md`)
- [ ] Demo plan (`DEMO_SCRIPT.md`)
- [ ] Presentation based on `PRESENTATION_OUTLINE.md`
