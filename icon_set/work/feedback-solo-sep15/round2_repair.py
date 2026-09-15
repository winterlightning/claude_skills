from pathlib import Path
import json
from edit_batch import revise
SOURCE_ICON_ID=None
SOURCE_PATH='/Users/jakesdev/Downloads/feedback-briefs 2/solo'
AUTHOR='gpt-6'
W=Path(__file__).parent;R=json.loads((W/'revisions.json').read_text())
def edit(n,pairs):
 p=W/'snapshot'/R[str(n)]['file'];s=p.read_text()
 for a,b in pairs:
  if a not in s:raise ValueError((n,a))
  s=s.replace(a,b)
 p.write_text(s)
edit(25,[('(6, 10)','(6, 6)'),('(15, 16)','(15, 15)'),('(31, 16)','(31, 15)')])
edit(58,[('(24 + side * 10, 32), (24 + side * 14, 24)','(24 + side * 10, 28), (24 + side * 14, 20)')])
edit(82,[("path(n, (x - rx, y), [('A', (x + rx, y), rx, ry, True), ('A', (x - rx, y), rx, ry, True)], True)","path(n, (x-rx,y), [('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)")])
edit(83,[("[('left', 14, 6), ('right', 34, 6), ('low', 24, 34)]","[('left', 12, 6), ('right', 36, 6), ('low', 24, 34)]"),('(cx - 8, y)','(cx - 6, y)'),('(cx + 8, y)','(cx + 6, y)')])
edit(87,[("(12, 27), [('A', (36, 27), 12, 8, True), ('A', (12, 27), 12, 11, True)]","(12, 33), [('A', (36, 33), 12, 7, True), ('A', (12, 33), 12, 7, True)]"),('(x(12), 27)','(x(12), 33)')])
edit(91,[("('L', (4, 20)), ('C', (14, 28), (8, 26), (10, 28)), ('C', (20, 22), (18, 28), (20, 27))","('L',(4,16)),('C',(14,24),(8,22),(10,24)),('C',(20,20),(18,24),(20,24))")])
edit(101,[("('L', (8, 23)), ('C', (16, 10), (8, 16), (12, 10)), ('L', (12, 4)), ('C', (28, 12), (22, 4), (26, 8))","('L',(8,4)),('C',(28,12),(22,4),(26,8))")])
edit(106,[("self.add_arc('dorsal-1', (6, 26), (7, 6), radius_x=24, radius_y=24, sweep=False)","self.add_line('dorsal-1',(6,26),(6,6))"),("self.add_arc('dorsal-2', (7, 6), (20, 12), radius_x=30, radius_y=30, sweep=True)","self.add_line('dorsal-2',(6,6),(20,12))")])
edit(123,[("self.add_contour('upper', 'hip-top'","self.contours=[c for c in self.contours if c.contour_id!='head-new']\n        self.add_contour('upper', 'hip-top'")])
edit(133,[("('L', (36, 42)), ('L', (32, 34)), ('L', (22, 34)), ('L', (18, 42))","('L',(34,42)),('L',(30,34)),('L',(24,34)),('L',(20,42))")])
edit(170,[("path('center', (20, 22), [('A', (28, 22), 4, 4, True), ('L', (28, 28)), ('L', (28, 30))","path('center',(20,26),[('A',(28,26),4,4,True),('L',(28,30))"),("('L', (20, 28)), ('L', (20, 22))","('L',(20,26))"),("line('center-collar', (20, 28), (28, 28))","line('center-collar',(20,30),(28,30))")])
# Reject stale bytecode when models are rapidly iterated with equal file sizes.
for p in (W/'snapshot').rglob('*.pyc'):p.unlink()
