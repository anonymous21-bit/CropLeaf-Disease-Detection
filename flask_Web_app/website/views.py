import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
from flask import Blueprint, request, render_template, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf 
import numpy as np
from PIL import Image



views = Blueprint('views', __name__)

# Set the upload folder path
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@views.route("/home") 
def home(): 
    return render_template('index.html')

@views.route("/") 
def home_page(): 
    return render_template('index.html')

# @views.route('/home', methods=['POST'])
# def model_prediction(image):

#     if 'file' not in request.files:
#         return redirect(url_for('views.home', error='No file part'))

#     file = request.files['file']
#     if file.filename == '':
#         return redirect(url_for('views.home', error='No selected file'))

#     if file:
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(UPLOAD_FOLDER, filename)
#         file.save(filepath)

#         image = Image.open(filepath)
#         model = tf.keras.models.load_model('trained_model.keras')
#         image = tf.keras.preprocessing.image.load_img(upload, target_size=(128, 128))
#         input_arr = tf.keras.preprocessing.image.img_to_array(image)
#         input_arr = np.array([input_arr]) #converting single image into a batch
#         prediction = model.predict(input_arr)
#         result_index = np.argmax(prediction)
#         result_filename = f'result_{result_index}'
#         result_filepath = os.path.join(UPLOAD_FOLDER, result_filename)
#         return redirect(url_for('views.result', filename=result_filename, prediction=result_index))
#     return redirect(url_for('views.index', error='File not processed'))


@views.route('/result')
def result():
    filename = request.args.get('filename')
    prediction = request.args.get('prediction')
    return render_template('result.html', filename=filename, prediction=prediction)

@views.route("/about") 
def about(): 
    return render_template('about.html')

@views.route("/services") 
def services(): 
    return render_template('services.html')

@views.route("/shop") 
def shop(): 
    return render_template('shop.html')

@views.route("/cart") 
def cart(): 
    return render_template('cart.html')

@views.route("/checkout") 
def checkout(): 
    return render_template('checkout.html')

@views.route("/contact") 
def contact(): 
    return render_template('contact.html')

@views.route("/login_signup")
def login_signup():
    return render_template('login_signup.html')

@views.route("/login") 
def login(): 
    return render_template('login_signup.html', active_tab='login')

@views.route("/signup") 
def signup(): 
    return render_template('login_signup.html', active_tab='signup')

@views.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        #jsonify({'success': 'File successfully uploaded', 'filename': filename})

        # Process the image and make a prediction
        image = Image.open(upload)
        image = image.resize((224, 224))  # Example size, adjust as needed
        image = np.array(image)
        image = image / 255.0  # Normalize if necessary
        image = image.reshape(1, 224, 224, 3)  # Reshape for model input if needed

        prediction = model.predict(image)
        predicted_class = np.argmax(prediction, axis=1)[0]

        # Save the result image (for demonstration, just re-saving the uploaded image)
        result_filename = f'result_{filename}'
        result_filepath = os.path.join(UPLOAD_FOLDER, result_filename)
        Image.fromarray((image[0] * 255).astype(np.uint8)).save(result_filepath)

        return redirect(url_for('views.result', filename=result_filename, prediction=predicted_class))

    return redirect(url_for('views.index', error='File not processed'))

# Route to display the result image
@views.route('/result')
def result():
    filename = request.args.get('filename')
    prediction = request.args.get('prediction')
    return render_template('result.html', filename=filename, prediction=prediction)


@views.route('/user_login', methods=['POST'])
def user_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if authenticate_user(email, password):
            return jsonify({'success': 'Login successful'})
        else:
            return jsonify({'error': 'Invalid email or password'}), 400



@views.route('/user_signup', methods=['POST'])
def user_signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password == confirm_password:
            register_user(first_name, last_name, email, password)
            return jsonify({'success': 'Signup successful, please login'})
        else:
            return jsonify({'error': 'Passwords do not match'}), 400


def authenticate_user(email, password):
    # Replace this with your actual authentication logic
    return email == "test@example.com" and password == "123"

def register_user(first_name, last_name, email, password):
    # Replace this with your actual registration logic
    print(f"User registered: {first_name} {last_name}, {email}")