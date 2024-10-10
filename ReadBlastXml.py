'''
用于提取本地 blaxt的结果，用于分析细菌的保守区域。
'''
import errno
import os.path
from tempfile import tempdir

import numpy as np
from Bio.Blast import  NCBIXML
from Bio import  SearchIO
import pandas as pd
from tqdm import tqdm
import pandas as pd

# from concat_NCBI_dataset_seq import out_file
from Bio import SearchIO

def match_alignment_title(record,match_title,e_value=0.000001):
    '''

    :param record: a NCBI xml handle record
    :param match_title: str
    :return: march_title list; unmatchc_title list
    '''

    match_l = []
    unmatch_l = []
    dict = {'Title': [], 'e': [],'aligment_lenth':[]}
    for alignment in record.alignments:
        for hsp in alignment.hsps:
            dict['Title'].append(alignment.title)
            dict['e'].append(hsp.expect)
            dict['aligment_lenth'].append(alignment.length)
            temp_df = pd.DataFrame(dict)
            temp_df.to_csv(f"1.csv")
            if hsp.expect <  e_value:
                # print(alignment.title,hsp.expect,hsp.expect)
                if match_title in alignment.title:
                    match_l.append(alignment.title)
                else:
                    unmatch_l.append(alignment.title)

    return [record.query,match_l,unmatch_l]
def get_len(match_alignment_result):
    return {'split_segment':match_alignment_result[0],
            'match_len':len(match_alignment_result[1]),
            'unmatch_len':len(match_alignment_result[2])}
def process_total(in_file):
    #打开文件，并读取
    result_handle = open(in_file,'rt')
    blast_records = NCBIXML.parse(result_handle)
    number = len(list(blast_records))
    result_handle.close()
    return number
def parse_blaxtxml(in_file,match_title,out_file_path,each_blast_flag=0):
    # 创建暂存结果的文件夹

    #打开文件，并读取
    result_handle = open(in_file,'rt')
    blast_records = NCBIXML.parse(result_handle)
    # 创建比对结果的字典，比对上与比对不上
    align_cont = {"title":[],"match":[],"unmatch":[]}
    # 创建进度条
    bar = tqdm(total=100, desc="比对结果进度条：",unit="%")
    #循环读取结果
    for blast_record in blast_records:
        blast_dict = {'Title': [],'Scientific':[],'e': [], 'score':[],'aligment_lenth': [],
                'sbjct_end':[],'sbjct_start':[]}

        #读取每条记录的信息并储存到字典
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                # 储存到字典中
                blast_dict['Title'].append(alignment.title)
                blast_dict['Scientific'].append(" ".join(alignment.title.split()[2:4]))
                blast_dict['e'].append(hsp.expect)
                blast_dict['score'].append(hsp.score)
                blast_dict['aligment_lenth'].append(hsp.align_length)
                blast_dict['sbjct_end'].append(hsp.sbjct_end)
                blast_dict['sbjct_start'].append(hsp.sbjct_start)
                # print(alignment.hit_id)
                # 转成字典
                temp_df = pd.DataFrame(blast_dict)
                #使用where进行判断
                temp_df["Identify"] = np.where(temp_df['Scientific'] == match_title,'Y',temp_df['Scientific'])
        #统计每个比对片段的结果
        Y_count = (temp_df['Identify'] == 'Y').sum()
        N_Y_count = (temp_df['Identify'] != 'Y').sum()
        align_cont["match"].append(Y_count)
        align_cont["unmatch"].append(N_Y_count)
        align_cont["title"].append(blast_record.query)
        #作为测试的，查看比对的单个结果的文件
        if each_blast_flag == 1:
            make_dir_path = os.path.join(out_file_path, "each_blast_res_file")
            try:
            #构建存储的文件夹
                os.makedirs(make_dir_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            file_save_name = os.path.join(make_dir_path, blast_record.query)
            temp_df.to_csv(f"{file_save_name}.csv")
        bar.update()
    result_handle.close()
    match_df = pd.DataFrame(align_cont)
    match_df.to_csv(f"{os.path.join(out_file_path,"res.csv")}")


def serachIO_parse_xml(in_file,match_title):
    #打开文件，并读取
    result_handle = open(in_file,'rt')
    blast_records = SearchIO.parse(result_handle,'blast-xml')
    #读取每个记录
    for record in blast_records:
        blast_dict = {'title':[],'Scientifit_name':[]}
        for hit in record.hits:
            blast_dict['title'].append(hit.description)
            blast_dict['Scientifit_name'].append(" ".join(hit.description.split()[0:2]))
            print(hit.description_all)
            res_df = pd.DataFrame(blast_dict)
            res_df.to_csv('2.csv')
        # print(record.description)
        print(record)


def main():
    # in_file = rf"{input('输入处理文件：')}"
    # out_file_path = rf"{input('文件保存位置：')}"
    # match_title = input("输入比对上的物种名称：")
    # each_blast_flag = input("每个单独的Blast结果是否保存（1/0）：")
    out_file_path = r"F:\01data\Klebsiella"
    match_title = 'Klebsiella oxytoca'
    in_file = r"F:\01data\Klebsiella\03chr1_con_blast-10000.xml"

    parse_blaxtxml(in_file=in_file,match_title=match_title,out_file_path=out_file_path,each_blast_flag=1)


    print(f"{'-'*10}结果已经输出{'-'*10}")



if __name__ == '__main__':
    main()