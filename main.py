from PIL import Image
import os
import shutil


def check_if_exists(path_to_directory):
    if os.path.exists(path_to_directory):
        print(f"Directory exists at: {path_to_directory}")
    else:
        print("False")


def make_new_directory(new_directory_name):
    appended_path = "/Users/mark/Desktop/"
    full_path = os.path.join(appended_path, new_directory_name)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
        print(f"Directory has been created at: {full_path}")
    else:
        print("Directory already exists.")


def name_directory():
    print("What do you want to name the new directory? No special chars")
    new_directory_name = input()
    return new_directory_name


# needs work
def load_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.tif'):
            img = Image.open(os.path.join(folder_path, filename)) # open allows for image manipulation-
            images.append(img)
            print("Adding tif: " + filename)
        else:
            print("This probably jpg not adding")
    return images


def view_image(photos):
    #to view we may have to view directly from the computer
    im = Image.open("/Users/mark/Desktop/testing/image_9.tif")
    im.show()
    # for photo in photos:
    #     v_photo = Image.open(photo)
    #     v_photo.show()


def resize_images(image_path, output_size=(512, 512)):
    resized_images = [img.resize(output_size) for img in image_path]
    return resized_images

#TODO: is the correct image being checked? can we make sure that the
def check_if_portrait(image_path):
    image_count = 0
    images = load_images_from_folder(image_path)

    for image in images:
        if image.height > image.width:
            print(f"Image {image_count} is portrait")
        elif image.width > image.height:
            print(f"Image {image_count} is landscape")
        else:
            print(f"Image {image_count} is square")
        print(f"Width: {image.width}, Height: {image.height}")
        image_count += 1
def copy_images(folder_path, new_path_name):
    filename_count = 0
    if not os.path.exists(new_path_name):   # probably needs to be deleted.
        os.makedirs(new_path_name)
    for filename in os.listdir(folder_path):
        # Copy the file to the new directory
        if filename.endswith('.tif'):
            shutil.copy(os.path.join(folder_path, filename), os.path.join(new_path_name, f"image_{filename_count}.tif"))
            filename_count += 1
    print(f"Copied {filename_count} images to {new_path_name}")



def main():
    while True:
        print("\nSelect an option:")
        print("1: Check if a directory exists")
        print("2: Create a new directory")
        print("3: Name a directory")
        print("4: Load images from a folder")
        print("5: Copy images to a new folder")
        print("6: Check if the image is landscape or portrait.")
        print("7: Testing if images exist in path ")
        print("0: Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            break
        elif choice == '1':
            path = input("Enter the path to check: ")
            check_if_exists(path)
        elif choice == '2':
            new_directory_name = name_directory()
            make_new_directory(new_directory_name)
        elif choice == '3':
            new_directory_name = name_directory()
            print(f"Directory name is: {new_directory_name}")
        elif choice == '4':
            folder_path = input("Enter the folder path to load images from: ")
            images = load_images_from_folder(folder_path)
            print(f"Loaded {len(images)} images.")
        elif choice == '5':
            folder_path = input("Enter the folder path to copy images from: ")
            new_path_name = input("Enter the new directory path to copy images to: ")
            copy_images(folder_path, new_path_name)
        elif choice == '6':
            image_path = input("What is the image path")
            check_if_portrait(image_path)
        elif choice == '7':
            print("Loading the images")
            images_loaded = load_images_from_folder("/Users/mark/Desktop/testing")
            print(images_loaded)
            view_image(images_loaded)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
