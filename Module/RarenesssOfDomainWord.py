# File path to people's domain
file_path = '../Dataset/Processed/DNSTraffic_Processed.txt'

# Read data from the file and create a list of domains
with open(file_path, 'r') as file:
    data_lines = file.readlines()

# Convert data lines to lowercase and strip extra whitespace
dataset = [line.strip().lower() for line in data_lines]

# Calculate rarity of domaain
def calculate_rarity_of_domain(domain):
    # To lower
    domain = domain.lower()

    # Calculate
    domain_count = dataset.count(domain)
    total_domains = len(dataset)

    if total_domains > 0:
        rarity_score = domain_count / total_domains
        return rarity_score
    else:
        return 0

''' 
Test :
print(calculate_rarity_of_domain("google.com"))     # People
print(calculate_rarity_of_domain("xgxhpyfwlrxdw.com"))      # Botnet
'''