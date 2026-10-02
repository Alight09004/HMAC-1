# SecureMessage: HMAC Message Authentication Tool
## Project Report

**Course:** Information Security  
**Project format:** NIST Cryptography & Vibe Coding  
**Topic:** HMAC — Keyed-Hash Message Authentication Code  
**Standard:** NIST FIPS PUB 198-1  
**Team members:** Nguyen Hoang Dieu Chau - Nguyen Lan Huong - Nguyen Hai Anh
**Class:** 24CS-GM  

## Abstract

This project develops SecureMessage, an educational application for generating and verifying HMAC tags for text messages. HMAC combines a cryptographic hash function with a shared secret key to support message authentication and integrity checking. The application uses Python's standard-library `hmac` module and provides positive and negative verification demonstrations. It also includes an optional file-authentication feature. The implementation is compared with the concepts and requirements described in NIST FIPS PUB 198-1. This project is a learning prototype and is not a claim of formal cryptographic-module validation.

## 1. Introduction

Information may be modified while stored or transmitted. A plain cryptographic hash can detect a change only when the expected digest is obtained through a trusted channel; by itself, it does not authenticate who created the data. HMAC addresses this limitation by combining a cryptographic hash function with a secret key shared by the originator and intended receiver.

The goal of this project is to demonstrate the generation and verification of HMAC tags through a simple user interface and to test how verification responds to modified messages, incorrect keys, and altered tags.

## 2. Objectives

1. Explain the purpose and operation of HMAC.
2. Build a working application to generate and verify HMAC tags.
3. Use an established cryptographic library rather than implementing primitives manually.
4. Test valid and invalid verification scenarios.
5. Compare design decisions with NIST FIPS PUB 198-1.
6. Document AI-assisted development and verify generated code through testing.

## 3. Background

### 3.1 Definitions

- **Cryptographic hash function:** maps input data to a fixed-length digest.
- **Message Authentication Code (MAC):** a value used to check message authenticity and integrity with a secret key.
- **HMAC:** a MAC construction that combines a secret key and a cryptographic hash function.
- **Secret key:** a value that must remain known only to authorized participants.
- **Authentication tag:** the HMAC output associated with a message.

### 3.2 How HMAC works

The sender and receiver share a secret key and agree on the hash algorithm. The sender computes an HMAC over the message and sends the message and tag. The receiver computes an HMAC over the received message using the same key and algorithm, then compares the newly computed tag with the received tag. A match supports acceptance of the message under the shared-key model; a mismatch means verification fails.

FIPS 198-1 defines the HMAC construction as:

`HMAC(K, text) = H((K0 ⊕ opad) || H((K0 ⊕ ipad) || text))`

Here, `K` is the shared secret key, `H` is the hash function, `ipad` and `opad` are the inner and outer padding values, `||` denotes concatenation, and `⊕` denotes bitwise XOR.

### 3.3 Security properties and limitations

HMAC supports message integrity and authentication among parties that share a secret key. It does not encrypt data, so the message may remain readable. It does not provide non-repudiation because any participant who knows the shared key can generate a valid tag. Its security depends on appropriate cryptographic choices and keeping the key secret.

## 4. System design

### 4.1 Architecture

The prototype has three layers:

1. **User interface:** Streamlit tabs for generation, verification, file authentication, and explanatory information.
2. **Cryptographic operations:** Python `hmac` and `hashlib` standard-library modules.
3. **Key generation:** Python `secrets` module for unpredictable demonstration keys.

### 4.2 Main use cases

- Generate an HMAC tag for a text message.
- Verify a message and supplied tag.
- Detect changes to a message.
- Detect use of a different key.
- Authenticate the bytes of an uploaded file.

### 4.3 Design decisions

| Decision | Implementation | Reason |
|---|---|---|
| HMAC implementation | Python `hmac` library | Uses a maintained standard-library implementation rather than handwritten cryptographic code. |
| Hash function | SHA-256 by default; SHA-384 and SHA-512 are selectable | Common cryptographic hash options for demonstration. |
| Tag representation | Hexadecimal | Easy to copy, compare, and include in test evidence. |
| Tag comparison | `hmac.compare_digest()` | Avoids ordinary early-exit string comparison for verification. |
| Random key generation | `secrets` module | Intended for security-sensitive random values. |
| Interface | Streamlit | Fast to build and easy to demonstrate in a browser. |

