#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
from PIL import Image

def resize_image(input_path, output_path, width, height):
    """
    将图片调整为指定尺寸并保存到指定路径
    
    参数:
        input_path (str): 输入图片的路径
        output_path (str): 输出图片的保存路径
        width (int): 目标宽度
        height (int): 目标高度
    """
    try:
        # 打开原始图片
        img = Image.open(input_path)
        
        # 调整图片大小
        resized_img = img.resize((width, height), Image.LANCZOS)
        
        # 确保输出目录存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 保存调整后的图片
        resized_img.save(output_path)
        
        print(f"图片已调整大小并保存到: {output_path}")
    except Exception as e:
        print(f"处理图片时出错: {e}")

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='调整图片大小的工具')
    parser.add_argument('--input', default='/home/wkr/workspace/workspace_lyl/Homepage/LYL1015.github.io/images/temple.png', help='输入图片的路径')
    parser.add_argument('--output', default='/home/wkr/workspace/workspace_lyl/Homepage/LYL1015.github.io/images/favicon-32x32.png', help='输出图片的保存路径')
    parser.add_argument('--width', type=int, default=32, help='目标宽度')
    parser.add_argument('--height', type=int, default=32, help='目标高度')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 调整图片大小
    resize_image(args.input, args.output, args.width, args.height)

if __name__ == "__main__":
    main()
