import os
# from Bio.Blast.Applications import NcbiblastnCommandline
from oauthlib.uri_validate import query
import subprocess

def local_blast(query_fasta,db_name,out_xml,word_size=28,e=0.05,threads=2):
    # blastn_cline = NcbiblastnCommandline(query=query_fasta,db=db_name,evalue=e,outfmt=5,out=out_xml,word_size=word_size,
    #                                      num_threads=threads)
    # print(blastn_cline)

    # 运行一个命令并等待其完成
    result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

    # 打印命令的输出和返回码
    print('stdout:', result.stdout)
    print('stderr:', result.stderr)
    print('returncode:', result.returncode)
def main():
    query_fata = r"F:\01data\Klebsiella\02Klebsiella_oxytoca_split_10.fasta"
    db_name = r"F:\01data\Klebsiella\Klebsiella"
    out_xml = query_fata[:-4] + ".xml"
    # blast_f = fr"{input("比对的序列：")}"
    # db_name = fr"{input("比对的库：")}"
    local_blast(query_fasta=query_fata,db_name=db_name,out_xml=5,word_size=200)

if __name__ == '__main__':
    main()




