from pathlib import Path
import json,shutil,textwrap
ROOT=Path(__file__).resolve().parent
items=json.loads((ROOT/'authored.json').read_text())
changes={
1:[("p(9,2)","p(9,4)"),("p(16,3)","p(16,5)")],
3:[("(x,34)","(x,32)"),("(13,37)","(12,39)"),("(35,37)","(36,39)")],
4:[("(12,32),(24,32),(32,20),(18,20),(12,32)","(12,32),(23,32),(32,20),(20,20)"),("self.add_line('seat-post',(24,32),(20,20))","") ,("self.relate('connect','seat-post','frame')","")],
7:[("(8,16),(21,16)","(9,14),(22,14)"),("(8,32),(21,32)","(9,35),(22,35)"),("(12,22),(15,22)","(12,21),(16,21)"),("(12,27),(15,27)","(12,28),(16,28)")],
9:[("self.rect('case',4,10,32,28,3)","self.add_polyline('case',(4,10),(36,10),(36,38),(4,38),closed=True)")],
10:[("(11,14)","(13,15)"),("(11,22)","(13,23)"),("(11,28),(23,28),(23,22)","(13,28),(23,28),(23,23)"),("(23,22)","(23,23)"),("(23,14)","(23,15)"),("(17,14),(17,35)","(18,15),(18,34)"),("(31,13)","(31,15)"),("(31,35)","(31,34)")],
12:[("self.circle('earth',24,20,11)","self.circle('earth',24,18,10)"),("(25,9)","(25,8)"),("(18,17),(28,14),(27,21)","(19,14),(28,12),(27,19)"),("(27,26),(31,21),(35,20)","(27,24),(30,20),(34,18)"),("(13,20)","(14,18)"),("(21,18),(18,27),(23,31)","(21,16),(19,24),(23,28)"),("24,39,5","24,40,4")],
13:[("((22,5),(20,6),(20,8)),((20,11),(27,10),(30,14))","((21,6),(21,12),(24,12)),((26,12),(28,12),(30,14))")],
14:[("(23,13)","(21,13)"),("(18,6)","(17,6)"),("(13,24)","(12,22)"),("((35,9),(31,8),(28,8)),((24,8),(24,13),(28,13))","((36,9),(32,8),(30,8)),((26,8),(26,14),(30,14))"),("((34,13),(36,19),(34,24))","((35,14),(36,19),(34,24))")],
15:[("((13,18),(15,22),(19,20))","((14,16),(14,20),(18,18))"),("((23,18),(26,16),(29,15))","((22,16),(26,14),(29,13))"),("(25,17)","(25,15)"),("((27,22),(34,22),(42,15))","((27,20),(34,20),(42,13))")],
17:[("self.add_bezier('dome',(6,42),((6,30),(42,30),(42,42)))","self.add_arc('dome',(6,42),(42,42),radius_x=18,radius_y=12)"),("(21,29),(29,29)","(21,29),(29,29)"),("(25,29),(25,33)","(25,29),(25,30)")],
19:[("[(14,15),(24,15),(34,15),(14,25),(24,25)]","[(13,14),(24,14),(35,14),(13,26),(24,26)]"),("x,y,3)","x,y,3)")]
}
body5='''
self.rect('body',4,30,40,10,3)
self.add_polyline('roof',(7,30),(10,6),(38,6),(41,30));self.relate('connect','roof','body')
for x in [17,31]:
 self.circle('head'+str(x),x,15,3)
 self.add_bezier('shoulders'+str(x),(x-5,30),((x-5,26),(x+5,26),(x+5,30)))
 self.add_dot('lamp'+str(x),(x-5 if x==17 else x+5,35))
for x in [10,38]:
 self.add_line('tire'+str(x),(x,40),(x,43));self.relate('connect','tire'+str(x),'body')
'''
body8='''
self.add_line('mouthpiece',(10,4),(16,4))
self.add_bezier('outer-neck',(16,4),((22,4),(24,9),(24,15)))
self.add_line('shaft',(16,4),(16,31))
self.add_bezier('outer-bow',(16,31),((16,48),(38,48),(38,30)))
self.add_polyline('bell',(38,30),(40,25),(32,17),(32,31))
self.add_bezier('inner-bow',(32,31),((32,37),(24,37),(24,31)))
self.add_line('inner-shaft',(24,15),(24,31))
for y in [16,24]:self.add_line('key'+str(y),(22,y),(26,y))
self.relate('connect','outer-neck','mouthpiece');self.relate('connect','shaft','mouthpiece');self.relate('connect','shaft','outer-bow');self.relate('connect','outer-bow','bell');self.relate('connect','bell','inner-bow');self.relate('connect','inner-bow','inner-shaft');self.relate('connect','inner-shaft','outer-neck')
'''
body16='''
self.rect('pill',8,18,23,10,5)
self.add_line('seam',(19,18),(19,28));self.relate('connect','seam','pill')
self.add_polyline('upper-back',(42,6),(34,10),(25,10),(18,17))
self.add_bezier('upper-thumb',(42,17),((39,19),(38,21),(35,21)),((33,24),(30,25),(29,23)),((28,21),(31,18),(33,16)))
self.add_bezier('palm',(6,34),((12,34),(17,33),(20,37)),((25,37),(31,36),(33,38)),((35,39),(36,42),(36,42)))
self.add_line('palm-base',(6,42),(36,42));self.relate('connect','palm','palm-base')
'''
for d in items:
 n=d['n']
 if n not in changes and n not in [5,8,16]:continue
 old=Path(d['run']);new=old.with_name(old.name[:-2]+'r2');new.mkdir(exist_ok=False)
 for f in old.iterdir():
  if f.suffix in ['.py','.md'] or f.name.endswith('metadata.json'):shutil.copyfile(f,new/f.name)
 p=new/Path(d['module']).name;s=p.read_text()
 if n in [5,8,16]:s=s.split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(textwrap.dedent({5:body5,8:body8,16:body16}[n]),'        ')
 else:
  for a,b in changes[n]:
   assert a in s,(n,a)
   s=s.replace(a,b)
 p.write_text(s);d['run']=str(new);d['module']=str(p)
(ROOT/'authored.json').write_text(json.dumps(items,indent=2))
