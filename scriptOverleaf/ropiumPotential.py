from ropium import *

# Load binary
rop = ROPium(ARCH.X64)
rop.load('/lib/x86_64-linux-gnu/libc-2.27.so')

# Build the ROP chain
chain = rop.compile('rbx = [rax + 0x20]')

print(chain.dump())
# output:
#0x000000000009a851 (sub rax, 0x10; ret)
#0x0000000000130018 (mov rax, qword ptr [rax + 0x30]; ret)
#0x0000000000052240 (push rax; pop rbx; ret)

print(chain.dump('python'))
# output:
from struct import pack
off = 0x0
p = ''
p += pack('<Q', 0x000000000009a851+off) # sub rax, 0x10; ret
p += pack('<Q', 0x0000000000130018+off) # mov rax, qword ptr [rax + 0x30]; ret
p += pack('<Q', 0x0000000000052240+off) # push rax; pop rbx; ret

print(chain.dump('raw'))
# output:
b'Q\xa8\t\x00\x00\x00\x00\x00\x18\x00\x13\x00\x00\x00\x00\x00@"\x05\x00\x00\x00\x00\x00'

# Bytes that should not appear in the ropchain
rop.bad_bytes = [0x00, 0x0a, 0x0b]

# Register that should not be clobbered by the ropchain
rop.keep_regs = ['rsi', 'rdx']

# Enable/Forbid ropchain to dereference registers that might hold invalid addresses
# Safe mode is 'True' by default
rop.safe_mem = False
