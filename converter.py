import os
import subprocess

def convert (directory, file_name , targetPath):
    subprocess.run(["C:/Program Files (x86)/Calibre2/ebook-convert.exe", 
        f'{os.path.join(directory, file_name)}.epub', 
        f'{os.path.join(targetPath, file_name)}.mobi'])

def search(oriPath, fPath):
    print(f'=========\nsearching {oriPath}')
    for name in os.listdir(oriPath):
        
        #dir
        element = os.path.join(oriPath, name)
        if (os.path.isdir(element)):
            # print(element)
            newFolderPath = os.path.join(fPath, name) 
            os.mkdir(newFolderPath)
            search(element, newFolderPath)

        #file
        elif (os.path.isfile(element)):
            #isEpub()
            file_name, ext = os.path.splitext(name)
            # print(ext)
            if ext != ".epub":
                continue
            # convert()
            print(name)
            convert(oriPath, file_name, fPath)


if __name__ == "__main__":
    oriPath = "C:/Users/nicky/OneDrive/桌面/kindleBackup/DK_Documents"
    fPath = "C:/Users/nicky/OneDrive/桌面/mobi"
    search(oriPath, fPath)
    # subprocess.run(["C:/Program Files (x86)/Calibre2/ebook-convert.exe", r"C:\Users\nicky\OneDrive\桌面\三張牌.epub", r"C:\Users\nicky\OneDrive\桌面\三張牌.mobi"])