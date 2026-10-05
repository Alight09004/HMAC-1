import hashlib
import hmac
import secrets

import streamlit as st


st.set_page_config(page_title="SecureMessage | HMAC Tool", page_icon="🔐", layout="wide")

st.title("🔐 SecureMessage")
st.subheader("HMAC Message Authentication Tool")
st.caption(
    "A learning prototype based on NIST FIPS PUB 198-1. "
    "It demonstrates message authentication and integrity verification."
)

with st.sidebar:
    st.header("Cryptographic settings")
    algorithm = st.selectbox(
        "Hash algorithm",
        ["SHA-256", "SHA-384", "SHA-512"],
        index=0,
        key="hash_algorithm",
    )
    st.info("The sender and receiver must use the same secret key and hash algorithm.")
    st.markdown("**Important:** HMAC authenticates data; it does not encrypt or hide the message.")

hash_map = {
    "SHA-256": hashlib.sha256,
    "SHA-384": hashlib.sha384,
    "SHA-512": hashlib.sha512,
}
hash_fn = hash_map[algorithm]


def calculate_hmac(key: bytes, message: bytes) -> str:
    return hmac.new(key, message, hash_fn).hexdigest()


def valid_key(key_text: str) -> bytes:
    key = key_text.encode("utf-8")
    if not key:
        raise ValueError("The secret key cannot be empty.")
    return key


def generate_random_key() -> None:
    """Populate the key input with a cryptographically random 256-bit key."""
    st.session_state.generate_key = secrets.token_hex(32)


def sync_generated_to_verify() -> None:
    """Copy the last generated sender payload into the receiver fields."""
    payload = st.session_state.get("generated_payload")
    if not payload:
        return

    st.session_state.verify_key = payload["key"]
    st.session_state.verify_message = payload["message"]
    st.session_state.verify_tag = payload["tag"]
    st.session_state.hash_algorithm = payload["algorithm"]
    st.session_state.sync_notice = True


tab_message, tab_file, tab_about = st.tabs(
    ["Message Authentication", "File Authentication", "About HMAC"]
)

with tab_message:
    st.caption(
        "Create a tag on the left, then send the exact values to the verification panel in one click."
    )
    generate_panel, verify_panel = st.columns(2, gap="large")

    with generate_panel:
        with st.container(border=True):
            st.markdown("### Generate HMAC")
            st.write("Create an authentication tag from a message and shared secret key.")

            key_field, random_key_action = st.columns([3, 2])
            with key_field:
                gen_key_text = st.text_input(
                    "Secret key (UTF-8 text)",
                    type="password",
                    key="generate_key",
                    help=(
                        "For a real system, use a securely generated key and store it "
                        "in a secret manager."
                    ),
                )
            with random_key_action:
                st.write("")
                st.write("")
                st.button(
                    "Generate random key",
                    use_container_width=True,
                    on_click=generate_random_key,
                )

            message = st.text_area(
                "Message",
                value="Transfer 100 USD to Bob",
                height=120,
                key="generate_message",
            )

            if st.button("Generate HMAC", type="primary", use_container_width=True):
                try:
                    key = valid_key(gen_key_text)
                    tag = calculate_hmac(key, message.encode("utf-8"))
                    st.session_state.generated_payload = {
                        "key": gen_key_text,
                        "message": message,
                        "tag": tag,
                        "algorithm": algorithm,
                    }
                    st.session_state.generation_notice = True
                except ValueError as exc:
                    st.session_state.pop("generated_payload", None)
                    st.error(str(exc))

            generated_payload = st.session_state.get("generated_payload")
            if generated_payload:
                if st.session_state.pop("generation_notice", False):
                    st.success("HMAC generated successfully.")

                st.markdown("**Authentication tag (hex)**")
                st.code(generated_payload["tag"], language=None)
                st.caption(
                    f"Algorithm: HMAC-{generated_payload['algorithm']} · "
                    f"Tag length: {len(generated_payload['tag']) * 4} bits"
                )

                st.button(
                    "Use these values in Verify →",
                    use_container_width=True,
                    on_click=sync_generated_to_verify,
                    help=(
                        "Copies the key, message, HMAC tag, and hash algorithm "
                        "to the Verify panel."
                    ),
                )
                st.download_button(
                    "Download message and tag",
                    data=(
                        f"Algorithm: HMAC-{generated_payload['algorithm']}\n"
                        f"Message: {generated_payload['message']}\n"
                        f"HMAC: {generated_payload['tag']}\n"
                    ),
                    file_name="hmac_message.txt",
                    mime="text/plain",
                    use_container_width=True,
                )

                if len(generated_payload["key"].encode("utf-8")) < 16:
                    st.warning(
                        "This key is shorter than 16 bytes. Use a stronger, securely "
                        "generated key for better security."
                    )

    with verify_panel:
        with st.container(border=True):
            st.markdown("### Verify HMAC")
            st.write("Recompute the HMAC and compare it with the received authentication tag.")

            verify_key_text = st.text_input(
                "Shared secret key (UTF-8 text)",
                type="password",
                key="verify_key",
            )
            verify_message = st.text_area(
                "Received message",
                value="Transfer 100 USD to Bob",
                height=120,
                key="verify_message",
            )
            supplied_tag = st.text_input("Received HMAC tag (hex)", key="verify_tag")

            if st.session_state.pop("sync_notice", False):
                st.success("Generated values were copied here and are ready to verify.")

            if st.button("Verify message", type="primary", use_container_width=True):
                try:
                    key = valid_key(verify_key_text)
                    cleaned_tag = supplied_tag.strip().lower()
                    if not cleaned_tag:
                        st.error("Please enter the received HMAC tag.")
                    else:
                        expected_tag = calculate_hmac(key, verify_message.encode("utf-8"))
                        if hmac.compare_digest(expected_tag, cleaned_tag):
                            st.success("AUTHENTICATION PASSED — the tag matches.")
                            st.write(
                                "The message matches the supplied tag under this shared key "
                                "and algorithm."
                            )
                        else:
                            st.error("AUTHENTICATION FAILED — the tag does not match.")
                            st.write(
                                "The message, tag, key, or selected algorithm may differ "
                                "from the sender's values."
                            )
                except ValueError as exc:
                    st.error(str(exc))

