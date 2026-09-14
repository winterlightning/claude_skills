from pathlib import Path
import json
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-short-repair/queue.json'
AUTHOR='gpt-6'
rs={r['original']:Path(r['file']) for r in json.load(open('icon_set/work/too-short-repair/mapping.json'))}
def edit(n,fn):p=rs[n];p.write_text(fn(p.read_text()))
for n in ['person-with-bindle','person-with-bindle-v2']:
 edit(n,lambda s:s.replace("self.add_line('torso', (26, 26), (24, 34))","self.add_polyline('torso', (26, 26), (34, 24), (24, 34))").replace("'arm', (26, 26), (33, 31)","'arm', (34, 24), (33, 31)").replace("self.relate('connect', 'pole', 'arm')",""))
edit('standing-back-stretch',lambda s:s.replace("'back', (25, 14), (17, 23), (23, 30)","'back', (22, 7), (28, 23), (23, 30)").replace("'arm', (17, 23), (29, 11)","'arm', (28, 23), (29, 11)"))
edit('standing-forward-fold',lambda s:s.replace("self.add_line('torso-arm', (32, 16), (20, 44))","self.add_line('torso-upper', (32, 16), (26, 26))\n        self.add_line('torso-arm', (26, 26), (26, 44))\n        self.relate('connect', 'body', 'torso-arm')").replace("'body', 'leg', 'hip', 'torso-arm'","'body', 'leg', 'hip', 'torso-upper'"))
edit('twisting-triangle-pose',lambda s:s.replace("'torso', (26, 4), (20, 25), (28, 32)","'torso', (26, 4), (22, 10), (22, 25), (28, 32)").replace('(20, 25)','(22, 25)'))
edit('wide-leg-inversion-pose',lambda s:s.replace("self.add_polyline('arms', (8, 33), (24, 28), (40, 33), closed=False)","self.add_polyline('arms', (16, 30), (24, 30), (32, 30))\n        self.add_line('left-arm', (8, 33), (16, 30))\n        self.add_line('right-arm', (32, 30), (40, 33))\n        self.relate('connect', 'left-arm', 'arms')\n        self.relate('connect', 'right-arm', 'arms')").replace("'torso', (24, 22), (24, 28)","'torso', (24, 22), (24, 30)"))
