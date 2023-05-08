import cv2
import numpy as np
# from PIL import ImageFont, ImageDraw, Image
import math
import MouseMinWidth

mx = 0
my = 0
radius0 = 81
radius1 = 102
lcx = 124
lcy = 198
lcenter = (lcx, lcy)  # 左圆心
rcx = 1142
rcy = 198
rcenter = (rcx, rcy)  # 右圆心
# 读取图片文件
img = cv2.imread("mskover.png")
xiaoup = cv2.imread("maskup.png")
xiaoleft = cv2.imread("maskleft.png")
xiaodown=cv2.imread("maskdown.png")
xiaoright=cv2.imread("maskright.png")
# 获取图像尺寸
# height, width, channels = img.shape
img_copy = img.copy()  # 保存原始图片的副本
print(img.shape)
def get_cercle(cx, cy):
    angle_rad = math.atan2(cy - my, mx - cx)
    if angle_rad >= 0:
        angle_rad1 = angle_rad
    else:
        angle_rad1 = angle_rad + 2 * 3.1415926
    # 就用弧度算，不需要转角度
    y2 = int(cy - (radius1 * math.sin(angle_rad1)))
    x2 = int(cx + (radius1 * math.cos(angle_rad1)))
    y1 = int(cy - (radius0 * math.sin(angle_rad1)))
    x1 = int(cx + (radius0 * math.cos(angle_rad1)))
    return x1, y1, x2, y2


def get_mouse_pos(event, x, y, flags, param):
    global mx, my, img, y2, x2, y1, x1
    # 微调高度，注意y轴正方向
    trim_up = -5
    trim_upup = -10
  # 设置需要显示的字体
        # fontpath = "font/simsun.ttc"
        # font = ImageFont.truetype(fontpath, 32)
        # img_pil = Image.fromarray(img_draw)
        # draw = ImageDraw.Draw(img_pil)
        # # # 绘制文字信息
        # draw.text((100, 300), "Hello World", font=font, fill=(255, 255, 255))
        # draw.text((100, 350), "你好", font=font, fill=(255, 255, 255))
        # img = np.array(img_pil)
        # cv2.imshow("add_text", img)