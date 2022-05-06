import angr 
import angrop

p = angr.Project("/bin/ls")
rop = p.analyses.ROP()
rop.find_gadgets()
# angrop includes methods to create certain common chains

# setting registers
chain = rop.set_regs(rax=0x1337, rbx=0x56565656)

# writing to memory 
# writes "/bin/sh\0" to address 0x61b100
chain = rop.write_to_mem(0x61b100, b"/bin/sh\0")

# calling functions
chain = rop.func_call("read", [0, 0x804f000, 0x100])

# adding values to memory
chain = rop.add_to_mem(0x804f124, 0x41414141)

# chains can be added together to chain operations
chain = rop.write_to_mem(0x61b100, b"/home/ctf/flag\x00") + rop.func_call("open", [0x61b100,os.O_RDONLY])

# chains can be printed for copy pasting into exploits
chain.print_payload_code()

print("Catena generata:" + chain)
