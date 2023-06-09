class MouseFilter(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.mx = 0
        # self.my = 0
        # self.radiusn = 86
        # self.radiusw = 104
        self.radiusn = 84
        self.radiusw = 100
        self.lcx = 100
        self.lcy = 148
        self.rcx = 1023
        self.rcy = 148
        self.y2 = None
        self.x2 = None
        self.y1 = None
        self.x1 = None
        self.b = None
        self.a = None
        self.piancha = 0
        # 微调高度，注意y轴正方向
        self.sutkuandu = 400
        self.trim_up = -5
        self.trim_upup = -10
        self.weitiaoleft = -8
        self.weitiaomiddle = 8
        self.img = cv2.imread("masked.png")
        self.xiaoup = cv2.imread("maskedup.png")
        self.xiaoright = cv2.imread("maskeright.png")
        self.xiaodown = cv2.imread("maskeddown.png")
        self.xiaoleft = cv2.imread("maskedleft.png")

    def get_circle(self, cx, cy):
        # print("cx,cy=", cx, cy)
        # print("self x,self y:",self.mx,self.my)
        angle_rad = math.atan2(cy - self.my, self.mx - cx)
        # # # # angle_rad = 3.14/8
        # # # print("园内鼠标坐标：", self.mx, self.my)
        if angle_rad >= 0:
            angle_rad1 = angle_rad
        else:
            angle_rad1 = angle_rad + 2 * math.pi
        print("圆心坐标", cx, cy)
        print("角度：", angle_rad1)
        y2 = int(cy - (self.radiusw * math.sin(angle_rad1)))
        x2 = int(cx + (self.radiusw * math.cos(angle_rad1)))
        y1 = int(cy - (self.radiusn * math.sin(angle_rad1)))
        x1 = int(cx + (self.radiusn * math.cos(angle_rad1)))
        # print("画线的两个交点坐标：", (x1, y1), (x2, y2))
        # x1 = 10
        # y1 = 10
        # x2 = 45
        # y2 = 45
        return angle_rad1,x1, y1, x2, y2

    # def get_angle(self, ccx, ccy):
    #     # print("cx,cy=", cx, cy)
    #     # print("self x,self y:",self.mx,self.my)
    #     angle = math.atan2(ccy - self.my, self.mx - ccx)
    #     # # # # angle_rad = 3.14/8
    #     print("园内鼠标坐标：", self.mx, self.my)
    #     if angle >= 0:
    #         angle = angle
    #     else:
    #         angle = angle + 2 *3.14
    #     print("角度是",angle)
    #     return angle

    def compute(self, mx, my):
        global x1, y1, y2, x2, flag, width, rate
        flag = True
        width = 1
        rate = 1

        if self.lcx > mx >= 0:
            angle_01, x1, y1, x2, y2 = self.get_circle(self.lcx, self.lcy)
            # flag, width, rate = MouseMinWidth.MouseMinWidthInRing(angle_01, 99,
            #                                                       100, self.radiusn, self.radiusw,
            #                                                       self.xiaoleft)
            flag, width, rate = MouseMinWidth.MouseMinWidthInRing(angle_01,self.lcx-1 ,
                                                                  self.radiusw, self.radiusn, self.radiusw,
                                                                  self.xiaoleft)



            # # flag, width,rate = MouseMinWidth.MouseMinWidthInRing(x2 - (self.lcx - self.radiusw),
            # #                                                 y2 - (self.lcy - self.radiusw) + self.piancha,
            # #                                                 x1 - (self.lcx - self.radiusw),
            # #                                                 y1 - (self.lcy - self.radiusw) + self.piancha,
            # #                                                 self.xiaoleft)
            # # flag, width, rate = MouseMinWidth.MouseMinWidthInRing(x2,
            # #                                                       y2 + self.piancha,
            # #                                                       x1,
            # #                                                       y1 + self.piancha,
            # #                                                       self.xiaoleft)
            # flag, width, rate = MouseMinWidth.MouseMinWidthInRing(x2,
            #                                                       y2 + self.piancha,
            #                                                       x1,
            #                                                       y1 + self.piancha,
            #                                                       self.xiaoleft)
            # print(flag,width)

        if self.lcx <= mx <= (self.lcx + (self.rcx - self.lcx) / 2) and 0 < my <= self.rcy:
            x1 = x2 = mx
            y1 = self.lcy - self.radiusw
            y2 = self.lcy - self.radiusn
            # print("中间交点坐标：",x1,y1,x2,y2)
            xx = x1 - self.lcx
            # print("xx:", xx)
            # print("鼠标坐标:", mx, my)
            # print(" ")
            flag, width, rate = MouseMinWidth.MouseMinWidthInLine(xx, self.xiaoup)
        if (self.lcx + (self.rcx - self.lcx) / 2) < mx <= self.rcx and 0 < my <= self.rcy:
            x1 = x2 = mx
            y1 = self.lcy - self.radiusw
            y2 = self.lcy - self.radiusn
            # print("中间交点坐标：",x1,y1,x2,y2)
            xx = x1 - self.lcx - 1
            # print("xx:", xx)
            # print("鼠标坐标:", mx, my)
            # print(" ")
            flag, width, rate = MouseMinWidth.MouseMinWidthInLine(xx, self.xiaoup)
        if self.lcx <= mx <= (self.lcx + (self.rcx - self.lcx) / 2) and my > self.rcy:
            x1 = x2 = mx
            y1 = self.lcy + self.radiusw + self.piancha
            y2 = self.lcy + self.radiusn + self.piancha
            # print("中间交点坐标：",x1,y1,x2,y2)
            xx = x1 - self.lcx
            # print("xx:", xx)
            # print("鼠标坐标:", mx, my)
            # print(" ")
            flag, width, rate = MouseMinWidth.MouseMinWidthInLine(xx, self.xiaoup)
        if (self.lcx + (self.rcx - self.lcx) / 2) < mx <= self.rcx and my > self.rcy:
            x1 = x2 = mx
            y1 = self.lcy + self.radiusw + self.piancha
            y2 = self.lcy + self.radiusn + self.piancha
            # print("中间交点坐标：",x1,y1,x2,y2)
            xx = x1 - self.lcx - 1
            # print("xx:", xx)
            # print("鼠标坐标:", mx, my)
            # print(" ")
            flag, width, rate = MouseMinWidth.MouseMinWidthInLine(xx, self.xiaoup)
        # if self.lcx <= mx < self.rcx and my > self.rcy:
        #     x1 = x2 = mx
        #     y1 = self.lcy + self.radiusw + self.piancha
        #     y2 = self.lcy + self.radiusn + self.piancha
        #     xx = x1 - self.lcx
        #     flag, width, rate = MouseMinWidth.MouseMinWidthInLine(xx, self.xiaodown)
        if mx > self.rcx:
            angle_01, x1, y1, x2, y2 = self.get_circle(self.rcx, self.rcy)
            # flag, width, rate = MouseMinWidth.MouseMinWidthInRing(angle_01, 0,
            #                                                       100, self.radiusn, self.radiusw,
            #                                                       self.xiaoright)
            flag, width, rate = MouseMinWidth.MouseMinWidthInRing(angle_01, -1,
                                                                  self.radiusw, self.radiusn, self.radiusw,
                                                                  self.xiaoright)

            # # flag, width, rate = MouseMinWidth.MouseMinWidthInRing(x2 - self.rcx,
            # #                                                       y2 - (self.lcy - self.radiusw) + self.piancha,
            # #                                                       x1 - self.rcx,
            # #                                                       y1 - (self.lcy - self.radiusw) + self.piancha,
            # #                                                       self.xiaoright)
            # flag, width, rate = MouseMinWidth.MouseMinWidthInRing(x2,
            #                                                       y2 + self.piancha - 49,
            #                                                       x1,
            #                                                       y1 + self.piancha - 49,
            #                                                       self.xiaoright)
        # print(x1, y1, x2, y2, flag, width, rate)

        return x1, y1, x2, y2, flag, width, rate