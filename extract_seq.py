from Bio import SeqIO,Seq


def extract_seq(seq_file ,extract_name):
    #读取文件
    f = open(seq_file,'rt')
    id_l = []
    seq_l = []
    for line in f.readlines():
        if ">" in line:
            id_l.append(line.strip())
        else:
            seq_l.append(line.strip())
    seq_dict = {}
    # 筛选出想要的文件
    for k,v in zip(id_l,seq_l):
        if k[1:] in extract_name:
            seq_dict[k] = v

    # 输出序列文件
    n_f = open("提取的文件.fasta",'wt')
    for k,v in seq_dict.items():
        v = "\n".join(v[i:i+80] for i in range(0,len(v),80))
        n_f.write(f"{k}\n{v}\n")

    n_f.close()
    f.close()

    return print("提取的文件已经输出")

def main():
    #提取想要的序列
    file = 'split_res.fasta'
    extract_name = ["s2451","s2155"]
    extract_l = extract_seq(seq_file=file,extract_name=extract_name)

#   输出新的文件
#     f = open("提取的序列.fasta",'wt')
#     for k,v in extract_l:
#         f.write(f">{k}\n{v}\n")
#     f.close()

if __name__ == "__main__":
    main()