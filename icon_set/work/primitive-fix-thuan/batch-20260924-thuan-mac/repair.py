from pathlib import Path
import json
rows=json.loads(Path('icon_set/work/primitive-fix-thuan/batch-20260924-thuan-mac/runs.json').read_text())
def edit(n,pairs):
 p=Path(next(r['module'] for r in rows if r['icon_id']==n));s=p.read_text()
 for a,b in pairs:
  assert a in s,(n,a)
  s=s.replace(a,b)
 p.write_text(s)
edit('handheld-circular-saw',[("(25,5),(28,8)","(25,6),(28,8)")])
edit('head-profile-wearing-broad-protective-mask',[("('C',(6,30),(6,22),(6,26)),('C',(14,36),(6,34),(10,36)),('L',(23,36))","('L',(8,30)),('A',(14,36),6,6,False),('L',(17,36)),('L',(23,36))"),("('L',(40,16))","('L',(40,20))"),("join('mask','skull')","join('mask','skull');join('strap','skull');join('strap','mask')")])
edit('headphone-wearing-dj-behind-two-turntables',[("(14,30),[('A',(24,24),10,6,True),('A',(34,30),10,6,True)]","(14,28),[('A',(24,24),10,4,True),('A',(34,28),10,4,True)]"),("(10,30),(14,30),(34,30),(38,30)","(10,28),(14,28),(34,28),(38,28)"),("(x-1,37),(x+1,37)","(x-1,36),(x+1,36)")])
edit('hedgehog',[("('C',(8,33),(12,35),(10,34))","('L',(8,35))"),("((6,16),(17,20)),((4,25),(14,26))","((6,16),(14,19)),((4,26),(12,27))")])
edit('horizontal-power-plug-with-leaf-vein-cord',[("('A',(34,28),8,8,True),('L',(22,28))","('L',(42,34))"),("join('leaf','vein')","join('leaf','vein');join('leaf','cord');join('cord','vein')")])
edit('horse',[("(43,25),(40,27)","(42,25),(40,27)"),("path('tail',(13,23),[('C',(6,33),(8,23),(6,27)),('L',(6,38))])","path('tail',(20,20),[('C',(6,32),(10,20),(6,24))])")])
edit('hot-roasted-pork-platter',[("(x,13),(x-2,9),(x+2,12)","(x,12),(x-2,9),(x+2,11)")])
edit('human-head-side-profile-scan-solo-b001-14',[("(25,14),[('C',(19,20),(21,14),(19,16))","(25,15),[('C',(19,21),(21,15),(19,17))")])
edit('i-love-you-hand-sign',[("('L',(7,27)),('A',(6,22),4,4,True),('C',(14,25),(8,19),(12,23))","('L',(7,27)),('C',(6,23),(6,26),(6,25)),('C',(14,25),(6,19),(12,23))")])
