from Bio import SeqIO

from concat_NCBI_dataset_seq import out_file


def extract_seq(seq_file ,extract_name):
    #读取文件
    records = SeqIO.parse(seq_file,'fasta')
    seq_dict = {}
    for record in records:
        if record.description in extract_name:
            seq = str(record.seq)
            seq_dict[record.description] = "\n".join([seq[i:i+80] for i in range(0,len(seq),80)])

    return seq_dict

def main():
    #提取想要的序列
    in_file = rf"{input("输入目标文件：")}"
    out_file = rf"{input("输出的文件位置：")}"
    extract_name = ["s875","s4816","s2451","s213","s1960","s4346","s140"]
    extract_l = extract_seq(seq_file=in_file,extract_name=extract_name)

#   输出新的文件
    f = open(out_file,'wt')
    for k,v in extract_l.items():
        f.write(f">{k}\n{v}\n")
    f.close()

if __name__ == "__main__":
    main()