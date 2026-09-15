from humans import *
for n in (15,16):
 body="""# Horizontal kayak leaves room for a full double-ended paddle above it.
self.add_bezier('hull-tr',(24,18),((32,18),(38,22),(42,30)))
self.add_bezier('hull-br',(42,30),((38,38),(32,42),(24,42)))
self.add_bezier('hull-bl',(24,42),((16,42),(10,38),(6,30)))
self.add_bezier('hull-tl',(6,30),((10,22),(16,18),(24,18)))
self.add_contour('hull','hull-tr','hull-br','hull-bl','hull-tl',closed=True)
for name,x in [('left',11),('right',37)]:
    self.add_arc(name+'-a',(x-5,9),(x+5,9),radius_x=5,radius_y=3)
    self.add_arc(name+'-b',(x+5,9),(x-5,9),radius_x=5,radius_y=3)
    self.add_contour(name,name+'-a',name+'-b',closed=True)
self.add_line('shaft',(16,9),(32,9))
self.relate('connect','shaft','left')
self.relate('connect','shaft','right')
"""
 if n==15:body+="""self.add_arc('cockpit-top',(18,30),(30,30),radius_x=6,radius_y=3)
self.add_arc('cockpit-bottom',(30,30),(18,30),radius_x=6,radius_y=3)
self.add_contour('cockpit','cockpit-top','cockpit-bottom',closed=True)
"""
 save(n,body,'Horizontal pointed kayak with a full double-ended paddle above it; keep the elongated cockpit in the cockpit variant. All four hull quarters share smooth tangents at the widest points. Source kayak and Lucide sailboat inspected; the horizontal layout preserves complete paddle blades without trapping wedges against the hull.','SQUARE')
# Simple busts: preserve shoulder geometry and correct exact detached gap.
for n,headspec in [(59,(24,11,5)),(78,(24,10,5)),(103,(27,12,5))]:
 d=create(rows[n-1]['selected']).draw();save(n,emit(d,{'head':headspec},{}),f'Keep the podium and sash/microphone construction. Place the centered head at {headspec[:2]} with radius5, exactly4 painted units above the existing shoulders. Shared full_body_ref.png bust vocabulary; preserve equipment asymmetry.')
