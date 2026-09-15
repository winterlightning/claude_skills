# SOURCE_ICON_ID and SOURCE_PATH are carried per variant by author.py.
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-full-set/pending.json'
for n,key,rx,ry in [('oval-1','VRECT_L',16,20),('oval-design','HRECT_L',20,16),('oval-shape','HRECT_L',20,16)]:
 design(n,key,'True elliptical outline','ellipse','One centered ellipse with two matching halves; preserve source orientation and proportions.',f"""
 self.add_arc('top',(24-{rx},24),(24+{rx},24),radius_x={rx},radius_y={ry})
 self.add_arc('bottom',(24+{rx},24),(24-{rx},24),radius_x={rx},radius_y={ry})
 self.add_contour('outline','top','bottom',closed=True)
 """)
for n,hole,cy in [('pin',True,20),('location-pin',True,19),('style-three-style-pin-empty',False,20)]:
 design(n,'VRECT_L','Smooth symmetric map pin','map-pin','Mirrored shoulders and a single flowing taper; keep the original open or inset center.',f"""
 path('outline',(8,{cy}),[('A',(40,{cy}),16,{cy-4},True),('C',(24,44),(40,29),(30,38)),('C',(8,{cy}),(18,38),(8,29))],True)
 """+(f"circle('inset',24,{cy},5)" if hole else ''))
design('drop-shape','VRECT_L','Smooth teardrop','droplet','Symmetric tapered shoulders meet a circular bowl with continuous vertical tangents.',"""
 path('drop',(24,4),[('C',(40,28),(29,10),(40,18)),('A',(8,28),16,16,True),('C',(24,4),(8,18),(19,10))],True)
 """)
for n,cy in [('heart-b74d773d',18),('love-it',19)]:
 design(n,'HRECT_L','Balanced flowing heart','heart','Matched lobes around the shared center; retain the broad heart and pointed bottom.',f"""
 path('heart',(24,13),[('C',(34,8),(27,10),(29,8)),('C',(44,{cy}),(40,8),(44,12)),('C',(39,27),(44,22),(42,24)),('L',(24,40)),('L',(9,27)),('C',(4,{cy}),(6,24),(4,22)),('C',(14,8),(4,12),(8,8)),('C',(24,13),(19,8),(21,10))],True)
 """)
design('logo-youtube-gaming','HRECT_L','Smooth broad gaming heart',None,'Preserve the flattened side walls and shallow notch that distinguish this emblem.',"""
 path('outline',(24,13),[('C',(34,8),(28,10),(29,8)),('C',(44,18),(40,8),(44,12)),('L',(44,23)),('C',(41,27),(44,25),(43,26)),('L',(24,40)),('L',(7,27)),('C',(4,23),(5,26),(4,25)),('L',(4,18)),('C',(14,8),(4,12),(8,8)),('C',(24,13),(19,8),(20,10))],True)
 """)
design('standing-lamp-lamps','VRECT_L','Balanced shade and connected stand','lamp-floor','A symmetric trapezoid shade owns its central stem attachment; preserve the broad flat base.',"""
 path('shade',(8,21),[('L',(14,4)),('L',(34,4)),('L',(40,21)),('L',(24,21)),('L',(8,21))],True)
 line('stem',(24,21),(24,44))
 path('base',(14,44),[('L',(24,44)),('L',(34,44))])
 join('stem','shade');join('stem','base')
 """)
for n,r in [('arrow-undo-left',12),('arrow-wayfinding',11)]:
 design(n,'HRECT_L','Continuous rounded return arrow','undo-2','A single semicircular turn meets horizontal runs tangentially; both wings share the arrow point.',f"""
 path('shaft',(25,8),[('L',({44-r},8)),('A',({44-r},{8+2*r}),{r},{r},True),('L',(4,{8+2*r}))])
 path('head',({12 if r==12 else 14},{8+2*r-10}),[('L',(4,{8+2*r})),('L',({12 if r==12 else 14},40))])
 join('shaft','head')
 """)
for n,mirror,r in [('turn-left',False,12),('turn-right',True,12),('turn-right-transportation',True,14)]:
 design(n,'VRECT_L','Smooth directional bend','undo-2','A quarter-circle bend joins straight runs; preserve direction and the longer upright stem.',f"""
 def pt(x,y):return (48-x,y) if {mirror} else (x,y)
 path('shaft',pt(8,12),[('L',pt({40-r},12)),('A',pt(40,{12+r}),{r},{r},{not mirror}),('L',pt(40,44))])
 path('head',pt(16,4),[('L',pt(8,12)),('L',pt(16,20))]);join('shaft','head')
 """)
for n,slant,bars in [('loading-bar',5,2),('loading-bar-1',14,2),('loading-bar-interface-essential',12,1)]:
 design(n,'HRECT_L','Regular curved loading bar',None,'Matching rounded ends and shared parallel stripe spacing; retain the source stripe count and slant.',f"""
 tops={([20,32] if slant==5 else [25,39]) if bars==2 else [30]}
 bottoms=[x-{slant} for x in tops]
 commands=[('L',(x,8)) for x in tops]+[('L',(38,8)),('C',(44,24),(42,8),(44,14)),('C',(38,40),(44,34),(42,40))]+[('L',(x,40)) for x in reversed(bottoms)]+[('L',(10,40)),('C',(4,24),(6,40),(4,34)),('C',(10,8),(4,14),(6,8))]
 path('body',(10,8),commands,True)
 for j,(a,b) in enumerate(zip(tops,bottoms)):
  line(f'stripe-{{j}}',(a,8),(b,40));join(f'stripe-{{j}}','body')
 """)
for n,rad,top in [('lock-8eddc674',3,18),('lock-e43b261d',4,19),('lock-interface-essential',2,19)]:
 design(n,'VRECT_L','Even lock body and shackle',None,'Match body corner radii and center the key slot; preserve the rounded U-shaped shackle.',f"""
 path('body',(11,{top}),[('L',(12,{top})),('L',(36,{top})),('L',({40-rad},{top})),('A',(40,{top+rad}),{rad},{rad},True),('L',(40,{44-rad})),('A',({40-rad},44),{rad},{rad},True),('L',({8+rad},44)),('A',(8,{44-rad}),{rad},{rad},True),('L',(8,{top+rad})),('A',({8+rad},{top}),{rad},{rad},True),('L',(11,{top}))],True)
 path('shackle',(12,{top}),[('L',(12,16)),('A',(36,16),12,12,True),('L',(36,{top}))]);join('shackle','body')
 line('slot',(24,28),(24,33))
 """)
design('lemon','VRECT_L','Flowing lemon silhouette',None,'Preserve the lemon tips and fuller middle; mirror the opposing shoulders without changing the upright silhouette.',"""
 path('fruit',(24,4),[('C',(30,8),(27,4),(27,6)),('C',(40,24),(37,13),(40,18)),('C',(30,40),(40,31),(36,36)),('C',(24,44),(27,42),(27,44)),('C',(18,40),(21,44),(21,42)),('C',(8,24),(12,36),(8,31)),('C',(18,8),(8,18),(11,13)),('C',(24,4),(21,6),(21,4))],True)
 """)
for n in ['badge-1','flower-badge']:
 design(n,'SQUARE','Smooth six-lobed outline','flower','Six rounded lobes with mirrored valleys; preserve the six-petal badge identity.',"""
 left=[('C',(17,11),(20,6),(18,8)),('C',(6,18),(11,9),(6,12)),('C',(8,24),(6,21),(8,22)),('C',(6,30),(8,26),(6,27)),('C',(17,37),(6,36),(11,39)),('C',(24,42),(18,40),(20,42))]
 commands=list(left);starts=[(24,6)]+[c[1] for c in left[:-1]]
 for c,start in reversed(list(zip(left,starts))):
  _,end,c1,c2=c
  commands.append(('C',(48-start[0],start[1]),(48-c2[0],c2[1]),(48-c1[0],c1[1])))
 path('outline',(24,6),commands,True)
 """)
design('badge-2','SQUARE','Regular eight-lobed badge','flower','Eight rounded lobes constructed from one quarter-turn definition; retain the original petal count.',"""
 quarter=[('C',(30,10),(27,6),(29,8)),('C',(38,10),(33,8),(36,8)),('C',(38,18),(40,12),(40,15)),('C',(42,24),(40,19),(42,21))]
 commands=[]
 def rot(p,n):
  x,y=p
  for _ in range(n):x,y=48-y,x
  return x,y
 for j in range(4):
  for _,end,a,b in quarter:commands.append(('C',rot(end,j),rot(a,j),rot(b,j)))
 path('outline',(24,6),commands,True)
 """)
design('wave','SQUARE','Three matching flowing waves',None,'One coherent S curve repeated at equal spacing; preserve the vertical wave direction.',"""
 for j,dx in enumerate([0,14,28]):
  path(f'wave-{j}',(12+dx,6),[('C',(6+dx,15),(10+dx,9),(6+dx,11)),('C',(14+dx,33),(6+dx,23),(14+dx,25)),('C',(8+dx,42),(14+dx,37),(10+dx,40))])
 """)
design('wave-e3459233','HRECT_L','Two matching wave strokes',None,'Repeat the same smooth horizontal wave; preserve the broad two-line sign.',"""
 for j,dy in enumerate([0,20]):
  path(f'wave-{j}',(4,15+dy),[('C',(14,8+dy),(8,10+dy),(10,8+dy)),('C',(34,20+dy),(22,8+dy),(26,20+dy)),('C',(44,13+dy),(38,20+dy),(42,16+dy))])
 """)
design('wave-forward-interface-essential','VRECT_L','Smooth paired wave fronts',None,'Preserve two forward-facing bows and the larger outer wave; mirrored top and bottom controls.',"""
 path('inner',(8,11),[('C',(17,24),(14,15),(17,19)),('C',(8,37),(17,29),(14,33))])
 path('outer',(26,4),[('C',(40,24),(35,11),(40,15)),('C',(26,44),(40,33),(35,37))])
 """)
design('return-arrow','HRECT_L','Rounded return corner','undo-2','Preserve the short upright tail and long arrow shaft; replace the kink with a tangent quarter arc.',"""
 path('shaft',(44,11),[('L',(44,18)),('A',(38,24),6,6,True),('L',(4,24))])
 path('head',(18,8),[('L',(4,24)),('L',(18,40))]);join('shaft','head')
 """)
for n,side in [('arrow-circle-bottom-4','down'),('arrow-circle-left-4','left')]:
 design(n,'SQUARE','Smooth open ring arrow',None,'Preserve the arrow attached to an open ring; reconstruct the ring as coherent cardinal arcs.',f"""
 def pt(x,y):return (48-y,x) if '{side}'=='left' else (x,y)
 path('ring-shaft',pt(24,34),[('L',pt(24,6)),('A',pt(6,24),18,18,False),('A',pt(24,42),18,18,False),('A',pt(42,24),18,18,False),('C',pt(29,7),pt(42,16),pt(37,9))])
 path('head',pt(15,25),[('L',pt(24,34)),('L',pt(33,25))]);join('head','ring-shaft')
 """)
for n,mirror,full in [('synchronize-refresh-arrow',False,False),('synchronize-refresh-arrow-1',False,False),('synchronize-refresh-arrow-1-interface-essential',False,True),('synchronize-refresh-arrow-a0553293',True,False),('synchronize-refresh-arrow-b3069a62',True,False),('synchronize-refresh-arrow-f65dbb66',False,True),('synchronize-refresh-arrow-interface-essential',True,False)]:
 design(n,'HRECT_L','Smooth refresh curve',None,'Preserve rotation direction and open-ring length; use matching quarter ellipses and a shared arrow point.',f"""
 def pt(x,y):return (48-x,y) if {mirror} else (x,y)
 commands=[('A',pt(26,8),18,16,{not mirror}),('A',pt(44,24),18,16,{not mirror}),('A',pt(26,40),18,16,{not mirror})]
 if {full}:commands.append(('C',pt(10,32),pt(19,40),pt(14,37)))
 path('curve',pt(8,24),commands)
 path('head',pt(4,19),[('L',pt(8,24)),('L',pt(13,19))]);join('head','curve')
 """)
design('synchronize-arrow','HRECT_L','Smooth refresh curve with center',None,'Keep the inset center ellipse and rotation direction; replace segmented perimeter with coherent arcs.',"""
 path('curve',(8,24),[('A',(26,8),18,16,True),('A',(44,24),18,16,True),('A',(26,40),18,16,True)])
 path('head',(4,19),[('L',(8,24)),('L',(13,19))]);join('head','curve')
 self.add_arc('center-top',(22,24),(32,24),radius_x=5,radius_y=4)
 self.add_arc('center-bottom',(32,24),(22,24),radius_x=5,radius_y=4)
 self.add_contour('center','center-top','center-bottom',closed=True)
 """)
design('card-a525cc8f','HRECT_L','Even card outline',None,'Four shared corner radii replace uneven corners and doubled edge runs; retain the short inset mark.',"""
 rounded('card',4,8,44,40,4);line('mark',(29,29),(33,29))
 """)
design('lift-hook-box','VRECT_L','Clean lifting sling',None,'The two sling straps share exact box attachment nodes; remove the retraced top edge.',"""
 path('box',(8,23),[('L',(13,23)),('L',(35,23)),('L',(40,23)),('L',(40,44)),('L',(8,44)),('L',(8,23))],True)
 path('sling',(13,23),[('L',(24,10)),('L',(35,23))]);line('hook',(24,4),(24,10));join('sling','box');join('hook','sling')
 """)
design('chart','HRECT_L','Smooth double-peaked chart',None,'Two coherent peaks and one trough replace narrow uneven segmented bends; retain their different heights.',"""
 path('wave',(4,35),[('C',(12,10),(9,35),(7,10)),('C',(22,40),(18,10),(16,40)),('C',(32,8),(28,40),(26,8)),('C',(44,38),(39,8),(36,38))])
 """)
design('handwritten-text-character','VRECT_L','Flowing handwritten M',None,'Preserve the handwritten M with two tall rounded shoulders and a deep central valley.',"""
 path('letter',(8,44),[('C',(17,4),(10,28),(10,4)),('C',(26,28),(24,4),(21,28)),('C',(37,4),(31,28),(32,4)),('C',(40,44),(40,4),(37,35))])
 """)
design('heart-beat','HRECT_L','Regular pulse stroke',None,'Preserve the high peak and deep trough while replacing the cramped curl at the end with a clear recovery.',"""
 poly('pulse',(4,26),(10,26),(16,8),(24,40),(30,14),(36,26),(44,26))
 """)
design('flash','VRECT_L','Clean lightning outline',None,'Preserve the broad top and pointed lower arm; consolidate the lower diagonal into one deliberate straight run.',"""
 poly('bolt',(14,44),(40,19),(24,19),(34,4),(22,4),(8,26),(22,26),closed=True)
 """)
design('deviant-art-logo','VRECT_L','Clean angular emblem',None,'Preserve the supplied angular Z silhouette and squared upper edge; remove the bumpy lower tip.',"""
 poly('mark',(24,4),(40,4),(28,22),(38,22),(16,44),(8,44),(19,28),(8,28),closed=True)
 """)
design('email-action-reply','HRECT_L','Flowing reply arrow','undo-2','Keep the outlined arrow and rising tail; match the two sweeping body curves.',"""
 path('reply',(20,28),[('L',(20,38)),('L',(4,23)),('L',(20,8)),('L',(20,17)),('C',(44,40),(36,17),(44,25)),('C',(20,28),(36,31),(30,28))],True)
 """)
for n,mirror in [('astrology-moon',False),('moon-right',False),('night-moon-new-weather',True)]:
 design(n,'VRECT_L','Smooth crescent silhouette',None,'Preserve the crescent direction; coherent outer and inner curves replace the broken tip transitions.',f"""
 def pt(x,y):return (48-x,y) if {mirror} else (x,y)
 path('moon',pt(8,4),[('C',pt(40,24),pt(27,4),pt(40,12)),('C',pt(8,44),pt(40,36),pt(27,44)),('C',pt(25,24),pt(20,41),pt(25,32)),('C',pt(8,4),pt(25,16),pt(20,7))],True)
 """)
design('apostrophe','VRECT_L','Smooth comma-shaped mark',None,'Retain the broad rounded head and curved tail; remove the uneven internal hook.',"""
 path('mark',(12,44),[('C',(40,17),(30,43),(40,30)),('C',(24,4),(40,7),(32,4)),('C',(8,15),(14,4),(8,8)),('C',(23,23),(8,24),(15,21)),('C',(12,40),(26,28),(21,36)),('C',(12,44),(9,41),(9,44))],True)
 """)
design('institution','VRECT_L','Balanced flag-topped building',None,'Preserve the domed roof and attached flag; broaden the flag into a clear triangular pennant.',"""
 path('roof',(8,31),[('C',(24,19),(10,23),(15,19)),('C',(40,31),(33,19),(38,23)),('L',(37,31)),('L',(11,31)),('L',(8,31))],True)
 path('building',(11,31),[('L',(11,44)),('L',(37,44)),('L',(37,31))]);join('building','roof')
 path('pole',(24,19),[('L',(24,14)),('L',(24,4)),('L',(36,9)),('L',(24,14))]);join('pole','roof')
 """)
design('legal-scale-2','HRECT_L','Matching balance pans',None,'Two equal semicircular pans share suspension lengths and a level beam; preserve the hanging-scale composition.',"""
 path('beam',(7,12),[('L',(12,12)),('L',(24,12)),('L',(36,12)),('L',(41,12))]);path('pivot',(24,8),[('L',(24,12)),('L',(24,17))]);join('beam','pivot')
 for j,cx in enumerate([12,36]):
  path(f'pan-{j}',(cx-8,32),[('L',(cx+8,32)),('A',(cx-8,32),8,8,True)],True)
  path(f'cord-{j}',(cx-8,32),[('L',(cx,12)),('L',(cx+8,32))]);join(f'cord-{j}',f'pan-{j}');join(f'cord-{j}','beam')
 """)
design('lgbt-gift','VRECT_L','Balanced gift bow',None,'Two matching open bow loops meet at the ribbon center; preserve the simple gift box.',"""
 path('box',(8,17),[('L',(24,17)),('L',(40,17)),('L',(40,44)),('L',(8,44)),('L',(8,17))],True)
 path('left',(24,17),[('C',(9,9),(17,6),(9,1)),('C',(24,17),(9,15),(18,17))],True)
 path('right',(24,17),[('C',(39,9),(31,6),(39,1)),('C',(24,17),(39,15),(30,17))],True)
 join('left','right');join('left','box');join('right','box')
 """)
for n in ['module-puzzle','puzzle']:
 design(n,'VRECT_L','Smooth puzzle piece',None,'Preserve one upper tab, one left socket and one lower socket; matched circular necks and regular walls.',"""
 path('piece',(19,14),[('L',(8,14)),('L',(8,23)),('C',(17,28),(12,19),(17,22)),('C',(8,33),(17,34),(12,37)),('L',(8,44)),('L',(19,44)),('C',(24,33),(15,40),(18,33)),('C',(29,44),(30,33),(33,40)),('L',(40,44)),('L',(40,14)),('L',(29,14)),('C',(24,4),(33,9),(30,4)),('C',(19,14),(18,4),(15,9))],True)
 """)
