import cvmvcf as vcf

"""
You need to download and pip install cvmvcf (a spinoff of pyvcf)
Here is the link: https://github.com/cvmohan-ds/cvmvcf
We all have been facing issues with pyvcf because of not being maintained.
No offence to Author of pyvcf - we all know the situation of covid in 2020 right the time when this lib became defunct.
Hope the Author is doing good. All my regards to the person who gave us pyvcf, May God Bless You.
There are a few changes that are needed in newer python version and cvmvcf has those changes present.
"""


def read_vcf(file_name):
    vcf_data = vcf.Reader(open(file_name, "r", encoding="utf-8"))
    return vcf_data
