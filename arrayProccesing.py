import numpy as np
from PIL import Image

def Estandarize(array, colors):
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i][j] not in colors:
                array[i][j] = 0
    return array


def ArrayToImage(array, filename):
    array = np.array(array)
    arr = ImageConvert(array)
    arr = Image.fromarray(arr, 'RGB')
    arr.save(filename)

def ImageConvert(array, startColor=None, endColor=None):
    temp = []
    for i in range(array.shape[0]):
        temp2=[]
        for j in range(array.shape[1]):
            match array[i][j]:
                case 1:
                    temp2.append([255,255,255])
                case 0:
                    temp2.append([0,0,0])
                case 4:
                    temp2.append([0,255,0])
                case 5:
                    temp2.append([255,0,0])
                case 8:
                    temp2.append([0,0,255])
        temp.append(temp2)
    return np.array(temp, dtype=np.uint8)

def NoNumpy(array):
    arr = array.tolist()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==4 or arr[i][j]==5:
                arr[i][j]=str(arr[i][j])
    return arr

def ImageSetup(path):
    im = Image.open(path)

    im = im.resize((30, 30), Image.NEAREST)
    im = im.quantize(6)
    array = np.array(im)
    array = Estandarize(array, [0,1,4,5])
    arr = NoNumpy(array)
    return arr
