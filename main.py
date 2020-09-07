import os


def createfolderifnotexist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folder,files):
    for file in files:
        os.replace(file,f"{folder}/{file}")

if __name__ == "__main__":
   
    files = os.listdir()
    files.remove("main.py")

    createfolderifnotexist("images")
    createfolderifnotexist("docs")
    createfolderifnotexist("media")
    createfolderifnotexist("others")

    imgExt = [".jpeg", ".png", ".jpg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]

    docExt = [".docx",".doc", ".pdf", ".zip", ".rar", ".txt"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExt]

    mediaExt = [".mp4", ".mp3"]
    media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]
   
    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExt) and (ext not in docExt) and (ext not in mediaExt) and (os.path.isfile(file)):
            others.append(file)

    move("images",images)
    move("docs",docs)
    move("media",media)
    move("others",others)