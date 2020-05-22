import numpy as np
import pickle

pickle_data = dict()

with open("hadamar.csv", "r") as data:
    rows = data.read().split('\n')
    pairs = []
    x = []
    score = []
    classification = []

    for entry in rows[1:-1]:
        entry_arr = entry.split(',')

        geneA = entry_arr[0]
        geneB = entry_arr[1]
        classif = entry_arr[-1]
        entry_score = float(entry_arr[-2])

        floats = []
        for number in entry_arr[2:-2]:
            floats.append(float(number))

        pairs.append((geneA, geneB))
        x.append(floats)
        score.append(entry_score)
        classification.append(classif)

    pickle_data['x'] = np.array(x)
    pickle_data['pairs'] = pairs
    pickle_data['score'] = score
    pickle_data['classification'] = classification

bytes_out = pickle.dumps(pickle_data)
max_bytes = 2**31 - 1

with open("hadamar2.pickle", "wb") as outfile:
    for idx in range(0, len(bytes_out), max_bytes):
        outfile.write(bytes_out[idx:idx+max_bytes])



