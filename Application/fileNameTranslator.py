"""main ideas taken from https://stackoverflow.com/questions/9553262/pyinstaller-ioerror-errno-2-no-such-file-or-directory"""
import os

def translateFileName(fileName):
    if '_MEIPASS2' in os.environ:
        fileName = os.path.join(os.environ['_MEIPASS2'], fileName))
    return fileName