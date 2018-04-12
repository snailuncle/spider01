from skimage import io
import matplotlib.pyplot as plt
from skimage import morphology
img_path=r"D:\captcha\original\jpeq82584.jpg"
img=io.imread(img_path)
img=morphology.remove_small_objects(img,min_size=300,connectivity=1)
io.imshow(img)
plt.show()
