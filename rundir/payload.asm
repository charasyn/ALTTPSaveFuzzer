arch snes.cpu
sei
sec
xce
stz $4200
stz $420c
stz $420b
lda #$80
sta $2100
clc
xce

rep #$38
lda #$01ff
tcs
pea $0000
plb
stz $212c
lda #$03e0
sep #$20
sta $2122
xba
sta $2122

lda #$0f
sta $2100

loop:
bra loop
