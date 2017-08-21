from raiden_mps.crypto import privkey_to_addr

CHANNEL_MANAGER_ADDRESS = '0x794bf0bb5dcf528c4b631c699ff37e91257fac84'
TOKEN_ADDRESS = '0xa9a7b9864de5217a0d1431a21823360ba1c6af12'
TEST_SENDER_PRIVKEY = '558ce5d09417f127c89097f8c41def07883cbec094da79f5dddfd4590607f7c2'  # 0x005d
# TEST_SENDER_PRIVKEY = '028f5efe7cb1d42997603a05d85d744031d5d5b5d187b132a7d42bb8c0de2ad4'  # 0xe2e4
TEST_RECEIVER_PRIVKEY = 'b6b2c38265a298a5dd24aced04a4879e36b5cc1a4000f61279e188712656e946' # 0x004b
TEST_SECONDARY_RECEIVER_PRIVKEY = '883f724ea3fa17728f759d3999f92aa46fee224f24efc09e4a354ba3f7b29411'  # 0xd1Bf
API_PATH = "/api/1"
GAS_LIMIT = 150000
GAS_PRICE = 20 * 1000 * 1000 * 1000

TEST_SENDER_ADDR = privkey_to_addr(TEST_SENDER_PRIVKEY)
TEST_RECEIVER_ADDR = privkey_to_addr(TEST_RECEIVER_PRIVKEY)
