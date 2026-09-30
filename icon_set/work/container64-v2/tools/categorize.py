"""Group report.json failures by their first error's check name."""
import json, re, sys
from collections import Counter, defaultdict
from pathlib import Path
report = json.loads((Path(__file__).parent.parent / 'report.json').read_text())
cats = defaultdict(list)
for iid, row in sorted(report.items()):
    if row['status'] == 'pass':
        continue
    for err in row['errors'] or ['(no error text)']:
        text = err if isinstance(err, str) else json.dumps(err)
        m = re.match(r'([a-z /_-]+?)(?: \[|:)', text)
        cats[m.group(1) if m else text[:40]].append(iid)
print(Counter({k: len(set(v)) for k, v in cats.items()}).most_common())
print(Counter(r['status'] for r in report.values()))
if '-v' in sys.argv:
    for k, v in cats.items():
        print(f'\n## {k} ({len(set(v))})'); print(' '.join(sorted(set(v))))
