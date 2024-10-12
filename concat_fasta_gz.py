"""合并fata文件"""
import os 
from Bio import SeqIO
import gzip
from tqdm import tqdm

def get_seq_path(f_path):
    #创建表格，用于路径保存
    path_l = []
    #打印路径,确定为fasta的文件路径
    for root,dirs,files in os.walk(f_path):
        for file in files:
            if '.gz' in file:
                seq_path = os.path.join(root,file)  
                path_l.append(seq_path)

    return path_l
                            
def main():
    path = r'F:\01data\Klebsiella\Klebsiella pneumoniae\ncbi_dataset\ncbi_dataset\data'
    #合并文件
    seq_paths = get_seq_path(f_path=path)

    bar = tqdm(total=len(seq_paths),desc="序列合并进度",ncols=100,leave=True,unit='B',unit_scale=True)
    #创建新的文件
    new_f = open(f'{path}\\concat.fasta','wt')
    for seq_path in seq_paths:

        try:
            reads = gzip.open(seq_path,'rt')
            new_f.write(reads.read())
        except:
            print(seq_path)
        bar.update()
    new_f.close()

if __name__ == '__main__':
    main()