for n in ['onigiri-japanese-riceball','riceball-onigiri-japanese-food']:
 design(n,'HRECT_L','Rounded rice ball with centered wrap',None,'Preserve the triangular rice ball and dark-wrap outline; give the wrap clear room below the shoulders.',"""
 path('rice',(24,8),[('C',(32,15),(28,8),(30,12)),('L',(41,28)),('C',(44,34),(43,31),(44,32)),('C',(38,40),(44,38),(42,40)),('L',(30,40)),('L',(18,40)),('L',(10,40)),('C',(4,34),(6,40),(4,38)),('C',(7,28),(4,32),(5,31)),('L',(16,15)),('C',(24,8),(18,12),(20,8))],True)
 path('wrap',(18,40),[('L',(18,28)),('L',(30,28)),('L',(30,40))]);join('wrap','rice')
 """)
design('road-curvy','VRECT_L','Smooth winding road',None,'Preserve the two winding road edges and distant meeting point; widen the near road coherently.',"""
 path('road',(8,44),[('C',(20,28),(24,36),(23,34)),('C',(38,4),(7,13),(20,6)),('C',(29,21),(26,12),(26,15)),('C',(36,44),(42,30),(40,35))])
 """)
# Rebalanced after the current release spacing checks.
design('deviant-art-logo','VRECT_L','Clean angular emblem',None,'Retain the angled Z-like emblem with a broader lower diagonal and crisp continuous edges.',"""
 poly('mark',(24,4),(40,4),(28,19),(40,19),(18,44),(8,44),(20,28),(8,28),closed=True)
 """)
design('apostrophe','VRECT_L','Smooth broad comma',None,'Retain the rounded head and tail; make the inner scoop broad enough to read at native size.',"""
 path('mark',(12,44),[('C',(40,17),(31,41),(40,31)),('C',(24,4),(40,7),(32,4)),('C',(8,15),(14,4),(8,8)),('C',(24,23),(8,24),(19,21)),('C',(12,44),(31,29),(22,40))],True)
 """)
design('institution','VRECT_L','Balanced flag-topped building',None,'Preserve the dome, building and pennant; keep a clear gap below the flag.',"""
 path('roof',(8,32),[('C',(24,23),(10,26),(16,23)),('C',(40,32),(32,23),(38,26)),('L',(37,32)),('L',(11,32)),('L',(8,32))],True)
 path('building',(11,32),[('L',(11,44)),('L',(37,44)),('L',(37,32))]);join('building','roof')
 path('pole',(24,23),[('L',(24,13)),('L',(24,4)),('L',(36,8)),('L',(24,13))]);join('pole','roof')
 """)
design('lgbt-gift','VRECT_L','Balanced gift bow',None,'Two mirrored bow loops retain the wrapped-gift silhouette and meet the box at its center.',"""
 path('box',(8,18),[('L',(24,18)),('L',(40,18)),('L',(40,44)),('L',(8,44)),('L',(8,18))],True)
 for j,mirror in enumerate([False,True]):
  def p(x,y):return (48-x,y) if mirror else (x,y)
  path(f'bow-{j}',p(24,18),[('C',p(12,4),p(22,10),p(16,4)),('C',p(8,8),p(9,4),p(8,5)),('C',p(24,18),p(8,15),p(16,18))],True);join(f'bow-{j}','box')
 join('bow-0','bow-1')
 """)
for n in ['module-puzzle','puzzle']:
 design(n,'VRECT_L','Smooth puzzle piece','puzzle','Keep the upper tab and two sockets; widen their spacing and give each socket one coherent curve.',"""
 path('piece',(19,16),[('L',(8,16)),('L',(8,25)),('C',(16,30),(12,25),(16,26)),('C',(8,35),(16,34),(12,35)),('L',(8,44)),('L',(20,44)),('C',(25,36),(18,40),(20,36)),('C',(30,44),(30,36),(32,40)),('L',(40,44)),('L',(40,16)),('L',(29,16)),('C',(24,4),(34,9),(30,4)),('C',(19,16),(18,4),(14,9))],True)
 """)
design('road-curvy','VRECT_L','Smooth winding road',None,'Preserve the winding road and vanishing point; broaden the outer bend coherently.',"""
 path('road',(8,44),[('C',(20,28),(24,36),(23,34)),('C',(38,4),(7,13),(20,6)),('C',(29,21),(26,12),(26,15)),('C',(40,33),(34,26),(40,27)),('C',(36,44),(40,38),(38,41))])
 """)
for n in ['t-shirt-537cb9e5','t-shirt-clothes']:
 design(n,'HRECT_L','Balanced short sleeves','shirt','Symmetric sleeves and shoulders with a shallow round neck; keep the original straight body.',"""
 path('shirt',(17,8),[('C',(31,8),(21,12),(27,12)),('L',(44,15)),('L',(39,24)),('L',(34,21)),('L',(34,40)),('L',(14,40)),('L',(14,21)),('L',(9,24)),('L',(4,15)),('L',(17,8))],True)
 """)
for n,neck,hem in [('tank-top','round','curve'),('tank-top-female','v','curve'),('tank-top-pattern','round','flat')]:
 design(n,'VRECT_L','Balanced sleeveless top','shirt','Equal shoulder straps and matched armholes; preserve the source neckline and hem character.',f"""
 commands=[('L',(20,4))]
 if '{neck}'=='round':commands += [('C',(28,4),(20,18),(28,18))]
 else:commands += [('C',(24,18),(20,10),(22,15)),('C',(28,4),(26,15),(28,10))]
 commands += [('L',(36,4)),('C',(40,20),(36,15),(36,16)),('L',(40,44))]
 if '{hem}'=='curve':commands += [('C',(8,44),(30,42),(18,42))]
 else:commands += [('L',(8,44))]
 commands += [('L',(8,20)),('C',(12,4),(12,16),(12,15))]
 path('top',(12,4),commands,True)
 """)
for n,v in [('vest',True),('vest-clothes',False)]:
 design(n,'VRECT_L','Balanced vest panels','shirt','Preserve the open vest front and neckline; paired straps and smooth armholes share exact nodes.',f"""
 commands=[('L',(20,4))]
 if {v}:commands += [('L',(24,18)),('L',(28,4))]
 else:commands += [('C',(24,14),(20,10),(21,14)),('C',(28,4),(27,14),(28,10))]
 commands += [('L',(36,4)),('C',(40,20),(36,14),(36,17)),('L',(40,42)),('L',(28,44)),('L',(24,40)),('L',(20,44)),('L',(8,42)),('L',(8,20)),('C',(12,4),(12,17),(12,14))]
 path('vest',(12,4),commands,True)
 line('seam',(24,{18 if v else 14}),(24,40));join('seam','vest')
 """)
for n in ['shield-ccabab03','sign-badge-badge']:
 design(n,'VRECT_L','Smooth shield shoulders','shield','Keep the three-point crown and curved shield base; mirror the shoulders and side scallops.',"""
 path('shield',(8,9),[('L',(12,4)),('L',(18,8)),('L',(24,4)),('L',(30,8)),('L',(36,4)),('L',(40,9)),('C',(36,17),(37,13),(36,14)),('C',(40,29),(36,21),(40,24)),('C',(24,44),(40,36),(31,41)),('C',(8,29),(17,41),(8,36)),('C',(12,17),(8,24),(12,21)),('C',(8,9),(12,14),(11,13))],True)
 """)
design('shopping-basket-shopping','HRECT_L','Clean basket rim','shopping-basket','Preserve the basket and two raised handles; remove the retraced rim and use shared attachment points.',"""
 path('basket',(4,17),[('L',(12,17)),('L',(36,17)),('L',(44,17)),('L',(38,40)),('L',(10,40)),('L',(4,17))],True)
 line('left',(12,17),(19,8));line('right',(36,17),(29,8));join('left','basket');join('right','basket')
 """)
design('shopping-bag-1b586bc1','VRECT_L','Balanced tapered shopping bag',None,'Preserve the two hanging handle ends and tapered bag; center the arch and widen the wall clearance.',"""
 path('bag',(8,44),[('L',(11,17)),('L',(16,17)),('L',(32,17)),('L',(37,17)),('L',(40,44)),('L',(8,44))],True)
 path('handle',(16,23),[('L',(16,17)),('L',(16,12)),('A',(32,12),8,8,True),('L',(32,17)),('L',(32,23))]);join('handle','bag')
 """)
for n in ['protection-helmet','safety-helmet']:
 design(n,'HRECT_L','Smooth hard hat','hard-hat','Preserve the tall crown, center reinforcement and broad brim; use matched sides and a clear brim opening.',"""
 path('crown',(7,31),[('L',(7,25)),('C',(19,8),(7,17),(13,9)),('L',(29,8)),('C',(41,25),(35,9),(41,17)),('L',(41,31))])
 path('brim',(7,31),[('L',(41,31)),('C',(44,35),(44,31),(44,32)),('C',(40,40),(44,39),(43,40)),('L',(8,40)),('C',(4,35),(5,40),(4,39)),('C',(7,31),(4,32),(4,31))],True);join('crown','brim')
 path('ridge',(19,8),[('L',(19,22)),('L',(29,22)),('L',(29,8))]);join('ridge','crown')
 """)
for n in ['tooth','tooth-fc42d854']:
 design(n,'VRECT_L','Smooth tooth crown and roots',None,'Keep the broad crown and two roots; replace angular bulges with smooth paired curves and an open root valley.',"""
 path('tooth',(24,7),[('C',(33,4),(28,6),(30,4)),('C',(40,14),(38,4),(40,8)),('C',(36,27),(40,20),(36,22)),('C',(32,44),(36,35),(37,44)),('C',(24,30),(27,44),(29,30)),('C',(16,44),(19,30),(21,44)),('C',(12,27),(11,44),(12,35)),('C',(8,14),(12,22),(8,20)),('C',(15,4),(8,8),(10,4)),('C',(24,7),(18,4),(20,6))],True)
 """)
for n in ['pen-8c7f7f5f','pen-design']:
 design(n,'SQUARE','Smooth pointed pen nib','pen-tool','Keep the teardrop nib and diagonal stem; center the slit and broaden the nib shoulders.',"""
 path('nib',(6,42),[('L',(14,18)),('C',(25,12),(17,13),(20,12)),('C',(36,23),(31,12),(36,17)),('C',(30,34),(36,28),(35,31)),('L',(6,42))],True)
 line('slit',(6,42),(24,24));join('slit','nib')
 line('stem',(33,15),(42,6));join('stem','nib')
 """)
design('pine-symbol','VRECT_L','Balanced pine silhouette',None,'Preserve the two-tier evergreen; use one mirrored axis and clean uninterrupted diagonals.',"""
 path('tree',(24,4),[('L',(36,20)),('L',(30,20)),('L',(40,38)),('L',(24,38)),('L',(8,38)),('L',(18,20)),('L',(12,20)),('L',(24,4))],True)
 line('trunk',(24,38),(24,44));join('trunk','tree')
 """)
design('pine-f98a2e8b','VRECT_L','Balanced three-tier pine',None,'Preserve all three tiers; mirrored branches join a centered trunk.',"""
 path('tree',(24,4),[('L',(34,15)),('L',(29,15)),('L',(37,27)),('L',(31,27)),('L',(40,38)),('L',(24,38)),('L',(8,38)),('L',(17,27)),('L',(11,27)),('L',(19,15)),('L',(14,15)),('L',(24,4))],True)
 line('trunk',(24,38),(24,44));join('trunk','tree')
 """)
for n in ['t-shirt-537cb9e5','t-shirt-clothes']:
 design(n,'HRECT_L','Balanced short sleeves','shirt','Matching short sleeves with horizontal cuffs, a shallow round neck and a straight body.',"""
 path('shirt',(17,8),[('C',(31,8),(21,12),(27,12)),('L',(44,14)),('L',(40,22)),('L',(32,22)),('L',(32,40)),('L',(16,40)),('L',(16,22)),('L',(8,22)),('L',(4,14)),('L',(17,8))],True)
 """)
for n in ['shield-ccabab03','sign-badge-badge']:
 design(n,'VRECT_L','Smooth shield shoulders','shield','Keep the crown and curved shield base; broaden the crown shoulders without narrowing the side scallops.',"""
 path('shield',(8,10),[('L',(12,4)),('L',(18,8)),('L',(24,4)),('L',(30,8)),('L',(36,4)),('L',(40,10)),('C',(37,19),(38,14),(37,16)),('C',(40,29),(37,23),(40,25)),('C',(24,44),(40,36),(31,41)),('C',(8,29),(17,41),(8,36)),('C',(11,19),(8,25),(11,23)),('C',(8,10),(11,16),(10,14))],True)
 """)
design('shopping-bag-1b586bc1','VRECT_L','Balanced tapered shopping bag',None,'Preserve hanging handle ends; widen the shoulders and move the hanging ends inward to maintain clear space.',"""
 path('bag',(8,44),[('L',(8,17)),('L',(17,17)),('L',(31,17)),('L',(40,17)),('L',(40,44)),('L',(8,44))],True)
 path('handle',(17,23),[('L',(17,17)),('L',(17,11)),('A',(31,11),7,7,True),('L',(31,17)),('L',(31,23))]);join('handle','bag')
 """)
for n in ['module-puzzle','puzzle']:
 design(n,'VRECT_L','Smooth puzzle piece','puzzle','Keep the upper tab and two circular sockets, with a wider bridge between the left and lower socket.',"""
 path('piece',(19,16),[('L',(8,16)),('L',(8,24)),('C',(15,29),(12,24),(15,25)),('C',(8,34),(15,33),(12,34)),('L',(8,44)),('L',(22,44)),('C',(27,36),(20,40),(22,36)),('C',(32,44),(32,36),(34,40)),('L',(40,44)),('L',(40,16)),('L',(29,16)),('C',(24,4),(34,9),(30,4)),('C',(19,16),(18,4),(14,9))],True)
 """)
design('institution','VRECT_L','Balanced flag-topped building',None,'Preserve the domed roof with a broad arch, building and clearly separated pennant.',"""
 path('roof',(8,33),[('A',(24,20),16,13,True),('A',(40,33),16,13,True),('L',(36,33)),('L',(12,33)),('L',(8,33))],True)
 path('building',(12,33),[('L',(12,44)),('L',(36,44)),('L',(36,33))]);join('building','roof')
 path('pole',(24,20),[('L',(24,12)),('L',(24,4)),('L',(35,8)),('L',(24,12))]);join('pole','roof')
 """)
# The two pine silhouettes keep their tier count with deeper, open branch steps.
design('pine-symbol','VRECT_L','Balanced pine silhouette',None,'Two distinct tiers with horizontal shoulders and a central trunk.',"""
 path('tree',(24,4),[('L',(35,20)),('L',(29,20)),('L',(40,38)),('L',(24,38)),('L',(8,38)),('L',(19,20)),('L',(13,20)),('L',(24,4))],True)
 line('trunk',(24,38),(24,44));join('trunk','tree')
 """)
# Broad stepped shoulders preserve all three tiers without narrow near-parallel wedges.
design('pine-f98a2e8b','VRECT_L','Balanced three-tier pine',None,'Three branch tiers widen progressively about a common axis and attach to a centered trunk.',"""
 path('tree',(24,4),[('L',(32,14)),('L',(27,14)),('L',(36,26)),('L',(29,26)),('L',(40,38)),('L',(24,38)),('L',(8,38)),('L',(19,26)),('L',(12,26)),('L',(21,14)),('L',(16,14)),('L',(24,4))],True)
 line('trunk',(24,38),(24,44));join('trunk','tree')
 """)
design('phone-1','SQUARE','Smooth telephone receiver','phone','Preserve the diagonal receiver; round both earpieces and use a broad continuous inner bend.',"""
 path('phone',(13,6),[('L',(20,12)),('C',(18,19),(23,15),(19,17)),('C',(29,30),(20,24),(24,28)),('C',(36,28),(32,26),(34,27)),('L',(42,35)),('C',(34,42),(42,39),(38,42)),('C',(6,14),(20,40),(6,26)),('C',(13,6),(6,10),(9,6))],True)
 """)
design('pets-allow','HRECT_L','Coherent dog silhouette',None,'Preserve the side-view dog and raised tail; balance the legs and smooth the head-to-back transition.',"""
 path('dog',(8,40),[('L',(8,24)),('C',(4,18),(5,23),(4,21)),('C',(12,23),(6,21),(8,23)),('L',(21,23)),('C',(27,12),(24,23),(24,14)),('L',(32,8)),('L',(32,13)),('L',(44,17)),('L',(42,23)),('L',(35,23)),('L',(35,40)),('L',(29,40)),('L',(27,32)),('L',(16,32)),('L',(14,40)),('L',(8,40))],True)
 """)
design('plane-1-travel','HRECT_L','Balanced side-facing airplane','plane','Preserve the horizontal plane and swept wings; mirror the wing and tail contours about the fuselage axis.',"""
 path('plane',(4,18),[('L',(10,18)),('L',(14,21)),('L',(20,21)),('L',(15,8)),('L',(20,8)),('L',(31,20)),('L',(39,20)),('C',(44,24),(42,20),(44,22)),('C',(39,28),(44,26),(42,28)),('L',(31,28)),('L',(20,40)),('L',(15,40)),('L',(20,27)),('L',(14,27)),('L',(10,30)),('L',(4,30)),('L',(7,24)),('L',(4,18))],True)
 """)
design('plane-1','HRECT_L','Smooth ascending aircraft','plane','Preserve the steep ascending silhouette and single visible wing; give the cabin nose one smooth turn.',"""
 path('plane',(4,29),[('L',(16,40)),('L',(40,20)),('C',(44,13),(42,18),(44,16)),('C',(39,8),(44,10),(42,8)),('L',(29,16)),('L',(16,12)),('L',(9,17)),('L',(23,23)),('L',(17,29)),('L',(9,25)),('L',(4,29))],True)
 """)
design('plane','HRECT_L','Smooth broad-wing aircraft','plane','Preserve the shallower ascending angle and two offset wings; use a smooth nose and clean wing roots.',"""
 path('plane',(4,25),[('L',(14,33)),('L',(23,28)),('L',(20,40)),('L',(28,36)),('L',(32,24)),('L',(40,20)),('C',(44,14),(43,18),(44,16)),('C',(37,11),(44,10),(40,9)),('L',(32,14)),('L',(19,8)),('C',(16,13),(16,8),(14,11)),('L',(22,18)),('L',(14,22)),('L',(6,20)),('L',(4,25))],True)
 """)
design('pregnancy-condom','SQUARE','Smooth condom outline',None,'Preserve the diagonal body, rolled open end and small reservoir tip; remove the lumpy cap.',"""
 path('body',(8,31),[('L',(27,12)),('C',(35,9),(30,9),(32,9)),('C',(40,6),(38,9),(38,6)),('C',(42,9),(42,6),(42,7)),('C',(39,14),(42,12),(39,12)),('C',(36,21),(39,17),(39,18)),('L',(17,40)),('L',(8,31))],True)
 line('rim',(6,29),(19,42));join('rim','body')
 """)
design('signature-sign-interface-essential','HRECT_L','Flowing signature stroke',None,'Retain the tall first loop and smaller finishing loop; smooth the reversals without changing the handwritten direction.',"""
 path('signature',(4,40),[('L',(15,14)),('C',(23,8),(18,8),(20,8)),('C',(22,24),(29,8),(25,17)),('C',(20,40),(18,33),(17,40)),('C',(31,24),(24,40),(27,24)),('C',(36,31),(37,18),(39,24)),('C',(39,40),(33,37),(36,40)),('C',(44,35),(42,40),(43,37))])
 """)
