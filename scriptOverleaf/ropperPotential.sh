ropper --file /bin/ls --search "sub eax"

ropper --file /bin/ls --semantic rax==0

ropper --file /bin/ls --search "sub eax" --badbytes 000a

ropper --file /bin/ls --search "sub eax" --badbytes 0a

# ropper --file /bin/ls --type rop