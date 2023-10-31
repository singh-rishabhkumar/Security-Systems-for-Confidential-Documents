port speech recognition as st
import time
import qrcode

 r=st.Recognizer()
while True:
try: with sr.Microphone() as source:
 print("say your name") 
audio= r.listen(source) 
text=r.recognize_google (audio)
 text= text.lower()
print (text)

excepts:
print("ot recognizable. Try Again")
r = st.Recognizer()
Continue

if(text == 'rishab'):
print("you are a wrong person")
print("Good, Here We go for next verification") 
break
else:
   print("you are wrong person")
   continue
x=int(input("Enter your document password"))

if(x==2403):
         print("successfully login")
else:
    print("Fassed incorrect.come after sometime and try againy

print("Wait, we are generating your QR code)

tinme.sleep(2)

features=grcode.GRCodiversion 6.1, bea_size=35,border)) features.add_data('https://drive.google.com/file/d/144X7/27/p/V5c0hp/vielupesce Link)
features.make(fit=true)
features.make(fitt Image features.nake image(fill_color="blue", back_color="brown")
United States Accessibility Investigate
image.save(image.png")