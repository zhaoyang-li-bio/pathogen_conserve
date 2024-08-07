"""
    储存Entrez的基本信息
"""
from Bio import Entrez
import time
from tqdm import tqdm

Entrez.email = "1045700857@qq.com"
# 查询基本的可查询库

def query_entrez_info(query=None):
    handle = Entrez.einfo(db=query)
    record = Entrez.read(handle)
    temp_l = []
    for field in record["DbInfo"]["FieldList"]:
        temp_l.append(f"{field['Name']}\t{field['FullName']}\t{field['Description']}")
    temp_l.append(record['DbInfo'].keys())
    return temp_l

#可查询的数据库
db_list = ['pubmed', 'protein', 'nuccore', 'ipg', 'nucleotide', 'structure', 'genome', 'annotinfo', 'assembly', 'bioproject',
           'biosample', 'blastdbinfo', 'books', 'cdd', 'clinvar', 'gap', 'gapplus', 'grasp', 'dbvar', 'gene', 'gds', 'geoprofiles',
           'medgen', 'mesh', 'nlmcatalog', 'omim', 'orgtrack', 'pmc', 'popset', 'proteinclusters', 'pcassay', 'protfam', 'pccompound',
           'pcsubstance', 'seqannot', 'snp', 'sra', 'taxonomy', 'biocollections', 'gtr']

def main():
    # 设置进度函数
    pbar = tqdm(total=len(db_list), desc='NCBI_info', leave=True, ncols=100, unit='B', unit_scale=True)
    # 循环下载各个库的信息
    for db_name in db_list:
        temp_l = query_entrez_info(db_name)
        # 写入文件中
        file = open(f"{db_name}.txt",'wt')
        for line in temp_l:
            file.write(f"{line}\n")
        file.close()
        pbar.update(1)


if __name__ == '__main__':
    main()