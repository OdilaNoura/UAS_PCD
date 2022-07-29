# 1. Tes smoothing

from tabnanny import verbose
from scipy import misc
import matplotlib.pyplot as plt
from skimage.filters import gaussian

foto = misc.face()

plt.gray()
plt.imshow(foto)
plt.show()
smoothed = gaussian(foto, multichannel=True, sigma=2)

plt.imshow(smoothed)
plt.show()

# 2. Edge Detection merupakan salah satu proses yang fundamental dalam Pengolahan Citra yang bertujuan mengidentifikasi titik-titik pada citra digital dimana tingkat kecerahan (brightness) berubah drastis atau terjadi diskontinuitas.

from skimage import data
import matplotlib.pyplot as plt
from skimage.filters import sobel
from skimage.color import rgb2gray

gambarasli = data.astronaut()
gambarabu = rgb2gray(gambarasli)

gambar_edge = sobel(gambarabu)

plt.imshow(gambarabu, cmap=plt.cm.gray)
plt.show()

plt.imshow(gambar_edge)
plt.show()

# 3. Local Thresholding merupakan salah satu metode segmentasi citra dimana prosesnya didasarkan pada perbedaan derajat keabuan citra.

from skimage import data
import matplotlib.pyplot as plt
from skimage.filters import sobel
from skimage.color import rgb2gray

gambarasli = data.astronaut()
gambarabu = rgb2gray(gambarasli)
gambar_edge = sobel(gambarabu)

plt.imshow(gambarabu, cmap=plt.cm.gray)
plt.show()
plt.gray()
plt.imshow(gambar_edge)
plt.show()

# 4. Thresholding Global merupakan metode dengan seluruh pixel pada citra dikonversi menjadi hitam dan putih dengan satu nilai thresholding.

from skimage.filters import try_all_threshold
from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

gambarasli = data.astronaut()
gambarabu = rgb2gray(gambarasli)
plt.imshow(gambarasli)
plt.show()

fig, ax = try_all_threshold(
    gambarabu, figsize=(10, 8), verbose=False
)

fig.tight_layout()
plt.show()

# 5. Flip image

from PIL import Image
from matplotlib import pyplot as plt

img = Image.open(r"logounmer.png")
# buat objek image rotate 90 (lawan jarum jam)
imgrotate90 = img.rotate(90)

# buat objek image rotate -90 (searah jarum jam)
imgrotate90clockwise = img.transpose(Image.ROTATE_270)

# img.show()

fig, axes = plt.subplots(1,2, figsize=(8,4))
ax = axes.ravel()

ax[0].imshow(img)
ax[0]. set_title("Original")
ax[1].imshow(imgrotate90)
ax[1]. set_title("imgrotate90")
ax[2].imshow(imgrotate90clockwise)
ax[2]. set_title("imgrotate90clockwise")
fig.tight_layout()
plt.show()
