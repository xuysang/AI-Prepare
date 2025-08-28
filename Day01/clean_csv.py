import csv

def clean_csv(input_file,output_file):
    rows = []
    seen = set()
    with open(input_file,"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if tuple(row) not in seen and all(row):
                seen.add(tuple(row))
                rows.append(row)
    rows.sort(key=lambda x:x[0])
    with open(output_file,"w",encoding="utf-8",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

if __name__=="__main__":
    clean_csv("2025-08-26_news.csv","cleaned_data.csv")
