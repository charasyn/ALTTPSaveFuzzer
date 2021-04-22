import sys
import random

sys.path.insert(1,"../fuzzer")
import fuzz_alttp as fuzz

tagalong_value = int(sys.argv[1], base=0)

random.seed(1)
random_data = (0 for _ in range(0x2000))
sf = fuzz.SaveFile(bytearray(random_data))
sv = sf.saves[0]
fixed_values = [
    (0x36c,0x08), # Number of hearts must be >1 to prevent destroying RAM
    (0x3ca,0x40), # Dark world
    (0x3c5,0x03), # Set us to late-game OW spawning
]
for a,d in fixed_values:
    sv[a]=d
sv[0x3cc]=tagalong_value
sf.update_checksum(0)
with open('rom.srm','wb') as f:
    f.write(sf.mem)
