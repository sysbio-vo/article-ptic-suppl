# download data from https://ftp.ncbi.nlm.nih.gov/pub/litarch/29/31/
# wget https://ftp.ncbi.nlm.nih.gov/pub/litarch/29/31/livertox_NBK547852.tar.gz 
# extract
# tar -xzf livertox_NBK547852.tar.gz 
# change varaible to correct folder path e.g. "./livertox_NBK547852/"

livertox_folder = "./livertox_NBK547852/"
# we will need much smarter parser to correctly work with books, so option is False by default
parse_books = False
output_file = "parsed_livertox.csv"

import csv
import glob
from xml.dom.minidom import parse

from metapub import PubMedFetcher
import tqdm

fetch = PubMedFetcher()

def clean(data):
    try:
        if data[0] == '(':
            # text in brackets
            data = data[1:]
        if data[-2:] == ").":
            data = data[:-2] + '.'
    except Exception as e:
        print(e)
        print(data)
    return data.replace('"','').replace('\n','').replace('”','\'').replace('“','\'')

def main():
    output = open(output_file, 'w', newline='')
    csvwriter = csv.writer(output)
    csvwriter.writerow(["type", "name", "dili_annotation","pmid", "abstract"])

    for drug in tqdm.tqdm(glob.glob(f"{livertox_folder}*.nxml")):
        document = parse(drug)
        if parse_books:
            mixed_citations = document.getElementsByTagName("mixed-citation")
            for citation in mixed_citations:
                try:
                    name = citation.firstChild.data
                    text = citation.getElementsByTagName("italic")[0].firstChild.data
                    print(name)
                    csvwriter.writerow(["book", clean(name), clean(text), 0, ""])
                except Exception:
                    pass

        element_citations = document.getElementsByTagName("element-citation")
        for citation in element_citations:
            try:
                name = citation.getElementsByTagName("article-title")[0].firstChild.data
                text = citation.getElementsByTagName("annotation")[0].getElementsByTagName("italic")[0].firstChild.data
                pmid = citation.getElementsByTagName("pub-id")[0].firstChild.data
                abstract = fetch.article_by_pmid(pmid).abstract
                csvwriter.writerow(["article", clean(name), clean(text), pmid, abstract])
            except Exception:
                pass


if __name__ == "__main__":
    main()

