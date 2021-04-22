import sys
sys.path.insert(1,"../fuzzer")
import fuzz_alttp as fuzz
import random
random.seed(1)
random_data = (random.randint(0,255) for _ in range(0x2000))
sv = fuzz.SaveFile(bytearray(random_data))
sv.update_all_checksums()
with open('rom.srm','wb') as f:
    f.write(sv.mem)