## 5. Implementation

The application is implemented in `app.py`. The Generate HMAC tab takes a message and secret key, then displays the tag. The Verify HMAC tab recomputes the expected tag and compares it with the supplied value. The File Authentication tab computes a tag over the exact uploaded file bytes.

The application rejects an empty key. It displays a warning when a manually entered key is shorter than 16 bytes. This is a basic educational safeguard, not a complete key-management policy. In a production application, key generation, storage, rotation, access control, and distribution require additional design.

## 6. Comparison with NIST FIPS PUB 198-1

| Standard concept or requirement | Project implementation | Assessment |
|---|---|---|
| HMAC combines a hash function with a secret key | Uses `hmac.new(key, message, hash_function)` | Conceptually aligned |
| Sender computes a tag over the message | Generate HMAC feature | Implemented |
| Receiver recomputes and compares the tag | Verify HMAC feature | Implemented |
| The secret key must be protected | Password-type key input; no persistent key storage | Partially addressed; UI masking is not a secure key vault |
| Appropriate hash function should be used | SHA-256, SHA-384, or SHA-512 via Python's library | Uses established hash algorithms; formal compliance is not claimed |
| Implementation security is the implementer's responsibility | Tests, limitations, and safe-library use are documented | Addressed at prototype level |
| Keys used for HMAC should not be reused for other purposes | Documentation advises dedicated keys | Documented, not technically enforced |

This table describes a classroom-level comparison, not a formal conformance assessment or cryptographic validation.

## 7. Testing plan and results

Run the automated tests with:

`python -m unittest -v tests.py`

| Test ID | Scenario | Expected result |
|---|---|---|
| T01 | Same message, same key, same tag | Verification passes |
| T02 | Message changed after tag generation | Verification fails |
| T03 | Different secret key | Verification fails |
| T04 | Authentication tag altered | Verification fails |
| T05 | Empty message with a valid non-empty key | HMAC can be generated and verified |
| T06 | Empty key entered in the UI | Application rejects the key |
| T07 | Short manually entered key | Application shows a warning |
| T08 | File content changes | A newly computed tag differs, except with negligible probability under the assumed security of HMAC |

**Evidence to capture:** the successful verification screen, the tampered-message failure screen, the wrong-key failure screen, and terminal output from the automated tests. Insert actual screenshots and observed results before submission; do not claim tests passed unless you ran them.

## 8. AI-assisted development

AI assistance was used to draft the application structure, explain cryptographic concepts, propose test cases, and prepare documentation. The generated implementation was reviewed against the standard and should be executed and tested by the team. The team remains responsible for understanding the code, verifying its behavior, and explaining its security limitations.

Before submission, add a real prompt log to `AI_USAGE.md`, record any changes made by team members, and note the test results actually observed.

## 9. Limitations and future improvements

- No secure key exchange or key vault.
- No user accounts, audit log, or key rotation.
- No formal cryptographic-module validation.
- File authentication is an educational extension, not a secure file-sharing protocol.
- Future work could include downloadable verification reports, test vectors, improved key lifecycle handling, and a dedicated key-management component.

## 10. Conclusion

SecureMessage demonstrates how HMAC can be used to authenticate messages and detect modification when the sender and receiver share a secret key. The project combines a simple interface with a standard cryptographic library, negative tests, and a standards comparison. The prototype illustrates core HMAC concepts but does not claim to be a production-ready or formally validated cryptographic system.

## References

1. National Institute of Standards and Technology (NIST), *FIPS PUB 198-1: The Keyed-Hash Message Authentication Code (HMAC)*, July 2008.
2. Python Software Foundation, Python documentation for `hmac`, `hashlib`, and `secrets`.
3. Streamlit documentation, for the application interface.
