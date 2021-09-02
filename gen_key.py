from web3 import Web3
import getpass
import logging
from rsa.EncryptService import EncryptService

logging.basicConfig(filename="log_gen.log",
                    format='%(asctime)s %(message)s',
                    level=logging.INFO)

w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.defibit.io/'))

def main():
    private_key = getpass.getpass('Vui long nhap private key: ')
    if private_key:
        wallet_from_private_key = w3.eth.account.privateKeyToAccount(
                private_key)
        my_wallet = wallet_from_private_key.address
        print('Dia chi vi nay co dung voi private key tren?')
        print('Wallet Address: {}'.format(my_wallet))
        check_wallet = int(input("1-Dung | 0-Sai:"))
        if check_wallet == 1:
            check_accept_gen = int(input("Ban co dong y gen key khong?(1-Ok | 0-Deo): "))
            if check_accept_gen == 1:
                rsa_gen = EncryptService()
                key = rsa_gen.encrypt(private_key)
                logging.info(
                            'Wallet: {} - Code_Active: {}'.format(my_wallet, key))
                print('Gen Key thanh cong. Ban co the xem trong file log_gen.log')
            else:
                print('Eo gen thi thoi. Di boi cho dung tool -_-')
                input()
        else:
            print('Thoat tool roi nhap lai nhe')
            input()
    else:
        print('Eo nhap thi thoi -_-')
        input()

main()