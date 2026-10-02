# Presentation Outline (English, 8–10 minutes)

## Slide 1 — Title
**SecureMessage: HMAC Message Authentication Tool**
- Course: Information Security
- Topic: HMAC
- Standard: NIST FIPS PUB 198-1
- Team members

## Slide 2 — Problem and Motivation
- Data may be modified during storage or transmission.
- A plain hash does not, by itself, authenticate the sender.
- HMAC combines a hash function and a shared secret key.

## Slide 3 — HMAC Fundamentals
- HMAC = Keyed-Hash Message Authentication Code.
- Inputs: secret key + message + hash function.
- Output: authentication tag.
- Provides message integrity and authentication under the shared-key model.
- Does not encrypt the message.

## Slide 4 — How HMAC Works
1. Sender and receiver share a secret key.
2. Sender computes the HMAC tag.
3. Sender sends the message and tag.
4. Receiver recomputes the tag.
5. Matching tags → verification passes; mismatch → verification fails.

Formula:
`HMAC(K, text) = H((K0 ⊕ opad) || H((K0 ⊕ ipad) || text))`

## Slide 5 — Application Architecture
- UI: Streamlit
- HMAC: Python `hmac`
- Hash functions: SHA-256 / SHA-384 / SHA-512
- Random key generation: `secrets`
- Constant-time comparison helper: `hmac.compare_digest`

## Slide 6 — Features
- Generate HMAC
- Verify HMAC
- Detect message tampering
- Generate random demo key
- Optional file authentication

## Slide 7 — NIST Comparison
Use the standards comparison table in `REPORT.md`.
Be clear that the project is a prototype and is not formally validated.

## Slide 8 — Security Testing
- Correct key + unchanged message → pass
- Modified message → fail
- Wrong key → fail
- Modified tag → fail
- Empty key → rejected by UI

## Slide 9 — Live Demo
Generate tag → verify successfully → alter message → verify failure → try wrong key.

## Slide 10 — Limitations and Conclusion
- HMAC is not encryption.
- No non-repudiation.
- Key management remains critical.
- Prototype demonstrates the core HMAC workflow.
- Questions
