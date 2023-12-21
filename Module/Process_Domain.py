import os
import csv
import TypingDifficulty
import CharacterFrequent

def Process_Domain(input_directory, output_directory):
    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_Processed.csv")

            with open(input_path, 'r') as file:
                lines = file.readlines()

            # Write in CSV
            with open(output_path, 'w', newline='') as csvfile:
                fieldnames = ['Domain', 'TypingDifficult', 'CharacterFrequent']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()  # Write column names

                for line in lines:
                    input_text = line.strip()

                    typing_difficult_score = TypingDifficulty.typing_difficulty_score(input_text)
                    character_frequent = CharacterFrequent.calculateProbability(input_text)

                    writer.writerow({
                        'Domain': input_text,
                        'TypingDifficult': typing_difficult_score,
                        'CharacterFrequent': character_frequent
                    })


Process_Domain("../Dataset/Raw/Full", "../Dataset/Processed/Full")