# Unambiguous two-person relationship; the carrier head sits over the carrier.
n=45;d=create(rows[n-1]['selected']).draw();pm={(24,23):(18,22),(36,23):(36,22)}
save(n,emit(d,{'carrier-head':(18,10,4),'director-head':(36,10,4)},{},pm),'Center each radius4 head over its own shoulder at y22, with head centers y10 and exact4 painted clearance. The pointing person and box carrier remain distinct. Original scene and full_body_ref.png inspected; both heads share radius and vertical spacing.')
# Flag protester: remove the doubled neck line which was falsely touching head.
save(64,"""self.ring('head',32,16,4)
self.add_bezier('torso',(32,28),((32,31),(28,32),(28,35)))
self.branches([('arm',[(32,28),(24,29),(17,25)]),('left-leg',[(28,35),(20,39),(16,44)]),('right-leg',[(28,35),(35,39),(39,44)]),('pole',[(8,4),(17,25),(20,32)]),('flag',[(8,4),(40,4),(30,14)])])
for p in ['arm-0','left-leg-0','right-leg-0']:self.relate('connect','torso',p)
""",'Flag protester: remove the duplicated line that ran into the head. Radius4 head at (32,16), actual shoulder (32,28), exact4 ink gap. Curved torso and two walking legs preserve the source flag-carrying action. full_body_ref.png owns human proportions.','VRECT_L')
# Ribbon surrounds the action; it is an open trace, not an umbrella canopy.
save(69,"""self.ring('head',24,16,4)
self.add_bezier('torso',(24,28),((24,31),(23,33),(23,35)))
self.branches([('arms-left',[(24,28),(12,27),(8,20)]),('arms-right',[(24,28),(34,32)]),('leg-left',[(23,35),(16,42)]),('leg-right',[(23,35),(33,42)])])
for p in ['arms-left-0','arms-right-0','leg-left-0','leg-right-0']:self.relate('connect','torso',p)
self.add_arc('ribbon',(10,10),(42,28),radius_x=19,radius_y=19)
""",'Ribbon gymnast: separate the open circular ribbon from the arms so it no longer reads as an umbrella. Radius4 head (24,16), torso junction (24,28), exact4 visible gap; preserve the spread arms and dancing legs of the source and full_body_ref.png.')
# Snowboard actions need real arm branches around the enlarged head.
for n in [101,102]:
 d=create(rows[n-1]['selected']).draw()
 skip={p.element_id for p in d.primitives if p.element_id.startswith('arms-')}
 from dataclasses import replace
 d=replace(d,primitives=tuple(p for p in d.primitives if p.element_id not in skip),contours=tuple(c for c in d.contours if not any(m in skip for m in c.members)),relationships=tuple(rel for rel in d.relationships if not any(m=='arms' or m in skip for m in rel.members)))
 if n==101:
  head=(23,11,5);s=(23,24);old=(23,23);hip=(19,28);pid='torso-1'
  arms="self.branches([('left-arm',[(23,24),(12,24),(6,17)]),('right-arm',[(23,24),(35,24),(42,15)])])"
 else:
  head=(20,10,4);s=(20,22);old=(20,19);hip=(19,26);pid='body-1'
  arms="self.branches([('left-arm',[(20,22),(8,24)]),('right-arm',[(20,22),(34,22),(34,6)])])"
  d=replace(d,primitives=tuple(replace(p,start=Point(*(hip if p.start.as_tuple()==(19,24) else p.start.as_tuple())),end=Point(*(hip if p.end.as_tuple()==(19,24) else p.end.as_tuple()))) for p in d.primitives))
 b=Bezier(pid,Point(*s),Point(*hip),(((s[0],s[1]+2),(hip[0],hip[1]-1),hip),))
 body=emit(d,{'head':head},{pid:b},{old:s})+'\n'+arms+f"\nself.relate('connect',{pid!r},'left-arm-0')\nself.relate('connect',{pid!r},'right-arm-0')"
 save(n,body,f'Preserve the snowboard and ramp/jump action; rebuild the raised arms as two clear shoulder branches. Head center{head[:2]}, radius{head[2]}, torso{s}, exact4 painted gap. Full-body reference and the original action drawing inspected.')
# The wheel and frame coordinates stay intact in this independent candidate.
specs[142]=('head','person-1',(16,22),(16,22),(16,10),4);repair_pose(142,specs[142])
# Restore legal lap clearance in the seated bather.
n=89;r=next(r for r in records if r['number']==n);d=create(r['icon_id']).draw();save(n,emit(d,{}, {},{(25,24):(25,23)}),r['reason']+' Keep the raised hand separate from the lap.')
# Bindle figure already had the correct circle, but needs a coherent upper back.
repair_pose(274,('head','torso-2',(34,24),(34,24),(34,10),6))
# Meditation: enlarge head while leaving a full-length spine and open hands.
n=431;d=create(rows[n-1]['selected']).draw();save(n,emit(d,{'head':(24,11,5)},{},{(24,21):(24,24)}),'Meditating figure: radius5 head center(24,11), shoulder(24,24), exact4 painted gap. Preserve crossed legs and two separate curved resting arms; full_body_ref.png proportions.')
# Prayer hands have their own shoulder/torso silhouette; keep a short central palm mark.
n=432;d=create(rows[n-1]['selected']).draw();save(n,emit(d,{'head':(24,11,5)},{},{(24,21):(24,24),(24,26):(24,28)}),'Seated prayer: radius5 head center(24,11) sits exactly4 painted units above the shoulder/palm junction(24,24). Preserve the prayer gesture and crossed legs; original and full_body_ref.png inspected.')
