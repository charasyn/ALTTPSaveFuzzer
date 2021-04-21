
make := make
cp := cp

libretro           := bsnes_libretro.so
libretro_path      := bsnes-libretro/bsnes_libretro.so
libretro_directory := bsnes-libretro
libretro_target    := all

nanoarch           := nanoarch
nanoarch_path      := nanoarch/nanoarch
nanoarch_directory := nanoarch
nanoarch_target    := all

all: $(libretro) $(nanoarch)

$(libretro):
	$(make) -C $(libretro_directory) $(libretro_target)
	$(cp) $(libretro_path) rundir/$(libretro)

$(nanoarch):
	$(make) -C $(nanoarch_directory) $(nanoarch_target)
	$(cp) $(nanoarch_path) rundir/$(nanoarch)

.PHONY: $(libretro) $(nanoarch)
