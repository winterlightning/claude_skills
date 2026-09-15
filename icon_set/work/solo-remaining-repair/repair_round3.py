from repair_more import *
if __name__=='__main__':
 patch(249,[("(26, 18), (32, 18)","(25, 16), (31, 16)"),("(32, 18), (26, 18)","(31, 16), (25, 16)")])
 # Remove the extra toe fold instead of leaving a thin parallel slit above the base.
 save(310,[("self.add_line('foreleg', (34, 34), (32, 40))", "self.add_line('foreleg', (34,34), (36,38))"),("self.add_line('toe', (32, 40), (37, 38))", "self.add_line('toe',(36,38),(40,38))"),("self.add_arc('foot', (37, 38), (32, 42), radius_x=6, radius_y=8)","self.add_bezier('foot',(40,38),((40,40),(36,42),(32,42)))"),("self.add_arc('knee', (32, 40), (23, 36), radius_x=9, radius_y=5, sweep=False)","self.add_arc('knee',(36,38),(23,34),radius_x=13,radius_y=4,sweep=False)")],reason='Replace the folded-back toe by an open rounded foot and keep the knee as one smooth attached curve.')
 save(386,[("pt(14, 30), pt(20, 24), pt(20, 22)","pt(14,30), pt(19,28), pt(20,22)")],reason='Widen the two symmetric dome valleys by lowering their connecting shoulders.')
 for n in (410,411):
  patch(n,[("(x + r, y), (x, y + r + 8), (x - r, y)","(x + r, y), (x, y + r), (x - r, y)")])
 # Three hearts use one compact leaf definition; outer leaves are moved apart and
 # their branches meet below their tips, with the pot deliberately separated vertically.
 for n in (477,491):
  body="""def heart(n,cx,y,tip):
    self.add_arc(n+'-l',(cx,y),(cx-6,y),radius_x=3,sweep=False)
    self.add_line(n+'-left',(cx-6,y),(cx,tip))
    self.add_line(n+'-right',(cx,tip),(cx+6,y))
    self.add_arc(n+'-r',(cx+6,y),(cx,y),radius_x=3,sweep=False)
    self.add_contour(n,n+'-l',n+'-left',n+'-right',n+'-r',closed=True)
heart('centre',24,7,17)
heart('left',12,24,32)
heart('right',36,24,32)
self.add_polyline('stem',(24,17),(24,34),(24,36))
self.add_line('branch-l',(12,32),(24,34))
self.add_line('branch-r',(36,32),(24,34))
for a,b in [('centre','stem'),('left','branch-l'),('right','branch-r'),('stem','branch-l'),('stem','branch-r'),('branch-l','branch-r')]:self.relate('connect',a,b)
self.add_polyline('pot',(18,36),(24,36),(30,36),(30,44),(18,44),closed=True)
self.relate('connect','pot','stem')"""
  if n==477:
   body=body.replace("24,7,17","24,9,19").replace("(24,17)","(24,19)").replace("(24,36)","(24,34)").replace("(18,36),(24,34),(30,36),(30,44),(18,44)","(6,34),(24,34),(42,34),(38,42),(10,42)").replace("(24,34),(24,34)","(24,34)")
  save(n,[("keyshape = Keyshape.VRECT_L","keyshape = Keyshape.VRECT_L") ] if False else (),body=body,reason='Rebuild three equal heart leaves with open counters; spread side leaves and place their shared branches below the leaf tips.')
  # The tall pot version needs the full square width for legal side-leaf separation.
  if n==491:
   r=next(x for x in existing if x['number']==n);p=ROOT/r['file'];s=p.read_text().replace('Keyshape.VRECT_L','Keyshape.SQUARE').replace("24, 7, 17","24, 9, 19").replace("(24, 17)","(24, 19)").replace("(30, 44)","(30, 42)").replace("(18, 44)","(18, 42)").replace("(18, 36)","(18, 34)").replace("(24, 36)","(24, 34)").replace("(30, 36)","(30, 34)");p.write_text(s)
