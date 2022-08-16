from base64 import b64decode
import os
import time
import pickle
import face_recognition as fr

def register_on_submit(email,image):
    header, encoded = image.split(",", 1)
    
    file_new = email
    
    with open("student/"+file_new + ".png", "wb") as f:
        f.write(b64decode(encoded))
        
    got_image = fr.load_image_file("student/"+file_new + ".png")
    if (len(fr.face_encodings(got_image,None,10,'small'))!= 1):
        os.remove("student/"+file_new + ".png")
        return "Registration failed! Cannot detect your face. Please try again."
    else:
        return "Registration Successful!"
