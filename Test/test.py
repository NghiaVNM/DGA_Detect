# Đọc dữ liệu từ tệp data.txt và tạo danh sách domains
file_path = '../Dataset/Raw/Full/Alexa_Benign.txt'  # Đường dẫn tới tệp data.txt

# Mở tệp và đọc các domain từ tệp
with open(file_path, 'r') as file:
    data_lines = file.readlines()

# Tạo danh sách domains từ các dòng dữ liệu trong tệp
domains_list = [line.strip().lower() for line in data_lines]  # Chuyển đổi về chữ thường

# Hàm tính độ hiếm của domain
def calculate_rarity_of_domain(domain, dataset):
    domain = domain.lower()  # Chuyển đổi domain cần kiểm tra về chữ thường
    domain_count = dataset.count(domain)
    total_domains = len(dataset)

    if total_domains > 0:
        rarity_score = domain_count / total_domains
        return rarity_score
    else:
        print('no')
        return 0  # Trường hợp không có dữ liệu

# Sử dụng hàm để xác định độ hiếm của domain cụ thể trong tập dữ liệu lớn
specific_domain = "paoajknkjzaiojdksd"  # Domain cụ thể bạn muốn xác định
rarity = calculate_rarity_of_domain(specific_domain, domains_list)
print(f"Rarity of Domain '{specific_domain}': {rarity}")
