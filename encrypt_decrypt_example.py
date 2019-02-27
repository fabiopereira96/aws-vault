from AESCrypt import AESCipher

## Examples ##
senha = '1234'
senha_encrypt = AESCipher().encrypt(senha)

print('Senha: ' + senha)
print('Senha encrypt: ' + senha_encrypt)
print('Senha decrypt: ' + AESCipher().decrypt(senha_encrypt))