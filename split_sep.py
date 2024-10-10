'''
   打断fasta序列,设置切段数目，根据长度进行切分
'''
import random
from  numpy import random
import numpy as np
import multiprocessing.pool as p
from Bio import SeqIO

# from concat_NCBI_dataset_seq import out_file


#根据传入的序列，打断的数目进行序列切分
def seq_split(file,split_lens,out_file=None):
    """
    file:fasta
    split_lens:切分长度
    out_file:out_path
    """
    record = SeqIO.read(file,'fasta')
    seq = record.seq
    # 确定每一段的长度,取整数
    seq_len = len(seq)
    blocks = seq_len//split_lens
    split_index = 0
    seq_dict = {}

    # 根据确定的长度进行切分，并输出到字典，键值为id名字，值为序列。
    for split_len in range(split_lens):
        tem_seq = seq[split_index:split_index + blocks]
        len_name = f"{str(split_index)}_{str(split_index + blocks)}"
        split_index = split_index + blocks
        seq_dict[f'>s{split_len}_{len_name}'] = tem_seq

    res_fasta = open(f'{out_file}','wt')
    for k,v in seq_dict.items():
        res_fasta.write(f'{k}\n{v}\n')
    res_fasta.close()

    return seq_dict



def main():
    file = r'F:\01data\Klebsiella\01Klebsiella_oxytoca.fasta'
    out_file = r'F:\01data\Klebsiella\02Klebsiella_oxytoca_split_10000.fasta'
    seq_dic = seq_split(file, 10000, out_file=out_file)


if __name__ == '__main__':
    main()