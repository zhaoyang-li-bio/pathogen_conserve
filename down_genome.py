"""使用biopython的entrez模块下载基因组序列
    日期：20240729
    作者：李朝阳
    思路：从db库genome搜索，得到对应的id,
        使用efetch进行下载，到对应的文件夹。
"""

from Bio import Entrez,SeqIO
from tqdm import  tqdm
import os
import subprocess
class NcbiSeqDown:
    """
        尝试写一个用于下载序列的类
    """
    #email填写，用于NCBI联系到我，告知不要用过度。
    Entrez.email = "1045700857@qq.com"
    def __init__(self,query,db):
        self.query = query
        self.db = db
    #定义获取查询的信息
    def query_info(self,mindate=None,maxdate=None):
        #查询的数据库，日期，datetype是查询的类型，
        handle = Entrez.esearch(db=self.db,term=self.query,datetype='pdat',mindate=mindate,maxdate=maxdate,retmax=1000)
        record = Entrez.read(handle)
        #查找的id构建成列表
        id_list = record['IdList']
        handle.close()
        return id_list
    def efetch_info(self,id_list,rettype='fasta',retmode="text",out_file='down_seq.fasta'):
        #根据列表查找对应的信息，用efetch进行查找。
        handle = Entrez.efetch(db=self.db,id=id_list,rettype=rettype,retmode=retmode)
        records = SeqIO.parse(handle,"fasta")
        #构建进度条
        pbar = tqdm(total=len(id_list),desc="序列下载进度",leave=True,ncols=100,unit='B',unit_scale=True,colour='yellow')
        fasta_f = open(out_file,'wt')
        #输出序列，形成fasta的文件
        e_l = []
        for record in records:
            #将下载不到序列的id输出到指定文件，同时将flag=1，以便输出提示
            seq_name = record.description

            try:
                fasta_f.write(f">{record.id}{seq_name}\n{record.seq}\n")
            except:
                e_l.append(record.id)
            pbar.update(1)

        fasta_f.close()


    def makedb(self,file,db_name):
        #使用命令行进行建库
        command = f"makeblastdb -dbtype nucl -in {file} -out {db_name}"
        subprocess.run(command)


    def mkdb(self,db_name):
        # 确定工作目录
        cur_path = os.getcwd()
        db_path = os.path.join(cur_path,db_name)
        # 创建序列库的文件夹
        if os.path.isdir(db_path):
            pass
        else:
            os.mkdir(db_path)
    def seq_balxt(self,fasta,db):
        #序列比对的软件
        command = f"blastn -db {db} -query {fasta} -evalue 1e-5 -outfmt 5 > con_blast.xml"

def main():

    seq = NcbiSeqDown(db='nucleotide',query='Cronobacter dublinensis')
    # 查找序列id
    id_list = seq.query_info(mindate="2014/01/01",maxdate="2024/06/01")

    print(id_list)

    # #下载序列
    # seq.efetch_info(id_list=id_list,out_file="Cronobacter_dublinensis.fasta")
    # # 创建库名
    # # seq.mkdb(db_name="Cronobacter_sakazakii")
    # #构建序列库
    # # seq.makedb(file="Cronobacter_sakazakii.fasta",db_name="Cronobacter_sakazakii")

if __name__ == '__main__':
    main()
