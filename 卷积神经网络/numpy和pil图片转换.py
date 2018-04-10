# 了在pillow.Image和numpy array之间进行转换，可以使用以下代码：

# from PIL import Image
# from numpy import array
# img = Image.open("input.png")
# arr = array(img)
# 1
# 2
# 3
# 4
# 5
# img = Image.fromarray(arr)
# 1
# 或

# def array2PIL(arr, size):
#     mode = 'RGBA'
#     arr = arr.reshape(arr.shape[0]*arr.shape[1], arr.shape[2])
#     if len(arr[0]) == 3:
#         arr = numpy.c_[arr, 255*numpy.ones((len(arr),1), numpy.uint8)]
#     return Image.frombuffer(mode, size, arr.tostring(), 'raw', mode, 0, 1)
