#!/bin/sh

#
# You need HarfBuzz CLI binary for using hb-view
#
# hb-view.exe on Windows?

# Debian/Ubuntu
# sudo apt-get install libharfbuzz-bin

# Mac OS
# brew install harfbuzz
#

hb-view \
  --shapers=fallback \
  --font-file=../A/f0ntuni-a.otf \
  --font-size=60 \
  --language=th_TH \
  --text-file=test-th.txt \
  --output-file=harfbuzz-fallback-th-a.png --output-format=png

hb-view \
  --shapers=fallback \
  --font-file=../A/f0ntuni-a.otf \
  --font-size=60 \
  --language=pi_TH \
  --text-file=test-pi.txt \
  --output-file=harfbuzz-fallback-pi-a.png --output-format=png

hb-view \
  --shapers=fallback \
  --font-file=../B/f0ntuni-b.otf \
  --font-size=60 \
  --language=th_TH \
  --text-file=test-th.txt \
  --output-file=harfbuzz-fallback-th-b.png --output-format=png

hb-view \
  --shapers=fallback \
  --font-file=../B/f0ntuni-b.otf \
  --font-size=60 \
  --language=pi_TH \
  --text-file=test-pi.txt \
  --output-file=harfbuzz-fallback-pi-b.png --output-format=png