design('paintbrush-symbol','SQUARE','Smooth fine paintbrush','paintbrush','Keep the pointed handle and soft bristle head; retain the broad diagonal brush proportions.',"""
 path('handle',(18,28),[('C',(20,22),(17,25),(18,24)),('L',(38,6)),('C',(42,10),(41,6),(42,7)),('L',(28,30)),('C',(21,32),(26,33),(23,33)),('L',(18,28))],True)
 path('bristle',(18,28),[('C',(10,35),(11,26),(10,30)),('C',(6,41),(10,38),(8,40)),('C',(21,32),(15,44),(23,38)),('L',(18,28))],True);join('bristle','handle')
 """)
design('folding-pocket-knife-tools','SQUARE','Smooth folded pocket knife',None,'Preserve the open blade above a curved handle; broaden the blade at its hinge and keep the original V arrangement.',"""
 path('blade',(31,29),[('C',(10,6),(19,23),(11,15)),('C',(36,24),(21,8),(31,17)),('L',(31,29))],True)
 path('handle',(36,24),[('C',(42,30),(40,23),(42,26)),('C',(14,42),(39,37),(22,42)),('C',(11,34),(8,42),(7,36)),('C',(31,29),(20,33),(27,31)),('L',(36,24))],True);join('blade','handle')
 """)
design('institution','VRECT_L','Balanced flag-topped building',None,'Preserve the dome and building; a broad rectangular pennant keeps the small flag opening readable.',"""
 path('roof',(8,33),[('A',(24,20),16,13,True),('A',(40,33),16,13,True),('L',(36,33)),('L',(12,33)),('L',(8,33))],True)
 path('building',(12,33),[('L',(12,44)),('L',(36,44)),('L',(36,33))]);join('building','roof')
 path('flag',(24,4),[('L',(36,4)),('L',(36,12)),('L',(24,12)),('L',(24,4))],True)
 line('pole',(24,12),(24,20));join('pole','roof');join('pole','flag')
 """)
for n in ['module-puzzle','puzzle']:
 design(n,'VRECT_L','Smooth puzzle piece','puzzle','Preserve all three tab and socket features with broad bridges between them.',"""
 path('piece',(19,16),[('L',(8,16)),('L',(8,24)),('C',(14,29),(12,24),(14,25)),('C',(8,34),(14,33),(12,34)),('L',(8,44)),('L',(21,44)),('C',(26,36),(19,40),(21,36)),('C',(31,44),(31,36),(33,40)),('L',(40,44)),('L',(40,16)),('L',(29,16)),('C',(24,4),(34,9),(30,4)),('C',(19,16),(18,4),(14,9))],True)
 """)
design('pine-symbol','VRECT_L','Smooth two-tier pine',None,'Preserve two tiers; gently curved lower branches open the narrow shoulder transition.',"""
 path('tree',(24,4),[('L',(35,18)),('L',(29,18)),('C',(40,38),(29,27),(35,34)),('L',(24,38)),('L',(8,38)),('C',(19,18),(13,34),(19,27)),('L',(13,18)),('L',(24,4))],True)
 line('trunk',(24,38),(24,44));join('trunk','tree')
 """)
design('pine-f98a2e8b','VRECT_L','Smooth three-tier pine',None,'Preserve three progressively wider tiers; matching curved branches open the shoulder transitions.',"""
 path('tree',(24,4),[('L',(32,14)),('L',(27,14)),('C',(36,26),(27,20),(32,24)),('L',(29,26)),('C',(40,38),(29,32),(35,35)),('L',(24,38)),('L',(8,38)),('C',(19,26),(13,35),(19,32)),('L',(12,26)),('C',(21,14),(16,24),(21,20)),('L',(16,14)),('L',(24,4))],True)
 line('trunk',(24,38),(24,44));join('trunk','tree')
 """)
design('pets-allow','HRECT_L','Coherent dog silhouette',None,'Preserve the side-view dog; broaden the legs and muzzle opening while retaining the raised tail.',"""
 path('dog',(8,40),[('L',(8,24)),('C',(4,18),(5,23),(4,21)),('C',(12,23),(6,21),(8,23)),('L',(21,23)),('C',(27,12),(24,23),(24,14)),('L',(32,8)),('L',(32,14)),('L',(44,18)),('L',(42,26)),('L',(36,26)),('L',(36,40)),('L',(28,40)),('L',(26,31)),('L',(18,31)),('L',(16,40)),('L',(8,40))],True)
 """)
design('folding-pocket-knife-tools','SQUARE','Smooth folded pocket knife',None,'Preserve the open blade and curved handle; broaden the handle heel without changing the V arrangement.',"""
 path('blade',(31,29),[('C',(10,6),(19,23),(11,15)),('C',(36,24),(21,8),(31,17)),('L',(31,29))],True)
 path('handle',(36,24),[('C',(42,30),(40,23),(42,26)),('C',(12,42),(39,37),(20,42)),('C',(6,37),(8,42),(6,41)),('C',(12,33),(6,34),(8,33)),('C',(31,29),(20,33),(27,31)),('L',(36,24))],True);join('blade','handle')
 """)
design('pregnancy-condom','SQUARE','Smooth condom outline',None,'Preserve the diagonal sleeve and rolled rim; use a smooth reservoir shoulder instead of tiny overlapping cap segments.',"""
 path('body',(8,31),[('L',(27,12)),('C',(36,8),(31,8),(33,8)),('C',(40,6),(38,8),(38,6)),('C',(42,10),(42,6),(42,8)),('C',(36,21),(42,15),(39,18)),('L',(17,40))])
 path('rim',(6,29),[('L',(8,31)),('L',(17,40)),('L',(19,42))]);join('rim','body')
 """)
design('signature-sign-interface-essential','HRECT_L','Flowing signature stroke',None,'Retain the tall first loop and smaller finishing loop; broaden their separation without changing the handwriting direction.',"""
 path('signature',(4,40),[('L',(15,14)),('C',(23,8),(18,8),(20,8)),('C',(21,24),(29,8),(24,17)),('C',(19,40),(17,33),(16,40)),('C',(33,24),(24,40),(29,24)),('C',(37,31),(39,19),(40,24)),('C',(39,40),(34,37),(36,40)),('C',(44,35),(42,40),(43,37))])
 """)
for n in ['pen-8c7f7f5f','pen-design']:
 design(n,'SQUARE','Smooth pointed pen nib','pen-tool','Keep the teardrop nib, centered slit and diagonal stem with an exact shared shoulder node.',"""
 path('nib',(6,42),[('L',(14,18)),('C',(25,12),(17,13),(20,12)),('C',(33,15),(28,12),(31,13)),('C',(36,23),(35,17),(36,19)),('C',(30,34),(36,28),(35,31)),('L',(6,42))],True)
 line('slit',(6,42),(24,24));join('slit','nib');line('stem',(33,15),(42,6));join('stem','nib')
 """)
# Keep the source's flared hem on the sleeveless garments.
for n,neck,hem in [('tank-top','round','curve'),('tank-top-female','v','curve'),('tank-top-pattern','round','flat')]:
 design(n,'VRECT_L','Balanced sleeveless top','shirt','Equal shoulder straps and armholes; preserve the neckline and gently flared source hem.',f"""
 commands=[('L',(20,4))]
 if '{neck}'=='round':commands += [('C',(28,4),(20,18),(28,18))]
 else:commands += [('L',(24,18)),('L',(28,4))]
 commands += [('L',(36,4)),('C',(40,20),(36,15),(36,16))]
 if '{hem}'=='curve':commands += [('C',(40,42),(37,30),(38,34)),('C',(24,44),(36,44),(30,44)),('C',(8,42),(18,44),(12,44)),('C',(8,20),(10,34),(11,30))]
 else:commands += [('L',(40,44)),('L',(8,44)),('L',(8,20))]
 commands += [('C',(12,4),(12,16),(12,15))]
 path('top',(12,4),commands,True)
 """)
design('protection-helmet','HRECT_L','Smooth open-ridge hard hat','hard-hat','Keep two separate reinforcing ribs and a broad brim; preserve the open-ridge variant.',"""
 path('crown',(7,31),[('L',(7,25)),('C',(19,8),(7,17),(13,9)),('L',(29,8)),('C',(41,25),(35,9),(41,17)),('L',(41,31))])
 path('brim',(7,31),[('L',(41,31)),('C',(44,35),(44,31),(44,32)),('C',(40,40),(44,39),(43,40)),('L',(8,40)),('C',(4,35),(5,40),(4,39)),('C',(7,31),(4,32),(4,31))],True);join('crown','brim')
 for x in [19,29]:line(f'rib-{x}',(x,8),(x,22));join(f'rib-{x}','crown')
 """)
for n in ['circle-r','copyright-and-protecttion']:
 design(n,'CIRCLE','Centered registered mark',None,'A true circle encloses a compact R; the bowl, stem and leg share deliberate endpoints and clear margins.',"""
 circle('ring',24,24,20)
 path('bowl',(18,24),[('L',(18,14)),('L',(24,14)),('A',(24,24),5,5,True),('L',(18,24))],True)
 line('stem',(18,24),(18,33));line('leg',(24,24),(29,33));join('stem','bowl');join('leg','bowl')
 """)
design('billboard','SQUARE','Even freestanding board',None,'A clean rectangular board owns two equally spaced feet with exact attachment nodes.',"""
 path('board',(6,6),[('L',(42,6)),('L',(42,34)),('L',(36,34)),('L',(12,34)),('L',(6,34)),('L',(6,6))],True)
 for x in [12,36]:
  line(f'leg-{x}',(x,34),(x,42));path(f'foot-{x}',(x-4,42),[('L',(x,42)),('L',(x+4,42))]);join(f'leg-{x}','board');join(f'leg-{x}',f'foot-{x}')
 """)
design('data-lake','VRECT_L','Regular water-storage cylinder',None,'Keep the elliptical tank and two ripple bands; center every wave band and share side attachments.',"""
 self.add_arc('top-a',(8,7),(40,7),radius_x=16,radius_y=3)
 self.add_arc('top-b',(40,7),(8,7),radius_x=16,radius_y=3)
 self.add_contour('top','top-a','top-b',closed=True)
 path('body',(8,7),[('L',(8,22)),('L',(8,32)),('L',(8,40)),('A',(40,40),16,4,False),('L',(40,32)),('L',(40,22)),('L',(40,7))]);join('body','top')
 for y in [22,32]:
  commands=[]
  for j,x in enumerate([8,16,24,32]):commands.append(('C',(x+8,y),(x+2,y+(-1 if j%2 else 1)),(x+6,y+(-1 if j%2 else 1))))
  path(f'ripple-{y}',(8,y),commands);join(f'ripple-{y}','body')
 """)
for n in ['earth-89744ee7','earth-d015ebfd','earth-fad4bbe1']:
 design(n,'CIRCLE','Smooth globe and land contours',None,'Preserve the asymmetric land contours inside a true circle; split the rim at their actual attachment nodes.',"""
 path('globe',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
 path('land',(24,4),[('C',(20,15),(22,8),(20,10)),('L',(27,20)),('C',(30,33),(26,29),(26,33)),('C',(38,26),(34,33),(34,27)),('C',(44,24),(40,25),(42,24))]);join('land','globe')
 path('south',(4,24),[('C',(13,30),(9,24),(12,25)),('C',(24,44),(15,40),(18,43))]);join('south','globe')
 """)
design('file-paper-document','VRECT_L','Clean folded document',None,'A regular page with a shared folded-corner node replaces uneven and doubled corner strokes.',"""
 path('page',(8,4),[('L',(28,4)),('L',(40,16)),('L',(40,44)),('L',(8,44)),('L',(8,4))],True)
 path('fold',(28,4),[('L',(28,16)),('L',(40,16))]);join('fold','page')
 """)
design('flip','SQUARE','Clean calendar corner',None,'Keep three equal binding marks and the lifted lower corner; every attachment is explicit.',"""
 path('page',(6,10),[('L',(14,10)),('L',(24,10)),('L',(34,10)),('L',(42,10)),('L',(42,30)),('L',(30,42)),('L',(6,42)),('L',(6,10))],True)
 path('fold',(42,30),[('L',(30,30)),('L',(30,42))]);join('fold','page')
 for x in [14,24,34]:path(f'ring-{x}',(x,6),[('L',(x,10)),('L',(x,15))]);join(f'ring-{x}','page')
 """)
design('half-circle','HRECT_L','Concentric arch',None,'Matched half-circles and straight end legs preserve a constant-width arch.',"""
 path('arch',(4,40),[('L',(4,28)),('A',(44,28),20,20,True),('L',(44,40)),('L',(34,40)),('L',(34,28)),('A',(14,28),10,10,False),('L',(14,40)),('L',(4,40))],True)
 """)
design('google-photos-logo','SQUARE','Regular four-blade pinwheel',None,'Preserve the four rotating blades using equal radii and exact central attachment nodes.',"""
 for j in range(4):
  def p(x,y):
   for _ in range(j):x,y=48-y,x
   return x,y
  path(f'blade-{j}',p(24,24),[('L',p(24,6)),('A',p(24,24),9,9,True)],True)
 for j in range(4):
  for k in range(j+1,4):join(f'blade-{j}',f'blade-{k}')
 """)
design('graph-line-spline','HRECT_L','Smooth chart splines',None,'Retain two distinct flowing series above the shared chart baseline; increase separation at the right tails.',"""
 path('axis',(4,8),[('L',(4,40)),('L',(44,40))])
 path('upper',(4,25),[('C',(17,12),(10,25),(11,12)),('C',(30,20),(23,12),(24,20)),('C',(44,8),(37,20),(39,13))]);join('upper','axis')
 path('lower',(4,34),[('C',(17,26),(9,32),(13,26)),('C',(31,31),(22,26),(27,31)),('C',(44,23),(37,31),(39,28))]);join('lower','axis')
 """)
design('flame','VRECT_L','Flowing flame silhouette',None,'Preserve the large flame and curled right tip; reconstruct the outer flow with coherent curves.',"""
 path('flame',(24,4),[('C',(34,24),(34,9),(38,16)),('C',(40,20),(33,29),(38,25)),('C',(24,44),(44,37),(34,44)),('C',(8,31),(14,44),(8,38)),('C',(24,4),(8,17),(29,15))],True)
 """)
design('dragon-fruit','VRECT_L','Balanced dragon fruit',None,'Preserve the pointed crown scales and oval fruit body; mirror the main silhouette while retaining the spiky identity.',"""
 path('fruit',(8,20),[('L',(12,22)),('L',(14,10)),('L',(19,15)),('L',(24,4)),('L',(29,15)),('L',(34,10)),('L',(36,22)),('L',(40,20)),('C',(24,44),(39,36),(35,44)),('C',(8,20),(13,44),(9,36))],True)
 """)
design('explosion-sound-effect-text','SQUARE','Balanced burst silhouette',None,'Preserve the irregular explosion and baseline; use deliberate sharp points and broader connecting valleys.',"""
 path('burst',(14,42),[('L',(6,25)),('L',(16,29)),('L',(12,14)),('L',(21,22)),('L',(24,6)),('L',(29,22)),('L',(40,16)),('L',(34,30)),('L',(42,30)),('L',(28,42))])
 path('base',(10,42),[('L',(14,42)),('L',(28,42)),('L',(38,42))]);join('base','burst')
 """)
design('feather','VRECT_L','Smooth feather vane',None,'Preserve the diagonal feather and long quill; broaden the vane and keep the notch in the trailing edge.',"""
 path('vane',(12,36),[('C',(8,26),(9,33),(8,30)),('C',(38,4),(8,16),(27,7)),('C',(40,14),(40,8),(40,10)),('C',(29,27),(40,20),(33,25)),('L',(36,25)),('C',(12,36),(29,37),(19,39))],True)
 path('quill',(8,44),[('L',(12,36)),('L',(30,15))]);join('quill','vane')
 """)
for n,r,foot in [('modern-tv-curvy-edge',4,8),('modern-tv-curvy-edge-fa5afd06',6,10),('modern-tv-curvy-edge-tv',5,9)]:
 design(n,'HRECT_L','Even television frame',None,'Preserve the rounded screen and center stand; match frame corners and keep clear space above the foot.',f"""
 path('screen',(4+{r},8),[('L',(44-{r},8)),('A',(44,8+{r}),{r},{r},True),('L',(44,32-{r})),('A',(44-{r},32),{r},{r},True),('L',(24,32)),('L',(4+{r},32)),('A',(4,32-{r}),{r},{r},True),('L',(4,8+{r})),('A',(4+{r},8),{r},{r},True)],True)
 line('stand',(24,32),(24,40));path('foot',(24-{foot},40),[('L',(24,40)),('L',(24+{foot},40))]);join('stand','screen');join('stand','foot')
 """)
for n,lip in [('megaphone-6b4a53f0',38),('megaphone-9e81b14e',40),('megaphone-interface-essential',39)]:
 design(n,'HRECT_L','Flowing megaphone bell',None,'Preserve the angled bell and hanging handle; smooth the bell curves around a clear, regular neck.',f"""
 path('body',(9,22),[('L',(18,22)),('C',({lip},8),(26,20),(32,13)),('L',(44,32)),('C',(18,32),(35,29),(26,30)),('L',(14,32)),('L',(9,32)),('A',(9,22),5,5,True)],True)
 line('neck',(18,22),(18,32));join('neck','body')
 path('handle',(14,32),[('C',(21,40),(16,35),(18,40)),('L',(26,38))]);join('handle','body')
 """)
design('horn','HRECT_L','Balanced horn outline',None,'Preserve both flared ends and the U-shaped lower loop; use shared horizontal neck dimensions.',"""
 path('horn',(4,8),[('L',(14,18)),('L',(34,18)),('L',(44,8)),('L',(44,32)),('L',(34,26)),('L',(14,26)),('L',(4,32)),('L',(4,8))],True)
 path('loop',(14,26),[('L',(14,36)),('A',(18,40),4,4,False),('L',(30,40)),('A',(34,36),4,4,False),('L',(34,26))]);join('loop','horn')
 """)
design('horn-transportation','HRECT_L','Smooth bulb horn',None,'Preserve the broad bell and circular bulb; the flare attaches to shared upper and lower bulb nodes.',"""
 path('flare',(4,8),[('C',(38,18),(4,15),(22,18)),('A',(38,30),6,6,False),('C',(4,40),(22,30),(4,33)),('L',(4,8))],True)
 path('bulb',(38,18),[('A',(38,30),6,6,True),('A',(38,18),6,6,True)],True);join('flare','bulb')
 """)
design('headphones-90ffd8be','HRECT_L','Balanced headphones',None,'A true circular headband and matched ear pads share their exact side-wall nodes.',"""
 path('band',(12,40),[('L',(12,38)),('L',(12,26)),('L',(12,20)),('A',(36,20),12,12,True),('L',(36,26)),('L',(36,38)),('L',(36,40))])
 path('left',(12,26),[('A',(12,38),8,6,False)]);path('right',(36,26),[('A',(36,38),8,6,True)]);join('left','band');join('right','band')
 """)
design('mobile-phone-control-play','VRECT_L','Balanced phone and play mark',None,'Keep the inset play triangle and lower phone band; ensure the triangle opening and margins remain clear.',"""
 path('phone',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(40,35)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,35)),('L',(8,8)),('A',(12,4),4,4,True)],True)
 line('band',(8,35),(40,35));join('band','phone');poly('play',(18,13),(30,19),(18,25),closed=True)
 """)
