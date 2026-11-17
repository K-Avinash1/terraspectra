"""Build docs/tomato_manifest.csv: which tomato cubes are usable, and why not."""
import csv

DAY_WORDS = {"one": 1, "three": 3, "five": 5, "seven": 7}
DUPLICATE_OF = {
    "Fusarium_oxysporum_8": "Alternaria_alternata_1",
    "Fusarium_oxysporum_7": "Alternaria_alternata_2",
    "Fusarium_oxysporum_6": "Alternaria_alternata_3",
    "Alternaria_solani_6": "Alternaria_solani_4",
    "Healthy_6": "Healthy_1",
    "Healthy_5": "Healthy_2",
    "Healthy_7": "Healthy_3",
    "Healthy_8": "Healthy_4",
}

with open("docs/cube_stats.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

header = ["file", "label_class", "label_day", "scale_guess", "duplicate_of", "usable_for_pca"]
out = []
for r in rows:
    stem = r["file"]
    dup = DUPLICATE_OF.get(stem, "")
    usable = r["scale_guess"] == "reflectance-like" and not dup
    out.append([stem, stem.rsplit("_", 1)[0], DAY_WORDS[r["variable"].split("_")[1]],
                r["scale_guess"], dup, usable])

with open("docs/tomato_manifest.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(out)

counts = {}
for row in out:
    if row[-1]:
        counts[row[1]] = counts.get(row[1], 0) + 1
print("Usable cubes per class:", counts)
print("Saved docs/tomato_manifest.csv")
