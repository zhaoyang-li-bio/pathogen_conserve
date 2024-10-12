from Bio import SeqIO

def extract_seq(seq_file ,extract_name):
    #读取文件
    records = SeqIO.parse(seq_file,'fasta')
    seq_dict = {}
    for record in records:
        if record.description in extract_name:
            seq = str(record.seq)
            seq_dict[record.description] = "\n".join([seq[i:i+80] for i in range(0,len(seq),80)])

    return seq_dict

class FastalKit:
    """
    用于提取基因序列。
    """
    def __init__(self,seq_f,option) -> None:
        self.records = SeqIO.parse(seq_f,'fasta')
    
    def extract_by_option(self,options):
        """从一个fasta文件中,按列表进行分类，给出字典。
        """
        for record in self.records:
            for option in options:
                if option in record.description:

def main():
    #提取想要的序列
    file = './data/spaovirus.fasta'
    # extract_name = ["s875","s4816","s2451","s213","s1960","s4346","s140"]
    # extract_l = extract_seq(seq_file=file,extract_name=extract_name)

#   输出新的文件
    # f = open("提取的序列.fasta",'wt')
    # for k,v in extract_l.items():
    #     f.write(f">{k}\n{v}\n")
    # f.close()
    
    FastalKit(seq_f=file)

if __name__ == "__main__":
    main()