design('microphone-karaoke','VRECT_L','Smooth microphone and cable',None,'Preserve the diagonal circular microphone, tapered handle and curling cable; share actual head attachments.',"""
 path('head',(18,15),[('A',(29,4),11,11,True),('A',(40,15),11,11,True),('A',(29,26),11,11,True),('A',(18,15),11,11,True)],True)
 path('handle',(18,15),[('L',(8,32)),('C',(12,38),(6,35),(8,38)),('L',(29,26))]);join('handle','head')
 path('cable',(12,38),[('C',(12,44),(5,38),(5,44)),('L',(28,44))]);join('cable','handle')
 """)
for n in ['navigation-left-3a696d74','navigation-left-6136ac07']:
 design(n,'HRECT_L','Flowing left turn',None,'Preserve the open curved arrow and long right-hand tail; smooth the bend and center the arrow point.',"""
 path('curve',(4,24),[('C',(25,16),(12,19),(17,16)),('C',(44,40),(39,16),(44,27))])
 path('head',(14,8),[('L',(4,24)),('L',(18,31))]);join('head','curve')
 """)
design('phone-box-symbol','VRECT_L','Balanced telephone kiosk',None,'Keep the domed roof, window divider and projecting base; all joins share exact nodes.',"""
 path('roof',(8,13),[('A',(40,13),16,9,True),('L',(8,13))],True)
 path('body',(10,13),[('L',(10,29)),('L',(10,44)),('L',(38,44)),('L',(38,29)),('L',(38,13))]);join('body','roof')
 line('sill',(10,29),(38,29));join('sill','body');path('base',(8,44),[('L',(10,44)),('L',(38,44)),('L',(40,44))]);join('base','body')
 """)
design('one-chilli','HRECT_L','Smooth curved chilli',None,'Preserve the bent pepper with a raised stem; use a flowing taper and rounded shoulder.',"""
 path('pepper',(4,29),[('C',(32,17),(16,34),(24,23)),('C',(40,19),(35,12),(40,15)),('C',(18,40),(45,29),(33,40)),('C',(4,29),(11,40),(6,35))],True)
 path('stem',(40,19),[('C',(44,8),(43,17),(44,13))]);join('stem','pepper')
 """)
design('horn-transportation','HRECT_L','Smooth bulb horn',None,'Preserve the flare and round bulb; their shared inner rim is drawn once.',"""
 path('flare',(4,8),[('C',(38,18),(4,15),(22,18)),('A',(38,30),6,6,False),('C',(4,40),(22,30),(4,33)),('L',(4,8))],True)
 path('bulb',(38,18),[('A',(38,30),6,6,True)]);join('flare','bulb')
 """)
design('phone-box-symbol','VRECT_L','Balanced telephone kiosk',None,'A broad domed roof, level window sill and projecting base share exact side-wall nodes.',"""
 path('roof',(8,13),[('A',(40,13),16,9,True),('L',(38,13)),('L',(10,13)),('L',(8,13))],True)
 for x in [10,38]:path(f'wall-{x}',(x,13),[('L',(x,29)),('L',(x,44))]);join(f'wall-{x}','roof')
 path('base',(8,44),[('L',(10,44)),('L',(38,44)),('L',(40,44))]);line('sill',(10,29),(38,29))
 for x in [10,38]:join(f'wall-{x}','sill');join(f'wall-{x}','base')
 """)
design('microphone-karaoke','VRECT_L','Smooth microphone and cable',None,'Preserve the diagonal circular microphone, broad handle and cable curl, using shared head attachments.',"""
 path('head',(18,15),[('A',(29,4),11,11,True),('A',(40,15),11,11,True),('A',(29,26),11,11,True),('A',(18,15),11,11,True)],True)
 path('handle',(18,15),[('L',(8,32)),('C',(12,38),(8,35),(8,38)),('L',(29,26))]);join('handle','head')
 path('cable',(12,38),[('C',(12,44),(8,38),(8,44)),('L',(28,44))]);join('cable','handle')
 """)
design('plane-1-travel','HRECT_L','Balanced side-facing airplane','plane','Keep the horizontal plane with broad swept wings and a distinct tail; widen the fuselage and wing interiors.',"""
 path('plane',(4,14),[('L',(16,20)),('L',(20,20)),('L',(14,8)),('L',(23,8)),('L',(27,20)),('L',(39,20)),('C',(44,24),(42,20),(44,22)),('C',(39,28),(44,26),(42,28)),('L',(27,28)),('L',(23,40)),('L',(14,40)),('L',(20,28)),('L',(16,28)),('L',(4,34)),('L',(8,24)),('L',(4,14))],True)
 """)
for n in ['circle-r','copyright-and-protecttion']:
 design(n,'CIRCLE','Centered registered mark',None,'Keep the R inside a true circle; widen its diagonal leg angle to avoid a pinched lower counter.',"""
 circle('ring',24,24,20)
 path('bowl',(18,24),[('L',(18,14)),('L',(24,14)),('A',(24,24),5,5,True),('L',(18,24))],True)
 line('stem',(18,24),(18,33));line('leg',(24,24),(31,32));join('stem','bowl');join('leg','bowl')
 """)
design('flame','VRECT_L','Flowing flame silhouette',None,'Keep the flame curl and lifted right tip; coherent curves preserve the original asymmetric fire shape.',"""
 path('flame',(24,4),[('C',(31,26),(34,9),(35,18)),('C',(38,22),(29,34),(36,29)),('C',(40,30),(39,25),(40,27)),('C',(24,44),(40,40),(33,44)),('C',(8,31),(14,44),(8,38)),('C',(24,4),(8,17),(29,15))],True)
 """)
for n in ['ship','ship-transportation']:
 design(n,'HRECT_L','Smooth sailboat and waves',None,'Preserve the curved sail and wave-shaped hull; draw the shared waterline once and attach the sail at exact deck nodes.',"""
 path('hull',(10,28),[('L',(18,28)),('L',(25,28)),('L',(38,28)),('L',(36,36)),('C',(24,40),(32,36),(28,40)),('C',(12,36),(20,40),(16,36)),('L',(10,28))],True)
 path('sail',(18,28),[('C',(18,8),(22,19),(20,12)),('C',(36,20),(28,8),(34,14)),('L',(25,28))]);join('sail','hull')
 path('wave-left',(4,40),[('C',(12,36),(8,40),(8,36))]);path('wave-right',(36,36),[('C',(44,40),(40,36),(40,40))]);join('wave-left','hull');join('wave-right','hull')
 """)
for n,cargo,cabtop,front in [('shipment',25,17,38),('shipment-delivery',25,17,38),('shipment-shipping',26,16,39),('truck',25,17,38),('truck-1',26,16,39),('truck-style',24,18,37),('truck-transportation',25,18,38)]:
 design(n,'HRECT_L','Balanced delivery truck','truck','Preserve the cargo box and stepped cab with full round wheels; clear the wheel space and omit the cramped small window stroke.',f"""
 rear={11 if cargo==24 else 12};front={front};r=5
 path('body',(4,8),[('L',({cargo},8)),('L',({cargo},{cabtop})),('L',(37,{cabtop})),('L',(44,27)),('L',(44,35)),('L',(front+r,35)),('A',(front-r,35),r,r,True),('L',({cargo},35)),('L',(rear+r,35)),('A',(rear-r,35),r,r,True),('L',(4,35)),('L',(4,8))],True)
 for name,cx in [('rear',rear),('front',front)]:path(name,(cx-r,35),[('A',(cx+r,35),r,r,True)]);join(name,'body')
 line('cargo',({cargo},{cabtop}),({cargo},35));join('cargo','body')
 """)
design('shape-cylinder','VRECT_L','Regular cylinder',None,'Preserve the tall cylinder; matching elliptical top and lower rim use exact side attachments.',"""
 path('top',(8,9),[('A',(40,9),16,5,True),('A',(8,9),16,5,True)],True)
 path('body',(8,9),[('L',(8,39)),('A',(40,39),16,5,False),('L',(40,9))]);join('body','top')
 """)
design('shop-4c6a59d7','HRECT_L','Regular shop awning',None,'Keep four awning scallops and the centered doorway; repeated lobes share exact wall attachments.',"""
 path('awning',(4,18),[('L',(8,8)),('L',(40,8)),('L',(44,18)),('C',(34,22),(44,24),(37,26)),('C',(24,22),(32,26),(26,26)),('C',(14,22),(22,26),(16,26)),('C',(4,18),(11,26),(4,24))],True)
 path('walls',(9,25),[('L',(9,40)),('L',(19,40)),('L',(29,40)),('L',(39,40)),('L',(39,25))]);join('walls','awning')
 path('door',(19,40),[('L',(19,31)),('L',(29,31)),('L',(29,40))]);join('door','walls')
 """)
design('small-office-building','HRECT_L','Balanced office entrance',None,'Keep the broad roof, two walls and arched doorway; every base and roof connection uses shared nodes.',"""
 path('roof',(4,8),[('L',(44,8)),('L',(44,18)),('L',(40,18)),('L',(8,18)),('L',(4,18)),('L',(4,8))],True)
 path('base',(4,40),[('L',(8,40)),('L',(18,40)),('L',(30,40)),('L',(40,40)),('L',(44,40))])
 for x in [8,40]:line(f'wall-{x}',(x,18),(x,40));join(f'wall-{x}','roof');join(f'wall-{x}','base')
 path('door',(18,40),[('L',(18,31)),('A',(30,31),6,6,True),('L',(30,40))]);join('door','base')
 """)
design('stethoscope','SQUARE','Smooth stethoscope loops',None,'Preserve the forked ear tubes, hanging hose and circular chestpiece; align both loops and share their junction.',"""
 path('ears',(11,6),[('L',(6,8)),('L',(6,17)),('A',(16,27),10,10,False),('A',(26,17),10,10,False),('L',(26,8)),('L',(21,6))])
 path('hose',(16,27),[('L',(16,30)),('A',(38,30),11,12,False),('L',(38,19))]);join('hose','ears')
 circle('bell',38,15,4);join('bell','hose')
 """)
design('text-strike-through','SQUARE','Smooth strikethrough S',None,'Preserve the S and central strike; a coherent letter curve crosses the shared line at a defined midpoint.',"""
 path('letter',(33,14),[('C',(23,6),(33,8),(29,6)),('C',(15,15),(17,6),(15,9)),('C',(24,24),(15,20),(19,23)),('C',(33,33),(30,26),(33,28)),('C',(23,42),(33,39),(29,42)),('C',(14,34),(17,42),(14,39))])
 path('strike',(6,24),[('L',(24,24)),('L',(42,24))]);join('strike','letter')
 """)
design('slab-serif-text-character','VRECT_L','Regular slab-serif M',None,'Preserve the broad M with four serif ends; consolidate the shared vertical stems and serif junctions.',"""
 path('left',(8,4),[('L',(13,4)),('L',(13,44))]);path('right',(40,4),[('L',(35,4)),('L',(35,44))])
 path('middle',(13,4),[('L',(24,30)),('L',(35,4))]);join('middle','left');join('middle','right')
 for name,x in [('left',13),('right',35)]:path(f'base-{name}',(x-4,44),[('L',(x,44)),('L',(x+4,44))]);join(f'base-{name}',name)
 """)
design('symbol-armor','HRECT_L','Smooth armored vehicle',None,'Preserve the low armored body, trapezoid turret and forward barrel; use one shared turret attachment.',"""
 path('body',(13,20),[('L',(35,20)),('C',(44,30),(41,20),(44,24)),('C',(35,40),(44,36),(41,40)),('L',(13,40)),('C',(4,30),(7,40),(4,36)),('C',(13,20),(4,24),(7,20))],True)
 path('turret',(12,20),[('L',(15,8)),('L',(29,8)),('L',(32,14)),('L',(33,20))]);join('turret','body');line('barrel',(32,14),(44,14));join('barrel','turret')
 """)
design('shop-4c6a59d7','HRECT_L','Regular shop awning',None,'Four equal elliptical scallops and a centered doorway preserve the storefront with clear headroom.',"""
 path('awning',(4,18),[('L',(8,8)),('L',(40,8)),('L',(44,18)),('A',(39,22),5,4,True),('A',(34,18),5,4,True),('A',(24,18),5,4,True),('A',(14,18),5,4,True),('A',(9,22),5,4,True),('A',(4,18),5,4,True)],True)
 path('walls',(9,22),[('L',(9,40)),('L',(19,40)),('L',(29,40)),('L',(39,40)),('L',(39,22))]);join('walls','awning')
 path('door',(19,40),[('L',(19,31)),('L',(29,31)),('L',(29,40))]);join('door','walls')
 """)
design('symbol-armor','HRECT_L','Smooth armored vehicle',None,'Preserve the low rounded body, trapezoid turret and forward barrel with exact shared attachments.',"""
 path('body',(13,20),[('L',(33,20)),('L',(35,20)),('C',(44,30),(41,20),(44,24)),('C',(35,40),(44,36),(41,40)),('L',(13,40)),('C',(4,30),(7,40),(4,36)),('C',(13,20),(4,24),(7,20))],True)
 path('turret',(13,20),[('L',(15,8)),('L',(29,8)),('L',(32,14)),('L',(33,20))]);join('turret','body');line('barrel',(32,14),(44,14));join('barrel','turret')
 """)
design('stethoscope','SQUARE','Smooth stethoscope loops',None,'Preserve the forked ear tubes, hanging hose and circular chestpiece; the hose meets an exact circle endpoint.',"""
 path('ears',(11,6),[('L',(6,8)),('L',(6,17)),('A',(16,27),10,10,False),('A',(26,17),10,10,False),('L',(26,8)),('L',(21,6))])
 path('hose',(16,27),[('L',(16,30)),('A',(38,30),11,12,False),('L',(38,19))]);join('hose','ears')
 path('bell',(38,19),[('A',(34,15),4,4,True),('A',(38,11),4,4,True),('A',(42,15),4,4,True),('A',(38,19),4,4,True)],True);join('bell','hose')
 """)
for n,cargo,cabtop,front in [('shipment',25,17,38),('shipment-delivery',25,17,38),('shipment-shipping',26,16,39),('truck',25,17,38),('truck-1',26,16,39),('truck-style',24,18,37),('truck-transportation',25,18,38)]:
 design(n,'HRECT_L','Balanced delivery truck','truck','Preserve cargo and cab proportions with full round wheels; curve the body shoulders into the wheel junctions.',f"""
 rear={11 if cargo==24 else 12};front={front};r=5
 path('body',(4,8),[('L',({cargo},8)),('L',({cargo},{cabtop})),('L',(37,{cabtop})),('L',(44,26)),('C',(front+r,35),(44,30),(front+r,32)),('A',(front-r,35),r,r,True),('L',({cargo},35)),('L',(rear+r,35)),('A',(rear-r,35),r,r,True),('C',(4,24),(rear-r,31),(4,29)),('L',(4,8))],True)
 for name,cx in [('rear',rear),('front',front)]:path(name,(cx-r,35),[('A',(cx+r,35),r,r,True)]);join(name,'body')
 line('cargo',({cargo},{cabtop}),({cargo},35));join('cargo','body')
 """)
design('phone-box-symbol','VRECT_L','Balanced telephone kiosk',None,'A smooth domed roof and level window sill share exact side-wall nodes, with clear room inside the dome.',"""
 path('roof',(8,16),[('A',(40,16),16,12,True),('L',(38,16)),('L',(10,16)),('L',(8,16))],True)
 for x in [10,38]:path(f'wall-{x}',(x,16),[('L',(x,29)),('L',(x,44))]);join(f'wall-{x}','roof')
 path('base',(8,44),[('L',(10,44)),('L',(38,44)),('L',(40,44))]);line('sill',(10,29),(38,29))
 for x in [10,38]:join(f'wall-{x}','sill');join(f'wall-{x}','base')
 """)
design('small-office-building','HRECT_L','Balanced office entrance',None,'Preserve the roof and arched doorway with a clear band above the arch and exact shared wall nodes.',"""
 path('roof',(4,8),[('L',(44,8)),('L',(44,18)),('L',(40,18)),('L',(8,18)),('L',(4,18)),('L',(4,8))],True)
 path('base',(4,40),[('L',(8,40)),('L',(18,40)),('L',(30,40)),('L',(40,40)),('L',(44,40))])
 for x in [8,40]:line(f'wall-{x}',(x,18),(x,40));join(f'wall-{x}','roof');join(f'wall-{x}','base')
 path('door',(18,40),[('L',(18,33)),('A',(30,33),6,6,True),('L',(30,40))]);join('door','base')
 """)
design('symbol-armor','HRECT_L','Smooth armored vehicle',None,'Preserve the low rounded body and turret; raise the barrel slightly for a clear gap above the hull.',"""
 path('body',(13,20),[('L',(33,20)),('L',(35,20)),('C',(44,30),(41,20),(44,24)),('C',(35,40),(44,36),(41,40)),('L',(13,40)),('C',(4,30),(7,40),(4,36)),('C',(13,20),(4,24),(7,20))],True)
 path('turret',(13,20),[('L',(15,8)),('L',(29,8)),('L',(32,12)),('L',(33,20))]);join('turret','body');line('barrel',(32,12),(44,12));join('barrel','turret')
 """)
design('two-pronged-fork-knife','VRECT_L','Clean fork and knife',None,'Preserve the two utensils; split the knife blade and handle at their real join and center the fork stem.',"""
 path('blade',(8,4),[('C',(16,25),(14,9),(16,18)),('L',(8,25)),('L',(8,4))],True)
 line('knife-handle',(8,25),(8,44));join('knife-handle','blade')
 path('fork',(28,4),[('L',(28,14)),('A',(34,20),6,6,False),('A',(40,14),6,6,False),('L',(40,4))]);line('fork-handle',(34,20),(34,44));join('fork-handle','fork')
 """)
design('vaccine-bottle','VRECT_L','Smooth vaccine vial',None,'Preserve the neck, broad bottle and liquid surface; use matching shoulders and a coherent waterline.',"""
 path('bottle',(18,4),[('L',(18,10)),('C',(8,18),(12,12),(8,13)),('L',(8,24)),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,24)),('L',(40,18)),('C',(30,10),(40,13),(36,12)),('L',(30,4))])
 path('cap',(14,4),[('L',(18,4)),('L',(30,4)),('L',(34,4))]);join('cap','bottle')
 path('liquid',(8,24),[('C',(24,24),(14,21),(18,21)),('C',(40,24),(30,27),(34,27))]);join('liquid','bottle')
 """)
design('virtual-shopping','VRECT_L','Balanced shopping carrier',None,'Preserve the tapered carrier and long inset handle; keep equal clear space beside both handle ends.',"""
 path('bag',(10,17),[('L',(19,17)),('L',(29,17)),('L',(38,17)),('L',(40,44)),('L',(8,44)),('L',(10,17))],True)
 path('handle',(19,23),[('L',(19,17)),('L',(19,9)),('A',(29,9),5,5,True),('L',(29,17)),('L',(29,23))]);join('handle','bag')
 """)
design('vip-crown-queen','HRECT_L','Balanced queen crown',None,'Preserve the three-point crown and curved band; mirror the peaks and use matching elliptical band halves.',"""
 path('crown',(4,16),[('L',(16,20)),('L',(24,8)),('L',(32,20)),('L',(44,16)),('L',(40,34)),('A',(8,34),16,6,True),('L',(4,16))],True)
 path('band',(8,34),[('A',(40,34),16,6,True)]);join('band','crown')
 """)
