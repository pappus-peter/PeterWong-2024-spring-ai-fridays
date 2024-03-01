# import datasets
# from transformers import pipeline
# from transformers import logging
# logging.set_verbosity_warning()



# pipe = pipeline("text-classification", model="FacebookAI/roberta-large-mnli")
# user_list = ["This restaurant is awesome", "This restaurant is awful"]
# print(pipe(user_list))


from PIL import Image
import requests

from transformers import pipeline

upscaler = pipeline("image-to-image", model="caidas/swin2SR-classical-sr-x2-64")
img = Image.open(requests.get("https://pbs.twimg.com/profile_images/1600764211378139137/HirERJI5_400x400.jpg", stream=True).raw)
img = img.resize((64, 64))
upscaled_img = upscaler(img)
print("Original image size = ", img.size)
print("Upscaled image size = ", upscaled_img.size)
upscaled_img.show()
