ropper --file ./primality_test --search "pop eax"
#0x08048606: pop eax; int 0x80;

ropper --file ./primality_test --search "pop eax"
#0x08048609: pop ebx; pop ecx; ret;

ropper --file ./primality_test --search "pop edx"
#0x0804860c: pop edx; ret;

ropper --f ./primality_test --string "/bin/sh"
#0x08048991  /bin/sh