#!/bin/sh

pango-view test-markup.txt \
  --font="F0ntUni A 60px" \
  --header \
  --pixels --width=660 \
  --language=th_TH \
  --markup \
  --output=pango-mac-a.png

pango-view test-markup.txt \
  --font="F0ntUni B 60px" \
  --header \
  --pixels --width=660 \
  --language=th_TH \
  --markup \
  --output=pango-mac-b.png
