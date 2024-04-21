from PIL import Image
import os
import subprocess

def convert_png_to_dds_with_bc5(input_image, output_image):
    try:
        subprocess.run(["nvcompress", "-bc5", input_image, output_image], check=True)
        print(f"Converted {input_image} to {output_image} using bc5 compression.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_image} to DDS: {e}")

def batch_convert_png_to_dds_with_bc5(input_folder):
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.lower().endswith(".png"):
                input_path = os.path.join(root, filename)
                output_path = os.path.join(root, os.path.splitext(filename)[0] + ".dds")
                convert_png_to_dds_with_bc5(input_path, output_path)

if __name__ == "__main__":
    input_folder2 = input("What is the location? ")
    input_folder = input_folder2.replace("\\", "\\\\")
    print(input_folder)
    batch_convert_png_to_dds_with_bc5(input_folder)  # Output files will be saved in the same directory
