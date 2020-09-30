'''
Author: Felix Tennouji
Date: 2020-09-30 10:13:31
LastEditTime: 2020-09-30 12:18:04
LastEditors: Felix Tennouji
Description: 如果需要代码注释，等我起来看有没有空再加，此代码仅供参考
  Text Encoding:UTF-8

Hello,Sion.
Good night,Sion.
Eden* There were only two,on the planet.
'''

plaintext=input("请输入明文\n>>>")
keytext=input("请输入密钥\n>>>")
ciphertext=""
plaintext_cache=""
keytext_cache=""
plaintext_cursor=0
keytext_cursor=0
for plaintext_cursor in range(0,len(plaintext)):
    if plaintext[plaintext_cursor]=='\\':
        plaintext_cache=plaintext_cache+"00092"
        continue
    plaintext_cache=plaintext_cache+"%05d"%ord(plaintext[plaintext_cursor])
for keytext_cursor in range(0,len(keytext)):
    if keytext[keytext_cursor]=='\\':
        keytext_cache=keytext_cache+"00092"
        continue
    keytext_cache=keytext_cache+"%05d"%ord(keytext[keytext_cursor])
sum=0
for plaintext_cache_cursor in range(0,len(plaintext_cache)):
    sum+=int(plaintext_cache[plaintext_cache_cursor])
for keytext_cache_cursor in range(0,len(keytext_cache)):
    sum+=int(keytext_cache[keytext_cache_cursor])
plaintext_cache_cursor=0
keytext_cache_cursor=0
for plaintext_cache_cursor in range(len(plaintext_cache)):
    ciphertext+="%d"%((int(plaintext_cache[plaintext_cache_cursor])+int(keytext_cache[keytext_cache_cursor%len(keytext_cache)]))%10)
    keytext_cache_cursor+=1

ciphertext="%d"%sum+"%"+ciphertext
print(ciphertext)

