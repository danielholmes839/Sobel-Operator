# Daniel Holmes
# 2019/1/6
# Functions
# These are the functions used for the Sobel operator

import math
import requests
from urllib.request import Request, urlopen
from PIL import Image


def open_image(image_name):
    """ returns a PIL Image and it's size from a file """
    img = Image.open(image_name, 'r')
    width, height = img.size

    return img, width, height


def open_image_url(url):
    """ returns a PIL Image and it's size from a url """
    response = requests.get(url)
    img = Image.open(urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})))
    width, height = img.size

    return img, width, height


def get_pixels(img, width, height):
    """ creates a list of pixels in RGB format """
    pixels = []
    for y in range(height):
        pixels.append([])
        for x in range(width):
            pixel_tuple = img.getpixel((x, y))

            pixels[y].append([pixel_tuple[0], pixel_tuple[1], pixel_tuple[2]])

    return pixels


def convert_pixels_to_grayscale(pixels, width, height):
    """ changes all RGB values to grayscale """
    for y in range(height):
        for x in range(width):
            sum_rgb = 0

            for i in range(3):
                sum_rgb += pixels[y][x][i]

            avg_rgb =  int(sum_rgb/3)
            pixels[y][x] = (avg_rgb, avg_rgb, avg_rgb)

    return pixels


def get_horizontal_values(pixels, width, height):
    """ get the horizontal values for the sobel operator """
    horizontal_values = []

    stop_y = height-1
    stop_x = width-1

    for y in range(1, stop_y):
        horizontal_values.append([])
        for x in range(1, stop_x):
            value = 0

            value += pixels[y-1][x-1][0]
            value += pixels[y-1][x][0] * 2
            value += pixels[y-1][x+1][0]

            value += -pixels[y+1][x-1][0]
            value += -pixels[y+1][x][0] * 2
            value += -pixels[y+1][x+1][0]

            horizontal_values[y-1].append(value)

    return horizontal_values


def get_vertical_values(pixels, width, height):
    """ get the vertical values for the sobel operator """
    vertical_values = []

    stop_y = height - 1
    stop_x = width - 1

    for y in range(1, stop_y):
        vertical_values.append([])
        for x in range(1, stop_x):
            value = 0

            value += pixels[y-1][x-1][0]
            value += pixels[y][x-1][0] * 2
            value += pixels[y+1][x-1][0]

            value += -pixels[y-1][x+1][0]
            value += -pixels[y][x+1][0] * 2
            value += -pixels[y+1][x+1][0]

            vertical_values[y-1].append(value)

    return vertical_values


def get_new_pixels(pixels, horizontal_values, vertical_values, width, height):
    """ calculates the new values for pixels with sobel operator applied by using the pythagorean theorem with the vertical and horizontal values """
    stop_y = height - 2
    stop_x = width - 2

    for y in range(0, stop_y):
        for x in range(0, stop_x):
            vh = math.pow(horizontal_values[y][x], 2)
            vv = math.pow(vertical_values[y][x], 2)

            v = int(math.sqrt(vh+vv))

            pixels[y+1][x+1] = (v, v, v)

    return pixels


def create_image(pixels, width, height):
    """ creates the new image using the new values """
    img = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            img.putpixel((x,y), pixels[y][x])

    return img


def sobel_from_file(image_name):
    """ combines functions and uses a file for getting the image """
    image, width, height = open_image(image_name)

    pixels = get_pixels(image, width, height)
    pixels = convert_pixels_to_grayscale(pixels, width, height)

    horizontal_values = get_horizontal_values(pixels, width, height)
    vertical_values = get_vertical_values(pixels, width, height)

    new_pixels = get_new_pixels(pixels, horizontal_values, vertical_values, width, height)

    sobel_image = create_image(new_pixels, width, height)

    return sobel_image


def sobel_from_url(image_url):
    """ combines functions and uses a url for getting the image """
    image, width, height = open_image_url(image_url)

    pixels = get_pixels(image, width, height)
    pixels = convert_pixels_to_grayscale(pixels, width, height)

    horizontal_values = get_horizontal_values(pixels, width, height)
    vertical_values = get_vertical_values(pixels, width, height)

    new_pixels = get_new_pixels(pixels, horizontal_values, vertical_values, width, height)

    sobel_image = create_image(new_pixels, width, height)

    return sobel_image