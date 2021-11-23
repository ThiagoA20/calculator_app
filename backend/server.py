import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyBkqUE0-byq4QduF-ENQk_TkG4md4u-dc0",
    'authDomain': "calculator-fc5f8.firebaseapp.com",
    'projectId': "calculator-fc5f8",
    'storageBucket': "calculator-fc5f8.appspot.com",
    'messagingSenderId': "38504597679",
    'appId': "1:38504597679:web:de4da8151be34f421eec5a",
    'measurementId': "G-260VZ3M5JP",
    'databaseURL': "https://calculator-fc5f8-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)

# db = firebase.database()
# auth = firebase.auth()
storage = firebase.storage()

# Autentication
# Login
# email = input("Type your email address: ")
# password = input("Type your password: ")
# try:
    # auth.sign_in_with_email_and_password(email, password)
    # print("Successfully Signed in!")
# except:
    # print("Wrong username or password, try again.")

# Register
# email = input("Type your email address: ")
# password = input("Type your password: ")
# confirmPassword = input("Confirm password: ")
# if password == confirmPassword:
    # auth.create_user_with_email_and_password(email, password)
    # print("User successfully created!")


#Storage
#upload
# filename = input("Type the name of the file that you want to upload: ")
# cloudFilename = input("Enter the name of the file on the cloud: ")
# storage.child(cloudFilename).put(filename)

#download
cloudFilename = input("Type the name of the file on the cloud: ")
storage.child(cloudFilename).download("", "downloaded.txt")