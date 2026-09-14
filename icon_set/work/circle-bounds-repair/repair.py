from pathlib import Path
import json,textwrap,ast
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/circle-bounds-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
helper='''
# CIRCLE envelope: center (24,24), centerline radius 20, visible radius 22.
# Shared cardinal nodes keep concentric geometry and attachments exact.
def circle(name, cx, cy, radius):
    points = [(cx + radius, cy), (cx, cy + radius), (cx - radius, cy), (cx, cy - radius)]
    for i in range(4):
        self.add_arc(f'{name}-{i}', points[i], points[(i + 1) % 4], radius_x=radius)
    self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)
'''
designs={
'compact-disc':("Concentric disc and central hole, informed by Lucide disc; no detail removed.",'''circle('disc', 24, 24, 20)
circle('hole', 24, 24, 6)'''),
'compact-disc-with-partition-segment':("Concentric disc with a lower-right sector; smaller circular hub leaves nine units to the sector.",'''circle('rim', 24, 24, 20)
circle('hub', 24, 24, 3)
self.add_line('sector-right', (44, 24), (36, 24))
self.add_arc('sector-turn', (36, 24), (24, 36), radius_x=12)
self.add_line('sector-bottom', (24, 36), (24, 44))
self.add_contour('sector', 'sector-right', 'sector-turn', 'sector-bottom')
self.relate('connect', 'rim', 'sector')'''),
'compact-disc-with-sheen-arcs':("Lucide disc-3 informs paired reflection arcs. Radius-two hub and radius-eleven sheen preserve nine-unit radial gaps.",'''circle('rim', 24, 24, 20)
circle('hub', 24, 24, 2)
self.add_arc('sheen-upper', (24, 13), (35, 24), radius_x=11)
self.add_arc('sheen-lower', (24, 35), (13, 24), radius_x=11)'''),
'cracked-compact-disc':("Open disc with an asymmetric lightning crack; Lucide disc informs the enclosing contour. Hub absent in source.",'''self.add_arc('rim-upper-left', (16, 7), (4, 24), radius_x=12, radius_y=17, sweep=False)
self.add_arc('rim-lower-left', (4, 24), (24, 44), radius_x=20, sweep=False)
self.add_arc('rim-lower-right', (24, 44), (44, 24), radius_x=20, sweep=False)
self.add_arc('rim-upper-right', (44, 24), (24, 4), radius_x=20, sweep=False)
self.add_contour('rim', 'rim-upper-left', 'rim-lower-left', 'rim-lower-right', 'rim-upper-right')
self.add_polyline('crack', (24, 4), (16, 18), (29, 18), (18, 34))
self.relate('connect', 'rim', 'crack')'''),
'face-wearing-round-glasses':("Circular face with mirrored round glasses and raised smile. Human reference icon_set/references/human_ref/user.svg supplies the round head vocabulary; no body or head-to-body gap applies. Lucide glasses informs paired lenses and bridge. Pupils and temple arms remain omitted.",'''circle('face', 24, 24, 20)
for side in (-1, 1):
    circle('lens-left' if side < 0 else 'lens-right', 24 + side * 8, 21, 3)
self.add_line('bridge', (19, 21), (29, 21))
self.relate('connect', 'bridge', 'lens-left')
self.relate('connect', 'bridge', 'lens-right')
self.add_arc('smile', (18, 33), (30, 33), radius_x=10, sweep=False)'''),
'disk-platter-with-drive-slots':("Disc platter with three short slots and a radius-two hub. Tangential slots retain visible lengths and safe radial clearance; Lucide disc informs the circles.",'''circle('rim', 24, 24, 20)
circle('hub', 24, 24, 2)
self.add_line('slot-top', (23, 13), (25, 13))
for side in (-1, 1):
    self.add_line('slot-left' if side < 0 else 'slot-right', (24 + side * 10, 28), (24 + side * 9, 30))''')}
for row in json.loads((W/'mapping.json').read_text()):
 p=Path(row['file']);s=p.read_text();note,body=designs[row['original']];s=s[:s.index('    def build')]+ '    def build(self) -> None:\n'+textwrap.indent(textwrap.dedent(helper).strip()+'\n'+body,'        ')+'\n'
 tree=ast.parse(s);doc=tree.body[0]
 if isinstance(doc,ast.Expr) and isinstance(doc.value,ast.Constant):
  ls=s.splitlines(keepends=True);s=''.join(ls[:doc.lineno-1])+repr(note+' CIRCLE visible radius 22; SOLO48 stroke 4.')+'\n'+''.join(ls[doc.end_lineno:])
 p.write_text(s)
