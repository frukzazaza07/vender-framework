from base64 import b64decode
import face_recognition as fr
import time
import os
import pickle
import glob

def login_check(uid,image):
    face_match = 0
    header, encoded = image.split(",", 1)
    file_new = str(time.time())
    #file_exist = str("tmp")+str(time.time())

    with open(file_new + ".png", "wb") as f:
        f.write(b64decode(encoded))
        
    got_image = fr.load_image_file(file_new + ".png")
    #face_locations = fr.face_locations(got_image)
    #got_image_facialfeatures = fr.face_encodings(got_image)[0]
    
    if (len(fr.face_encodings(got_image,None,10,'small'))!= 1):
        os.remove(file_new + ".png")
        return "No face detected"
    else:
        existing_image = fr.load_image_file('student/'+uid+'.png')            
        existing_image_facialfeatures = fr.face_encodings(existing_image)[0]
        got_image_facialfeatures = fr.face_encodings(got_image)[0]
        results = fr.compare_faces([existing_image_facialfeatures], got_image_facialfeatures , 0.3)
        if(results[0]):
            os.remove(file_new + ".png")
            return "Match"
        else:
            os.remove(file_new + ".png")
            return "Not match"
            
