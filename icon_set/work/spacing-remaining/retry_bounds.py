SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/spacing-remaining/targets.json'
AUTHOR='gpt-6'
from repair_candidates import *
rows=json.load(open(W/'bounds-adjusted.json'));ns=list(rows);start=int(sys.argv[1]);end=int(sys.argv[2]);out=[]
for n in ns[start:end]:
 q=propose(n);out.append(q);(W/f'refine-bounds-{start:02}.json').write_text(json.dumps(out,indent=2));print(n,q['score'],flush=True)
