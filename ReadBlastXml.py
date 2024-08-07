'''
用于提取本地 blaxt的结果，用于分析细菌的保守区域。
'''


from Bio.Blast import  NCBIXML
import pandas as pd
from tqdm import tqdm

def match_alignment_title(record,match_title,e_value=0.000001):
    '''

    :param record: a NCBI xml handle record
    :param match_title: str
    :return: march_title list; unmatchc_title list
    '''

    match_l = []
    unmatch_l = []
    for alignment in record.alignments:
        for hsp in alignment.hsps:
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
def main():
    #file = input('输入处理文件：')
    file = r"F:\data\Enterobacteria\Cronobacter_sakazakii_db\con_blast.xml"
    result_handle = open(file,'rt')
    result_records = NCBIXML.parse(result_handle)

    #提取记录并进行处理
    res_dic = {'split_segment':[],'match_len':[],'unmatch_len':[]}
    bar = tqdm(total=5000,desc="比对结果进度条：")
    for record in result_records:

        tem_dic = {}
        # 设置 elvaue 值为 0.000001 ,将匹配上的和未匹配上统计到列表中，输出标题
        match_align_res = match_alignment_title(record,"Cronobacter sakazakii")
        #输出比对上和未必对上的长度和片段名称
        match_res = get_len(match_alignment_result=match_align_res)
        # 将结果添加到res_dic字典中,索引0：片段名称 1:比对到的长度 2：未匹配到的长度
        res_dic['split_segment'].append(match_res['split_segment'])
        res_dic['match_len'].append(match_res['match_len'])
        res_dic['unmatch_len'].append(match_res['unmatch_len'])
        bar.update()
    #输出比对的结果
    res_df = pd.DataFrame(res_dic)

    print(f"{'-'*10}结果已经输出{'-'*10}")
    res_df.to_csv('blast的解析结果.csv')
    result_handle.close()
    
    
if __name__ == '__main__':
    main()