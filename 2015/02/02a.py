import re
from pathlib import Path


boxes = Path("input").read_text().split()

total_paper = total_ribbon = 0
for dimensions in boxes:
    l, w, h = sorted([int(d) for d in re.search(r"(\d+)x(\d+)x(\d+)", dimensions).groups()])
    total_paper += (2*l*w + 2*w*h + 2*h*l) + l*w
    total_ribbon += (l+l+w+w) + l*w*h

print(total_paper)
print(total_ribbon)