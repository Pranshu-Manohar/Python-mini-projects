import speech_recognition as sr
import os,webbrowser,pyttsx3 as pt
import datetime,pyjokes,subprocess,pyautogui,pathlib
class parent():

     def __init__(self):
             
          


                         self.engine = pt.init('sapi5')
                         self.engine.setProperty('rate', 140)    
                         # engine.setProperty('voice', 'hindi') 
                         self.engine.setProperty('volume',1.0)
                         self.ob1=sr.Recognizer()
                         # ob2=pt.engine()
                         # engine.say("Hi")
                         
                         self.systemapps= {
                                             "camera": "start microsoft.windows.camera:",
                                             "calculator": "calc",
                                             "notepad": "notepad",
                                             "paint": "mspaint",
                                             "vs code":"code"
                                             }
                         self.close_systemapps= {
                                             "camera": "taskkill /f /im WindowsCamera.exe",
                                             "calculator": "taskkill /f /im CalculatorApp.exe",
                                             "notepad": "taskkill /f /im Notepad.exe",
                                             "paint": "taskkill /f /im mspaint.exe",
                                             "vs code": "taskkill /f /im code.exe",
                                             "chrome": "taskkill /f /im chrome.exe",
                                             }


                                             # time=datetime.date.today()
                                             # print(time)

                         self.ytlist=[
                                             "yt",
                                             "youtube",
                                             "video",
                                             "song",
                                             "youtobe",
                                             "youtbee"
                                             ]

                        
                         self.assist_shutdown_command=[
                                             "exit",
                                             "close yourself",
                                             "get back",
                                             "stop it",
                                             
                                             "release",
                                             "goodbye"
                                             ]



     def functionality(self):
                         #  engine.setProperty('rate', 150) 
                              self.speak("OK, Hello I am a voice based desktop assistant ")
                              self.speak("I have created using the multiple python librabries")
                              self.speak("I can open the most daily apps you have to just say 'OPEN' then the app name")
                              self.speak("for closing the app you need to say 'Terminate' then the app name")
                              self.speak("I can tell u a joke, time , weather too , you have to just say the name")
                              self.speak("You can say 'Terminate','release' or 'goodbye' for shutting me down")

     def greet(self):
                              time = datetime.datetime.now().hour
                              
                              if(time>0 and time<12):
                                   self.speak("Good morning")
                              elif(time>=12 and time<17):
                                   self.speak("Good afternoon")
                              else:
                                   self.speak("Good evening")
                              self.speak("How can i assist you ?")



     def openapp(self,command):
                              subprocess.run(command, shell=True)
                              return

     def closeapp(self,command):
                              
                              os.system(f"{command}")     
                              return

     def get_jokes(self):
                              new_jokes=pyjokes.get_joke()
                              self.speak(new_jokes)
                              return

     def speak(self,text):
                              print(f"Kai: {text}")
                              self.engine.say(text)
                              self.engine.runAndWait()
                              return

     def time(self):
                              current_time = datetime.datetime.now().strftime("%I:%M %p")
                              print(current_time)
                              self.speak(f"The time is {current_time}")
                              return

     def search(self,m):
                              self.speak("would u like to search something on google?")
                              print("I am listening for google: ")
                              self.audio=self.ob1.listen(m)
                              self.querry3=self.ob1.recognize_google(self.audio,language='eng-IN')
                              if(self.querry3=="Nothing" or self.querry3=="none"):
                                   webbrowser.open_new("https://www.google.com")
                              else:
                                   webbrowser.open_new(f"https://www.google.com/search?q={self.querry3}")
                              return


     def erp(self):
                              self.speak("Opening college erp")
                              webbrowser.open_new("https://student.cgc.ac.in/")



     def ytctrl(self,m):
                              self.speak("will u search something on youtube?")
                              print("I am listening for yt: ")
                              audio=self.ob1.listen(m)
                              self.querry3=self.ob1.recognize_google(audio,language='eng-IN')

                              if(self.querry3=="no"or self.querry3=="nothing"):
                                        yt=webbrowser.open_new_tab(f"https://www.youtube.com")
                                        return
                              else:
                                        yt=webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={self.querry3}")
                                        return

     def ss(self):
                              save_folder = pathlib.Path.home() / "OneDrive" / "Pictures" / "Screenshots"

                              filename = f"screenshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

                              path = save_folder / filename

                              pyautogui.screenshot(str(path))

                              print(f"Saved to: {path}")
                              self.speak("Screenshot captured")

                              return



                        
                        
                         

