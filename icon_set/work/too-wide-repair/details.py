from pathlib import Path
import json,textwrap
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-wide-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
rows={r['original']:Path(r['file']) for r in json.loads((W/'mapping.json').read_text())}
def body(n,b):
 p=rows[n];s=p.read_text();p.write_text(s[:s.index('    def build')]+ '    def build(self) -> None:\n'+textwrap.indent(textwrap.dedent(b).strip(),'        ')+'\n')
body('cat-paw','''
# Two broad toe lobes and two separated toe pads; omit crowded side dots.
self.add_line('leg-left', (8, 44), (8, 18))
self.add_arc('outer-toe-left', (8, 18), (14, 12), radius_x=6)
self.add_arc('inner-toe-left', (14, 12), (24, 12), radius_x=5, radius_y=8)
self.add_arc('inner-toe-right', (24, 12), (34, 12), radius_x=5, radius_y=8)
self.add_arc('outer-toe-right', (34, 12), (40, 18), radius_x=6)
self.add_line('leg-right', (40, 18), (40, 44))
self.add_contour('outline', 'leg-left', 'outer-toe-left', 'inner-toe-left', 'inner-toe-right', 'outer-toe-right', 'leg-right')
self.add_dot('toe-left', (18, 21))
self.add_dot('toe-right', (30, 21))
self.add_arc('palm-left', (17, 38), (24, 32), radius_x=7, radius_y=6)
self.add_arc('palm-right', (24, 32), (31, 38), radius_x=7, radius_y=6)
self.add_arc('palm-base-right', (31, 38), (24, 42), radius_x=7, radius_y=4)
self.add_arc('palm-base-left', (24, 42), (17, 38), radius_x=7, radius_y=4)
self.add_contour('palm', 'palm-left', 'palm-right', 'palm-base-right', 'palm-base-left', closed=True)
''')
body('dinosaur-skull','''
# Rounded braincase and elongated snout with one generous jaw opening.
self.add_polyline('snout', (4, 24), (4, 22), (8, 12), (30, 8), (32, 8))
self.add_arc('braincase', (32, 8), (44, 20), radius_x=12)
self.add_line('back', (44, 20), (44, 28))
self.add_arc('jaw-back', (44, 28), (32, 40), radius_x=12)
self.add_polyline('jaw', (32, 40), (12, 40), (4, 32), (30, 32), (34, 24), (4, 24))
self.add_contour('skull', 'snout', 'braincase', 'back', 'jaw-back', 'jaw', closed=True)
self.add_dot('eye', (30, 16))
# Nostril omitted: the upper snout cannot house another mark with safe clearance.
''')
