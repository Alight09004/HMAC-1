import hashlib
import hmac
import unittest

def tag(key: bytes, message: bytes) -> str:
    return hmac.new(key, message, hashlib.sha256).hexdigest()

class HMACTests(unittest.TestCase):
    def setUp(self):
        self.key = b"correct horse battery staple"
        self.message = b"Transfer 100 USD to Bob"
        self.valid_tag = tag(self.key, self.message)

    def test_same_message_and_key_pass(self):
        self.assertTrue(hmac.compare_digest(tag(self.key, self.message), self.valid_tag))

    def test_modified_message_fails(self):
        changed = b"Transfer 900 USD to Bob"
        self.assertFalse(hmac.compare_digest(tag(self.key, changed), self.valid_tag))

    def test_wrong_key_fails(self):
        self.assertFalse(hmac.compare_digest(tag(b"wrong key", self.message), self.valid_tag))

    def test_modified_tag_fails(self):
        changed_tag = "0" + self.valid_tag[1:]
        self.assertFalse(hmac.compare_digest(tag(self.key, self.message), changed_tag))

    def test_empty_message_is_supported(self):
        empty_tag = tag(self.key, b"")
        self.assertTrue(hmac.compare_digest(tag(self.key, b""), empty_tag))

    def test_empty_key_is_technically_computable_but_not_recommended(self):
        # Python can compute this, but the app intentionally rejects empty keys.
        empty_key_tag = tag(b"", self.message)
        self.assertEqual(len(empty_key_tag), 64)

if __name__ == "__main__":
    unittest.main(verbosity=2)
