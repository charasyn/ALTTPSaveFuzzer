import sys
import hexdump
sys.path.insert(1,"../fuzzer")
import fuzz_alttp as fuzz
with open('rom.srm','rb') as f:
    fdata = bytearray(f.read())
fdata_orig = bytearray(fdata)
sv = fuzz.SaveFile(fdata)
old_cksum = sv.mem[0x4fe:0x500]
sv.update_checksum(0)
new_cksum = sv.mem[0x4fe:0x500]
print("Old Data:")
print(hexdump.dump(fdata_orig))
print("New Data:")
print(hexdump.dump(sv.mem))
print('Old checksum:', old_cksum.hex())
print('New checksum:', new_cksum.hex())
if fdata_orig != sv.mem:
    print('UH-OH! Data differs!')