with tab_file:
    st.markdown("### Authenticate a file")
    st.write("Generate or verify an HMAC for the exact bytes of an uploaded file.")

    st.markdown("#### Generate file HMAC")
    uploaded = st.file_uploader("Choose a file", key="file_to_sign")
    file_key_text = st.text_input(
        "File authentication key (UTF-8 text)", type="password", key="file_key"
    )
    if uploaded is not None and st.button("Generate file HMAC", type="primary"):
        try:
            key = valid_key(file_key_text)
            content = uploaded.getvalue()
            tag = calculate_hmac(key, content)
            st.success("File HMAC generated.")
            st.write(f"**File:** {uploaded.name}")
            st.write(f"**Size:** {len(content):,} bytes")
            st.code(tag, language=None)
            st.caption(
                "Keep the file, key, algorithm and tag associated correctly. "
                "Anyone who knows the secret key can create valid tags."
            )
        except ValueError as exc:
            st.error(str(exc))

    st.divider()
    st.markdown("#### Verify file HMAC")
    st.write("Upload the received file and enter the HMAC tag supplied with it.")
    file_to_verify = st.file_uploader("File to verify", key="file_to_verify")
    verify_file_key_text = st.text_input(
        "Shared secret key (UTF-8 text)", type="password", key="verify_file_key"
    )
    supplied_file_tag = st.text_input("Received file HMAC tag (hex)", key="verify_file_tag")
    if file_to_verify is not None and st.button("Verify file", type="primary"):
        try:
            key = valid_key(verify_file_key_text)
            cleaned_tag = supplied_file_tag.strip().lower()
            if not cleaned_tag:
                st.error("Please enter the received file HMAC tag.")
            else:
                expected_tag = calculate_hmac(key, file_to_verify.getvalue())
                if hmac.compare_digest(expected_tag, cleaned_tag):
                    st.success("FILE AUTHENTICATION PASSED — the tag matches this file.")
                else:
                    st.error("FILE AUTHENTICATION FAILED — the tag does not match this file.")
                    st.write(
                        "The file, tag, key, or selected algorithm may differ from the sender's values."
                    )
        except ValueError as exc:
            st.error(str(exc))

with tab_about:
    st.markdown("### What does HMAC provide?")
    st.markdown(
        """
- **Message integrity:** detects accidental or malicious changes when verification is performed correctly.
- **Message authentication:** supports verification that the message was created by someone who knows the shared secret key.
- **Shared-key model:** both sender and receiver must protect the same secret key.
- **Not encryption:** the message contents remain readable unless a separate encryption mechanism is used.
- **No non-repudiation:** because both parties share the key, HMAC does not prove which one created a tag to an outside party.
"""
    )
    st.markdown("### Implementation choices")
    st.markdown(
        f"""
- HMAC implementation: Python's standard-library `hmac` module.
- Hash function: **{algorithm}** (selectable in the sidebar).
- Tag encoding: hexadecimal.
- Verification: `hmac.compare_digest()` is used for comparison.
- Key generation: Python's `secrets` module.
"""
    )
    st.markdown("### Standard reference")
    st.write(
        "NIST FIPS PUB 198-1, *The Keyed-Hash Message Authentication Code (HMAC)*, "
        "especially Sections 3–6."
    )
    st.warning(
        "This is an educational prototype, not a formally validated cryptographic module "
        "or production key-management system."
    )
