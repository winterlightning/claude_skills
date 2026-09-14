from pathlib import Path
import json,re
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-wide-repair/queue.json'
AUTHOR='gpt-6'
rows={r['original']:Path(r['file']) for r in json.loads(Path('icon_set/work/too-wide-repair/mapping.json').read_text())}
def edit(n,fn):
 p=rows[n];p.write_text(fn(p.read_text()))
edit('external-hard-drive',lambda s:s.replace(', 24)',', 22)').replace("'slot', (12, 32), (36, 32)","'slot', (13, 31), (35, 31)"))
edit('libra-zodiac-symbol',lambda s:s.replace(', 32)',', 26)').replace('radius_x=15','radius_x=13'))
edit('ladies-hat-with-bow',lambda s:s.replace('(35, 26)','(34, 26)').replace('(25,','(24,').replace(', 20)',', 18)').replace(', 32)',', 34)'))
# The fourth bud joins from above the mouth rather than crossing through the bowl.
edit('round-bud-vase',lambda s:s.replace("('side', 37, 29)","('side', 37, 28)").replace("(x, y + 3), (24, 30)","((x - 3, y) if name == 'side' else (x, y + 3)), (24, 30)").replace("(x, y + 3), (x, y - 3)","(x - 3, y), (x + 3, y)").replace("(x, y - 3), (x, y + 3)","(x + 3, y), (x - 3, y)"))
# Widen the neck by moving its rear wall and shoulder together.
edit('standing-deer',lambda s:s.replace('(34, 18)','(32, 18)').replace('(34, 12)','(32, 12)').replace("radius_x=6, radius_y=6, sweep=False","radius_x=4, radius_y=6, sweep=False"))
# Emit line primitives in one contour; nested contours are not model elements.
def dino(s):
 for name,pts in [('snout',[(4,24),(4,22),(8,12),(30,8),(32,8)]),('jaw',[(32,40),(12,40),(4,32),(30,32),(34,24),(4,24)])]:
  line=next(l for l in s.splitlines() if f"self.add_polyline('{name}'" in l)
  new='\n'.join(f"        self.add_line('{name}-{i}', {a}, {b})" for i,(a,b) in enumerate(zip(pts,pts[1:]),1))
  s=s.replace(line,new)
 s=s.replace("'skull', 'snout', 'braincase', 'back', 'jaw-back', 'jaw'","'skull', 'snout-1', 'snout-2', 'snout-3', 'snout-4', 'braincase', 'back', 'jaw-back', 'jaw-1', 'jaw-2', 'jaw-3', 'jaw-4', 'jaw-5'")
 return s
edit('dinosaur-skull',dino)
