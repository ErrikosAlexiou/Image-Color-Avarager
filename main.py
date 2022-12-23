import os
from tkinter import *
from tkinter import filedialog

from PIL import Image

from screenSize import ScreenSize

# building the Tkinter window
root = Tk()

# Create the name of the GUI
root.title("Image Color Average")

# Calculate the size of the screen
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# Apply screensize calulations to the GUI
appGeometry = ScreenSize(screenWidth, screenHeight)
root.geometry(appGeometry)

# Configure the background color of the GUI
root.configure(bg="Black")

# Convert images of any filetype to .png images and resize to width of 300
def convert_to_png(image_path):

    # Open the image file
    image = Image.open(image_path)

    # Get the Width and Height of the Image
    width, height = image.size

    # Set the desired width
    desiredwidth = 300

    # Calculate the adjustment required to acheive the desired width
    resizedscalerwidth = width / desiredwidth
    resizedscalerheight = height / resizedscalerwidth

    # Set the desired width and rounding to integers
    sizewidth = int(round(width / resizedscalerwidth, 0))
    sizeheight = int(round(resizedscalerheight, 0))

    image = image.resize((sizewidth, sizeheight))

    # Get the file name and extension of the original image
    file_name, file_ext = os.path.splitext(image_path)

    # Create the new file name for the PNG image
    png_file_name = file_name + ".png"

    # Save the image in the PNG format
    image.save(png_file_name, format="PNG")

    # Delete the original image
    # os.remove(image_path)

    # Returns the Path of the file to be calculated
    return str(png_file_name)


def Calculate():
    # Sets the image variable to global
    global image

    # Converts the image through PIL to avoid 'image not reconginasble error'
    convert_to_png(image)

    # Opens the Image
    image = Image.open(image)

    # Get the image width and height
    width, height = image.size

    # Initialize variables for storing the sum of the RGB values
    red_sum = 0
    green_sum = 0
    blue_sum = 0

    # Loop through all the pixels in the image
    for x in range(width):
        for y in range(height):
            # Get the RGB values for the current pixel
            red, green, blue = image.getpixel((x, y))

            # Add the RGB values to the corresponding sums
            red_sum += red
            green_sum += green
            blue_sum += blue

    # Calculate the total number of pixels in the image
    total_pixels = width * height

    # Calculate the average RGB values
    red_avg = red_sum / total_pixels
    green_avg = green_sum / total_pixels
    blue_avg = blue_sum / total_pixels

    # Create a new image with the average RGB values
    average_image = Image.new(
        "RGB", (1, 1), (int(red_avg), int(green_avg), int(blue_avg))
    )

    # Save the new image
    average_image.save(r"calculated_image.png")

    # Open the image file
    image = Image.open(r"calculated_image.png")

    # Get the original width and height of the image
    original_width, original_height = image.size

    # Set the enlargement factor
    enlarge_factor = 300

    # Calculate the new width and height of the enlarged image
    new_width = original_width * enlarge_factor
    new_height = original_height * enlarge_factor

    # Resize the image using the NEAREST resampling method
    enlarged_image = image.resize(
        (new_width, new_height), resample=Image.Resampling.NEAREST
    )

    # Save the enlarged image
    enlarged_image.save(r"calculated_image.png")

    # Rounding RBG values for better consumption
    roundedRed = int(round(red_avg, 0))
    roundedGreen = int(round(green_avg, 0))
    roundedBlue = int(round(blue_avg, 0))

    # Print the average RGB values
    print(f"Average RGB values: ({roundedRed}, {roundedGreen}, {roundedBlue})")

    # Gets the Path of the image
    enlarged_image = r"calculated_image.png"

    global PhotoFile2

    # Displays the image in the GUI
    PhotoFile2 = PhotoImage(file=enlarged_image)
    PhotoOutput.config(image=PhotoFile2)


# Open the Explorer for a image to be selected
def selectFile():
    filetypes = (
        ("Images", ("*.jpg", "*.png")),
        ("Icon Files", "*.ico"),
        ("All files", "*.*"),
    )

    global image

    # Stores an image path after selection
    image = filedialog.askopenfilename(
        title="Open files",
        filetypes=filetypes,
        initialdir="C:/Desktop",
    )

    # Converts the image through PIL to avoid 'image not reconginasble error'
    image = convert_to_png(image)

    # Displays the Path to the GUI
    filenameLabel.config(text=image)

    global PhotoFile

    # Displays the Image on the GUI
    PhotoFile = PhotoImage(file=image)
    Photo.config(image=PhotoFile)


# Tk button that opens the file selector
selectFileButton = Button(
    root,
    width=10,
    height=1,
    text="Select A File",
    command=selectFile,
)
selectFileButton.pack()

# Tk label that shows the path of the file
filenameLabel = Label(root, text=" no image yet ")
filenameLabel.pack()

# TK Button that converts an inputted image into a color average
CalculateButton = Button(
    root,
    width=10,
    height=1,
    text="Calculate",
    command=Calculate,
)
CalculateButton.pack()

# Tk label that contains the starting image
PhotoFile = PhotoImage(file="")
Photo = Label(
    root,
    image=PhotoFile,
)
Photo.pack()

# Tk label that contains the output image
PhotoFile2 = PhotoImage(file="")
PhotoOutput = Label(
    root,
    image=PhotoFile2,
)
PhotoOutput.pack()

# Keeping the Tk GUI open
root.mainloop()
