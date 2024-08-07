import os

def local_blast(balst_file,db_name):
    command = f"blastn -db {db_name} -query {local_blast()} -evalue 1e-5 -outfmt 5 > con_blast.xml"
    os.system(command)


def main():
    blast_f = input("比对的序列：")
    db_name = input("比对的本地库：")
    local_blast(blast_f,db_name)

if __name__ == '__main__':
    main()