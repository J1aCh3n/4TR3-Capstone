import paho.mqtt.client as mqtt
import os
from pet_face_recognition import recognition  # Import the pet face recognition function


directory = "./Documents/Capstone/recieve_from_mqtt"
file_name = "received_image.jpg"
full_path = os.path.join(directory, file_name)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Capstone/img")


def on_message(client, userdata, msg):
    with open(full_path, "wb") as img_file:
        img_file.write(msg.payload)
    print(f"Image saved: {full_path}")
    # Call the imported image processing function here
    recognition(full_path)


def mqtt_subscribe_and_save_image():
    client = mqtt.Client("Capstone")
    client.on_connect = on_connect #connect to mqtt server
    client.on_message = on_message #save image
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_forever()


if __name__ == "__main__":
    mqtt_subscribe_and_save_image()
