from datetime import datetime

from rembg import remove
from PIL import Image
import easygui

input_path = easygui.fileopenbox(title='Select image to remove background: ',
                                 filetypes=[["*.png", "*.jpg", "Image files"]])

image_input = Image.open(input_path)
output = remove(image_input)

current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
output_path = easygui.filesavebox(title='Save file to: ',
                                  default='C:\\Users\\Monika\\Desktop\\'
                                          + current_time + '.png',
                                  filetypes=[["*.png", "*.jpg", "Image files"]])

# output_path = easygui.filesavebox(title='Save file to: ',
#                                   default='specify the path to the destination folder',
#                                   filetypes=[["*.png", "*.jpg", "Image files"]])

output.save(output_path)
# output.save(output_path + current_time + '_test.png')
exit()
