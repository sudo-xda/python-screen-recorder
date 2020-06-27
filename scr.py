import cv2
import numpy as np
import pyscreenshot as scr

forcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', forcc , 8 , (1920,1080))

while True:
    img = scr.grab()
    img_np = np.array(img)



    cv2.imshow('screen' , img_np)
    out.write(img_np)



    if cv2.waitKey(20) & 0xff == ord('e'):
        break




    out.release()
    cv2.destroyAllWindows()