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
                else:
                    kernal_size = 3
                    low_threshold_ratio = 0.05
                    high_threshold_ratio = 0.09
                    gradient_estimation_filter_type = "sobel"
                    kernal = fn.get_gaussian_kernel(kernal_size)
                    image_without_noise = fn.apply_filtering(img.tolist(), kernal)

                    # step 3 : gradient estimation
                    assert (gradient_estimation_filter_type in ["sobel", "prewitt", "robert"]), "gradient estimation filter type should be [\"prewitt\", \"sobel\", \"robert\"]"
                    G, theta = fn.gradient_estimate(image_without_noise, gradient_estimation_filter_type)

                    # step 4 : non maxima suppression
                    image_with_thin_edges = fn.non_maxima_suppression(G, theta)

                    # step 5 : double threshold
                    final_image, weak, strong = fn.double_threshold(image_with_thin_edges, low_threshold_ratio, high_threshold_ratio)

                    # edge tracking with hysteresis
                    output = fn.hysteresis_edge_track(final_image, weak, strong=255)   
                cv2.imwrite('server//static//assests//output.jpg', output)    
            return []            
                 
