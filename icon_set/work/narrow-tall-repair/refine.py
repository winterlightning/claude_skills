from pathlib import Path
import json,sys,textwrap,ast
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/narrow-tall-repair/results.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'results.json').read_text());by={r['root']:r for r in rows}
def edit(k,changes,note):
 r=by[k];p=ROOT/r['file'];s=p.read_text()
 for a,b in changes:
  assert a in s,(k,a);s=s.replace(a,b)
 p.write_text(s);r['note']=note
def build(k,body,note):
 r=by[k];p=ROOT/r['file'];s=p.read_text();s=s[:s.index('    def build')];p.write_text(s+'    def build(self) -> None:\n'+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n');r['note']=note
build('buffalo-head','''
# SQUARE (6,6)-(42,42). Mirrored horn quarters and broad round jaw.
# Face stations leave a full eight-unit eye inset and a distinct muzzle.
x,left,right,top,jaw_y,r=24,12,36,16,30,12
self.add_arc('horn-left',(6,6),(left,top),radius_x=6,radius_y=10,sweep=False)
self.add_line('brow',(left,top),(right,top))
self.add_arc('horn-right',(right,top),(42,6),radius_x=6,radius_y=10,sweep=False)
self.add_contour('horns','horn-left','brow','horn-right')
self.add_line('left-cheek',(left,top),(left,jaw_y))
self.add_arc('left-jaw',(left,jaw_y),(x,42),radius_x=r,sweep=False)
self.add_arc('right-jaw',(x,42),(right,jaw_y),radius_x=r,sweep=False)
self.add_line('right-cheek',(right,jaw_y),(right,top))
self.add_contour('face','left-cheek','left-jaw','right-jaw','right-cheek')
self.relate('connect','horns','face')
for side,ex in [('left',20),('right',28)]:self.add_dot('eye-'+side,(ex,24))
self.add_line('muzzle',(22,33),(26,33))
''','Rebuilt mirrored horns and a broad circular jaw; retained both eyes and muzzle with proper clearance.')
edit('minoan-palace',[('(x, 43)','(x, 42)')],'Square envelope; ended the repeated columns exactly at the common base.')
edit('mammoth-head',[('radius_x=9, radius_y=14','radius_x=9, radius_y=13'),('radius_x=12, radius_y=12, sweep=True','radius_x=8, radius_y=11, sweep=True'),("(36, 19)","(34, 19)")],'Square envelope; canonical forehead quarters remove tiny overshoot and the eye moves inward.')
edit('salamander',[("radius_x=15, radius_y=15","radius_x=11, radius_y=14"),("radius_x=18, radius_y=18","radius_x=18, radius_y=17"),("(16, 14)","(16, 16)")],'Square envelope; exact head/tail ellipses and centered eye preserve the curled silhouette.')
edit('shark-head',[("(28, 15)","(28, 10)"),("(24, 28)","(24, 30)"),("self.add_line('eye', (29, 22), (31, 22))","self.add_dot('eye', (28, 22))")],'Square envelope; opened the forehead and mouth around a single eye dot while preserving the wedge snout.')
edit('swimming-shark',[("(18, 23), (18, 28)","(22, 23), (22, 27)")],'Square envelope; moved and shortened the gill within the broadest body region.')
edit('turreted-chateau-hotel',[("(12, 27)","(14, 27)"),("(12, 42)","(14, 42)"),("(12, 32)","(14, 32)"),("(20, 42)","(22, 42)"),("(20, 33)","(22, 33)"),("(27, 23)","(28, 23)")],'Square envelope; narrowed and centered the main gable to leave eight units beside the turret divider.')
edit('penguin-face',[("(16, 21)","(17, 21)"),("(16, 23)","(17, 23)"),("(32, 21)","(31, 21)"),("(32, 23)","(31, 23)")],'Square envelope; corrected the dome to exact quarter ellipses and moved the eyes inward symmetrically.')
edit('sloth-face',[("(17, 29)","(17, 30)"),("(31, 29)","(31, 30)")],'Square envelope; repositioned both eyes equally between the mask curves and cheek outline.')
edit('dinosaur-skull',[("(6, 12)","(6, 10)"),("(6, 37)","(6, 34)"),("(29, 37)","(29, 34)"),("(36, 28)","(36, 26)"),("(6, 28)","(6, 26)"),("(31, 18)","(29, 16)"),("(37, 18)","(33, 16)"),("radius_x=3","radius_x=2"),("(13, 20)","(15, 17)")],'Square envelope; opened the jaw bands, raised the snout and retained a smaller circular eye and nostril.')
edit('usb-cable-connector',[("(18,20)","(18,22)"),("(38,20)","(38,22)"),("(16,20)","(16,22)"),("(40,20)","(40,22)"),("(cx,12)","(cx,13)")],'Broadened the grip and opened the USB tip for a centered mark with margin above and below.')
(W/'results.json').write_text(json.dumps(rows,indent=2))
