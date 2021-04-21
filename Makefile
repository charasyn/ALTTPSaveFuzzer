# Straight up lifted from bsnes-libretro makefile
ifeq ($(platform),)
platform = unix
ifeq ($(shell uname -s),)
	platform = win
else ifneq ($(findstring MINGW,$(shell uname -s)),)
	platform = win
else ifneq ($(findstring Darwin,$(shell uname -s)),)
	platform = osx
else ifneq ($(findstring win,$(shell uname -s)),)
	platform = win
endif
endif

make := make
cp := cp

ifeq ($(platform),win)
	libretro           := bsnes_libretro.dll
	nanoarch           := nanoarch.exe
	make := mingw32-make
else ifeq ($(platform),osx)
	libretro           := bsnes_libretro.dylib
	nanoarch           := nanoarch
else
	libretro           := bsnes_libretro.so
	nanoarch           := nanoarch
endif


libretro_srcpath   := bsnes-libretro/$(libretro)
libretro_dstpath   := rundir/$(libretro)
libretro_directory := bsnes-libretro
libretro_target    := all

nanoarch_srcpath   := nanoarch/$(nanoarch)
nanoarch_dstpath   := rundir/$(nanoarch)
nanoarch_directory := nanoarch
nanoarch_target    := all

all: $(libretro_dstpath) $(nanoarch_dstpath)

run:
	$(nanoarch_dstpath) $(libretro_dstpath) rundir/rom.sfc

$(libretro_dstpath):
	$(make) -C $(libretro_directory) $(libretro_target)
	$(cp) $(libretro_srcpath) $(libretro_dstpath)

$(nanoarch_dstpath):
	$(make) -C $(nanoarch_directory) $(nanoarch_target)
	$(cp) $(nanoarch_srcpath) $(nanoarch_dstpath)

.PHONY: all run $(libretro_dstpath) $(nanoarch_dstpath)
