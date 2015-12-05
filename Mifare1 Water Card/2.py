from smartcard.scard import *
import smartcard.util

hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)

assert hresult==SCARD_S_SUCCESS

hresult, readers = SCardListReaders(hcontext, [])

assert len(readers)>0

reader = readers[0]

hresult, hcard, dwActiveProtocol = SCardConnect(
    hcontext,
    reader,
    SCARD_SHARE_SHARED,
    SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)

#hresult, response = SCardTransmit(hcard,dwActiveProtocol,[0xFF,0x82,0x00,0x00,0x06,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF])

#print(response)
#print smartcard.util.toHexString(response)

def load_key():
    response = SCardTransmit(hcard,dwActiveProtocol,[0xFF,0x82,0x00,0x00,0x06,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF])
    print smartcard.util.toHexString(response[1])

def authenticate_block():
    response = SCardTransmit(hcard,dwActiveProtocol,[0xFF,0x86,0x00,0x00,0x05,0x01,0x00,0x01,0x60,0x00])
    print smartcard.util.toHexString(response[1])

def read_data():
    response = SCardTransmit(hcard,dwActiveProtocol,[0xFF,0xB0,0x00,0x01,0x10])
    print smartcard.util.toHexString(response[1])

def w_data():
    response = SCardTransmit(hcard,dwActiveProtocol,[0xFF,0xD6,0x00,0x01,0x10,0x60,0x60,0x61,0x61])
    print response #,[0xFF,0xD6,0x00,0x01,0x10,0x61,0x61,0x61,0x61,0x61,0x61,0x61,0x61,0x61,0x61,0x61,0x61,0x61,0x61,0x61,0x61])
    print smartcard.util.toHexString(response[1])

if __name__ == '__main__':
    load_key()
    authenticate_block()
    read_data()

    w_data()
    read_data()