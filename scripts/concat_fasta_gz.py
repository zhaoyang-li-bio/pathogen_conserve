"""合并fata文件"""
import os 
from Bio import SeqIO
import gzip
from tqdm import tqdm
from pathlib import Path

def get_seq_path(f_path):
    #创建表格，用于路径保存
    path_l = []
    #打印路径,确定为fasta的文件路径
    for root,dirs,files in os.walk(f_path):
        for file in files:
            if '.gz' in file:
                seq_path = os.path.join(root,file)  
                path_l.append(seq_path)
    #增加了fn的压缩包文件合并
            elif '.fn' in file:
                seq_path = os.path.join(root,file)
                path_l.append(seq_path)
    return path_l

def concat_seq(seq_paths,out_path,type):
    """
    type:input file format,'.gz' or '.fn' 'fasta'
    seq_paths: list contain path of seq
    out_path: path of save fasta file
    """

    # make a line of process
    bar = tqdm(total=len(seq_paths),desc="序列合并进度",ncols=100,leave=True,unit='B',unit_scale=True)
    # make new fasta file
    new_f = open(f'{out_path}.fasta','wt')
    for seq_path in seq_paths:
        try:
            if type == 'gz':
                content = gzip.open(seq_path,'rt')
            elif type == 'fna':
                content = open(seq_path,'rt')
            new_f.write(content.read())
        except:
            print(seq_path)

        bar.update()
    new_f.close()

def main():
    option = input("合并单个文件夹还是多个文件夹（选择0或1）：")
    if option == "0" :
        path = input("输入要合并的NCBI下载的gz：")
        type = input("输入的文件合并类型（fna/gz）:")
        path = fr'{path}'
        #合并文件
        seq_paths = get_seq_path(f_path=path)
        concat_seq(seq_paths=seq_paths,out_path=path,type=type)
    elif option == "1" :
        paths = input("输入要合并主要的文件夹：")
        type = input("输入的文件合并类型（fna/gz）:")
        file_path = []
        for path in os.listdir(paths):
            # 合并文件
            path = os.path.join(paths,path)
            if os.path.isdir(path):
                seq_paths = get_seq_path(f_path=path)
                file_path.append(seq_paths[0])
                #确认名字与解压文件一致
                file_name_list = path.split("\\")
                file_name = file_name_list[-1]

    out_file = os.path.join(paths,"concat")
    concat_seq(seq_paths=file_path, out_path=out_file, type=type)

if __name__ == '__main__':
    main()