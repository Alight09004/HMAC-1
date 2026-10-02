# AI Usage Log — SecureMessage HMAC Project

> **Purpose:** This file documents how AI assistance was used during the development and reporting of the SecureMessage HMAC prototype.
>
> **Important:** This draft records AI-assisted activities reflected in the project workflow. Before submission, the team must confirm dates, prompts, code changes, and verification steps against what it actually did. Do not report a test as completed unless a team member ran it and recorded the result.

## 1. Project Context

- **Project:** SecureMessage — HMAC Message Authentication Tool
- **Topic:** HMAC and message authentication
- **Reference standard:** NIST FIPS PUB 198-1, *The Keyed-Hash Message Authentication Code (HMAC)*
- **Implementation approach:** Python application with a Streamlit user interface; Python's `hmac` and `hashlib` modules are used for HMAC operations.
- **Purpose of the prototype:** Demonstrate HMAC generation and verification, and show how verification responds to changed messages, incorrect keys, and altered tags.

## 2. Purpose and Scope of AI Assistance

AI assistance was used in the project workflow to help with:

1. **Project planning:** Organizing prototype features and proposing a simple user flow.
2. **Technical explanation:** Explaining HMAC concepts in accessible language, including the shared secret key, hash function, authentication tag, and the distinction between integrity/authentication and encryption.
3. **Code drafting and explanation:** Assisting with a Python/Streamlit prototype and explaining the roles of the interface and Python's cryptographic modules.
4. **Testing design:** Suggesting test cases for valid verification, message tampering, incorrect keys, modified tags, and invalid key input.
5. **Documentation and presentation:** Drafting report sections, slide structure, a demonstration flow, and short English explanations for the presentation.

AI output was treated as assistance, not as proof of correctness. The team remains responsible for reviewing the implementation, checking the standard, running the application and tests, and ensuring that the submitted report reflects observed results.

## 3. AI-Assisted Task Log

The following entries summarize tasks reflected in the project workflow. They are **not a substitute for the exact prompt history**. Add actual dates and amend each row to match the team's records before submission.

| Date | Task / prompt summary | AI output used | Required human review or verification | Status / changes |
|---|---|---|---|---|
| To confirm | Plan a small HMAC application for an information-security assignment and identify suitable features. | Project structure and feature suggestions. | Confirm the features match the assignment and can be demonstrated locally. | Review and record the final feature set. |
| To confirm | Draft a Python application with a Streamlit interface for generating and verifying HMAC tags. | Draft application code and UI structure. | Read the code; verify use of the standard `hmac` and `hashlib` modules; run the app locally and correct errors. | Record actual code changes and local run result. |
| To confirm | Explain Streamlit's role in the application. | Explanation of UI components versus HMAC computation. | Confirm that Streamlit handles user interaction/display while Python code performs HMAC operations. | Use only explanations that match the final code. |
| To confirm | Propose security tests for a valid message, modified message, incorrect key, modified tag, empty key, and short key. | Test scenarios and expected outcomes. | Run each applicable test; distinguish expected outcomes from observed outcomes; fix or document failures. | Add actual results and evidence. |
| To confirm | Help organize an English report and presentation, including a NIST comparison and a live demonstration. | Draft report/slide outline and presenter notes. | Check technical claims against FIPS PUB 198-1 and the implementation; remove unsupported claims. | Add final references and screenshots. |

## 4. Verification and Testing Record

Complete the **Actual result** and **Evidence** columns only after running the corresponding tests.

| Test ID | Test scenario | Expected result | Actual result | Evidence |
|---|---|---|---|---|
| ST-01 | Original message, correct secret key, and matching HMAC tag | Verification passes | To be recorded by the team | Screenshot or test output |
| ST-02 | Change the message but keep the original tag and key | Verification fails | To be recorded by the team | Screenshot or test output |
| ST-03 | Use a different key with the original message and tag | Verification fails | To be recorded by the team | Screenshot or test output |
| ST-04 | Modify the supplied HMAC tag | Verification fails | To be recorded by the team | Screenshot or test output |
| ST-05 | Submit an empty key | The application follows its documented input-validation rule; if empty keys are rejected, an error is shown | To be recorded by the team | Screenshot or test output |
| ST-06 | Submit a short key | The application follows its implemented policy; if configured as a warning, the warning is displayed | To be recorded by the team | Screenshot or test output |
| UT-01 | Run the automated unit-test suite | The test runner reports the actual pass/fail summary | To be recorded by the team | Terminal screenshot or saved output |

**Reporting rule:** Do not write “all tests passed” unless the team has run the relevant tests and retained the output. If a test fails, document the failure, investigate it, and record the fix or limitation.

## 5. NIST Standard Review

The team should use NIST FIPS PUB 198-1 as the primary reference for the HMAC construction and verify that descriptions in the report match the standard.

The review should cover:

- HMAC combines a secret key with a cryptographic hash function to produce an authentication tag.
- The receiver verifies a tag by computing the corresponding HMAC over the received message with the shared secret key and comparing the result with the supplied tag.
- HMAC supports message integrity checking and authentication in a shared-secret setting.
- HMAC does **not** encrypt the message and does **not** provide non-repudiation between parties who share the same key.
- Use of a standard library and comparison with a standard do not, by themselves, establish formal NIST validation or certification.

Before submission, the team should check the relevant passages of FIPS PUB 198-1 directly and add accurate section/page references to the report.

## 6. Human Review Checklist

Mark an item complete only after the team has performed it.

- [ ] Team members can explain the HMAC formula and the roles of the secret key, hash function, `ipad`, and `opad`.
- [ ] Team members can explain why the sender and receiver use the same secret key.
- [ ] The team has read and reviewed the relevant sections of NIST FIPS PUB 198-1.
- [ ] The application has been run locally by a team member.
- [ ] The final code has been reviewed and matches the report's description.
- [ ] Automated tests have been executed and the actual results recorded.
- [ ] The team has manually tested the key security scenarios and saved evidence.
- [ ] Empty-key and short-key behavior has been checked against the actual implementation.
- [ ] No real credentials, production secrets, or private keys were included in AI prompts.
- [ ] The report distinguishes implemented features, expected outcomes, and observed test results.
- [ ] The report does not claim NIST certification or formal compliance beyond the available evidence.
- [ ] References and technical claims have been checked by the team.
- [ ] Team members can explain which parts were AI-assisted and what human review was performed.

## 7. Limitations and Responsible Use

AI-generated code and explanations can contain mistakes, omit edge cases, or describe behavior that differs from the final implementation. Therefore, AI output must be reviewed and tested before it is relied upon.

This project is an educational prototype. Unless separately established through the appropriate process, it should not be described as a production-ready security product or as formally validated/certified by NIST. Secret-key distribution, secure storage, rotation, and broader operational security are outside the scope of a basic classroom demonstration and should be discussed as limitations.

## 8. Reference

National Institute of Standards and Technology (NIST). *FIPS PUB 198-1: The Keyed-Hash Message Authentication Code (HMAC).* The team should verify the official publication and use the exact reference format required by the instructor.

---

**Final submission note:** Replace every “To confirm” / “To be recorded by the team” placeholder, verify the prompt history, and tick only the checklist items actually completed. This document should be an honest record of the team's work, not a claim that unperformed verification has taken place.
