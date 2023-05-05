import cv2

import math

mx = 0.0
my = 0.0
radius0 = 70
radius1 = 80
cx = 82
cy = 81
center = (cx, cy)  # 圆心
# 读取图片文件
img = cv2.imread("cycle.png")
img_copy = img.copy()  # 保存原始图片的副本


def get_mouse_pos(event, x, y, flags, param):
    global mx, my, img

    if event == cv2.EVENT_MOUSEMOVE:

        mx, my = x, y

        img_draw = img_copy.copy()
        print("鼠标坐标：", (x, y))
        angle_rad = 0

        angle_rad = math.atan2(cy - my, mx - cx)  # 计算弧度值
        #方一--对弧度制取余2*pi
        angle_rad1= angle_rad%(2*3.1415926)
        #方二--判断
        # if angle_rad >= 0:
        #     angle_rad1 = angle_rad
        # else:
        #     angle_rad1 = angle_rad + 2 * 3.1415926
        # 就用弧度算，不需要转角度
        y2 = int(cy - (radius1 * math.sin(angle_rad1)))
        x2 = int(cx + (radius1 * math.cos(angle_rad1)))
        y1 = int(cy - (radius0 * math.sin(angle_rad1)))
        x1 = int(cx + (radius0 * math.cos(angle_rad1)))
        print("x1=", x1, "y1=", y1)
        print("x2=", x2, "y2=", y2)
        print(" ")
        # 把圆心标注出来
        img_draw[cy, cx] = [255, 255, 255]
        cv2.line(img_draw, (x1, y1), (x2, y2), (0, 255, 0), 1)
        # 在图像上绘制圆，最后一个参数是线条的宽度，-1 表示填充整个圆形
        # cv2.circle(img_draw, center, radius0, (255, 255, 255), 1)
        # cv2.circle(img_draw, center, radius1, (255, 255, 255), 1)


        # 显示更新后的图像
        cv2.imshow("image", img_draw)


# 初始化显示窗口
cv2.namedWindow("image")

# 绑定鼠标事件处理函数
cv2.setMouseCallback("image", get_mouse_pos)
# 在窗口中显示图片
cv2.imshow("image", img)

cv2.waitKey(0)

# 释放窗口资源
cv2.destroyAllWindows()

