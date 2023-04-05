import csv
import os
import requests

def download_csv(urlpath):
    source_dir = os.path.join(os.path.dirname(__file__), 'source_data')
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)

    filename = 'username.csv'
    filepath = os.path.join(source_dir, filename)

    response = requests.get(urlpath)
    with open(filepath, 'wb') as f:
        f.write(response.content)

    with open(filepath, 'r') as f:
        data = list(csv.reader(f))
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data[:-1])

    print('Completed!')

def get_text_info(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
        words = [word.lower() for word in text.split() if word.isalpha()]

        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        for word, count in word_count.items():
            print(f"{word} - {count}")

get_text_info("article.txt")
download_csv('https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv')