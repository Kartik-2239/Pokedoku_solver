from PIL import Image

def make_image():

    width, height = 165, 169
    color = (0, 255, 0)  
    image = Image.new("RGB", (width, height), color)
    return image


def crop_img(im):
    #crop coordinates (left, top, right, bottom)
    crop_area = (561,236,1201,858)
    cropped_image = im.crop(crop_area)
    overlay = make_image()
    overlay = overlay.convert("RGBA")
    cropped_image.paste(overlay, (0, 0), overlay)
    return cropped_image