import csv
import math


with open("file.csv", "r") as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    bucket = {"amazing": 1, "fantastic": 2, "good": 1, "great": 3, "enjoy": 1, "cozy": 1,"dream": 0, "comfortable": 1,"excellent": 3,
              "wonderful": 2,"special":3, "cuisine":2,"extraordinary":3,"beautiful":2, "pleasant":1, "hospitality":1, "charm":1,
              "thank":1,"thanks":1,"delicious":2,"nice":2,"favourite":1,"enjoyed":2, "magnificent":2,"worth":1, "delightful":1,"dreams":1,
              "relax":1, "architecture":1,"congratulations":2, "best": 2, "very": 1, "weather": 1 ,"nature": 1}

    z = 1
    for row in reader:
        # print(row)
        data = []
        for ent in row:
            if ent:
                data.append(ent.rstrip())
        all_data = []
        for l in data:
            b = l.split()
            for i in b:
                all_data.append(i)
        score = 0
        for word in all_data:
            if word.lower() in bucket:
                score += bucket[word.lower()]
        final_score = math.ceil((score/len(all_data)) * 100)
        print([[f'Syntax-{z}'],[final_score]])
        z += 1






