from pathlib import Path
import json,re
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-short-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows={r['original']:Path(r['file']) for r in json.loads((W/'mapping.json').read_text())}
def edit(n,fn):p=rows[n];p.write_text(fn(p.read_text()))
# Shared human reference: head/body visible gap4 = centerline8.
for n in ['person-bust-with-sash','person-bust-with-strap']:edit(n,lambda s:s.replace(', 29)',', 28)').replace(', 37)',', 36)'))
edit('user-bust',lambda s:s.replace('radius_y=14','radius_y=16'))
edit('user',lambda s:s.replace('radius_y=15','radius_y=16'))
edit('user-profile',lambda s:s.replace('radius_y=13','radius_y=14'))
edit('graduate-person',lambda s:s.replace('radius_y=7','radius_y=8'))
edit('user-bust-square-shoulders',lambda s:s.replace(', 33)',', 32)').replace(', 39)',', 38)'))
edit('person-waving',lambda s:s.replace(', 25)',', 24)'))
edit('person-wearing-headphones',lambda s:s.replace(', 40)',', 39)').replace('radius_x=8, radius_y=4','radius_x=8, radius_y=5'))
edit('girl-pigtails',lambda s:s.replace('radius_x=12, radius_y=9','radius_x=10, radius_y=7'))
edit('mountain-pose',lambda s:s.replace(', 19)',', 18)').replace('radius_x=16, radius_y=6','radius_x=16, radius_y=7'))
for n in ['tree-pose','standing-full-body-stretch']:edit(n,lambda s:s.replace('(21, 12)','(21, 13)').replace('(27, 12)','(27, 13)'))
# Broaden the rear damaged wing instead of leaving a tapered slot.
edit('burning-crashed-aircraft',lambda s:s.replace('(40, 40), (36, 44), (25, 41)','(40, 34), (40, 44), (25, 44)'))
