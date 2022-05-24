ropper --file /bin/ls --search "sub eax"

ropper --file /bin/ls --semantics rax==0

ropper --file /bin/ls --type rop

ropper.py --file /bin/ls --search "sub eax" --badbytes 000a
