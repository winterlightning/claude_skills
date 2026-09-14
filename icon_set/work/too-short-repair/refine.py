from pathlib import Path
import json,textwrap
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-short-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows={r['original']:Path(r['file']) for r in json.loads((W/'mapping.json').read_text())}
def edit(n,fn):p=rows[n];p.write_text(fn(p.read_text()))
def body(n,s):edit(n,lambda old:old[:old.index('    def build')]+ '    def build(self) -> None:\n'+textwrap.indent(textwrap.dedent(s).strip(),'        ')+'\n')
for n in ['end-point-none','subtract','subtract-interface-essential']:edit(n,lambda s:s.replace('(4, 40), (44, 40)','(4, 24), (44, 24)'))
edit('head-with-drinking-straw',lambda s:s.replace("(13, 35), (20, 44), radius_x=7, radius_y=7","(13, 35), (20, 42), radius_x=7, radius_y=7").replace("'neck-front', (20, 44), (20, 44)","'neck-front', (20, 42), (20, 44)"))
edit('money-plant',lambda s:s.replace('radius_x=11, radius_y=13','radius_x=11, radius_y=15'))
for n in ['soldier-behind-sandbags','soldier-behind-sandbags-v2']:
 edit(n,lambda s:s.replace("A('helmet', (30, 15), (42, 15), 6)","A('helmet', (30, 15), (42, 15), 6, 7)"))
edit('moving-server-stack',lambda s:s.replace('enumerate((6, 23))','enumerate((4, 23))'))
edit('waterside-fortress',lambda s:s.replace('(20, 19), (32, 19)','(20, 21), (32, 21)').replace('(26, 19)','(26, 21)'))
edit('hand-holding-remote-with-signal',lambda s:s.replace("(28, 23), (36, 31), (36, 38), (40, 44)","(28, 23), (40, 29), (40, 44)"))
# Reconstruct wings with deliberate corners and eight-unit root widths.
body('fighter-jet','''
# Mirror the airframe about x=24; broad wings and one broad tail replace pinched fin slivers.
right = [(24, 4), (29, 12), (29, 18), (40, 28), (40, 38), (29, 30), (29, 36), (32, 44), (24, 40)]
left = [(48 - x, y) for x, y in reversed(right[1:-1])]
self.add_polyline('airframe', *right + left, closed=True)
''')
body('military-drone-overhead','''
# Mirror the wing and tail geometry; nine-unit wing tips keep the thin wing slots open.
right = [(24, 4), (28, 10), (28, 18), (40, 22), (40, 31), (28, 27), (28, 36), (34, 40), (24, 44)]
left = [(48 - x, y) for x, y in reversed(right[1:-1])]
self.add_polyline('airframe', *right + left, closed=True)
''')
# A broad broken fuselage and wing; omit the two folded fins that collapse into slivers.
body('burning-crashed-aircraft','''
self.add_polyline('plane', (8, 25), (20, 30), (17, 18), (27, 23), (28, 34), (40, 40), (36, 44), (25, 41), (8, 36), closed=True)
self.add_polyline('fire', (28, 25), (26, 17), (31, 9), (30, 4), (40, 14), (40, 23), (34, 37))
self.relate('connect', 'fire', 'plane')
self.add_line('smoke', (12, 4), (10, 14))
''')