for n in ['wheat','wheat-farming']:
 design(n,'VRECT_L','Balanced wheat sprig',None,'Preserve the single grain head and two broad leaves; share the central stem and mirror the leaf shapes.',"""
 path('grain',(24,4),[('C',(32,12),(28,7),(32,7)),('C',(24,20),(32,17),(28,19)),('C',(16,12),(20,19),(16,17)),('C',(24,4),(16,7),(20,7))],True)
 path('stem',(24,20),[('L',(24,34)),('L',(24,44))]);join('stem','grain')
 path('left',(24,34),[('C',(8,22),(22,25),(14,22)),('C',(24,34),(8,31),(16,34))],True)
 path('right',(24,34),[('C',(40,22),(26,25),(34,22)),('C',(24,34),(40,31),(32,34))],True)
 join('left','stem');join('right','stem');join('left','right')
 """)
design('warp-rise','SQUARE','Even rising wave bands',None,'Preserve the rising three-line ribbon; repeat the same curve with equal offsets for consistent spacing.',"""
 path('ribbon',(6,18),[('C',(42,6),(21,18),(27,6)),('L',(42,18)),('L',(42,30)),('C',(6,42),(27,30),(21,42)),('L',(6,30)),('L',(6,18))],True)
 path('middle',(6,30),[('C',(42,18),(21,30),(27,18))]);join('middle','ribbon')
 """)
design('wattpad-logo','HRECT_L','Regular outlined W',None,'Preserve the three upright bars and rounded lower-left return; use consistent slot and stem widths.',"""
 path('mark',(4,8),[('L',(12,8)),('L',(12,28)),('A',(14,30),2,2,False),('L',(20,30)),('L',(20,8)),('L',(28,8)),('L',(28,30)),('L',(36,30)),('L',(36,8)),('L',(44,8)),('L',(44,40)),('L',(16,40)),('A',(4,28),12,12,True),('L',(4,8))],True)
 """)
for n,smile in [('happiness-emotions',True),('ptsd-disorder-symptoms',False)]:
 design(n,'VRECT_L','Smooth human profile',None,'Human reference: icon_set/references/human_ref/user.svg and full_body_ref.png. Preserve the continuous neck and profile, with a circular skull and the identifying inner mark.',f"""
 path('profile',(15,44),[('L',(15,35)),('C',(8,20),(10,29),(8,26)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,26)),('L',(35,26)),('L',(35,30)),('C',(29,37),(35,35),(33,37)),('L',(29,44))])
 """+("path('smile',(27,26),[('C',(35,30),(27,31),(31,33))]);join('smile','profile')" if smile else "path('crack',(24,4),[('L',(18,14)),('L',(24,21))]);join('crack','profile')"))
for n in ['thumb','thumb-symbol']:
 design(n,'VRECT_L','Smooth thumbs-up silhouette',None,'Human reference: icon_set/references/human_ref/full_body_ref.png. Preserve the raised thumb and broad hand with a rounded, clearly separated thumb.',"""
 path('hand',(8,23),[('C',(17,18),(12,23),(16,21)),('C',(22,4),(18,14),(18,4)),('C',(31,9),(28,4),(31,5)),('L',(29,21)),('L',(36,22)),('C',(40,26),(40,22),(40,24)),('L',(36,40)),('C',(30,44),(35,43),(33,44)),('L',(19,44)),('C',(13,40),(16,44),(16,40)),('L',(8,40)),('L',(8,23))],True)
 """)
design('thumbs-up-5680cb28','SQUARE','Balanced thumbs-up hand',None,'Human reference: icon_set/references/human_ref/full_body_ref.png. Keep the upright thumb, cuff and broad folded-finger silhouette; smooth the cramped finger bumps.',"""
 path('hand',(6,23),[('C',(17,17),(13,23),(16,20)),('C',(22,6),(18,12),(18,6)),('C',(31,11),(28,6),(31,7)),('L',(29,22)),('L',(37,22)),('C',(42,27),(41,22),(42,24)),('C',(38,39),(42,31),(40,36)),('C',(32,42),(36,42),(34,42)),('L',(20,42)),('C',(12,39),(16,42),(16,39)),('L',(6,39)),('L',(6,23))],True)
 """)
design('multiple-neutral-1','HRECT_L','Balanced two-person group',None,'Human references: user.svg and full_body_ref.png. Two circular heads and open shoulders preserve the group; each detached head has exactly four units of visible clearance to its own shoulder.',"""
 circle('front-head',14,15,7);circle('back-head',36,15,6)
 path('front-body',(4,40),[('L',(4,36)),('C',(14,30),(4,32),(10,30)),('C',(26,36),(20,30),(26,32)),('L',(26,40))])
 path('back-body',(36,29),[('C',(44,35),(40,29),(44,32)),('L',(44,40)),('L',(36,40))])
 """)
design('hand-down-1','HRECT_L','Flowing pointing hand',None,'Human reference: full_body_ref.png. Preserve the downward diagonal finger, tucked thumb and open wrist with smooth, coherent curves.',"""
 path('hand',(35,8),[('C',(23,12),(31,11),(27,12)),('C',(4,23),(17,12),(8,18)),('C',(17,22),(4,28),(11,24)),('L',(10,33)),('C',(15,40),(7,38),(10,40)),('L',(22,40)),('C',(28,35),(25,40),(26,37)),('L',(44,16))])
 """)
design('arm-flex','VRECT_L','Smooth flexed arm',None,'Human reference: full_body_ref.png. Preserve the bent arm and curled fist; keep broad muscle curves and a clear inner forearm.',"""
 path('arm',(40,44),[('L',(12,44)),('C',(8,38),(8,44),(8,41)),('L',(11,17)),('C',(18,11),(12,14),(15,13)),('L',(29,4)),('C',(35,12),(32,6),(35,9)),('C',(24,20),(35,17),(29,20)),('L',(19,21)),('L',(19,31)),('C',(35,31),(25,25),(30,26)),('C',(40,29),(38,28),(39,29))])
 """)
design('imessage-logo','HRECT_L','Smooth speech bubble',None,'Preserve the broad oval bubble and lower-left tail; use coherent arcs and a clear tail join.',"""
 path('bubble',(12,33),[('C',(4,23),(7,30),(4,28)),('C',(24,8),(4,13),(14,8)),('C',(44,23),(34,8),(44,13)),('C',(24,36),(44,32),(34,36)),('L',(18,35)),('C',(8,40),(15,38),(11,40)),('L',(12,33))],True)
 """)
design('pouch','VRECT_L','Smooth drawstring pouch',None,'Preserve the gathered neck and rounded bag; mirror the shoulders and separate the drawstring ends.',"""
 path('bag',(18,14),[('L',(14,4)),('L',(34,4)),('L',(30,14)),('C',(40,34),(36,19),(40,25)),('C',(30,44),(40,41),(37,44)),('L',(18,44)),('C',(8,34),(11,44),(8,41)),('C',(18,14),(8,25),(12,19))],True)
 path('tie',(18,14),[('L',(24,14)),('L',(30,14))]);join('tie','bag')
 line('left-tie',(18,14),(17,22));line('right-tie',(30,14),(31,22));join('left-tie','bag');join('right-tie','bag')
 """)
design('pile-poo','SQUARE','Smooth stacked swirl',None,'Preserve the three-tier swirl and curled top; share each stacked edge rather than retracing it.',"""
 path('base',(13,29),[('L',(35,29)),('A',(35,42),7,7,True),('L',(13,42)),('A',(13,29),7,7,True)],True)
 path('middle',(13,29),[('C',(12,23),(9,28),(9,25)),('C',(19,20),(13,20),(15,20)),('L',(30,20)),('C',(35,29),(36,20),(39,26))]);join('middle','base')
 path('top',(19,20),[('C',(24,6),(19,15),(29,14)),('C',(33,15),(29,7),(33,10)),('C',(30,20),(33,18),(31,20))]);join('top','middle')
 """)
design('rain-umbrella','SQUARE','Balanced umbrella canopy',None,'Preserve three canopy scallops and the hooked handle; use mirrored canopy arcs with an exact center attachment.',"""
 path('canopy',(6,24),[('C',(24,8),(9,14),(16,8)),('C',(42,24),(32,8),(39,14)),('C',(30,24),(38,20),(34,20)),('C',(24,24),(28,20),(26,20)),('C',(18,24),(22,20),(20,20)),('C',(6,24),(14,20),(10,20))],True)
 path('handle',(24,24),[('L',(24,37)),('A',(14,37),5,5,True)]);join('handle','canopy');line('tip',(24,6),(24,8));join('tip','canopy')
 """)
design('shopping-bag-side','VRECT_L','Regular side-gusset bag',None,'Preserve the asymmetric side panel and arched handle; keep the side seam clear of the handle.',"""
 path('bag',(8,44),[('L',(11,14)),('L',(15,14)),('L',(31,14)),('L',(36,14)),('L',(40,44)),('L',(30,44)),('L',(8,44))],True)
 path('handle',(15,14),[('L',(17,7)),('C',(28,7),(20,3),(26,4)),('L',(31,14))]);join('handle','bag')
 line('gusset',(31,14),(30,44));join('gusset','bag')
 """)
design('time-stopwatch-half','VRECT_L','Regular split stopwatch',None,'Preserve the circular case, vertical half divider and two top controls; split every actual attachment point.',"""
 path('case',(24,12),[('A',(40,28),16,16,True),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('A',(24,12),16,16,True)],True)
 line('divider',(24,12),(24,44));join('divider','case');line('stem',(24,4),(24,12));join('stem','case')
 path('button',(19,4),[('L',(24,4)),('L',(29,4))]);join('button','stem')
 line('side',(35,16),(39,12));join('side','case')
 """)
design('trekking-shelter','SQUARE','Balanced open shelter',None,'Preserve the peaked shelter and inner A frame; align their central axes and shared base points.',"""
 path('frame',(6,24),[('L',(24,6)),('L',(42,24)),('L',(42,42)),('L',(34,42)),('L',(14,42)),('L',(6,42)),('L',(6,24))],True)
 path('inside',(14,42),[('L',(24,22)),('L',(34,42))]);join('inside','frame')
 """)
for n,is_circle in [('actions-authentication-square-circle',True),('actions-authentication-squares',False)]:
 design(n,'SQUARE','Clean routed connection',None,'Preserve the two endpoint types and S-shaped route; use coherent semicircular turns and clear node spacing.',f"""
 if {is_circle}:circle('start',12,12,6)
 else:path('start',(6,6),[('L',(18,6)),('L',(18,12)),('L',(18,18)),('L',(6,18)),('L',(6,6))],True)
 path('end',(32,32),[('L',(42,32)),('L',(42,42)),('L',(32,42)),('L',(32,36)),('L',(32,32))],True)
 path('route',(18,12),[('L',(32,12)),('A',(32,24),6,6,True),('L',(21,24)),('A',(21,36),6,6,False),('L',(32,36))]);join('route','start');join('route','end')
 """)
design('arrange-letter','VRECT_L','Clear A-to-Z sorting mark',None,'Preserve the downward arrow and A/Z letters; enlarge the A counter and share its crossbar nodes.',"""
 line('arrow',(13,10),(13,35));path('head',(8,29),[('L',(13,35)),('L',(18,29))]);join('arrow','head')
 path('a',(26,18),[('L',(28,14)),('L',(33,4)),('L',(38,14)),('L',(40,18))]);line('bar',(28,14),(38,14));join('bar','a')
 poly('z',(26,29),(40,29),(26,44),(40,44))
 """)
design('arrange-number','VRECT_L','Clear numeric sorting mark',None,'Preserve the downward arrow and 1/9 digits; use a true circular counter and a clear diagonal tail.',"""
 line('arrow',(13,10),(13,35));path('head',(8,29),[('L',(13,35)),('L',(18,29))]);join('arrow','head')
 poly('one',(29,7),(33,4),(33,19))
 circle('nine-loop',36,30,4);line('nine-tail',(40,30),(29,44));join('nine-loop','nine-tail')
 """)
design('br','HRECT_L','Regular Br lettering',None,'Preserve the capital B and lowercase r; use broad rounded bowls and an explicitly joined shoulder.',"""
 path('upper-b',(4,24),[('L',(4,8)),('L',(12,8)),('C',(20,16),(18,8),(20,11)),('C',(12,24),(20,21),(18,24)),('L',(4,24))],True)
 path('lower-b',(4,24),[('L',(4,40)),('L',(12,40)),('C',(22,32),(18,40),(22,37)),('C',(12,24),(22,27),(18,24))]);join('lower-b','upper-b')
 path('r-stem',(32,18),[('L',(32,22)),('L',(32,40))]);path('r-shoulder',(32,22),[('C',(44,20),(35,16),(42,16))]);join('r-stem','r-shoulder')
 """)
design('bitcoin','VRECT_L','Regular Bitcoin letterform',None,'Preserve the double vertical bars, serifs and two B bowls; share all crossing nodes and equalize the counter widths.',"""
 path('upper',(16,9),[('L',(24,9)),('L',(28,9)),('C',(40,17),(36,9),(40,12)),('C',(28,25),(40,22),(36,25)),('L',(24,25)),('L',(16,25)),('L',(16,9))],True)
 path('lower',(16,25),[('L',(16,41)),('L',(24,41)),('L',(28,41)),('C',(40,33),(36,41),(40,38)),('C',(28,25),(40,28),(36,25))]);join('lower','upper')
 for name,y in [('top',9),('bottom',41)]:line(name,(8,y),(16,y));join(name,'upper' if y==9 else 'lower')
 line('left-top',(16,4),(16,9));line('left-bottom',(16,41),(16,44));join('left-top','upper');join('left-bottom','lower')
 path('right',(24,4),[('L',(24,9)),('L',(24,25)),('L',(24,41)),('L',(24,44))]);join('right','upper');join('right','lower')
 """)
design('time-stopwatch-half','VRECT_L','Regular split stopwatch',None,'A true circular case is optically shifted one unit left to balance the side button. The divider and controls meet exact circle nodes.',"""
 path('case',(23,14),[('A',(35,20),15,15,True),('A',(38,29),15,15,True),('A',(23,44),15,15,True),('A',(8,29),15,15,True),('A',(23,14),15,15,True)],True)
 line('divider',(23,14),(23,44));join('divider','case');line('stem',(23,4),(23,14));join('stem','case')
 path('button',(18,4),[('L',(23,4)),('L',(28,4))]);join('button','stem');line('side',(35,20),(40,15));join('side','case')
 """)
design('pile-poo','SQUARE','Smooth stacked swirl',None,'Preserve the three-tier swirl and curled top; use a broad rounded base and draw each shared edge once.',"""
 path('base',(13,28),[('L',(35,28)),('A',(35,42),7,7,True),('L',(13,42)),('A',(13,28),7,7,True)],True)
 path('middle',(13,28),[('C',(12,22),(9,27),(9,24)),('C',(19,18),(13,18),(15,18)),('L',(30,18)),('C',(35,28),(36,18),(39,25))]);join('middle','base')
 path('top',(19,18),[('C',(24,6),(19,14),(29,13)),('C',(33,14),(29,7),(33,9)),('C',(30,18),(33,16),(31,18))]);join('top','middle')
 """)
design('anchor-logo','SQUARE','Balanced anchor',None,'Preserve the loop, crossbar and two flukes; mirrored arms meet at the central stem and exact arrow tips.',"""
 path('ring',(24,14),[('A',(20,10),4,4,True),('A',(24,6),4,4,True),('A',(28,10),4,4,True),('A',(24,14),4,4,True)],True)
 path('stem',(24,14),[('L',(24,19)),('L',(24,42))]);join('stem','ring');path('bar',(18,19),[('L',(24,19)),('L',(30,19))]);join('bar','stem')
 path('arms',(8,27),[('C',(24,42),(8,36),(16,42)),('C',(40,27),(32,42),(40,36))]);join('arms','stem')
 path('left',(6,33),[('L',(8,27)),('L',(14,31))]);path('right',(34,31),[('L',(40,27)),('L',(42,33))]);join('left','arms');join('right','arms')
 """)
design('astronomy-planet-pluto','CIRCLE','Smooth planetary contour',None,'Preserve the asymmetric inner loop inside a true circular planet; attach it at exact rim nodes.',"""
 path('rim',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
 path('surface',(44,24),[('C',(30,16),(37,24),(37,16)),('C',(22,26),(23,16),(20,21)),('C',(28,34),(22,30),(27,31)),('C',(24,44),(29,38),(26,41))]);join('surface','rim')
 """)
design('night-moon-new','VRECT_L','Smooth crescent',None,'Preserve the left-facing crescent; coherent outer and inner curves keep broad, smoothly tapering horns.',"""
 path('moon',(8,4),[('C',(40,24),(27,4),(40,12)),('C',(8,44),(40,36),(27,44)),('C',(25,24),(20,41),(25,32)),('C',(8,4),(25,16),(20,7))],True)
 """)
design('do-not-disturb-sleep-mode','SQUARE','Smooth diagonal crescent',None,'Preserve the diagonal moon with its upper-left and lower-right horns; replace the fitted lumps with flowing curves.',"""
 path('moon',(21,6),[('C',(6,24),(12,8),(6,15)),('C',(24,42),(6,34),(14,42)),('C',(42,32),(32,42),(38,39)),('C',(21,6),(19,41),(10,18))],True)
 """)
design('calendly-logo','SQUARE','Smooth open C emblem',None,'Preserve the outlined C; give the inner curve a clear, broad opening and balanced terminal tabs.',"""
 path('mark',(42,17),[('C',(24,6),(37,10),(31,6)),('C',(6,24),(14,6),(6,14)),('C',(24,42),(6,34),(14,42)),('C',(42,31),(31,42),(37,38)),('L',(31,28)),('C',(24,33),(29,31),(28,33)),('C',(15,24),(19,33),(15,29)),('C',(24,15),(15,19),(19,15)),('C',(31,20),(28,15),(29,17)),('L',(42,17))],True)
 """)
design('affinity-designer-logo','HRECT_L','Clean angular designer emblem',None,'Preserve the triangular partition and diagonal band; widen the narrow outer band and share every facet node.',"""
 path('outline',(4,30),[('L',(18,8)),('L',(28,8)),('L',(44,8)),('L',(44,29)),('L',(44,40)),('L',(21,40)),('L',(4,40)),('L',(4,30))],True)
 path('band',(28,8),[('L',(21,18)),('L',(14,29)),('L',(21,40))]);join('band','outline')
 path('facet',(14,29),[('L',(29,29)),('L',(44,29))]);line('diagonal',(21,18),(29,29));join('facet','outline');join('facet','band');join('diagonal','facet');join('diagonal','band')
 """)
design('affinity-publisher-logo','SQUARE','Regular diagonal publisher bands',None,'Preserve the four diagonal divisions; rebalance their spacing and make shared edge intersections exact.',"""
 path('outline',(6,32),[('L',(10,24)),('L',(15,15)),('L',(20,6)),('L',(32,6)),('L',(42,6)),('L',(42,24)),('L',(42,42)),('L',(30,42)),('L',(20,42)),('L',(6,42)),('L',(6,32))],True)
 for j,(a,b) in enumerate([((10,24),(20,42)),((15,15),(30,42)),((20,6),(42,42)),((32,6),(42,24))]):line(f'band-{j}',a,b);join(f'band-{j}','outline')
 """)
