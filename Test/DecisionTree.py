from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Đọc dữ liệu từ file Zeus.txt và Alexa_Benign.txt
with open('../Dataset/Raw/Full/Zeus.txt', 'r') as file:
    bot_data = file.readlines()

with open('../Dataset/Raw/Full/Alexa_Benign.txt', 'r') as file:
    people_data = file.readlines()

# Gán nhãn cho dữ liệu: 1 - botnet, 0 - người
bot_labels = np.ones(len(bot_data))
people_labels = np.zeros(len(people_data))

# Kết hợp dữ liệu và nhãn
data = bot_data + people_data
labels = np.concatenate([bot_labels, people_labels])

# Sử dụng CountVectorizer để chuyển đổi dữ liệu văn bản thành vector đặc trưng
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Xây dựng và huấn luyện mô hình cây quyết định
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

# Đánh giá mô hình
accuracy = tree.score(X_test, y_test)
print(f"Độ chính xác của mô hình cây quyết định: {accuracy:.2f}")
