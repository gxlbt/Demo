#!/usr/bin/python3
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-4-10 11:03
# @File    : game1.py
# @Software: PyCharm


# 代码参考来源：微信公众号：菜鸟学Python

import tkinter
import random
import time
import tkinter.messagebox
import sys

tk = tkinter.Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = tkinter.Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)  # 设置窗口大小
canvas.pack()
tk.update()


# 定义一个球类
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.paddle = paddle
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[0] <= 0:
            self.x = 1
        if pos[3] >= self.canvas_height:
            self.y = -1
        if pos[2] >= self.canvas_width:
            self.x = -1
        if self.hit_paddle(pos):
            self.y = -3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            a = tkinter.messagebox.showinfo('提示', '游戏结束')
            if a:
                sys.exit(0)


# 定义一个木板类
class Paddle:
    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 150, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0


paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")
while 1:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
