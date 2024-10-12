"""
    Author:zhaoyangLi
    Data:20241011
    Purpose:build a GUI for script
    Configure of environments: python 3.12; flet 0.24.1
"""

import flet as ft
import os
from Blaxtfunction import makeblast_db,local_blast

from pandas import DataFrame

def current_dir():
    #构建当前文件的路径
    file_path = os.path.abspath(__file__)
    # 获取当前目录
    script_dir = os.path.dirname(file_path)
    # #获取上级目录
    # file_superior_path = os.path.dirname(script_dir)

    return script_dir
def main(page:ft.Page):
    #获取当前文件的目录
    superior_path = current_dir()

    #设置应用标题
    page.title = "细菌保守序列查找"
    #导入自定义字体
    page.fonts = {"Italics":os.path.join(superior_path,'LuoGuoChengMaoBiXiaoXingJianTi-2.ttf')}
    #创建第1个行布局
    row_1_layout = ft.Row()
    row_1_layout.controls.append(ft.Text("步骤1：下载基因组序列",size=38,font_family="Italics"))

    #创建第2个行布局
    row_2_layout = ft.Row()

    row_2_layout.controls.append(ft.Text("步骤2：构建对应的本地库",size=38,font_family="Italics"))
    #添加文件提取
    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            print(selected_files.value)
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        )
    )

    #库名的返回
    row_2_field = ft.TextField(label="构建的库名",text_size=38)
    row_2_layout.controls.append(row_2_field)


    #创建第3个行布局
    row_3_layout = ft.Row()
    row_3_layout.controls.append(ft.Text("步骤3：确定参考基因组",size=38,font_family="Italics"))

    #创建第4个行布局
    row_4_layout = ft.Row()
    row_4_layout.controls.append(ft.Text("步骤4：切分参考基因组",size=38,font_family="Italics"))

    #创建第5个行布局
    row_5_layout = ft.Row()
    row_5_layout.controls.append(ft.Text("步骤5：序列比对分析",size=38,font_family="Italics"))

    #创建第6个行布局
    row_6_layout = ft.Row()
    row_6_layout.controls.append(ft.Text("步骤6：查看比对结果",size=38,font_family="Italics"))

    #创建第7个行布局
    row_7_layout = ft.Row()
    row_7_layout.controls.append(ft.Text("步骤7：提取对应的保守序列",size=38,font_family="Italics"))

    #将布局添加到页面中
    page.add(row_1_layout,row_2_layout,row_3_layout,row_4_layout,row_5_layout,row_6_layout,row_7_layout)
    page.update()

ft.app(target=main)