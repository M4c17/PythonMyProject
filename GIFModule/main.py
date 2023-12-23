import requests
from PIL import Image


def photo_download():
    url = input("Lütfen fotoğrafın linkini giriniz: ")
    response = requests.get(url)
    photo_name = input("Lütfen fotoğraf ismini giriniz: ")
    with open(f"{photo_name}.jpg", "wb") as outfile:
        outfile.write(response.content)

while True:

    print("Gif için G\nFotoğraf indirmek için D\nÇıkmak için Q")
    chose = input("Lütfen menülerden birini seçiniz: ")

    if chose=="G":
        photo_one = input("Fotoğraf ismi: ")
        photo_two = input("Fotoğraf ismi: ")
        #gif_name = input("GIF in ismini giriniz: ")

        # Take list of paths for images
        image_path_list = [f'{photo_one}', f'{photo_two}']

        # Create a list of image objects
        image_list = [Image.open(file) for file in image_path_list]

        # Save the first image as a GIF file
        image_list[0].save(
            'animation.gif',
            save_all=True,
            append_images=image_list[1:],  # append rest of the images
            duration=1000,  # in milliseconds
            loop=0)
        break



    elif chose == "D":
        while True:
            photo_download()
            photo_download()

            break
    elif chose == "Q":
        break









