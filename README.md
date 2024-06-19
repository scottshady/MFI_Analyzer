# MFI Analyzer

##强烈建议将待处理的荧光视频软件提前通过davinci等视频处理软件去除背景信号峰确保分析结果准确

## 简介

 MFI Analyzer 用于处理生化实验中的荧光视频文件（尤其是记录pefusion chamber的荧光视频），从帧的特定区域提取数据，并将结果保存到 CSV 文件中。该工具已打包为可独立于 Python 环境运行的可执行文件。

## 功能

- 处理以下格式的视频文件： `.mov`、`.mp4` 和 `.avi`
- 每秒提取一帧图片并选取五个区域做重复
- 分析每帧中的特定区域并计算平均强度
- 将分析结果输出为 CSV 文件

## 使用方法

1. **下载和准备**：下载MFI_Analyzer.exe文件并在相同目录中新建input，output文件夹
2. **准备输入文件**：将您的视频文件放在 `input` 目录中。
3. **运行应用程序**：双击可执行文件（`MFI_Analyzer.exe`）开始处理。程序会自动处理 `input` 目录中的所有视频文件。
4. **查看结果**：处理结果将保存到 `output` 目录中，格式为 CSV 文件。

## 输入文件要求

- **视频格式**： `.mov`、`.mp4`、`.avi`

## Introduction

The `MFI_Analyzer` software is designed to process video files, extract data from specific areas of the frames, and save the results into a CSV file. This tool has been packaged into an executable file that runs independently of the Python environment. 

## Features

- Processes video files in formats: `.mov`, `.mp4`, and `.avi`.
- Analyzes specific squares in each frame and computes the mean intensity.
- Outputs the analysis results into a CSV file.

## How to Use

1. **Download and Unpack**: Download the executable package and unpack it into a directory.
2. **Prepare Input Files**: Place your video files in the `input` directory within the unpacked folder.
3. **Run the Application**: Double-click the executable file (`MFI_Analyzer.exe`) to start the processing. The program will automatically process all video files in the `input` directory.
4. **View Results**: Processed results will be saved in the `output` directory as CSV files.

## Input File Requirements

- **Video Formats**: `.mov`, `.mp4`, `.avi`

## Contact Us

For any questions, please contact the authors:
- Tianyu Wang      Terrywangtianyu@gmail.com
- Shaoyun Zhou
- Chuanbin Shen

## License

See LICENSE file for license details.
