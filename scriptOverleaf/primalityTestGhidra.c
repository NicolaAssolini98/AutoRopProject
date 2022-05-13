void FUN_0804872d(void)

{
  char *pcVar1;
  size_t sVar2;
  int iVar3;
  undefined4 local_54;
  char local_50 [64];
  size_t local_10;
  
  printf("Enter a number: ");
  pcVar1 = fgets(local_50,0x200,stdin);
  if (pcVar1 == (char *)0x0) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  sVar2 = strlen(local_50);
  local_10 = sVar2;
  if ((sVar2 != 0) && (local_50[sVar2 - 1] == '\n')) {
    local_10 = sVar2 - 1;
    local_50[sVar2 - 1] = '\0';
  }
  iVar3 = strcmp(local_50,"/bin/sh");
  if (iVar3 == 0) {
    puts("Exploitation attempt detected! This incident will be reported.");
  }
  else {
    iVar3 = __isoc99_sscanf(local_50,&DAT_080489db,&local_54);
    if (iVar3 < 1) {
      puts("Please enter a number!");
    }
    else if ((int)local_54 < 2) {
      puts("Please enter a number greater than 1");
    }
    else {
      iVar3 = FUN_0804860e(local_54);
      if (iVar3 == 0) {
        printf("%d is definitely not a prime.\n",local_54);
      }
      else {
        printf("%d might be a prime.\n",local_54);
      }
    }
  }
  return;
}
