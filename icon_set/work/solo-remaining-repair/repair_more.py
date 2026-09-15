from repair import *

def patch(n,pairs,reason=None):
 r=next(x for x in existing if x['number']==n);p=ROOT/r['file'];s=p.read_text()
 for a,b in pairs:
  assert a in s,(n,a)
  s=s.replace(a,b)
 p.write_text(s)
 if reason:r['reason']=reason;(W/'repairs.json').write_text(json.dumps(existing,indent=2)+'\n')

if __name__=='__main__':
 patch(65,[("(16, 36)","(16, 34)"),("(6, 36)","(6, 34)"),("(26, 36)","(26, 34)"),("self.circle('pulley', 24, 22, 8)","self.circle('pulley', 24, 20, 6)"),("(24, 14)","(24, 14)"),("(16, 22)","(18, 20)"),("(32, 22)","(30, 20)")])
 patch(119,[("circle('ball', 9, 34, 3)","circle('ball', 9, 38, 3)")])
 patch(127,[("circle('head', 37, 27, 3)","circle('head', 38, 27, 3)"),("(37, 38)","(38, 38)")])
 # A stand is a clear solid bar rather than a closed counter too shallow to survive.
 save(191,body="""self._circle('globe', 18, 16, 10)
self._path('meridian', (32,4), [('A',(40,20),20,20,True),('A',(22,34),18,14,True),('A',(8,32),24,24,True)])
self.add_line('stem',(22,34),(22,44))
self.add_polyline('base',(13,44),(22,44),(31,44))
self.relate('connect','stem','meridian')
self.relate('connect','stem','base')""",reason='Use a flat pedestal bar with a real central stem; remove the pinched shallow stand counter.')
 patch(249,[("(25, 17), (31, 17)","(26, 18), (32, 18)"),("(31, 17), (25, 17)","(32, 18), (26, 18)")])
 save(272,body="""self.circle('head',24,11,5)
self.add_polyline('book',(10,24),(24,28),(38,24),(38,30),(38,38),(24,42),(10,38),(10,30),closed=True)
self.add_line('fold',(24,28),(24,42))
self.relate('connect','book','fold')
for side,x in (('left',6),('right',42)):
    end=10 if side=='left' else 38
    self.add_line('hand-'+side,(x,30),(end,30))
    self.relate('connect','book','hand-'+side)""",reason='Simplify the tiny hand rings into short gripping fingers joined to the book; lower page tops give the head exactly4 ink clearance.')
 save(310,[("self.add_line('foreleg', (34, 34), (32, 40))", "self.add_line('foreleg', (34, 34), (30, 38))"),("self.add_line('toe', (32, 40), (37, 38))", "self.add_line('toe', (30, 38), (40, 38))"),("self.add_arc('foot', (37, 38), (32, 42), radius_x=6, radius_y=8)","self.add_bezier('foot',(40,38),((40,40),(36,42),(32,42)))"),("(32, 40), (23, 36)","(30, 38), (21, 34)")],reason='Open the koala toe recess and use a smooth foot curve with its bottom tangent on the baseline.')
 save(386,[("pt(14, 30), pt(20, 24), pt(20, 22)","pt(14,30), pt(20,26), pt(20,22)")],reason='Lower both shoulder bends so their dome junctions do not trap tiny specks.')
 # Keep the gun-to-bed gap; move the wheel lower and make all wheel instances equal.
 save(474,[("(6, 34),(18, 34),radius_x=6,radius_y=6","(6, 35),(16, 35),radius_x=5,radius_y=5"),("(18, 34),(6, 34),radius_x=6,radius_y=6","(16, 35),(6, 35),radius_x=5,radius_y=5"),("(30, 34),(42, 34),radius_x=6,radius_y=6","(32, 35),(42, 35),radius_x=5,radius_y=5"),("(42, 34),(30, 34),radius_x=6,radius_y=6","(42, 35),(32, 35),radius_x=5,radius_y=5"),("(6, 34),(4, 34)","(6, 35),(4, 35)"),("(44, 34),(42, 34)","(44, 35),(42, 35)"),("(18, 34),(30, 34)","(16, 35),(32, 35)")],reason='Lower and slightly reduce both repeated wheels to clear the bed corners while preserving the mounted gun spacing.')
 for n in (410,411):
  save(n,[("x,35,r=2,width=6","x,30,r=3,width=6"),("y+7","y+12"),("(x,y+r)","(x,y+r+8)"),("radius_y=7-r","radius_y=1"),("        self.relate('connect',name+'-head',name+'-shoulders')","")]+([] if n==410 else [("(6,24),(12,24),(24,24),(36,24),(42,24)","(6,18),(12,18),(24,18),(36,18),(42,18)"),("(x,24)","(x,18)")]),reason='Open the three equal head rings and give every person exactly4 ink units to its shoulder apex, following full_body_ref.png.')
 for n in (489,492):
  save(n,[("(7,24,41)","(8,24,40)"),("y=12 if lower else 8","y=12 if lower else 8"),("belly=4 if lower else 3","belly=4"),("rx=belly-2","rx=belly-3"),("cx-3,y+3","cx-4,y+4"),("cx+3,y+3","cx+4,y+4"),("radius_x=3)","radius_x=4)"),("cx+2,18","cx+3,20"),("cx-2,18","cx-3,20"),("radius_y=11","radius_y=9"),("cx+2,base","cx+3,base"),("cx-2,base","cx-3,base")],reason='Rebuild all three pins from one wider head and neck definition; equal16-unit spacing preserves4-unit ink gaps.')
 # Duplicate shared strokes: keep the actual paint once and expose its attachment nodes.
 save(35,[("self.add_line('legs-2', (24, 24), (30, 24))", ""),("self.add_contour('legs', *('legs-1', 'legs-2', 'legs-3'), closed=False)","self.relate('connect','legs-1','table')\n        self.relate('connect','legs-3','table')\n        self.relate('connect','legs-1','bench')\n        self.relate('connect','legs-3','bench')\n        self.relate('connect','legs-1','shelter')\n        self.relate('connect','legs-3','shelter')"),("        self.relate('connect', *('legs', 'table'))", ""),("        self.relate('connect', *('legs', 'bench'))", ""),("        self.relate('connect', *('legs', 'shelter'))", ""),("self.add_line('table', (20, 24), (34, 24))","self.add_polyline('table',(20,24),(24,24),(30,24),(34,24))")],reason='Remove the duplicated tabletop segment between the legs and keep genuine shared attachment nodes.')
 for n,side in ((55,1),(88,-1)):
  x=42 if side==1 else 6;mid=37 if side==1 else 11;leg=40 if side==1 else 8;end=28 if side==1 else 20;cx=12 if side==1 else 36
  save(n,[(f"self.add_polyline('laptop', ({x}, 10), ({mid}, 25), ({end}, 25), closed=False)",f"self.add_line('laptop',({x},10),({mid},25))"),(f"self.add_line('desktop', ({x}, 25), (24, 25))",f"self.add_polyline('desktop',({x},25),({leg},25),({mid},25),(24,25))"),(f"({cx}, 23)",f"({cx}, 22)")],reason='Keep the desk edge once, split its true laptop and leg attachments, and set the head-to-shoulder ink gap to4.')
 save(57,[("[('A', (33, 13), 9, 9, True), ('L', (15, 13))], True","[('A', (33, 13), 9, 9, True)]"),("self.add_line('rim', (8, 13), (40, 13))","self.add_polyline('rim',(8,13),(15,13),(33,13),(40,13))")],reason='Remove the repeated bulb base; the continuous rim owns this shared edge.')
 save(255,[("'nine-stem', (12, 16), (12, 36)","'nine-stem', (12, 20), (12, 36)")],reason='Start the nine descender at the bowl endpoint so its right wall is drawn once.')
 save(369,[("(33,4),(36,16),(12,16)","(33,4),(36,16)")],reason='Remove the hat baseline duplicated by the brim; preserve the circular avatar face and its shoulder contact.')
