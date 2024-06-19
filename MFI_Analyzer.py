# -*- coding: utf-8 -*-
"""
MFI_Analyzer

© 2024 Tianyu Wang, Shaoyun Zhou, Chuanbin Shen
Institution: Ocean University of China

This software is for academic use only.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use the Software for personal, non-commercial purposes only, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
# -*- coding: utf-8 -*-
"""
BurgerCat 视频处理工具

© 2024 王天宇, 周绍芸, 申传斌
单位: 中国海洋大学
联系方式：terrywangtianyu@gmail.com
该软件仅限学术用途。

特此免费授予获得本软件及相关文档文件（“软件”）副本的任何人使用本软件的权利，仅限于个人、非商业用途，条件如下：

上述版权声明和本许可声明应包含在本软件的所有副本或主要部分中。

本软件按“原样”提供，不附带任何明示或暗示的担保，包括但不限于适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有人均不对因软件或软件的使用或其他交易中的行为而产生的任何索赔、损害或其他责任负责，无论是在合同诉讼、侵权诉讼还是其他方面。
"""


import datetime
import sys

# 获取当前日期
current_date = datetime.datetime.now()

# 设定截止日期
deadline_date = datetime.datetime(2025, 6, 18)

# 判断日期并执行相应操作
if current_date < deadline_date:
    import sys
    import os
    import cv2
    import csv
    import numpy as np
    import random

    # 获取当前程序所在目录
    if hasattr(sys, 'frozen'):
        current_directory = os.path.dirname(sys.executable)
    else:
        current_directory = os.path.dirname(os.path.abspath(__file__))

    print(f"当前目录: {current_directory}")

    # 定义输入和输出目录
    input_folder = os.path.join(current_directory, 'input')
    output_folder = os.path.join(current_directory, 'output')
    os.makedirs(output_folder, exist_ok=True)

    # 列出输入目录中的所有文件
    input_files = os.listdir(input_folder)
    print(f"所有输入文件: {input_files}")

    processed_files = []


    def process_fa(video_path, output_file_path):
        try:
            def select_squares(gray_frame, num_squares=5, square_size=None):
                squares = []
                for _ in range(num_squares):
                    x = random.randint(0, gray_frame.shape[1] - square_size)
                    y = random.randint(0, gray_frame.shape[0] - square_size)
                    squares.append((x, y))
                return squares

            def analyze_frame(frame, selected_squares, scale_factor=10000000 / 255):
                frame_results = []
                for x, y in selected_squares:
                    square = frame[y:y + square_size, x:x + square_size]
                    mean_intensity = np.mean(square)
                    frame_results.append(mean_intensity * scale_factor)
                return frame_results

            cap = cv2.VideoCapture(video_path)
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            square_size = frame_width // 5
            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_count = 0
            selected_squares = []
            output_file_path_csv = output_file_path.replace('.xlsx', '.csv')
            with open(output_file_path_csv, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['time(sec)', '1', '2', '3', '4', '5'])
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    if frame_count == 0:
                        selected_squares = select_squares(gray_frame, square_size=square_size)
                    if frame_count % int(fps) == 0:
                        frame_results = analyze_frame(gray_frame, selected_squares)
                        writer.writerow([frame_count // int(fps)] + frame_results)
                    frame_count += 1
            cap.release()
            print(f"处理视频文件: {video_path}")
        except Exception as e:
            print(f"处理文件 {video_path} 时出错: {e}")


    # 处理所有输入文件
    for file in input_files:
        file_path = os.path.join(input_folder, file)
        output_file_path = os.path.join(output_folder, f"output-{os.path.splitext(file)[0]}.xlsx")

        if file.endswith(('.mov', '.mp4', '.avi')):
            process_fa(file_path, output_file_path)
            processed_files.append(output_file_path)

    print(f"本次共处理 {len(processed_files)} 个文件，其中包括：")
    for file in processed_files:
        print(file)

else:
    sys.exit()
