# suppose that you have a pre-existing function that takes a screenshot
# and returns Bitmap, and you want to save it as an image file,
# but you don't have a pre-existing functionality to do so directly
# however, the pre-existing Image class has a save() method that you can use
# to save the image.

# you have a problem:
# 1. rewrite the logic that takes a screenshot can be too complex
# 2. add a save() method to the Bitmap class will also be too complex

# possible solution: use an adapter that converts Bitmap to Image


class Bitmap():
    # a pre-existing bitmap class
    pass


class Image():
    # a pre-existing image class
    def __init__(self) -> None:
        pass

    def save(self, path):
        print(f'image saved at path: {path}')


def take_screenshot() -> Bitmap:
    # logic that takes a screenshot and returns Bitmap
    pass


class BitmapToImageAdapter():
    def __init__(self, bitmap: Bitmap) -> None:
        self.bitmap = bitmap

    def adapt(self) -> Image:
        # logic that converts Bitmap to Image and returns it
        pass


bitmap = take_screenshot()
image = BitmapToImageAdapter(bitmap).adapt()
image.save('image.png')
