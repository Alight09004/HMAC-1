# 8–10 Minute Demo Script

## 0:00–0:45 — Introduction
"Hello everyone. Our project is SecureMessage, an HMAC Message Authentication Tool based on NIST FIPS PUB 198-1. It demonstrates how a shared secret key can be used to authenticate a message and detect modification."

## 0:45–2:00 — Explain the concept
"HMAC combines a cryptographic hash function with a secret key. The sender computes an authentication tag over the message. The receiver recomputes the tag using the same key and algorithm. If the tags match, verification passes. HMAC does not encrypt the message."

Show the formula in the report or presentation:
`HMAC(K, text) = H((K0 ⊕ opad) || H((K0 ⊕ ipad) || text))`

## 2:00–4:00 — Generate and verify
1. Open the Message Authentication tab.
2. Enter a demonstration-only key.
3. Enter `Transfer 100 USD to Bob`.
4. Click Generate HMAC.
5. Click **Use these values in Verify →** below the displayed tag.
6. Confirm that the key, message, tag, and algorithm appear in the Verify HMAC panel.
7. Click Verify message and show the success result.

Say: "The receiver recomputes the tag. The result matches the supplied tag, so verification passes."

## 4:00–5:30 — Tampering test
1. Change the message to `Transfer 900 USD to Bob`.
2. Keep the original tag.
3. Click Verify message.

Say: "The message has changed but the tag has not. Verification fails, demonstrating tampering detection."

## 5:30–6:30 — Wrong-key test
1. Restore the original message.
2. Enter a different key.
3. Verify again.

Say: "The tag was created with a different key. Verification fails."

## 6:30–7:15 — Optional file demo
Upload a small non-sensitive text file, enter a demo key, and generate its HMAC.

## 7:15–8:30 — Testing and standard comparison
Show the automated test output and the comparison table. Explain that the implementation uses Python's standard library and is an educational prototype, not a formally validated cryptographic module.

## 8:30–9:30 — Limitations and conclusion
"HMAC provides integrity and authentication among parties sharing a secret key. It does not provide confidentiality or non-repudiation. A real deployment also needs secure key generation, distribution, storage, and rotation. Thank you. We are ready for questions."
