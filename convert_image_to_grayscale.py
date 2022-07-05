# convert images from color to grayscale
# python convert image to grayscale.py --input color --output blackwhite

from PIL import Image
from glob import glob
from argparse import ArgumentParser

parser = ArgumentParser(description='Converting jpeg color images to black-white images')
parser.add_argument('--input', help='Directory from which the images will be downloaded.', required=True)
parser.add_argument('--output', help='Directory/Folder where the images will be saved.', required=True)
args = parser.parse_args()
print(args.input, args.output)

for path in glob(args.input + '/*'):  # asterisk gets filenames from a folder (input directory)
    directory, filename = path.split('\\')
    print(path, directory, filename)

    # to convert color images to grayscale:
    with Image.open(path) as new_image:
        grayscale_image = new_image.convert('L')
        grayscale_image.save(args.output + '/' + filename)  # save(0 argument: path to new convert photos)

# run the file:
# open terminal, command: python convert_image_to_grayscale.py --input color --output grayscale
# to display help information: python convert_image_to_grayscale.py -h (or --help)
