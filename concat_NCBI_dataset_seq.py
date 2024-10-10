import os
from tqdm import tqdm

f = r'F:\01data\Enterococcus_faecium\ncbi_dataset\ncbi_dataset\data'


def merge_seq(path,out_file):
    bar = tqdm(total=len(os.listdir(path)),desc="序列文件合并进度",ncols=100,leave=True,unit="B",unit_scale=True)
    with open(out_file,'wt') as out_f:
        #遍历文件夹
        for floder_path in os.listdir(path):
            #确定每个子文件夹的路径
            floder_path = os.path.join(path,floder_path)
            #判断是不是文件夹
            if os.path.isdir(floder_path):
                for file_path in os.listdir(floder_path):
                    file_path = os.path.join(floder_path,file_path)
                    infile = open(file_path,'rt',encoding='utf-8')
                    out_f.write(infile.read())
                    out_f.write('\n')
                    bar.update()
                    infile.close()
    out_f.close()

def main():
    out_file = input("输出文件名：")
    merge_seq(path=f,out_file='res.fasta')

if __name__ == "__main__":
    main()