class child(parent):
       def __init__(self):
        
        super().__init__()
        super().greet()
       
        while True:
                              try:
                                        with sr.Microphone()as m:
                                                  print("I am listening: ")
                                                  audio=self.ob1.listen(m)
                                                  self.querry=self.ob1.recognize_google(audio,language='eng-IN')
                                                  self.querry=self.querry.lower()
                                                  
                                                  print(self.querry)

                                                  for i in self.systemapps:
                                                       if(f"open {i}" in self.querry):
                                                            self.speak(f"opening {i}")
                                                            self.openapp(self.systemapps[i])
                                                            break

                                                  for i in self.close_systemapps:
                                                       if(f"terminate {i}" in self.querry):
                                                            self.speak(f"Closing {i}")
                                                            self.closeapp(self.close_systemapps[i])
                                                            break

                                                  if any(command in self.querry for command in self.assist_shutdown_command):
                                                       self.speak("Going to sleep...Bye")
                                                       break

                                                  if any(ytlists in self.querry for ytlists in self.ytlist):
                                                       self.ytctrl(m)
                                                       continue


                                                  if "time" in self.querry or "clock" in self.querry:
                                                       self.time()
                                                       continue

                                                  if("tell me a joke" in self.querry) or "joke" in self.querry:
                                                       self.get_jokes()
                                                       continue

                                                  #    for i in systemapps:
                                                  #         if(f"open {i}" in querry):
                                                  #              speak(f"opening {i}")
                                                  #              openapp(systemapps[i])
                                                  #    for i in close_systemapps:
                                                  #         if(f"terminate {i}" in querry):
                                                  #              openapp(close_systemapps[i])

                                                  if(f"open google" in self.querry or "search"in self.querry):
                                                       self.search(m)
                                                       continue
                                                  
                                                  if(f"functionality" in self.querry or "functions"in self.querry):
                                                       self.functionality()
                                                       continue

                                                  if (f"screenshot" in self.querry or "ss" in self.querry):
                                                       self.ss()
                                                       continue
                                                       
                                                  if "resume" in self.querry or "freeze" in self.querry:
                                                            print("Action: Toggling Play/Pause")
                                                            pyautogui.press('playpause')
                                                            continue
                                                       
                                                  if"volume up" in self.querry or "volume increase" in self.querry:
                                                       pyautogui.press("volumeup",presses=5)
                                                       continue
                                                  if"volume down" in self.querry or "volume decrease" in self.querry:
                                                       pyautogui.press("volumedown",presses=2)
                                                       continue

                                                  if "max volume" in self.querry or "full volume" in self.querry:
                                                       pyautogui.press("volumeup", presses=50)
                                                       continue
                                                  if "mute" in self.querry or "silence" in self.querry:
                                                       pyautogui.press("volumemute")
                                                       continue

                                                  if "next" in self.querry:
                                                       pyautogui.press("nexttrack")
                                                       continue
                                                  if "previous" in self.querry:
                                                       pyautogui.press("prevtrack")
                                                       continue

                                                  if "full screen" in self.querry:
                                                       pyautogui.press("f")
                                                       continue
                                                  if "open portal" in self.querry or "portal open" in self.querry or "open erp"in self.querry:
                                                       self.erp() 
                                                  
                                                  if("sign off" in self.querry):
                                                       pyautogui.hotkey("win","x")
                                                       pyautogui.press("u")
                                                       pyautogui.press("u")
                              except sr.UnknownValueError:
                                   continue

                              except sr.RequestError:
                                   self.speak("Internet connection problem.")
                                   continue

                              except Exception as e:
                                   print(e)
                                   continue

ob=child()
        





        
            