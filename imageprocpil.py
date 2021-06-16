from PIL import Image , ImageFilter

im=Image.open('shakeerpicnew.jpeg')

# # im.rotate(180).show()
#
# im.thumbnail ((1000,1000))
# im.show()
# # im.size(1000,1000)
# # print(im)

im=im.convert("L")
im = im.filter(ImageFilter.FIND_EDGES)
im.save(r"Edge_Sample_shakeer.png")

