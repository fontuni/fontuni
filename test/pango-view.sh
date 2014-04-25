pango-view \
  --font="F0ntUni A 60px" \
  --header \
  --pixels --width=660 \
  --language=th_TH \
  --markup \
  --text 'พี่ป๋ำฎูนู๋น้ำเป่าฝุ่นหญู่ก้นปี่ กตัญญู <span lang="pi-TH">ฐาตุํ ญาติํ ปุํปิํ</span>' \
  --output=pango-a.png

pango-view \
  --font="F0ntUni B 60px" \
  --header \
  --pixels --width=660 \
  --language=th_TH \
  --markup \
  --text 'พี่ป๋ำฎูนู๋น้ำเป่าฝุ่นหญู่ก้นปี่ กตัญญู <span lang="pi-TH">ฐาตุํ ญาติํ ปุํปิํ</span>' \
  --output=pango-b.png
