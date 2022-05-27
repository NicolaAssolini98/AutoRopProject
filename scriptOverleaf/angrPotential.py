import angr, angrop

p = angr.Project("/bin/ls")  # Create angr project
rop = p.analyses.ROP()  # Create ROP object
rop.find_gadgets()  # Find every gadgets in binary
chain = rop.set_regs(rax=0x1337, rbx=0x56565656)  # Build ROP chain setting register
chain.payload_str()  # Print bytes of ROP chain
# output:
b'\xb32@\x00\x00\x00\x00\x007\x13\x00\x00\x00\x00\x00\x00\xa1\x18@\x00\x00\
    \x00\x00\x00VVVV\x00\x00\x00\x00'

chain.print_payload_code()  # Print string of ROP chain
# output:
chain = b""
chain += p64(0x410b23)  # pop rax; ret
chain += p64(0x1337)
chain += p64(0x404dc0)  # pop rbx; ret
chain += p64(0x56565656)

# Calling functions
chain = rop.func_call("read", [0, 0x804f000, 0x100])

# Adding values to memory
chain = rop.add_to_mem(0x804f124, 0x41414141)

# Chains can be added together to chain operations
chain = rop.write_to_mem(0x61b100, b"/home/ctf/flag\x00") + \
        rop.func_call("open", [0x61b100, os.O_RDONLY]) + \
        rop.write_to_mem(0x61b100, b"/bin/sh\0")
