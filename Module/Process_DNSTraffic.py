import pandas as pd

def process_dns_traffic(input_file, output_file):
    # Read DNS traffic dataset
    data = pd.read_csv(input_file)

    # Combine 'domain' and 'sub' columns
    data['Combined_Columns'] = data['domain'] + '.' + data['sub']

    # Write the combined column to the output file
    data['Combined_Columns'].to_csv(output_file, sep='\t', index=False, header=False)

process_dns_traffic("../Dataset/raw/DNSTraffic.csv", "../Dataset/Processed/DNSTraffic_Processed.txt")




