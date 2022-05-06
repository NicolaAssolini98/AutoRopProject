import angr 
import angrop

p = angr.Project("/bin/ls")
rop = p.analyses.ROP()
rop.find_gadgets()
chain = rop.set_regs(rax=0x1337, rbx=0x56565656)
chain.payload_str()
chain.print_payload_code()

print(chain)

