import qrcode
from PIL import Image

#This is the function called generate_qr_code.
#The data will be carry the information that will be storing the data.
#filename will be the name of the file 
#logo_path is none because later it will allow the user to put their own logo into it.
#You could put an image in there like "logo_path = image.png"
def generate_qr_code(data, filename, logo_path=None):

    qr = qrcode.QRCode(
        version=1,
        #The error correction rate is High, which makes it to where appx. A certain % of the
        #qr code can be recovered if the qr code is damaged.
        error_correction=qrcode.constants.ERROR_CORRECT_H,

        #This is the size of the box in the qr code.
        box_size=10,

        #The width of the border around the qr code.
        border=4,
    )

    #It adds the data to the qr
    qr.add_data(data)
    #It makes it to where the qr code will adjust its size based on the amount of information that needs to be encoded. 
    qr.make(fit=True)

    #This creates the qr code to be represented by an image.
    #The background will be white and the modules will be black.
    qr_img = qr.make_image(fill_color="black", back_color="white")

    #This is an "if statement", where it c
    if logo_path:
        #This is what opens the image you want to be in the qr code.
        logo = Image.open(logo_path)
        #This makes it transparent.
        qr_img = qr_img.convert("RGBA")
        #This changes the size of the logo in the center
        max_size = (300, 300)

        logo.thumbnail(max_size)
        logo_width, logo_height = logo.size




        
        qr_width, qr_height = qr_img.size

        #This helps to center the logo.
        pos = ((qr_width - logo_width) // 2, (qr_height - logo_height) // 2)
        #This is putting the entire logo onto the qr code.
        qr_img.paste(logo, pos, logo)

    #This will save the qr code 
    qr_img.save(filename)


if __name__ == "__main__":

    #input("Whatever you put here.") is how you get the input of the user to use later.
    #Then afterwards, it gets stored into a variable.

    #This is the site you want the usesrs to go to.
    data = input("Enter the website here.: ")
    #This is to get the name that you want the image to be saved under.
    filename = input("Enter the filename to save the QR code (e.g., qr_code.png): ")
    #If you have the logo in the folder, provide the path to it.
    logo_path = input("Enter the path to the logo image (leave empty for no logo): ")
    #This is calling the function to start working with the input of the user.
    generate_qr_code(data, filename, logo_path)

    #This will print in the terminal when everything is successful.
    print("QR code generated successfully!")
