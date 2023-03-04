from server import app, utilities as fn
from flask import request
import os
import cv2
from PIL import Image



@app.route('/uploadImage',  methods=['POST'])
def uploadImage():

    if request.method == 'POST':
            file1 = request.files["Image_File1"]
            file1.save(os.path.join(
                'server//static//assests//image1.jpg'))

    return []


@app.route('/imgProcessing' ,  methods=['POST'])
def imgProcessing():
    if request.method == 'POST':
        jsonData = request.get_json()  
        data = jsonData['formElement']

        if (data[0]== False):
            return []
                
        else:

            img= cv2.imread('server//static//assests//image1.jpg')
            img = fn.rgbtogray(img)
            if (data[1]=='None'):
                output = img
                cv2.imwrite('server//static//assests//output.jpg', output)
            else:
                if(data[1]=='Uniform'):
                    output = fn.uniform_noise(img)
                elif(data[1]=='Gaussian'):
                    output = fn.gaussian_noise(img)
                elif(data[1]=='salt'):
                    output = fn.salt_and_pepper(img)
                cv2.imwrite('server//static//assests//output.jpg', output)

                
            

            img= cv2.imread('server//static//assests//output.jpg')
            img = fn.rgbtogray(img)

            if (data[2]=='None'):
                output = img
                cv2.imwrite('server//static//assests//output.jpg', output)
            else:
                if(data[2]=='Average'):
                    output = fn.meanLowPass(img)
                elif(data[2]=='Gaussian'):
                    output = fn.GaussianLowFilter(img)
                elif(data[2]=='Median'):
                    output = fn.median_filter(img)
                cv2.imwrite('server//static//assests//output.jpg', output)


            img= cv2.imread('server//static//assests//output.jpg')
            img = fn.rgbtogray(img)

            if (data[3]=='None'):
                output = img
                cv2.imwrite('server//static//assests//output.jpg', output)
            else:
                if(data[2]=='Sobel'):
                    output = fn.sobel(img)
                elif(data[2]=='Robert'):
                    output = fn.robert(img)
                elif(data[2]=='Prewitt'):
                    output = fn.prewit(img)
                else:return[]    
                cv2.imwrite('server//static//assests//output.jpg', output)    
            return []            
                 
