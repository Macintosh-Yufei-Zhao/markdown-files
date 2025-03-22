from PIL import Image

# 打开图片
image = Image.open('./temporary/250312.jpg')
# 转换为黑白
image_gray = image.convert('L')
# 反色操作
image_inverted = Image.eval(image_gray, lambda x: 255 - x)
# 保存或显示结果
image_inverted.save('inverted_image.jpg')
image_inverted.show()