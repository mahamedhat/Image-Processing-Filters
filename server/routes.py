from server import app
from flask import request
import os



@app.route('/uploadImage',  methods=['POST'])
def uploadImage():

    if request.method == 'POST':
            file1 = request.files["Image_File1"]
            file1.save(os.path.join(
                'server/static/assets/Image1.jpg'))



    return []