design('pyup-logo','VRECT_L','Clean hexagonal P emblem',None,'Preserve the open hexagonal border and inner P; consolidate the left stem and share the counter junction.',"""
 poly('outside',(16,40),(8,36),(8,15),(24,4),(40,15),(40,34),(25,44))
 poly('inside',(16,40),(16,29),(16,19),(24,14),(32,19),(32,29),(24,35),(16,29));join('inside','outside')
 """)
design('virtual-coin-crypto-tron','VRECT_L','Clean triangular Tron facets',None,'Preserve all three facets and the skewed outer triangle; use one uninterrupted outer diagonal and shared hub.',"""
 poly('outline',(8,4),(35,10),(40,17),(21,44),closed=True)
 for j,end in enumerate([(8,4),(40,17),(21,44)]):line(f'facet-{j}',(21,20),end);join(f'facet-{j}','outline')
 for j in range(3):
  for k in range(j+1,3):join(f'facet-{j}',f'facet-{k}')
 """)
design('vodafone-logo','CIRCLE','Smooth circular speech mark',None,'Preserve the inner speech loop and its rising tail; use true circles with exact tail attachment nodes.',"""
 path('rim',(24,4),[('A',(36,8),20,20,True),('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
 path('loop',(18,17),[('A',(34,25),10,10,True),('A',(24,35),10,10,True),('A',(14,25),10,10,True),('A',(18,17),10,10,True)],True)
 path('tail',(18,17),[('C',(36,8),(20,11),(28,8))]);join('tail','loop');join('tail','rim')
 """)
design('vray-logo','CIRCLE','Smooth flowing V emblem',None,'Preserve the flowing inner V inside a true circle; attach both ends at exact rim nodes.',"""
 path('rim',(24,4),[('A',(40,12),20,20,True),('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
 path('mark',(24,4),[('C',(14,24),(17,7),(14,14)),('C',(18,31),(14,31),(16,34)),('C',(30,18),(23,31),(25,22)),('C',(40,12),(34,12),(37,10))]);join('mark','rim')
 """)

# Final clearance refinements on owning symbols.
for n,replacements in {
 'arrange-number': [('(33,19)','(33,18)')],
 'anchor-logo': [('24,19','24,23'),('18,19','18,23'),('30,19','30,23')],
 'affinity-designer-logo': [('(18,8)','(17,8)')],
 'pyup-logo': [('(24,14)','(24,15)'),('(32,19)','(31,20)'),('(32,29)','(31,29)')],
 'vodafone-logo': [('(20,11),(28,8)','(24,13),(29,8)')],
 'vaccine-bottle': [('(18,10)','(18,13)'),('(30,10)','(30,13)'),('(12,12),(8,13)','(12,15),(8,16)'),('(40,13),(36,12)','(40,16),(36,15)')],
 'wheat': [('(8,22)','(8,27)'),('(22,25),(14,22)','(22,29),(14,27)'),('(8,31),(16,34)','(8,34),(16,36)'),('(40,22)','(40,27)'),('(26,25),(34,22)','(26,29),(34,27)'),('(40,31),(32,34)','(40,34),(32,36)')],
 'wheat-farming': [('(8,22)','(8,27)'),('(22,25),(14,22)','(22,29),(14,27)'),('(8,31),(16,34)','(8,34),(16,36)'),('(40,22)','(40,27)'),('(26,25),(34,22)','(26,29),(34,27)'),('(40,31),(32,34)','(40,34),(32,36)')],
 'arm-flex': [('(25,25),(30,26)','(25,30),(30,30)')],
 'actions-authentication-squares': [('(21,24)','(26,24)'),('(21,36)','(26,36)')],
}.items():
 key,label,ref,plan,body=DESIGNS[n]
 for a,b in replacements:body=body.replace(a,b)
 design(n,key,label,ref,plan,body)
design('shopping-bag-side','VRECT_L','Regular side-gusset bag',None,'Preserve the side panel and arched handle; widen the side panel and use an exact circular handle arch.',"""
 path('bag',(8,44),[('L',(10,16)),('L',(14,16)),('L',(26,16)),('L',(28,16)),('L',(36,16)),('L',(40,44)),('L',(28,44)),('L',(8,44))],True)
 path('handle',(14,16),[('L',(14,10)),('A',(20,4),6,6,True),('A',(26,10),6,6,True),('L',(26,16))]);join('handle','bag')
 line('gusset',(28,16),(28,44));join('gusset','bag')
 """)
design('gift','VRECT_L','Smooth bow gift','gift','Preserve the plain box and two-loop bow. Mirror rounded loops and share their meeting point with the lid.',"""
 path('box',(10,17),[('L',(24,17)),('L',(38,17)),('L',(38,44)),('L',(10,44)),('L',(10,17))],True)
 path('lid',(8,17),[('L',(10,17)),('L',(24,17)),('L',(38,17)),('L',(40,17))]);join('lid','box')
 path('left',(24,17),[('C',(12,9),(17,17),(12,15)),('C',(17,4),(12,6),(14,4)),('C',(24,17),(22,4),(24,12))],True)
 path('right',(24,17),[('C',(31,4),(24,12),(26,4)),('C',(36,9),(34,4),(36,6)),('C',(24,17),(36,15),(31,17))],True)
 join('left','right');join('left','box');join('right','box');join('left','lid');join('right','lid')
 """)
design('graph-v-lines','SQUARE','Clear zigzag chart',None,'Preserve the angular two-sided trace and axes; broaden the diagonal band with fewer equal straight sections.',"""
 poly('axis',(6,6),(6,42),(42,42))
 poly('trace',(16,6),(25,15),(16,24),(34,42),(42,42),(28,24),(38,14),(30,6),(21,15),(16,10))
 join('trace','axis')
 """)
design('kimono','SQUARE','Balanced wrapped kimono',None,'Preserve wide sleeves, crossed lapels and flared skirt. Shared waist nodes separate the wrapping panels.',"""
 path('garment',(6,18),[('L',(18,6)),('L',(30,6)),('L',(42,18)),('L',(37,25)),('L',(32,21)),('L',(32,29)),('L',(35,42)),('L',(13,42)),('L',(16,29)),('L',(16,21)),('L',(11,25)),('L',(6,18))],True)
 path('lapel',(18,6),[('L',(24,20)),('L',(30,6))]);join('lapel','garment')
 path('wrap',(24,20),[('L',(20,29)),('L',(16,29))]);join('wrap','lapel');join('wrap','garment')
 path('waist',(20,29),[('L',(32,29))]);join('waist','wrap');join('waist','garment')
 """)
design('lead-nuturing-plant','SQUARE','Smooth paired seedling','leaf','Preserve two cupped leaves and curved soil line. Mirror broad leaf contours around a shared central stem.',"""
 path('left',(24,32),[('C',(6,6),(8,32),(6,20)),('C',(24,32),(22,8),(24,17))],True)
 path('right',(24,32),[('C',(42,6),(24,17),(26,8)),('C',(24,32),(42,20),(40,32))],True)
 join('left','right');line('stem',(24,32),(24,38));join('stem','left');join('stem','right')
 path('soil',(8,42),[('C',(24,38),(13,40),(19,38)),('C',(40,42),(29,38),(35,40))]);join('soil','stem')
 """)
design('love-it-break','HRECT_L','Smooth broken heart','heart-crack','Preserve the broad heart and attached zigzag crack; mirror the outer lobes with a roomy middle.',"""
 path('heart',(24,12),[('C',(14,8),(21,9),(18,8)),('C',(4,19),(7,8),(4,12)),('C',(24,40),(4,27),(18,36)),('C',(44,19),(30,36),(44,27)),('C',(34,8),(44,12),(41,8)),('C',(24,12),(30,8),(27,9))],True)
 path('crack',(24,12),[('L',(19,19)),('L',(25,25)),('L',(20,30))]);join('crack','heart')
 """)
design('monitor-heart-beat','SQUARE','Smooth heart pulse','heart-crack','Preserve the heart and pulse line. Use one shared waveform with deliberate entry and exit nodes.',"""
 path('heart',(24,10),[('C',(15,6),(21,7),(19,6)),('C',(6,17),(9,6),(6,10)),('C',(10,27),(6,21),(8,24)),('C',(24,42),(14,33),(20,39)),('C',(38,27),(28,39),(34,33)),('C',(42,17),(40,24),(42,21)),('C',(33,6),(42,10),(39,6)),('C',(24,10),(29,6),(27,7))],True)
 path('pulse',(6,27),[('L',(10,27)),('L',(16,27)),('L',(21,17)),('L',(27,33)),('L',(31,27)),('L',(38,27)),('L',(42,27))]);join('pulse','heart')
 """)
design('outdoors-machete','SQUARE','Smooth broad machete',None,'Preserve the broad curved blade and short handle; enlarge both bands perpendicular to the blade direction.',"""
 path('blade',(18,25),[('L',(42,6)),('C',(35,28),(42,17),(41,23)),('L',(24,36)),('L',(18,25))],True)
 path('handle',(18,25),[('L',(6,35)),('L',(6,42)),('L',(11,42)),('L',(24,36))]);join('handle','blade')
 """)
design('quill','SQUARE','Smooth broad quill','leaf','Preserve the diagonal tapering leaf and short quill stroke. Use two coherent vane curves and a central partial shaft.',"""
 path('vane',(13,35),[('C',(42,6),(8,20),(27,9)),('C',(13,35),(39,27),(26,41))],True)
 path('shaft',(6,42),[('L',(13,35)),('L',(26,22))]);join('shaft','vane')
 """)
design('refresh-arrow','SQUARE','True circular refresh',None,'Preserve the almost-complete circular arrow and left lower head; use true arcs instead of a segmented fitted ring.',"""
 path('turn',(24,42),[('A',(42,24),18,18,False),('A',(24,6),18,18,False),('A',(6,24),18,18,False),('A',(13,38),18,18,False)])
 poly('head',(13,28),(13,38),(6,38));join('head','turn')
 """)
design('network-and-content-delivery','VRECT_L','Smooth network cloud','cloud','Preserve the cloud and three spreading network terminals. The center stem joins the cloud at a real midpoint.',"""
 path('cloud',(20,28),[('C',(8,17),(13,28),(8,23)),('C',(20,4),(8,10),(13,4)),('C',(31,12),(26,4),(29,7)),('C',(40,20),(37,10),(40,15)),('C',(32,28),(40,25),(37,28)),('L',(24,28)),('L',(20,28))],True)
 path('stem',(24,28),[('L',(24,35)),('L',(24,44))]);join('stem','cloud');poly('branches',(13,40),(24,30),(35,40));join('branches','stem')
 """)
design('presentation-board-graph','SQUARE','Clear presentation graph',None,'Preserve a rectangular display, compact line chart and tripod. Share the chart attachment with the frame.',"""
 path('board',(6,6),[('L',(42,6)),('L',(42,30)),('L',(24,30)),('L',(6,30)),('L',(6,20)),('L',(6,6))],True)
 path('chart',(6,20),[('L',(17,20)),('L',(21,15)),('L',(28,22)),('L',(33,14))]);join('chart','board')
 path('stem',(24,30),[('L',(24,34)),('L',(24,42))]);poly('legs',(16,42),(24,34),(32,42));join('legs','stem');join('stem','board')
 """)
design('tools-palette-spatula','VRECT_L','Smooth broad spatula',None,'Preserve the broad flat blade and narrow rounded grip, with balanced shoulders and one shared blade edge.',"""
 path('tool',(8,4),[('L',(40,4)),('L',(35,21)),('L',(33,27)),('L',(28,31)),('L',(30,40)),('C',(24,44),(31,43),(28,44)),('C',(18,40),(20,44),(17,43)),('L',(20,31)),('L',(15,27)),('L',(13,21)),('L',(8,4))],True)
 line('edge',(13,21),(35,21));join('edge','tool')
 """)
for n in ['tooth-c824bba6','tooth-health']:
 design(n,'VRECT_L','Smooth rooted tooth',None,'Preserve two roots and a gently notched crown. Broaden the inner root channel while keeping the natural asymmetric crown.',"""
 path('tooth',(24,7),[('C',(14,4),(20,6),(18,4)),('C',(8,15),(10,4),(8,9)),('C',(12,32),(8,21),(11,27)),('C',(17,44),(13,40),(14,44)),('C',(24,28),(21,44),(18,28)),('C',(31,44),(30,28),(27,44)),('C',(36,32),(34,44),(35,40)),('C',(40,15),(37,27),(40,21)),('C',(34,4),(40,9),(38,4)),('C',(24,7),(30,4),(28,6))],True)
 """)
design('tape','HRECT_L','Regular tape roll',None,'Preserve the circular tape roll and attached loose end. Two concentric circles share one axis.',"""
 path('roll',(28,8),[('A',(44,24),16,16,True),('A',(28,40),16,16,True),('A',(12,24),16,16,True),('A',(28,8),16,16,True)],True)
 circle('hole',28,24,5)
 poly('end',(12,24),(4,32),(14,32));join('end','roll')
 """)
design('sushi','HRECT_L','Balanced striped sushi',None,'Preserve the oval rice base and arched topping with three broad bands. Repeated divisions share exact top and bottom nodes.',"""
 path('rice',(16,22),[('L',(32,22)),('C',(40,31),(38,22),(40,26)),('C',(32,40),(40,36),(38,40)),('L',(16,40)),('C',(8,31),(10,40),(8,36)),('C',(16,22),(8,26),(10,22))],True)
 path('top',(8,31),[('L',(4,28)),('C',(12,12),(5,20),(8,16)),('C',(24,8),(16,9),(20,8)),('C',(36,12),(28,8),(32,9)),('C',(44,28),(40,16),(43,20)),('L',(40,31))]);join('top','rice')
 line('stripe-left',(12,12),(16,22));line('stripe-mid',(24,8),(24,22));line('stripe-right',(36,12),(32,22));join('stripe-left','top');join('stripe-left','rice');join('stripe-mid','top');join('stripe-mid','rice');join('stripe-right','top');join('stripe-right','rice')
 """)
design('seat-settings','SQUARE','Smooth seat and pointer',None,'Preserve the low-backed chair and pointer in the upper right. Use a broad seat channel and clear diagonal pointer stem.',"""
 path('seat',(6,6),[('L',(14,6)),('C',(17,24),(17,12),(17,18)),('L',(17,32)),('L',(35,30)),('C',(40,33),(39,30),(40,31)),('L',(39,39)),('C',(35,42),(38,41),(37,42)),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,6))],True)
 poly('pointer',(28,8),(31,21),(35,15),(42,12),closed=True);line('tail',(35,15),(42,23));join('tail','pointer')
 """)
design('satellite','SQUARE','Smooth satellite dish',None,'Preserve the tilted concave dish, support and feed. The dish uses one broad arc; the feed meets the rim at an exact node.',"""
 path('dish',(12,6),[('L',(24,18)),('L',(36,30)),('L',(42,36)),('C',(14,34),(32,45),(20,42)),('C',(12,6),(5,26),(6,16))],True)
 poly('base',(14,34),(6,42),(26,42),(22,38));join('base','dish')
 path('feed',(24,18),[('L',(38,18)),('L',(38,10))]);join('feed','dish');circle('receiver',38,6,4);join('receiver','feed')
 """)
design('adobe-cloud-logo','HRECT_L','Smooth interlocking cloud',None,'Preserve the two overlapping cloud loops and diagonal inner stroke; reconstruct them as coherent curves.',"""
 path('outer',(16,40),[('C',(4,26),(9,40),(4,34)),('C',(16,13),(4,18),(9,13)),('C',(24,16),(19,13),(22,14)),('C',(32,8),(25,11),(28,8)),('C',(44,24),(40,8),(44,16)),('C',(32,40),(44,33),(39,40)),('L',(16,40))],True)
 path('inner',(22,40),[('L',(13,30)),('C',(16,23),(9,25),(13,20)),('L',(28,36)),('L',(32,40))]);join('inner','outer')
 path('upper',(24,16),[('L',(30,23))]);join('upper','outer')
 """)
design('airbnb-logo','VRECT_L','Smooth looped travel mark',None,'Preserve the tall rounded triangular loop and central crossing oval, with mirrored lower lobes.',"""
 path('outer',(24,4),[('C',(30,9),(27,4),(28,5)),('L',(40,33)),('C',(33,44),(43,40),(37,44)),('C',(24,39),(30,44),(27,42)),('C',(15,44),(21,42),(18,44)),('C',(8,33),(11,44),(5,40)),('L',(18,9)),('C',(24,4),(20,5),(21,4))],True)
 path('loop',(24,39),[('C',(18,27),(20,34),(18,30)),('A',(30,27),6,6,True),('C',(24,39),(30,30),(28,34))],True);join('loop','outer')
 """)
design('equipment-cement-cart','HRECT_L','Clear cement wheelbarrow',None,'Preserve the loaded tray, single wheel and raised handle. The load is a broad scalloped mound, with a separate wheel clearance.',"""
 path('tray',(4,18),[('L',(10,18)),('L',(34,18)),('L',(38,18)),('L',(28,30)),('L',(20,30)),('L',(12,30)),('L',(4,18))],True)
 path('load',(10,18),[('C',(15,13),(9,14),(12,12)),('C',(23,8),(16,9),(19,8)),('C',(30,13),(27,8),(30,10)),('C',(34,18),(34,12),(36,15))]);join('load','tray')
 circle('wheel',12,35,5);join('wheel','tray');line('handle',(38,18),(44,10));join('handle','tray')
 poly('leg',(28,30),(38,38),(38,18));join('leg','tray')
 """)
design('google-voice-logo','SQUARE','Smooth phone and voice wedge',None,'Preserve the telephone handset and upper-right quarter-disc. Use coherent handset curves and one true quarter circle.',"""
 path('handset',(13,6),[('L',(20,14)),('L',(16,21)),('C',(27,32),(18,26),(22,30)),('L',(33,28)),('L',(42,36)),('C',(31,42),(39,40),(36,42)),('C',(6,17),(20,42),(6,28)),('C',(13,6),(6,11),(9,7))],True)
 path('voice',(28,6),[('A',(42,20),14,14,True),('L',(28,20)),('L',(28,6))],True)
 """)
design('lightning-with-wrench','HRECT_L','Clear wrench and lightning',None,'Preserve both wrench and bolt; diagonal tool construction keeps the two silhouettes distinct.',"""
 path('wrench',(4,32),[('L',(17,19)),('C',(18,8),(14,14),(15,10)),('C',(29,8),(21,6),(26,7)),('L',(23,14)),('L',(28,19)),('C',(21,25),(29,25),(25,27)),('L',(9,38))])
 poly('bolt',(39,16),(32,29),(44,29),(34,40))
 """)
design('love-compatibility','HRECT_L','Smooth overlapping hearts','heart-crack','Preserve two overlapping hearts at different depths. Keep the rear outline open only where the front heart occludes it.',"""
 path('front',(31,22),[('C',(38,18),(33,19),(36,18)),('C',(44,25),(42,18),(44,21)),('C',(31,40),(44,31),(36,36)),('C',(18,25),(26,36),(18,31)),('C',(24,18),(18,21),(20,18)),('C',(31,22),(26,18),(29,19))],True)
 path('rear',(21,34),[('L',(16,40)),('C',(4,20),(10,34),(4,27)),('C',(13,8),(4,12),(8,8)),('C',(21,12),(16,8),(19,10)),('C',(29,8),(23,10),(26,8)),('C',(38,18),(34,8),(38,12))]);join('rear','front')
 """)
