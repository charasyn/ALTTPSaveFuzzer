#!/usr/bin/env python3

class VerJP10:
    savesize = 0x500
    # UNKNOWN
    l_sig = 0x000
    l_cksum = 0x000
class VerUSA12:
    savesize = 0x500
    l_sig = 0x3e5
    l_cksum = 0x4fe
class SaveFile:
    def __init__(self, savedata=bytearray(0x2000), version=VerUSA12):
        self.mem = memoryview(savedata)
        self.ver = version
        self.saves = []
        for i in range(6):
            base = i * self.ver.savesize
            end = base + self.ver.savesize
            self.saves.append(self.mem[base:end])

    def update_checksum(self, save_ind):
        save = self.saves[save_ind]
        save[self.ver.l_sig]=0xaa
        save[self.ver.l_sig+1]=0x55
        ###############################################################
        ### Equivalent 65816 code: M=16bit and X=16bit
        # Loop:
        #   LDX #$0000
        #   TXA
        #   CLC
        #   ADC $7EF000,x
        #   INX
        #   INX
        #   CPX #$04FE
        #   BNE Loop
        #   STA $00
        #   PLY
        #   LDA #$5A5A
        #   SEC
        #   SBC $00
        ###############################################################
        cksum = 0
        for i,b in enumerate(save[:0x4fe]):
            if i % 2 != 0:
                b *= 256
            cksum += b
        cksum = (0x1_5a5a - (cksum & 0xffff)) & 0xffff
        save[self.ver.l_cksum] = cksum & 0xff # Low byte
        save[self.ver.l_cksum+1] = cksum >> 8   # High byte

    def update_all_checksums(self):
        for i, _ in enumerate(self.saves):
            self.update_checksum(i)

        
