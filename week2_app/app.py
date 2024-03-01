import gradio as gr
from transformers import pipeline
from PIL import Image
import torch


model_id = "caidas/swin2SR-classical-sr-x2-64"
upscaler = pipeline("image-to-image", model=model_id)



def upscale(input_img):
    low_res_img = resize_on_scale(input_img)
    upscaled_img = upscaler(low_res_img)
    print("Low resolution image size = ", low_res_img.size)
    print("Upscaled image size = ", upscaled_img.size)
    return upscaled_img


def resize_on_scale(input_img):
    return input_img
    low_res_img = input_img.convert("RGB")
    wsize = 300
    wpercent = (wsize / float(input_img.size[0]))
    hsize = int((float(input_img.size[1]) * float(wpercent)))
    low_res_img = low_res_img.resize((wsize, hsize))
    return low_res_img

    
gradio_app = gr.Interface(
    upscale, 
    inputs=gr.Image(label="Select a blurry image", sources=['upload', 'webcam', 'clipboard'], type="pil"),
    outputs=gr.Image(label="Processed Image"), 
    title="Image Upscaler",
)

if __name__ == "__main__":
    gradio_app.launch()

