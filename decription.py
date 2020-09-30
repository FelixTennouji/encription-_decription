'''
Author: Felix Tennouji
Date: 2020-09-30 10:14:35
LastEditTime: 2020-09-30 16:00:55
LastEditors: Felix Tennouji
Description: 
  Text Encoding:UTF-8

Hello,Sion.
Good night,Sion.
Eden* There were only two,on the planet.
'''
import sys
ciphertext=input("请输入密文\n>>>")
keytext=input("请输入密钥\n>>>")
plaintext=""
keytext_cache=""
plaintext_cache=""
actual_value=0
expect_value=0
for ciphertext_cursor in range(0,len(ciphertext)):
    if ciphertext[ciphertext_cursor]=="%":
        expect_value=int(ciphertext[:ciphertext_cursor])
        break
    
if ciphertext_cursor+1==len(ciphertext):
    print("不合法密文或者密文核心分隔符被破坏")
    sys.exit(0)
ciphertext=ciphertext[ciphertext_cursor+1:]
for keytext_cursor in range(0,len(keytext)):
    if keytext[keytext_cursor]=='\\':
        keytext_cache=keytext_cache+"00092"
        continue
    keytext_cache=keytext_cache+"%05d"%ord(keytext[keytext_cursor])
ciphertext_cursor=0
keytext_cache_cursor=0
for ciphertext_cursor in range(0,len(ciphertext)):
    plaintext_cache+="%d"%((int(ciphertext[ciphertext_cursor])-int(keytext_cache[keytext_cache_cursor%len(keytext_cache)]))%10)
    keytext_cache_cursor+=1
for keytext_cache_cursor in range(0,len(keytext_cache)):
    actual_value+=int(keytext_cache[keytext_cache_cursor])
for plaintext_cache_cursor in range(0,len(plaintext_cache)):
    actual_value+=int(plaintext_cache[plaintext_cache_cursor])
if actual_value!=expect_value:
    print("密钥不正确或者密文遭到篡改")
    sys.exit(0)
for plaintext_cache_cursor in range(0,len(plaintext_cache),5):
    plaintext+=chr(int(plaintext_cache[plaintext_cache_cursor])*10000+int(plaintext_cache[plaintext_cache_cursor+1])*1000+int(plaintext_cache[plaintext_cache_cursor+2])*100+int(plaintext_cache[plaintext_cache_cursor+3])*10+int(plaintext_cache[plaintext_cache_cursor+4]))
print(plaintext)