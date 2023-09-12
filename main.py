from data_processor import DataProcessor
import argparse


def create_excel_from_vcf(filepath):
    DataProcessor(filename=filepath).start_process()


if __name__ == "__main__":
    print("Converting VCF file to Excel file")
    parser = argparse.ArgumentParser("VCF to Excel Utility")
    parser.add_argument("-f", "--file", help="Your absolute filepath", required=False,
                        default="sample.vcf")
    options = parser.parse_args()
    file_path = options.file
    create_excel_from_vcf(file_path)