design('music-clef','VRECT_L','Flowing treble clef',None,'Preserve the upper loop, broad lower loop and hooked stem. Use coherent sweeps with real crossing nodes.',"""
 path('stem',(24,25),[('L',(19,7)),('C',(30,4),(21,4),(26,4)),('C',(33,11),(36,4),(37,8)),('C',(24,19),(31,14),(27,16)),('C',(8,29),(16,22),(8,24)),('C',(24,36),(8,35),(17,36)),('C',(40,29),(31,36),(40,35)),('C',(24,25),(40,23),(31,24)),('L',(28,40)),('C',(17,44),(30,46),(21,44)),('L',(16,41))])
 """)
design('mx-linux-logo','HRECT_L','Clean mountain X mark',None,'Preserve the crossed poles and double-peaked base. Use shared intersection nodes and roomy lower slopes.',"""
 poly('left-pole',(17,8),(28,22),(33,28));poly('right-pole',(35,8),(28,16),(21,24),(4,40),(44,40),(34,28),(30,32));join('left-pole','right-pole')
 """)
design('pearl','SQUARE','Smooth pearl shell',None,'Preserve an open scalloped shell and centered pearl. Symmetric bowl and lid curves leave the pearl clearly separated.',"""
 path('lid',(14,26),[('C',(6,17),(9,24),(6,22)),('C',(12,10),(6,13),(9,10)),('C',(24,6),(16,10),(17,6)),('C',(36,10),(31,6),(32,10)),('C',(42,17),(39,10),(42,13)),('C',(34,26),(42,22),(39,24))])
 circle('pearl',24,27,5)
 path('bowl',(6,32),[('C',(19,32),(10,29),(15,30)),('C',(29,32),(22,33),(26,33)),('C',(42,32),(33,30),(38,29)),('C',(24,42),(39,40),(31,42)),('C',(6,32),(17,42),(9,40))],True);join('pearl','bowl')
 """)
design('picasa-logo','CIRCLE','Regular circular shutter',None,'Preserve five shutter facets; use a true circle and exact integer attachment nodes for the inner frame.',"""
 path('rim',(24,4),[('A',(36,8),20,20,True),('A',(44,24),20,20,True),('A',(36,40),20,20,True),('A',(24,44),20,20,True),('A',(8,36),20,20,True),('A',(4,24),20,20,True),('A',(8,12),20,20,True),('A',(24,4),20,20,True)],True)
 poly('frame',(8,36),(16,28),(24,20),(36,32),(36,8));join('frame','rim')
 poly('top',(8,12),(24,20));join('top','frame');join('top','rim')
 poly('bottom',(16,28),(16,40));join('bottom','frame')
 line('bar',(16,32),(36,32));join('bar','frame')
 """)
design('rhythmic-ribbon','VRECT_L','Smooth flowing ribbon',None,'Preserve the ribbon wand and two loose waves. Use broad alternating turns with enough space between returning strokes.',"""
 path('ribbon',(8,44),[('L',(22,30)),('C',(16,20),(14,26),(12,22)),('C',(31,23),(21,16),(28,26)),('C',(27,12),(35,20),(31,15)),('C',(20,7),(23,10),(18,9)),('C',(30,4),(20,3),(26,4)),('C',(40,11),(34,4),(37,8))])
 """)
design('sawmill','SQUARE','Clear sawmill blade',None,'Preserve the irregular cutting teeth and lower opening. Use broad teeth rather than many thin spikes.',"""
 path('blade',(9,42),[('L',(9,33)),('L',(6,25)),('L',(14,25)),('L',(11,15)),('L',(20,19)),('L',(21,6)),('L',(29,16)),('L',(35,10)),('L',(36,23)),('L',(42,20)),('L',(39,32)),('L',(42,32)),('L',(40,42))])
 path('base',(6,42),[('L',(9,42)),('L',(17,42)),('L',(31,42)),('L',(40,42)),('L',(42,42))]);join('base','blade')
 path('opening',(17,42),[('C',(24,27),(17,31),(20,27)),('C',(31,42),(28,27),(31,31))]);join('opening','base')
 """)
design('seasoning-chilli','SQUARE','Smooth curved chilli',None,'Preserve the bowed pepper, cap and short stem. Build the outer and inner curves as a broad continuous taper.',"""
 path('pepper',(31,16),[('C',(40,16),(33,10),(40,10)),('C',(29,39),(41,30),(38,35)),('C',(6,32),(20,47),(8,37)),('C',(29,27),(16,40),(26,37)),('L',(31,16))],True)
 path('cap',(31,16),[('C',(40,22),(31,22),(37,24))]);join('cap','pepper')
 path('stem',(36,12),[('C',(42,6),(36,8),(39,6))]);join('stem','pepper')
 """)
design('spa-lotus','HRECT_L','Smooth layered lotus','flower-2','Preserve five petals. Mirror each petal pair and use shared basal nodes for a balanced open flower.',"""
 path('center',(24,40),[('C',(24,8),(13,30),(16,18)),('C',(24,40),(32,18),(35,30))],True)
 path('left',(24,40),[('C',(10,16),(11,40),(8,29)),('C',(18,20),(13,16),(16,18))]);join('left','center')
 path('right',(24,40),[('C',(38,16),(37,40),(40,29)),('C',(30,20),(35,16),(32,18))]);join('right','center')
 path('base',(18,39),[('C',(4,28),(9,39),(7,33)),('L',(11,28))]);join('base','left')
 path('base-right',(30,39),[('C',(44,28),(39,39),(41,33)),('L',(37,28))]);join('base-right','right')
 """)
design('swift-logo','HRECT_L','Smooth flying bird emblem',None,'Preserve the swept wings and broad flying-bird silhouette with deliberate asymmetry.',"""
 path('bird',(4,16),[('L',(23,28)),('L',(13,12)),('L',(31,25)),('C',(30,8),(36,23),(34,15)),('C',(39,30),(42,17),(40,24)),('C',(44,39),(43,32),(44,35)),('C',(34,36),(40,36),(37,35)),('C',(4,34),(23,44),(12,39)),('L',(21,35)),('C',(4,16),(12,29),(7,23))],True)
 """)
design('terrier','VRECT_L','Smooth alert terrier',None,'Preserve pointed ears, broad cheeks and narrow muzzle. Mirror the face but keep the ears tall and open.',"""
 path('face',(8,4),[('L',(18,14)),('C',(30,14),(22,12),(26,12)),('L',(40,4)),('C',(36,24),(40,13),(39,19)),('C',(24,44),(34,37),(31,42)),('C',(12,24),(17,42),(14,37)),('C',(8,4),(9,19),(8,13))],True)
 self.add_dot('left-eye',(20,24));self.add_dot('right-eye',(28,24));line('muzzle',(24,36),(24,44));join('muzzle','face')
 """)
design('vimeo-logo','HRECT_L','Smooth looping V emblem',None,'Preserve the hooked left terminal and looping right return. Broad coherent curves keep the diagonal counter open.',"""
 path('mark',(4,17),[('C',(17,8),(9,12),(13,8)),('C',(22,22),(21,8),(21,17)),('C',(26,31),(23,29),(23,33)),('C',(34,19),(30,27),(34,22)),('C',(30,17),(35,15),(31,14)),('C',(44,14),(34,7),(43,8)),('C',(22,40),(44,25),(29,40)),('C',(14,29),(17,40),(16,34)),('L',(11,18)),('L',(4,17))],True)
 """)
design('vr-headset','VRECT_L','Smooth headset profile','headset','Human reference: user.svg and full_body_ref.png. Preserve the continuous human profile and broad visor, with a separate shared strap edge.',"""
 path('head',(15,44),[('L',(15,37)),('C',(8,22),(11,32),(8,29)),('A',(24,6),16,16,True),('C',(35,10),(28,6),(32,8))])
 path('visor',(28,12),[('L',(40,12)),('L',(40,24)),('L',(28,24)),('A',(28,12),6,6,True)],True)
 path('strap',(8,18),[('L',(22,18))]);join('strap','head');join('strap','visor')
 path('profile',(35,24),[('L',(37,31)),('L',(32,31)),('L',(32,37)),('L',(25,39)),('L',(25,44))]);join('profile','visor')
 """)
for n,replacements in {
 'plane-1-travel':[('(14,8)','(10,8)'),('(14,40)','(10,40)')],
 'plane-1':[('(4,29)','(4,27)'),('(9,25)','(9,22)'),('(17,29)','(18,29)'),('(16,12)','(17,8)'),('(9,17)','(7,15)')],
 'plane':[('(6,20)','(6,17)'),('(20,40)','(17,40)'),('(19,8)','(15,8)'),('(16,13)','(12,13)'),('(16,8),(14,11)','(12,8),(10,11)')],
 'truck-style':[('(37,18)','(35,16)'),('(44,26)','(44,22)')],
 'truck-transportation':[('(37,18)','(36,16)'),('(44,26)','(44,22)')],
 'vaccine-bottle':[('(8,24)','(8,29)'),('(40,24)','(40,29)'),('(24,24)','(24,29)'),('(14,21),(18,21)','(14,26),(18,26)'),('(30,27),(34,27)','(30,32),(34,32)')],
 'lead-nuturing-plant':[('(24,32)','(24,29)'),('(8,32),(6,20)','(8,29),(6,18)'),('(22,8),(24,17)','(22,8),(24,15)'),('(24,17),(26,8)','(24,15),(26,8)'),('(42,20),(40,32)','(42,18),(40,29)')],
 'google-voice-logo':[('(20,14)','(19,14)')],
 'music-clef':[('(30,46),(21,44)','(30,44),(21,44)')],
 'rhythmic-ribbon':[('(20,3),(26,4)','(20,4),(26,4)')],
 'terrier':[('(20,24)','(20,22)'),('(28,24)','(28,22)')],
 'sawmill':[('(42,20)','(42,18)'),("('L',(42,32)),",'')],
 'seat-settings':[('(31,21)','(29,21)'),('(35,15)','(36,17)'),('(42,23)','(42,25)')],
}.items():
 key,label,ref,plan,body=DESIGNS[n]
 for a,b in replacements:body=body.replace(a,b)
 design(n,key,label,ref,plan,body)
design('graph-line-spline','HRECT_L','Smooth two-series graph',None,'Preserve both chart series and axes. Repeat a shallow coherent wave at a twelve-unit offset and start clear of the vertical axis.',"""
 poly('axis',(4,8),(4,40),(44,40))
 path('upper',(13,16),[('C',(28,12),(19,8),(22,12)),('C',(44,8),(34,14),(39,13))])
 path('lower',(13,28),[('C',(28,24),(19,20),(22,24)),('C',(44,20),(34,26),(39,25))])
 """)
design('paintbrush-symbol','SQUARE','Smooth broad paintbrush','paintbrush','Preserve diagonal handle and tapered soft bristles; broaden the grip and use one exact bottom curve extreme.',"""
 path('handle',(17,24),[('L',(34,6)),('C',(42,12),(39,6),(42,7)),('L',(27,33)),('L',(17,24))],True)
 path('bristle',(17,24),[('C',(11,32),(12,24),(11,28)),('C',(6,42),(11,37),(9,40)),('L',(12,42)),('C',(27,33),(21,42),(27,39))]);join('bristle','handle')
 """)
design('pine-f98a2e8b','VRECT_L','Balanced three-tier pine',None,'Preserve three branches on each side. Broader tier spacing keeps a recognizable conifer silhouette.',"""
 path('tree',(24,4),[('L',(31,14)),('L',(27,14)),('L',(35,26)),('L',(29,26)),('L',(40,38)),('L',(24,38)),('L',(8,38)),('L',(19,26)),('L',(13,26)),('L',(21,14)),('L',(17,14)),('L',(24,4))],True)
 line('trunk',(24,38),(24,44));join('trunk','tree')
 """)
design('dragon-fruit','VRECT_L','Smooth crowned dragon fruit',None,'Preserve the oval fruit and leafy crown. Three broad overlapping crown points replace cramped small spikes.',"""
 path('fruit',(8,16),[('L',(18,21)),('L',(24,4)),('L',(30,21)),('L',(40,16)),('C',(24,44),(40,34),(35,44)),('C',(8,16),(13,44),(8,34))],True)
 """)
design('feather','VRECT_L','Smooth notched feather','leaf','Preserve the broad vane, diagonal shaft and one intentional notch; the notch ends at a shared vane node.',"""
 path('vane',(13,35),[('C',(8,25),(9,33),(8,29)),('C',(38,4),(8,15),(27,7)),('C',(40,13),(40,7),(40,10)),('C',(29,27),(40,20),(34,24)),('L',(34,27)),('C',(13,35),(30,36),(20,39))],True)
 path('quill',(8,44),[('L',(13,35)),('L',(25,20))]);join('quill','vane')
 """)
design('graph-v-lines','SQUARE','Clear zigzag chart',None,'Preserve the two zigzag chart traces and axes. Open traces remove the cramped parallel channel while retaining the jagged graph.',"""
 poly('axis',(6,6),(6,42),(28,42),(42,42))
 poly('left',(16,6),(23,14),(14,24),(28,42));join('left','axis')
 poly('right',(27,6),(37,14),(28,24),(42,42));join('right','axis')
 """)
design('kimono','SQUARE','Balanced wrapped kimono',None,'Preserve wide sleeves, crossed lapels and flared skirt. Use a single diagonal wrap across a broad waist.',"""
 path('garment',(6,18),[('L',(18,6)),('L',(30,6)),('L',(42,18)),('L',(37,25)),('L',(32,21)),('L',(32,29)),('L',(35,42)),('L',(13,42)),('L',(16,29)),('L',(16,21)),('L',(11,25)),('L',(6,18))],True)
 path('lapel',(18,6),[('L',(24,19)),('L',(30,6))]);join('lapel','garment')
 path('wrap',(24,19),[('L',(20,29)),('L',(32,29))]);join('wrap','lapel');join('wrap','garment');line('belt',(16,29),(20,29));join('belt','wrap');join('belt','garment')
 """)
design('tape','HRECT_L','Regular tape roll',None,'Preserve the circular roll and projecting loose end. The tail meets two exact integer nodes on a circle.',"""
 path('roll',(28,8),[('A',(44,24),16,16,True),('A',(28,40),16,16,True),('A',(12,24),16,16,True),('A',(28,8),16,16,True)],True)
 circle('hole',28,24,5)
 poly('end',(12,24),(4,34),(28,40));join('end','roll')
 """)
design('sushi','HRECT_L','Balanced striped sushi',None,'Preserve the oval rice and arched striped topping. Use a single shared top edge instead of overlapping rice and topping contours.',"""
 path('rice',(8,26),[('C',(24,22),(12,22),(17,22)),('C',(40,26),(31,22),(36,22)),('C',(32,40),(43,34),(39,40)),('L',(16,40)),('C',(8,26),(9,40),(5,34))],True)
 path('top',(8,26),[('L',(4,25)),('C',(13,12),(6,17),(8,14)),('C',(24,8),(17,9),(20,8)),('C',(35,12),(28,8),(31,9)),('C',(44,25),(40,14),(42,17)),('L',(40,26))]);join('top','rice')
 line('stripe-mid',(24,8),(24,22));join('stripe-mid','top');join('stripe-mid','rice')
 """)
design('satellite','SQUARE','Smooth satellite dish',None,'Preserve the tilted dish, feed and pedestal. Join the stand to an exact bottom node of the broad bowl.',"""
 path('dish',(12,6),[('L',(24,18)),('L',(42,36)),('C',(25,38),(36,41),(31,40)),('C',(12,6),(6,35),(3,20))],True)
 poly('base',(25,38),(29,42),(9,42),(14,32));join('base','dish')
 path('feed',(24,18),[('L',(38,18)),('L',(38,14))]);join('feed','dish')
 path('receiver',(38,14),[('A',(34,10),4,4,True),('A',(38,6),4,4,True),('A',(42,10),4,4,True),('A',(38,14),4,4,True)],True);join('receiver','feed')
 """)
# Restore identifying details and prove every attachment with shared nodes.
design('tooth-health','SQUARE','Smooth tooth with floss',None,'Preserve the tooth and attached floss tail. The crown and roots remain distinct from the separate curled floss.',"""
 path('tooth',(19,9),[('C',(11,6),(15,8),(14,6)),('C',(6,15),(8,6),(6,10)),('C',(10,29),(6,20),(9,25)),('C',(13,42),(10,37),(10,42)),('C',(19,28),(17,42),(15,28)),('C',(25,42),(23,28),(21,42)),('C',(28,29),(28,42),(28,37)),('C',(32,15),(29,25),(32,20)),('C',(27,6),(32,10),(30,6)),('C',(19,9),(24,6),(23,8))],True)
 path('floss',(32,15),[('C',(40,24),(38,15),(40,19)),('L',(40,35)),('C',(42,38),(40,38),(41,39))]);join('floss','tooth')
 """)
key,label,ref,plan,body=DESIGNS['network-and-content-delivery'];design('network-and-content-delivery',key,label,ref,plan,body.replace("('L',(24,35))","('L',(24,30)),('L',(24,35))"))
design('mx-linux-logo','HRECT_L','Clean mountain X mark',None,'Preserve two crossed poles and the mountain outline; split the crossing and peak at exact nodes.',"""
 poly('left-pole',(17,8),(25,18),(33,28))
 poly('right-pole',(35,8),(25,18),(4,40),(44,40),(34,28),(30,32));join('left-pole','right-pole')
 """)
design('equipment-cement-cart','HRECT_L','Clear cement wheelbarrow',None,'Preserve the loaded tray, single wheel and rear leg. A curved shoulder connects the tray to the full round wheel.',"""
 path('tray',(4,18),[('L',(10,18)),('L',(34,18)),('L',(38,18)),('L',(28,28)),('L',(20,28)),('C',(17,35),(18,28),(17,31)),('A',(7,35),5,5,True),('C',(4,18),(7,28),(4,23))],True)
 path('wheel',(7,35),[('A',(17,35),5,5,True)]);join('wheel','tray')
 path('load',(10,18),[('C',(15,13),(9,14),(12,12)),('C',(23,8),(16,9),(19,8)),('C',(30,13),(27,8),(30,10)),('C',(34,18),(34,12),(36,15))]);join('load','tray')
 line('handle',(38,18),(44,10));join('handle','tray');poly('leg',(28,28),(38,38),(38,18));join('leg','tray')
 """)
design('spa-lotus','HRECT_L','Smooth layered lotus','flower-2','Preserve the layered lotus through broad mirrored petals. Each outer petal ends at the central basal node, with no nearly overlapping extra contour.',"""
 path('center',(24,40),[('C',(24,8),(13,30),(16,18)),('C',(24,40),(32,18),(35,30))],True)
 path('left',(24,40),[('C',(7,16),(10,40),(7,29)),('C',(18,20),(12,16),(16,18))]);join('left','center')
 path('right',(24,40),[('C',(41,16),(38,40),(41,29)),('C',(30,20),(36,16),(32,18))]);join('right','center')
 path('base',(24,40),[('C',(4,29),(13,43),(7,37)),('L',(9,29))]);join('base','center');join('base','left');join('base','right')
 path('base-right',(24,40),[('C',(44,29),(35,43),(41,37)),('L',(39,29))]);join('base-right','center');join('base-right','left');join('base-right','right');join('base','base-right')
 """)
