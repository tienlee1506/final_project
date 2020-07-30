import speech_recognition
from gtts import gTTS
import os 
from playsound import playsound
from datetime import date, datetime  

while True: 
     #khởi tạo
     #Tai AI
     robot_ear = speech_recognition.Recognizer()#nghe người dùng nói

     with speech_recognition.Microphone() as mic:
        print("Người yêu: Đang nghe...")
        audio = robot_ear.record(mic, duration = 10) #robot nghe
        print("\n Người yêu:.....")
     try:
        you = robot_ear.recognize_google(audio, language= 'vi')#AI thu tiếng của bạn và in ra màn hình
        print("\n Bạn:  " + you)
     except:
       you = ""
       print("\n Bạn:"  + you)
     ### Bộ não AI
     if you == "":    
        robot_brain = "tôi không nghe được bạn nói, xin hãy thử lại"
     elif "Xin chào" in you:
        robot_brain = "Người yêu của em về rồi à!"
     elif " Hôm nay em khỏe không" in you:
        robot_brain = " Em ở nhà nghỉ ngơi nhiều nên khỏe ạ!"
     elif "Hôm nay anh buồn" in you:                                                                                             # Bật nhạc
        robot_brain = (" Ô kê anh, đợi em vài giây" + playsound('C:\\Users\\This MC\\Downloads\\kiss.mp3')+"Anh đỡ buồn chưa ạ") #
     elif "ngày" in you:
        today = date.today()
        robot_brain = ("Hôm nay là" + today.strftime("%d/%m%Y") + "anh ạ!") #ngày
        now = datetime.now()
        robot_brain = (" Bây giờ là" + now.strftime("%H:%M:%S")+"anh ạ!")#GIỜ
     elif "Em nghỉ đi" in you:#Chào để kết thúc chuong trình
        robot_brain = " Anh nghỉ ngơi đi nhá!"
        tts = gTTS(text=robot_brain, lang='vi')
        tts.save("ai.mp3")
        os.system("ai.mp3")
        exit()
     else:
        robot_brain = "Cảm ơn bạn"
    #Miệng AI  
     tts = gTTS(text=robot_brain, lang='vi')#AI đưa suy nghĩ của mình sang mp3 rồi chạy chúng
     tts.save("ai.mp3")
     os.system("ai.mp3")