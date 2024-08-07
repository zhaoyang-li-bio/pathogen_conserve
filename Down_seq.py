"""
    使用NCBI_GENOME_DOWNLOAD
"""
import ncbi_genome_download as ngd
import inspect

def main():

    ngd.download(species_taxids='562')


if __name__ == "__main__":
    main()