design('vr-headset','VRECT_L','Smooth headset profile','headset','Human reference: user.svg and full_body_ref.png. Preserve the continuous neck, visor and shared strap. Every connection is split at an exact endpoint.',"""
 path('head',(15,44),[('L',(15,37)),('C',(8,20),(11,32),(8,27)),('A',(24,4),16,16,True),('C',(35,12),(30,4),(34,8))])
 path('visor',(28,12),[('L',(35,12)),('L',(40,12)),('L',(40,24)),('L',(35,24)),('L',(28,24)),('A',(22,18),6,6,True),('A',(28,12),6,6,True)],True);join('head','visor')
 path('strap',(8,20),[('L',(22,18))]);join('strap','head');join('strap','visor')
 path('profile',(35,24),[('L',(37,32)),('L',(32,32)),('L',(32,37)),('L',(25,39)),('L',(25,44))]);join('profile','visor')
 """)
design('seasoning-chilli','SQUARE','Smooth curved chilli',None,'Preserve the curved pepper, cap and rising stem. Exact curve extrema and cap nodes keep the tapered silhouette coherent.',"""
 path('pepper',(30,17),[('C',(36,12),(30,14),(32,12)),('C',(40,20),(39,12),(40,15)),('C',(23,42),(40,33),(33,42)),('C',(6,32),(15,42),(9,38)),('C',(28,29),(17,41),(27,37)),('L',(30,17))],True)
 path('cap',(30,17),[('C',(40,20),(32,23),(37,25))]);join('cap','pepper')
 path('stem',(36,12),[('C',(42,6),(36,8),(39,6))]);join('stem','pepper')
 """)
design('pearl','SQUARE','Smooth pearl shell',None,'Preserve the open scalloped lid, round pearl and cupped shell. The bowl meets the pearl at exact side nodes.',"""
 path('lid',(10,24),[('C',(6,16),(7,23),(6,20)),('C',(12,10),(6,12),(9,10)),('C',(24,6),(16,10),(17,6)),('C',(36,10),(31,6),(32,10)),('C',(42,16),(39,10),(42,12)),('C',(38,24),(42,20),(41,23))])
 path('pearl',(19,28),[('A',(24,23),5,5,True),('A',(29,28),5,5,True),('A',(24,33),5,5,True),('A',(19,28),5,5,True)],True)
 path('bowl',(19,28),[('C',(6,32),(14,28),(9,29)),('C',(24,42),(9,40),(17,42)),('C',(42,32),(31,42),(39,40)),('C',(29,28),(39,29),(34,28))]);join('bowl','pearl')
 """)
design('satellite','SQUARE','Smooth satellite dish',None,'Preserve the diagonal dish and feed. A low pedestal joins one exact bowl point; the feed is a straight diagonal to the receiver.',"""
 path('dish',(12,6),[('L',(24,18)),('L',(42,36)),('C',(25,38),(36,41),(31,40)),('C',(6,24),(14,36),(6,32)),('C',(12,6),(6,17),(8,11))],True)
 path('base',(25,38),[('L',(25,42)),('L',(9,42))]);join('base','dish')
 line('feed',(24,18),(35,10));
 path('receiver',(35,10),[('A',(39,6),4,4,True),('A',(43,10),4,4,True),('A',(39,14),4,4,True),('A',(35,10),4,4,True)],True);join('receiver','feed');join('feed','dish')
 """)
for n,replacements in {
 'google-voice-logo':[('(33,28)','(33,29)')],
 'seat-settings':[('(42,25)','(40,22)')],
 'airbnb-logo':[('(43,40),(37,44)','(40,40),(37,44)'),('(11,44),(5,40)','(11,44),(8,40)'),('(18,27)','(19,29)'),('(30,27)','(29,29)'),('6,6,True','5,5,True'),('(20,34),(18,30)','(20,35),(19,32)'),('(30,30),(28,34)','(29,32),(28,35)')],
 'monitor-heart-beat':[('(31,27)','(33,23)'),('(38,27)','(38,27)')],
 'music-clef':[('(28,40)','(28,41)'),('(17,44)','(18,44)'),('(30,44),(21,44)','(28,44),(22,44)'),('(16,41)','(17,43)')],
 'kimono':[('(20,29)','(24,29)')],
 'feather':[("('L',(34,27)),",''),('(30,36),(20,39)','(29,35),(20,39)')],
 'vimeo-logo':[('(22,22)','(20,22)'),('(26,31)','(26,33)'),('(23,29),(23,33)','(21,30),(22,36)'),('(34,19)','(35,17)'),('(30,27),(34,22)','(31,29),(35,21)')],
}.items():
 key,label,ref,plan,body=DESIGNS[n]
 for a,b in replacements:body=body.replace(a,b)
 design(n,key,label,ref,plan,body)
design('pine-f98a2e8b','VRECT_L','Balanced three-tier pine',None,'Preserve three distinct branch tiers; widen the repeated re-entrant gaps rather than flattening the tree to a triangle.',"""
 path('tree',(24,4),[('L',(30,12)),('L',(26,12)),('L',(36,24)),('L',(26,24)),('L',(40,38)),('L',(24,38)),('L',(8,38)),('L',(22,24)),('L',(12,24)),('L',(22,12)),('L',(18,12)),('L',(24,4))],True)
 line('trunk',(24,38),(24,44));join('trunk','tree')
 """)
design('explosion-sound-effect-text','SQUARE','Balanced explosion burst',None,'Preserve the rising pointed blast and low baseline. Broader asymmetrical rays keep their identity without cramped slivers.',"""
 path('burst',(14,42),[('L',(6,24)),('L',(17,29)),('L',(15,13)),('L',(24,22)),('L',(28,6)),('L',(33,24)),('L',(42,19)),('L',(35,34)),('L',(42,34)),('L',(31,42))])
 path('base',(10,42),[('L',(14,42)),('L',(31,42)),('L',(38,42))]);join('base','burst')
 """)
design('monitor-heart-beat','SQUARE','Smooth heart pulse','heart-crack','Preserve the heart and single waveform. An open shared baseline and broad central pulse avoid a cramped return along the heart wall.',"""
 path('heart',(24,10),[('C',(15,6),(21,7),(19,6)),('C',(6,17),(9,6),(6,10)),('C',(10,27),(6,21),(8,24)),('C',(24,42),(14,33),(20,39)),('C',(38,27),(28,39),(34,33)),('C',(42,17),(40,24),(42,21)),('C',(33,6),(42,10),(39,6)),('C',(24,10),(29,6),(27,7))],True)
 path('pulse',(6,27),[('L',(10,27)),('L',(16,27)),('L',(21,17)),('L',(26,31)),('L',(29,27)),('L',(38,27)),('L',(42,27))]);join('pulse','heart')
 """)
design('lightning-with-wrench','SQUARE','Clear wrench and lightning',None,'Preserve a diagonal wrench and separate bolt. Rebalance the two symbols with a wider open wrench handle.',"""
 path('wrench',(6,32),[('L',(17,19)),('C',(15,13),(15,18),(14,16)),('C',(24,6),(15,8),(20,6)),('L',(29,6)),('L',(23,12)),('L',(27,17)),('C',(22,25),(28,22),(26,25)),('L',(12,38))])
 poly('bolt',(39,23),(32,33),(42,33),(34,42))
 """)
design('adobe-cloud-logo','HRECT_L','Smooth interlocking cloud',None,'Preserve the cloud silhouette and inner diagonal loop. Widen the inner rounded counter while keeping the interlocking structure.',"""
 path('outer',(16,40),[('C',(4,26),(9,40),(4,34)),('C',(16,13),(4,18),(9,13)),('C',(24,16),(19,13),(22,14)),('C',(32,8),(25,11),(28,8)),('C',(44,24),(40,8),(44,16)),('C',(32,40),(44,33),(39,40)),('L',(26,40)),('L',(16,40))],True)
 path('inner',(26,40),[('L',(16,29)),('C',(19,23),(13,26),(16,21)),('L',(32,40))]);join('inner','outer')
 line('upper',(24,16),(30,23));join('upper','outer')
 """)
design('picasa-logo','CIRCLE','Regular circular shutter',None,'Preserve the five shutter facets. Attach the inner pentagonal routing at exact circle nodes and separate long parallel bands.',"""
 path('rim',(24,4),[('A',(36,8),20,20,True),('A',(44,24),20,20,True),('A',(40,36),20,20,True),('A',(24,44),20,20,True),('A',(12,40),20,20,True),('A',(4,24),20,20,True),('A',(8,12),20,20,True),('A',(24,4),20,20,True)],True)
 poly('diagonal',(8,12),(24,24),(32,32),(40,36));join('diagonal','rim')
 poly('top',(36,8),(32,20),(32,32));join('top','diagonal');join('top','rim')
 poly('left',(4,24),(16,24),(24,24));join('left','diagonal');join('left','rim')
 poly('bottom',(12,40),(16,32),(16,24));join('bottom','left');join('bottom','rim')
 line('base',(16,32),(32,32));join('base','bottom');join('base','diagonal')
 """)
for n,replacements in {
 'music-clef':[('(17,43)','(18,44)')],
 'pearl':[('(10,24)','(10,19)'),('(38,24)','(38,19)'),('(7,23),(6,20)','(7,19),(6,18)'),('(42,20),(41,23)','(42,18),(41,19)')],
 'satellite':[('(35,10)','(34,10)'),('(39,6)','(38,6)'),('(43,10)','(42,10)'),('(39,14)','(38,14)'),('(9,42)','(32,42)')],
 'seasoning-chilli':[('(17,41),(27,37)','(15,34),(26,30)'),('(28,29)','(28,27)')],
 'sawmill':[("('L',(39,32)),",'')],
 'spa-lotus':[('(13,43),(7,37)','(13,40),(7,36)'),('(35,43),(41,37)','(35,40),(41,36)'),("('L',(9,29))", "('L',(9,29))" )],
 'swift-logo':[('(23,44),(12,39)','(23,40),(12,38)'),('(21,35)','(18,31)'),('(23,28)','(25,28)'),('(13,12)','(10,8)'),('(31,25)','(29,21)')],
}.items():
 key,label,ref,plan,body=DESIGNS[n]
 for a,b in replacements:body=body.replace(a,b)
 design(n,key,label,ref,plan,body)
for n,replacements in {
 'pine-f98a2e8b':[('(26,12)','(27,12)'),('(22,12)','(21,12)'),('(26,24)','(25,24)'),('(22,24)','(23,24)')],
 'explosion-sound-effect-text':[("('L',(42,34)),",'')],
 'monitor-heart-beat':[('(26,31)','(24,30)'),('(29,27)','(28,27)')],
 'satellite':[('(25,38)','(25,32)'),('(36,41),(31,40)','(36,36),(31,35)'),('(14,36),(6,32)','(14,32),(6,30)'),('(32,42)','(35,42)')],
 'music-clef':[('(24,36)','(24,34)'),('(8,35),(17,36)','(8,33),(17,34)'),('(31,36),(40,35)','(31,34),(40,33)')],
 'lightning-with-wrench':[('(12,38)','(14,38)'),('(29,6)','(31,6)'),('(23,12)','(24,12)'),('(34,42)','(32,42)')],
 'sawmill':[("('L',(42,18)),",'')],
}.items():
 key,label,ref,plan,body=DESIGNS[n]
 for a,b in replacements:body=body.replace(a,b)
 design(n,key,label,ref,plan,body)
design('spa-lotus','HRECT_L','Smooth layered lotus','flower-2','Preserve the layered open flower with broad central and side petals. Omit the two crowded basal curls while retaining the lotus silhouette.',"""
 path('center',(24,40),[('C',(24,8),(12,30),(14,18)),('C',(24,40),(34,18),(36,30))],True)
 path('left',(24,40),[('C',(4,20),(9,40),(4,31)),('C',(16,24),(9,20),(13,22))]);join('left','center')
 path('right',(24,40),[('C',(44,20),(39,40),(44,31)),('C',(32,24),(39,20),(35,22))]);join('right','center');join('left','right')
 """)
design('swift-logo','HRECT_L','Smooth flying bird emblem',None,'Preserve the swept wings and hooked flying-bird outline; broad returning curves retain the asymmetrical flight gesture.',"""
 path('bird',(4,16),[('L',(25,28)),('L',(10,8)),('L',(29,21)),('C',(30,8),(36,23),(34,15)),('C',(39,30),(42,17),(40,24)),('C',(44,39),(43,32),(44,35)),('C',(34,36),(40,36),(37,35)),('C',(22,40),(30,38),(27,40)),('C',(4,32),(14,40),(8,36)),('L',(18,31)),('C',(4,16),(12,27),(7,23))],True)
 """)
for n,replacements in {
 'satellite':[('(35,42)','(15,42)')],
 'sawmill':[('(31,42)','(30,42)'),('(28,27),(31,31)','(27,27),(30,31)')],
 'lightning-with-wrench':[('poly(\'bolt\',(39,23),(32,33),(42,33),(32,42))',"poly('bolt',(42,22),(29,32),(42,32),(32,42))")],
}.items():
 key,label,ref,plan,body=DESIGNS[n]
 for a,b in replacements:body=body.replace(a,b)
 design(n,key,label,ref,plan,body)
# Keep the strongest recognizable silhouettes for explicit exception review.
design('pine-f98a2e8b','VRECT_L','Three-tier pine — spacing review',None,'Attempted wider branch gaps and shorter tier overhangs. Keep three tiers and the trunk; the tight branch returns remain flagged for manual exception review.',"""
 path('tree',(24,4),[('L',(32,14)),('L',(27,14)),('C',(36,26),(27,20),(32,24)),('L',(29,26)),('C',(40,38),(29,32),(35,35)),('L',(24,38)),('L',(8,38)),('C',(19,26),(13,35),(19,32)),('L',(12,26)),('C',(21,14),(16,24),(21,20)),('L',(16,14)),('L',(24,4))],True)
 line('trunk',(24,38),(24,44));join('trunk','tree')
 """)
design('plane-1-travel','HRECT_L','Side-view plane — spacing review','plane','Attempted wider wing tips, wider fuselage and shortened tail. Keep this distinct horizontal plane; swept-wing returns still need a spacing exception review.',"""
 path('plane',(4,14),[('L',(16,20)),('L',(20,20)),('L',(14,8)),('L',(23,8)),('L',(27,20)),('L',(39,20)),('C',(44,24),(42,20),(44,22)),('C',(39,28),(44,26),(42,28)),('L',(27,28)),('L',(23,40)),('L',(14,40)),('L',(20,28)),('L',(16,28)),('L',(4,34)),('L',(8,24)),('L',(4,14))],True)
 """)
design('plane-1','HRECT_L','Ascending plane — spacing review','plane','Attempted broader wings and tail at several integer-grid positions. Preserve the ascending single-wing perspective; the wing and tail returns still need manual spacing review.',"""
 path('plane',(4,29),[('L',(16,40)),('L',(40,20)),('C',(44,13),(42,18),(44,16)),('C',(39,8),(44,10),(42,8)),('L',(29,16)),('L',(16,12)),('L',(9,17)),('L',(23,23)),('L',(17,29)),('L',(9,25)),('L',(4,29))],True)
 """)
design('plane','HRECT_L','Swept-wing plane — spacing review','plane','Attempted wider wing and tail returns. Preserve this distinct two-wing perspective; narrow diagonal channels still need a spacing exception review.',"""
 path('plane',(4,25),[('L',(14,33)),('L',(23,28)),('L',(20,40)),('L',(28,36)),('L',(32,24)),('L',(40,20)),('C',(44,14),(43,18),(44,16)),('C',(37,11),(44,10),(40,9)),('L',(32,14)),('L',(19,8)),('C',(16,13),(16,8),(14,11)),('L',(22,18)),('L',(14,22)),('L',(6,20)),('L',(4,25))],True)
 """)
design('adobe-cloud-logo','HRECT_L','Interlocking cloud — spacing review',None,'Attempted broader inner counters and shifted loop terminals. Preserve the interlocking cloud mark; the parallel diagonal loop cannot yet meet the four-unit ink gap without a substantial logo change.',"""
 path('outer',(16,40),[('C',(4,26),(9,40),(4,34)),('C',(16,13),(4,18),(9,13)),('C',(24,16),(19,13),(22,14)),('C',(32,8),(25,11),(28,8)),('C',(44,24),(40,8),(44,16)),('C',(32,40),(44,33),(39,40)),('L',(22,40)),('L',(16,40))],True)
 path('inner',(22,40),[('L',(13,30)),('C',(16,23),(9,25),(13,20)),('L',(28,36)),('L',(32,40))]);join('inner','outer')
 line('upper',(24,16),(30,23));join('upper','outer')
 """)
design('vimeo-logo','HRECT_L','Looping V — spacing review',None,'Attempted widening the looping counter and moving the returning stroke. Preserve the recognizable hooked V; its curved return still needs a spacing exception review.',"""
 path('mark',(4,17),[('C',(17,8),(9,12),(13,8)),('C',(22,22),(21,8),(21,17)),('C',(26,31),(23,29),(23,33)),('C',(34,19),(30,27),(34,22)),('C',(30,17),(35,15),(31,14)),('C',(44,14),(34,7),(43,8)),('C',(22,40),(44,25),(29,40)),('C',(14,29),(17,40),(16,34)),('L',(11,18)),('L',(4,17))],True)
 """)
design('picasa-logo','CIRCLE','Circular shutter — spacing review',None,'Attempted a roomier five-facet routing, but it changed the logo too much. Preserve the original facet arrangement; the narrow right rim band needs manual spacing review.',"""
 path('rim',(24,4),[('A',(36,8),20,20,True),('A',(44,24),20,20,True),('A',(40,36),20,20,True),('A',(24,44),20,20,True),('A',(12,40),20,20,True),('A',(4,24),20,20,True),('A',(8,12),20,20,True),('A',(24,4),20,20,True)],True)
 poly('diagonal',(8,12),(24,24),(36,36),(40,36));join('diagonal','rim')
 poly('right',(36,8),(36,36));join('right','rim');join('right','diagonal')
 poly('left',(4,24),(16,24),(24,24));join('left','rim');join('left','diagonal')
 poly('bottom',(12,40),(16,36),(16,24));join('bottom','rim');join('bottom','left')
 line('bar',(16,36),(36,36));join('bar','bottom');join('bar','diagonal');join('bar','right')
 """)
design('dragon-fruit','VRECT_L','Crowned fruit — spacing review',None,'Attempted three broader crown leaves, but that removed the distinctive spiky fruit shape. Preserve five crown points; their short returns need manual spacing review.',"""
 path('fruit',(8,20),[('L',(12,22)),('L',(14,10)),('L',(19,15)),('L',(24,4)),('L',(29,15)),('L',(34,10)),('L',(36,22)),('L',(40,20)),('C',(24,44),(39,36),(35,44)),('C',(8,20),(13,44),(9,36))],True)
 """)
design('satellite','SQUARE','Smooth satellite dish',None,'Preserve the diagonal bowl, feed and triangular pedestal. Split the bowl at two exact stand attachments.',"""
 path('dish',(12,6),[('L',(24,18)),('L',(42,36)),('C',(25,32),(36,36),(31,35)),('C',(14,28),(21,31),(17,30)),('C',(6,20),(9,25),(6,23)),('C',(12,6),(6,14),(8,10))],True)
 poly('base',(14,28),(6,42),(30,42),(25,32));join('base','dish')
 line('feed',(24,18),(34,10));path('receiver',(34,10),[('A',(38,6),4,4,True),('A',(42,10),4,4,True),('A',(38,14),4,4,True),('A',(34,10),4,4,True)],True);join('receiver','feed');join('feed','dish')
 """)
