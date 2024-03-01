import gradio as gr

from diffusers import StableDiffusionUpscalePipeline
from PIL import Image
from io import BytesIO
import torch



model_id = "stabilityai/stable-diffusion-x4-upscaler"
pipeline = StableDiffusionUpscalePipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipeline = pipeline.to("cuda")


# def predict(input_img):
#     predictions = predictor(input_img)
#     return input_img, {p["label"]: p["score"] for p in predictions} 


def upscalex4(input_img):
    low_res_img = resize_on_scale(input_img)
    prompt = "highly detailed"
    upscaled_img = pipeline(prompt=prompt, image=low_res_img).images[0]
    print("Low resolution image size = ", low_res_img.size)
    print("Upscaled image size = ", upscaled_img.size)
    return upscaled_img


def resize_on_scale(input_img):
    low_res_img = input_img.convert("RGB")
    wsize = 300
    wpercent = (wsize / float(input_img.size[0]))
    hsize = int((float(input_img.size[1]) * float(wpercent)))
    low_res_img = low_res_img.resize((wsize, hsize))
    return low_res_img


gradio_app = gr.Interface(
    upscalex4, 
    inputs=gr.Image(label="Select a blurry image", sources=['upload', 'webcam', 'clipboard'], type="pil"),
    outputs=gr.Image(label="Processed Image"), 
    title="Image Upscaler",
)

if __name__ == "__main__":
    gradio_app.launch()








# img = Image.open(requests.get("https://pbs.twimg.com/profile_images/1600764211378139137/HirERJI5_400x400.jpg", stream=True).raw)
# img = img.resize((64, 64))

# print("Original image size = ", img.size)
# print("Upscaled image size = ", upscaled_img.size)
# upscaled_img.show()