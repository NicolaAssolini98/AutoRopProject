ropper --file ./es --search "pop"
# ...
#0x08049234: pop ebp; ret;
#0x08049233: pop edi; pop ebp; ret;
# ...

ropper --file ./es --symbols
# ...
#56  FUNC     GLOBAL  add_bin
#57  FUNC     GLOBAL  add_sh
#61  FUNC     GLOBAL  exec_string
# ...

# Search function address in Ghidra