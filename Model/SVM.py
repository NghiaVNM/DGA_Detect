import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_curve, roc_auc_score, confusion_matrix
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import scipy.sparse as sp

# Paths to CSV files
people_path = "../Dataset/Processed/Full/Alexa_Benign_Processed.csv"
cryptolocker_path = "../Dataset/Processed/Full/Cryptolocker_Processed.csv"
zeus_path = "../Dataset/Processed/Full/Zeus_Processed.csv"
pushdo_path = "../Dataset/Processed/Full/Pushdo_Processed.csv"
rovnix_path = "../Dataset/Processed/Full/Rovnix_Processed.csv"
tinba_path = "../Dataset/Processed/Full/Tinba_Processed.csv"
matsnu_path = "../Dataset/Processed/Full/Matsnu_Processed.csv"
ramdo_path = "../Dataset/Processed/Full/Ramdo_Processed.csv"

# Read data from CSV files
people_data = pd.read_csv(people_path)
cryptolocker_data = pd.read_csv(cryptolocker_path)
zeus_data = pd.read_csv(zeus_path)
pushdo_data = pd.read_csv(pushdo_path)
rovnix_data = pd.read_csv(rovnix_path)
tinba_data = pd.read_csv(tinba_path)
matsnu_data = pd.read_csv(matsnu_path)
ramdo_data = pd.read_csv(ramdo_path)

# Label data: 1 - botnet, 0 - people
people_data['Label'] = 0
cryptolocker_data['Label'] = 1
zeus_data['Label'] = 1
pushdo_data['Label'] = 1
rovnix_data['Label'] = 1
tinba_data['Label'] = 1
matsnu_data['Label'] = 1
ramdo_data['Label'] = 1

# Combine data from files
data = pd.concat([people_data, cryptolocker_data, zeus_data, pushdo_data, rovnix_data, tinba_data, matsnu_data, ramdo_data], ignore_index=True)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data[['Domain', 'TypingDifficult', 'CharacterFrequent']], data['Label'], test_size=0.2, random_state=42)

# Use CountVectorizer to transform 'Domain' column from text to feature vector
vectorizer = CountVectorizer()
X_train_domain = vectorizer.fit_transform(X_train['Domain'])
X_test_domain = vectorizer.transform(X_test['Domain'])

# Combine feature vectors with training and testing data
X_train = sp.hstack((X_train[['TypingDifficult', 'CharacterFrequent']].values, X_train_domain))
X_test = sp.hstack((X_test[['TypingDifficult', 'CharacterFrequent']].values, X_test_domain))

# Build and train the SVM model
svm = SVC(probability=True)  # Use probability=True to enable predict_proba for ROC curve
svm.fit(X_train, y_train)

# Predict
y_pred_proba = svm.predict_proba(X_test)
y_pred = svm.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:, 1])
roc_auc = roc_auc_score(y_test, y_pred_proba[:, 1])
conf_matrix = confusion_matrix(y_test, y_pred)

# Draw ROC Curve and save to PDF
with PdfPages('../Result/SVM_ROC_Curve.pdf') as pdf:
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    pdf.savefig()
    plt.close()

# Draw Confusion Matrix and save to PDF
with PdfPages('../Result/SVM_Confusion_Matrix.pdf') as pdf:
    plt.figure()
    plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.xticks([0, 1], ['0', '1'])
    plt.yticks([0, 1], ['0', '1'])

    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            plt.text(j, i, str(conf_matrix[i, j]), horizontalalignment="center", color="white" if conf_matrix[i, j] > conf_matrix.max() / 2 else "black")

    plt.tight_layout()
    pdf.savefig()
    plt.close()

# Save evaluation result
with open('../Result/SVM.txt', 'w') as file:
    file.write(f"Accuracy: {accuracy:.2f}\n")
    file.write(f"Precision: {precision:.2f}\n")
    file.write(f"Recall: {recall:.2f}\n")
    file.write(f"ROC AUC: {roc_auc:.2f}\n")
    file.write(f"Confusion Matrix:\n{conf_matrix}\n")