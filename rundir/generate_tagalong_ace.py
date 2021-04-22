import sys
import random

sys.path.insert(1,"../fuzzer")
import fuzz_alttp as fuzz

tagalong_value = 15

random.seed(1)
random_data = (0 for _ in range(0x2000))
sf = fuzz.SaveFile(bytearray(random_data))
sv = sf.saves[5]
poke_values = [
    (0x36c,0x08), # Number of hearts must be >1 to prevent destroying RAM
    (0x3ca,0x40), # Dark world
    (0x3c5,0x03), # Set us to late-game OW spawning
    (0x3cc,tagalong_value) # The actual tagalong
]
for a,d in poke_values:
    sv[a]=d

# put instructions in memory at 76dd60
with open('payload.bin','rb') as f:
    payload = bytes(f.read())
payload_start = (0x76dd60&0x1fff)-0x500*5 # 0x460
payload_end = payload_start + len(payload)
assert payload_end <= 0x4fe, "Payload too big, overwritten by checksum"

sv[payload_start:payload_end] = payload[:]
sf.update_checksum(5)
sf.saves[2][:] = sf.saves[5][:]
sf.saves[0][:] = sf.saves[5][:]
# sf.saves[3][:] = sf.saves[5][:]


with open('rom.srm','wb') as f:
    f.write(sf.mem)
