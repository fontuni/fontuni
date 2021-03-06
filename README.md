[![Build Status](https://travis-ci.org/BoonUni/f0ntuni.svg?branch=master)](https://travis-ci.org/BoonUni/f0ntuni)

# F0ntUni OpenType Library

**ฟอนต์อยู่นี่** เกิดจากการพูดคุยกันที่ [F0nt.com](http://www.f0nt.com/forum/index.php/topic,21995.0.html) เพราะต้องการเทมเพลตสำหรับการทำฟอนต์ไทยแบบ Unicode พร้อมทั้งทำ OpenType Features ที่เหมาะสมสำหรับการแก้ปัญหาทั่วไปที่จำเป็นคนทำฟอนต์ไทย อีกทั้งหวังว่าจะช่วยให้ผู้ที่สนใจการทำฟอนต์รุ่นใหม่หัดทำฟอนต์ไทยได้ง่ายขึ้น

### ฟีเจอร์ทั่วไป

- แก้ปัญหาวรรณยุกต์ลอย แม้แต่กรณีที่ไม่มีฟีเจอร์ใดๆ เลย (HarfBuzz's Thai built-in functionality)
- แก้ปัญหาสระบน-ล่างหรือวรรณยุกต์ทับซ้อนกับพยัญชนะ เช่น ป, ฝ, ฟ กับ สระบน หรือ ญ, ฐ, ฎ, ฏ กับ สระล่าง เป็นต้น
- รองรับการใช้งานกับภาษาชาติพันธุ์ (Minority Languages) ที่ใช้ตัวอักษรไทยแต่มีวิธีเขียนที่แตกต่างจากภาษาไทยมาตรฐาน (ขึ้นอยู่กัน text engine ของระบบปฏิบัติการด้วยว่ารองรับวิธีเขียนแบบนั้นหรือไม่)

### ฟีเจอร์เสริม

- เพิ่มทางเลือกในการใช้งานภาษาบาลีและสันสกฤตภายในฟอนต์ไทยตัวเดียว ในกรณีโปรแกรมที่ใช้งานฟอนต์มีความสามารถพอ

**F0ntUni** เพิ่งอยู่ในช่วงเริ่มต้นพัฒนา อาจมีข้อผิดพลาดเมื่อนำไปใช้งาน อีกทั้งระบบปฏิบัติการและโปรแกรมต่างๆ ที่ใช้งานฟอนต์ก็มีความสามารถในการรองรับ OpenType Features ไม่เท่ากัน จึงได้ทำเทมเพลตไว้หลายแบบเพื่อเป็นทางเลือก

## การใช้งานเทมเพลต
ยังไม่มีเวลาทำเอกสารอธิบายวิธีการใช้งาน หากมีปัญหาหรือข้อสงสัยก็พูดคุยกันได้ที่ [F0nt Forum](http://www.f0nt.com/forum/) ครับ
