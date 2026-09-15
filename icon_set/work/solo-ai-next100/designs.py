"""Individually reviewed standalone subjects, preserving original identities."""
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-next100/selected.json'
AUTHOR='gpt-6'

design('building-building','SQUARE','building-2','Keep a broad high-rise and lower right annex; exact baseline and a centered upper window.', """
poly('tower',(10,42),(10,6),(32,6),(32,42))
poly('annex',(32,18),(42,23),(42,42),(6,42));join('tower','annex')
line('window',(19,16),(23,16))
""")
design('building-c2e118c4','SQUARE','building-2','Preserve the asymmetric sloped roof and low left annex. The roof mast and facade meet at exact nodes.', """
poly('tower',(22,42),(22,6),(36,15),(42,19),(42,42),(6,42),(6,22),(22,22));join('tower','tower')
line('mast',(36,6),(36,15));join('mast','tower')
line('window',(6,32),(12,32));join('window','tower')
""")
design('building-dac12e36','SQUARE','building-2','A wider main facade and narrow setback annex distinguish this source while retaining its stepped silhouette.', """
poly('tower',(8,42),(8,6),(34,6),(34,42))
poly('annex',(34,20),(42,24),(42,42),(6,42));join('tower','annex')
line('window',(18,17),(24,17))
""")
design('buildings','VRECT_L','building-2','Maintain a sloped main roof, lower neighboring block and entrance rooted on their shared baseline.', """
poly('main',(8,44),(8,4),(28,16),(28,44),(8,44))
poly('annex',(28,16),(40,16),(40,44),(28,44));join('main','annex')
line('door',(18,44),(18,36));join('door','main')
""")
for name,cherry in [('cake',False),('cake-cherry',True)]:
 design(name,'HRECT_L','cake-slice','Keep the wedge of cake and its round cherry; smooth the curved back and preserve a broad lower cake layer.'+(' Add a short natural cherry stem.' if cherry else ''),f"""
circle('cherry',25,{'16' if cherry else '13'},5)
path('cake',(4,30),[('C',(20,{'16' if cherry else '13'}),(4,20),(12,{'16' if cherry else '13'})),('A',(25,{'21' if cherry else '18'}),5,5,False),('A',(30,{'16' if cherry else '13'}),5,5,False),('L',(44,30)),('L',(44,40)),('L',(4,40)),('L',(4,30))],True)
line('layer',(4,30),(44,30));join('layer','cake');join('cake','cherry')
"""+("path('stem',(25,11),[('C',(35,8),(26,8),(31,8))]);join('stem','cherry')" if cherry else ''))
design('camping-tent','HRECT_L','tent','A low wide tent with paired poles and a centered doorway. Mirrored coordinates keep the pitch even.', """
poly('canvas',(4,40),(24,12),(44,40),(4,40))
poly('poles',(20,8),(24,12),(28,8));join('poles','canvas')
poly('door',(16,40),(24,26),(32,40));join('door','canvas')
""")
design('camping-tent-outdoors','SQUARE','tent','Retain the arched dome tent, with matching outer slopes and a roomy arched entrance.', """
path('tent',(6,42),[('C',(24,6),(10,24),(16,6)),('C',(42,42),(32,6),(38,24)),('L',(32,42)),('L',(16,42)),('L',(6,42))],True)
path('door',(16,42),[('C',(24,20),(17,30),(20,20)),('C',(32,42),(28,20),(31,30))]);join('door','tent')
""")
design('can','VRECT_L','cylinder','A cylindrical can with a true elliptical rim and mirrored base; replace the uneven traced rim with coherent arcs.', """
path('rim',(8,10),[('A',(40,10),16,6,True),('A',(8,10),16,6,True)],True)
path('body',(8,10),[('L',(8,38)),('A',(40,38),16,6,False),('L',(40,10))]);join('body','rim')
""")
design('canoe','HRECT_L',None,'Preserve the broad canoe with raised ends and a scooped gunwale; both ends share curvature and the hull stays low.', """
path('hull',(4,8),[('C',(24,21),(8,17),(16,21)),('C',(44,8),(32,21),(40,17)),('L',(44,18)),('C',(24,40),(44,36),(38,40)),('C',(4,18),(10,40),(4,36)),('L',(4,8))],True)
""")
design('canoe-paddles','SQUARE',None,'Two diagonal canoe paddles share one blade definition and a central crossing; preserve the crossed-paddle meaning.', """
poly('blade-left',(6,10),(10,6),(19,15),(19,19),(15,19),(6,10))
poly('blade-right',(42,10),(38,6),(29,15),(29,19),(33,19),(42,10))
poly('shaft-left',(19,19),(24,24),(42,42));poly('shaft-right',(29,19),(24,24),(6,42))
join('shaft-left','blade-left');join('shaft-right','blade-right');join('shaft-left','shaft-right')
""")
# Car families retain the source roof types. All wheels share a native-size radius.
cars={
 'car':([(4,27),(8,22),(13,10),(18,8),(26,8),(32,20),(40,23),(44,27)],False),
 'car-2':([(4,25),(12,8),(25,8),(34,22),(41,22),(44,27)],True),
 'car-5e6ba5b0':([(4,27),(8,22),(13,8),(27,8),(34,22),(40,22),(44,27)],False),
 'car-796e3289':([(4,27),(9,21),(13,11),(19,8),(26,8),(32,21),(41,25),(44,29)],False),
 'car-9e5f3201':([(4,28),(10,22),(16,8),(28,8),(36,22),(40,22),(44,28)],False),
 'car-eaa7f06c':([(4,28),(9,23),(13,8),(26,8),(34,23),(40,23),(44,28)],False),
 'car-side':([(4,26),(9,22),(16,8),(27,8),(36,22),(42,24),(44,28)],False),
 'car-transportation':([(4,27),(4,21),(12,10),(19,8),(27,8),(36,20),(44,25)],False)}
for name,(roof,divider) in cars.items():
 body="""
for x in (12,36):circle(f'wheel-{x}',x,35,5)
"""+f"poly('body',(7,35),(4,35),*{roof!r},(44,35),(41,35))\n"+"line('sill',(17,35),(31,35));join('body','wheel-12');join('body','wheel-36');join('sill','wheel-12');join('sill','wheel-36')\n"
 if name in ('car-2','car-5e6ba5b0','car-9e5f3201'):body+="line('belt',(8,22),(34,22));join('belt','body')\n" if name=='car-5e6ba5b0' else ("line('belt',(4,25),(34,22));join('belt','body')\n" if name=='car-2' else "line('belt',(10,22),(36,22));join('belt','body')\n")
 if divider:body+="line('pillar',(21,8),(21,23));join('pillar','body');join('pillar','belt')\n"
 if name=='car-transportation':body+="line('door-handle',(18,22),(23,22))\n"
 design(name,'HRECT_L','car','Preserve the source compact car roof and stance, with two equal round wheels and a clean open wheel line. Roof slopes and body proportions distinguish this variant.',body)
for name,roof in [('car-e1ae9ac1',32),('car-retro',34)]:
 design(name,'HRECT_L','car','Retain the rounded vintage roof and split cabin, with smooth matching wheel circles and a lower horizontal body.',f"""
for x in (12,36):circle(f'wheel-{{x}}',x,35,5)
path('body',(7,35),[('L',(4,35)),('L',(4,28)),('A',(10,22),6,6,True),('L',(38,22)),('A',(44,28),6,6,True),('L',(44,35)),('L',(41,35))])
line('sill',(17,35),(31,35));join('body','wheel-12');join('body','wheel-36');join('sill','wheel-12');join('sill','wheel-36')
path('roof',(12,22),[('C',(24,8),(12,14),(16,8)),('C',({roof},22),(30,8),({roof},14))]);join('roof','body')
line('pillar',({'24' if roof==32 else '25'},8),({'24' if roof==32 else '25'},22));join('pillar','roof');join('pillar','body')
""")
design('cargo-ship-symbol','SQUARE','ship','Keep the forward-facing cargo ship, stepped deckhouse and low waves. Shared axis keeps the bow and deck balanced.', """
poly('cabin',(12,20),(12,14),(19,14),(19,6),(29,6),(29,14),(36,14),(36,20))
poly('hull',(10,39),(6,23),(24,20),(42,23),(38,39));join('hull','cabin')
path('water',(6,42),[('L',(10,39)),('L',(17,42)),('L',(24,39)),('L',(31,42)),('L',(38,39)),('L',(42,42))]);join('water','hull')
""")
for name,style in [('cart',0),('cart-e3de8236',1),('cart-spas',2)]:
 design(name,'HRECT_L','shopping-basket','Keep the source hand basket; paired handles share endpoints with its rim. Each basket retains a different taper or handle construction.',f"""
poly('basket',(4,20),(44,20),({36+style},40),({12-style},40),(4,20))
poly('handle-left',(12,20),({20-style},8));poly('handle-right',({28+style},8),(36,20));join('handle-left','basket');join('handle-right','basket')
"""+("line('weave',(24,20),(24,40));join('weave','basket')" if style==2 else ''))
for name,style in [('cart-d135db2c',0),('cart-e7cacb27',1),('cart-shopping',2)]:
 design(name,'HRECT_L','shopping-cart','Retain the wheeled shopping cart, its handle direction and a broad basket. Round wheel dots match and remain clear of the basket.',f"""
poly('basket',({4 if style!=1 else 12},16),({40 if style!=1 else 44},16),({32 if style!=1 else 38},30),({12 if style!=1 else 16},30),({4 if style!=1 else 12},16))
"""+("poly('handle',(4,8),(9,8),(12,16));join('handle','basket')\n" if style==1 else "poly('handle',(40,16),(44,8));join('handle','basket')\n")+f"self.add_dot('wheel-left',({16 if style!=2 else 14},40));self.add_dot('wheel-right',({30 if style!=2 else 32},40))")
design('cashew','SQUARE',None,'Restore a smooth crescent-shaped cashew with broad rounded ends and a soft inner curve.', """
path('nut',(25,9),[('C',(42,20),(34,0+6),(42,9)),('C',(19,42),(42,34),(33,42)),('C',(6,30),(10,42),(6,37)),('C',(15,25),(6,24),(10,23)),('C',(25,20),(23,29),(28,24)),('C',(25,9),(22,14),(22,11))],True)
""")
design('casino-chip-1','CIRCLE','disc','A circular chip with a centered ring and four diagonal radial sectors; matched sectors keep rotational balance.', """
circle('rim',24,24,20);circle('core',24,24,10)
for i,(a,b) in enumerate([((10,10),(17,17)),((38,10),(31,17)),((38,38),(31,31)),((10,38),(17,31))]):
 line(f'sector-{i}',a,b);join(f'sector-{i}','rim');join(f'sector-{i}','core')
""")
design('casino-clover','SQUARE','clover','Retain the three-leaf casino clover with heart-shaped leaves and a short stem. Shared left/right geometry keeps the emblem balanced.', """
path('leaf',(24,30),[('C',(9,34),(13,42),(6,39)),('C',(9,24),(6,29),(6,25)),('C',(6,17),(3+3,23),(6,20)),('C',(17,16),(6,11),(12,12)),('C',(15,9),(12,12),(12,6)),('C',(24,10),(18,6),(20,6)),('C',(33,9),(28,6),(30,6)),('C',(31,16),(36,6),(36,12)),('C',(42,17),(36,12),(42,11)),('C',(39,24),(42,20),(42,23)),('C',(39,34),(42,25),(42,29)),('C',(24,30),(42,39),(35,42))],True)
line('stem',(24,30),(24,42));join('stem','leaf')
""")
design('cat-bed','HRECT_L',None,'Keep the oval pet bed and lowered front entry. A shared elliptical rim makes both ends equal without flattening the cushion.', """
path('back',(4,20),[('A',(44,20),20,12,True)])
path('front',(4,20),[('L',(4,30)),('A',(44,30),20,10,False),('L',(44,20)),('L',(34,24)),('L',(32,30)),('L',(16,30)),('L',(14,24)),('L',(4,20))],True);join('front','back')
""")
design('cat-cat-ball','CIRCLE','disc','A basketball-like cat ball has a true circular outline and mirrored panel arcs around a centered cross.', """
path('rim',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
poly('horizontal',(4,24),(24,24),(44,24));poly('vertical',(24,4),(24,24),(24,44));join('horizontal','rim');join('vertical','rim');join('horizontal','vertical')
for side in (-1,1):
 x=lambda d:24+side*d
 path(f'panel-{side}',(x(14),10),[('C',(x(9),24),(x(10),14),(x(9),19)),('C',(x(14),38),(x(9),29),(x(10),34))]);join(f'panel-{side}','rim');join(f'panel-{side}','horizontal')
""")
design('cat-toy','SQUARE',None,'Preserve the round toy and its loose curved string. Fewer smooth curves replace the wavering trace.', """
circle('ball',16,16,10)
path('string',(24,22),[('C',(42,30),(28,28),(42,24)),('C',(30,36),(42,35),(38,36)),('L',(26,36)),('A',(26,42),3,3,False),('L',(30,42))]);join('string','ball')
""")
design('cauldron','HRECT_L','cooking-pot','A round-bellied cauldron keeps a flared lip and broad base. Paired shoulders and the belly use mirrored curves.', """
path('pot',(8,8),[('L',(40,8)),('A',(40,14),3,3,True),('L',(38,14)),('L',(44,23)),('C',(24,40),(43,36),(35,40)),('C',(4,23),(13,40),(5,36)),('L',(10,14)),('L',(8,14)),('A',(8,8),3,3,True)],True)
""")
for name,r in [('cd',5),('cd-electronics',10)]:design(name,'CIRCLE','disc','Preserve the disc and its source hub size. Both boundaries are true concentric circles.',f"circle('disc',24,24,20)\ncircle('hub',24,24,{r})")
design('ceiling-ball-chandelier-retro','SQUARE','lamp-ceiling','A three-globe chandelier keeps a level arm and matched oval lamps; shared suspension nodes avoid uneven traced joins.', """
line('ceiling',(18,6),(30,6));poly('stem',(24,6),(24,20),(24,34));join('stem','ceiling')
poly('arm',(8,34),(8,20),(24,20),(40,20),(40,34));join('arm','stem')
for x in (10,24,38):
 path(f'globe-{x}',(x,34),[('A',(x,42),4,4,True),('A',(x,34),4,4,True)],True)
 join(f'globe-{x}','stem' if x==24 else 'arm')
""")
design('ceiling-lamp-double','HRECT_L','lamp-ceiling','A two-shade ceiling fixture uses one mirrored shade definition and matching hanging arms.', """
line('ceiling',(14,8),(34,8));line('stem',(24,8),(24,20));join('stem','ceiling')
path('arms',(12,28),[('L',(12,24)),('A',(16,20),4,4,True),('L',(24,20)),('L',(32,20)),('A',(36,24),4,4,True),('L',(36,28))]);join('arms','stem')
for x in (12,36):
 path(f'shade-{x}',(x-8,40),[('L',(x-5,31)),('C',(x,28),(x-4,29),(x-2,28)),('C',(x+5,31),(x+2,28),(x+4,29)),('L',(x+8,40)),('L',(x-8,40))],True);join(f'shade-{x}','arms')
""")
for name,base in [('ceramic',8),('ceramic-tool',12)]:
 design(name,'VRECT_L','amphora','Preserve the vase neck, full belly and narrow foot. Shared axis mirrors the two continuous walls; the foot width distinguishes the vessel.',f"""
path('vase',(16,4),[('L',(32,4)),('C',(40,22),(30,10),(40,14)),('C',({48-base},44),(40,31),({48-base},35)),('L',({base},44)),('C',(8,22),({base},35),(8,31)),('C',(16,4),(8,14),(18,10))],True)
""")
design('champagne-glass','VRECT_L','wine','Keep the generous angular bowl and long central stem; mirrored bowl walls smooth into the stem junction.', """
path('bowl',(12,4),[('L',(36,4)),('L',(40,18)),('C',(24,28),(40,25),(29,26)),('C',(8,18),(19,26),(8,25)),('L',(12,4))],True)
line('stem',(24,28),(24,44));line('foot',(12,44),(36,44));join('stem','bowl');join('stem','foot')
""")
design('check-towing-device','SQUARE',None,'Keep the tow hook as a long bent shank with a round towing eye; a tangent quarter-circle replaces the kinked elbow.', """
circle('eye',34,14,8)
path('hook',(34,22),[('L',(34,32)),('A',(24,42),10,10,True),('L',(6,42))]);join('hook','eye')
""")
design('chef-gear-biscuits-cup','SQUARE','cup-soda','Two broad biscuit sticks sit in a tapered cup. Their rounded tips and shared rim attachments retain the original snack reading.', """
poly('cup',(8,22),(40,22),(34,42),(14,42),(8,22))
path('left-biscuit',(14,22),[('L',(7,11)),('C',(16,6),(6,6),(11,6)),('L',(24,22))]);join('left-biscuit','cup')
path('right-biscuit',(24,22),[('L',(32,6)),('C',(41,11),(37,6),(42,6)),('L',(34,22))]);join('right-biscuit','cup');join('left-biscuit','right-biscuit')
""")
design('chef-gear-cookie-bowl','SQUARE',None,'Preserve a bitten cookie in its bowl. The cookie has a few clear bite arcs and the bowl keeps a stable foot.', """
path('bowl',(6,24),[('L',(42,24)),('C',(34,36),(41,30),(37,34)),('L',(34,42)),('L',(14,42)),('L',(14,36)),('C',(6,24),(11,34),(7,30))],True)
path('cookie',(10,24),[('C',(26,6),(8,12),(18,6)),('C',(31,13),(25,12),(27,13)),('C',(36,20),(30,18),(33,20)),('L',(38,24))]);join('cookie','bowl')
""")
for name,style in [('chef-gear-mug',0),('cup',1),('cup-1',2)]:
 design(name,'HRECT_L','coffee','Keep the source cup bowl and a full-size handle opening. Rounded base corners and handle radii are coherent; cup depth and handle profile distinguish this version.',f"""
path('cup',(4,8),[('L',(32,8)),('L',(32,16)),('L',(32,30)),('A',(22,40),10,10,True),('L',(14,40)),('A',(4,30),10,10,True),('L',(4,8))],True)
"""+("path('handle',(32,16),[('L',(36,16)),('A',(44,24),8,8,True),('A',(36,32),8,8,True),('L',(32,32))]);join('handle','cup')" if style!=2 else "poly('handle',(32,16),(40,16),(44,22),(44,28),(40,32),(32,32));join('handle','cup')"))
design('chess-pawn','VRECT_L',None,'A pawn retains its oval head, tapered neck and broad pedestal; true ellipse geometry replaces irregular head segments.', """
path('head',(24,4),[('A',(24,20),12,8,True),('A',(24,4),12,8,True)],True)
poly('neck',(18,19),(14,34),(34,34),(30,19));join('neck','head')
path('base',(14,34),[('L',(34,34)),('A',(40,40),6,6,True),('L',(40,44)),('L',(8,44)),('L',(8,40)),('A',(14,34),6,6,True)],True);join('base','neck')
""")
for name,tip in [('chilli',30),('chilli-jelapeno',34)]:
 design(name,'HRECT_L',None,'A curved pepper keeps its pointed left tip, plump right shoulder and curved stem. The longer lower curve distinguishes this source.',f"""
path('pepper',(4,24),[('C',(32,17),(15,{tip}),(25,20)),('C',(40,18),(36,13),(40,14)),('C',(21,40),(44,27),(33,40)),('C',(4,24),(13,40),(7,32))],True)
path('stem',(40,18),[('C',(40,8),(44,16),(44,8)),('L',(38,8))]);join('stem','pepper')
""")
for name,radius in [('chip',0),('chip-symbol',5),('computer-chip',3)]:
 design(name,'SQUARE','microchip','Preserve the square chip with paired leads; each axis uses shared pin spacing and exact body contacts. Corner radius retains this variant identity.',f"""
"""+(f"rounded('body',14,14,34,34,{radius})\n" if radius else "poly('body',(14,14),(34,14),(34,34),(14,34),closed=True)\n")+"""
for p in (20,28):
 for k,a,b in [('t',(p,6),(p,14)),('b',(p,34),(p,42)),('l',(6,p),(14,p)),('r',(34,p),(42,p))]:
  line(f'{k}-{p}',a,b);join(f'{k}-{p}','body')
""")
design('chocolate-bar','VRECT_L',None,'Keep the exposed chocolate grid and folded wrapper; broad divisions preserve the food silhouette without tiny squares.', """
poly('bar',(12,22),(12,4),(36,4),(36,22));poly('grid',(12,13),(24,13),(36,13));line('divide',(24,4),(24,22));join('grid','bar');join('divide','grid');join('divide','bar')
path('wrapper',(8,22),[('L',(16,22)),('L',(24,28)),('L',(40,22)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,22))],True);join('wrapper','bar')
""")
design('chocolate-box','HRECT_L',None,'Keep the heart-shaped chocolate box in perspective. Two matching lobes lead to the central point; the lower edge describes box depth.', """
path('lid',(24,13),[('C',(4,16),(14,4),(4,8)),('L',(24,31)),('L',(44,16)),('C',(24,13),(44,8),(34,4))],True)
poly('depth',(4,16),(4,25),(24,40),(44,25),(44,16));line('seam',(24,31),(24,40));join('depth','lid');join('seam','depth');join('seam','lid')
""")
design('christmas-sock','VRECT_L','sock','Retain a broad stocking cuff, long ankle and left-facing rounded toe. A coherent heel curve replaces the wavering trace.', """
rounded('cuff',16,4,40,13,4)
path('sock',(20,13),[('L',(20,24)),('L',(12,29)),('C',(8,36),(8,31),(8,33)),('C',(17,44),(8,41),(12,44)),('L',(30,40)),('C',(36,32),(35,39),(36,36)),('L',(36,13))]);join('sock','cuff')
""")
# Drawing compasses: preserve the diagonal instrument, not a navigation badge.
for name,wide in [('circinus',False),('circinus-state',True)]:
 design(name,'SQUARE',None,'A drafting compass keeps its round hinge and two angled legs. The two leg spreads differ, retaining the source instrument posture.',f"""
circle('hinge',32,14,8)
line('top',(38,8),(40,6));join('top','hinge')
poly('left-leg',(26,20),(6,{'34' if wide else '32'}));join('left-leg','hinge')
poly('right-leg',(34,22),({'24' if wide else '26'},42));join('right-leg','hinge')
poly('brace',(19,25),(30,32),(35,34));join('brace','left-leg');join('brace','right-leg')
""")
design('classical-piano','SQUARE','piano','Keep the asymmetric grand-piano lid and broad keyboard, with level legs and a smooth shoulder.', """
path('lid',(12,26),[('L',(12,6)),('L',(20,6)),('C',(32,16),(24,6),(23,16)),('L',(36,16)),('A',(42,22),6,6,True),('L',(42,26))])
poly('keys',(10,26),(42,26),(42,36),(6,36),(10,26));join('keys','lid')
for x in (12,36):line(f'leg-{x}',(x,36),(x,42));join(f'leg-{x}','keys')
""")
for name,hour in [('clock-4ab76b4c',(32,31)),('clock-4e5cefd6',(33,28)),('clock-office',(31,32))]:
 design(name,'CIRCLE','clock','Keep a round clock face and bent hands; true circular construction and one shared center remove the uneven trace. The hand angle distinguishes this clock.',f"circle('face',24,24,20)\npoly('hands',(24,13),(24,24),{hour!r})")
for name,high in [('cloud',True),('cloud-internet',False)]:
 design(name,'HRECT_L','cloud','Keep the source cloud as a single lobed outline. A high central dome and matched lower corners preserve a soft cloud silhouette.', """
path('cloud',(14,40),[('C',(4,29),(8,40),(4,35)),('C',(12,18),(4,22),(7,18)),('C',(24,8),(13,11),(17,8)),('C',(36,18),(31,8),(35,11)),('C',(44,29),(41,18),(44,22)),('C',(34,40),(44,35),(40,40)),('L',(14,40))],True)
""" if high else """
path('cloud',(14,40),[('C',(4,29),(8,40),(4,35)),('C',(12,19),(4,23),(7,19)),('C',(23,8),(13,12),(17,8)),('C',(36,21),(31,8),(36,13)),('C',(44,30),(41,21),(44,24)),('C',(34,40),(44,36),(40,40)),('L',(14,40))],True)
""")
for name,stem in [('clover',20),('clover-symbol',26)]:
 design(name,'SQUARE','clover','Four heart-like leaves share one rotated definition around the center; a gently bent stem preserves the organic clover identity.',f"""
quarter=[('C',(8,10),(10,20),(6,17)),('C',(16,10),(10,6),(13,6)),('C',(24,6),(16,6),(20,6)),('C',(24,24),(32,6),(31,15))]
turn=lambda p,n:p if n==0 else turn((48-p[1],p[0]),n-1)
# Three broad lobes and a lower-left lobe retain four-leaf reading.
for n in range(4):
 path(f'leaf-{{n}}',turn((24,24),n),[(k,turn(e,n),turn(a,n),turn(b,n)) for k,e,a,b in quarter],True)
 for m in range(n):join(f'leaf-{{n}}',f'leaf-{{m}}')
path('stem',(24,24),[('C',({stem},42),(25,34),({stem},38))])
for n in range(4):join('stem',f'leaf-{{n}}')
""")
design('cocktail','VRECT_L','martini','Keep the rounded cocktail bowl, central stem and angled straw, with a wider opening and clean shared lip contact.', """
path('bowl',(8,16),[('L',(31,16)),('L',(40,16)),('A',(24,32),16,16,True),('A',(8,16),16,16,True)],True)
poly('straw',(24,24),(31,16),(35,6),(40,4));join('straw','bowl')
line('stem',(24,32),(24,44));line('foot',(16,44),(32,44));join('stem','bowl');join('stem','foot')
""")
design('cocktail-martini','VRECT_L','martini','Retain the classic triangular martini glass with a centered stem and level foot; all joins use shared points.', """
poly('bowl',(8,4),(40,4),(24,24),(8,4));line('stem',(24,24),(24,44));line('foot',(16,44),(32,44));join('stem','bowl');join('stem','foot')
""")
design('coffee-aeropress','VRECT_L',None,'Preserve the press plunger, straight chamber and flared lower filter stand. Shared vertical walls and wide bands keep the mechanism readable.', """
line('top',(12,4),(36,4));poly('chamber',(16,4),(16,24),(16,34),(8,40),(12,44),(36,44),(40,40),(32,34),(32,24),(32,4));join('top','chamber')
line('band',(8,24),(40,24));line('base-band',(16,34),(32,34));join('band','chamber');join('base-band','chamber')
""")
for name,kind in [('cog-1',0),('cog-4c6e5052',1)]:
 design(name,'SQUARE','cog','Preserve the gear silhouette using a repeated quarter definition. Shared tooth widths and exact rotational copies remove wavy unequal teeth.',f"""
quarter={([(20,6),(28,6),(30,11),(35,11),(37,13),(37,18),(42,20),(42,28)] if kind==0 else [(20,6),(28,6),(28,11),(33,13),(37,10),(42,15),(38,19),(39,20),(42,20),(42,28)])!r}
turn=lambda p,n:p if n==0 else turn((48-p[1],p[0]),n-1)
points=[]
for n in range(4):points.extend(turn(p,n) for p in quarter[:-1])
poly('gear',*points,closed=True)
""")
design('condom','VRECT_L',None,'Keep the packet with regular sealed teeth at the top and bottom; the central packet remains spacious.', """
points=[(8,4),(12,8),(16,4),(20,8),(24,4),(28,8),(32,4),(36,8),(40,4),(40,44),(36,40),(32,44),(28,40),(24,44),(20,40),(16,44),(12,40),(8,44)]
poly('packet',*points,closed=True)
""")
design('cone','VRECT_L','cone','Preserve the upright cone with symmetric sloping sides and a smooth curved base.', """
path('cone',(24,4),[('L',(40,38)),('C',(24,44),(36,42),(29,44)),('C',(8,38),(19,44),(12,42)),('L',(24,4))],True)
""")
design('console-drawers','HRECT_L',None,'Keep the low console with open left bay and two right drawers. Repeated grid positions keep shelf spacing even.', """
poly('cabinet',(4,8),(44,8),(44,34),(4,34),(4,8));line('partition',(24,8),(24,34));line('shelf',(24,21),(44,21));join('partition','cabinet');join('shelf','partition');join('shelf','cabinet')
for x in (8,40):line(f'leg-{x}',(x,34),(x,40));join(f'leg-{x}','cabinet')
""")
design('content-pen','SQUARE','pen','Keep the diagonal pencil with a long broad shaft and pointed tip; clean corners replace traced wavering edges.', """
poly('pencil',(6,42),(10,30),(34,6),(42,14),(18,38),(6,42))
""")
design('controls-movie','HRECT_L','clapperboard','Retain the clapperboard and diagonal upper stripes. Regular strip spacing and equal body corners smooth the original.', """
rounded('body',4,8,44,40,4);line('rim',(4,18),(44,18));join('rim','body')
for a,b in [((10,18),(20,8)),((28,18),(38,8))]:line(f'stripe-{a[0]}',a,b);join(f'stripe-{a[0]}','body');join(f'stripe-{a[0]}','rim')
line('lower',(4,32),(44,32));join('lower','body')
""")
design('convertible','HRECT_L','car','Keep the open-top car and lowered seat section. Two equal wheels balance the short body without closing the cabin.', """
for x in (12,36):circle(f'wheel-{x}',x,35,5)
path('body',(7,35),[('L',(4,35)),('L',(4,18)),('L',(17,18)),('C',(27,22),(19,26),(24,27)),('L',(30,16)),('L',(40,18)),('A',(44,22),4,4,True),('L',(44,35)),('L',(41,35))])
line('sill',(17,35),(31,35));join('body','wheel-12');join('body','wheel-36');join('sill','wheel-12');join('sill','wheel-36')
line('windshield',(12,18),(12,8));line('seat',(30,16),(28,8));join('windshield','body');join('seat','body')
""")
design('corn','VRECT_L',None,'Keep a rounded cob emerging between two broad husk leaves. Mirrored leaf curves join at the lower tip.', """
path('cob',(16,29),[('L',(16,12)),('A',(32,12),8,8,True),('L',(32,29))])
path('husk',(8,22),[('C',(24,44),(10,32),(10,44)),('C',(40,22),(38,44),(38,32)),('C',(24,44),(29,23),(24,33)),('C',(8,22),(24,33),(19,23))],True);join('husk','cob')
""")
design('crane-hook','VRECT_L',None,'Preserve the pulley block and hanging hook. A diagonal block seam and a smooth open hook keep the tool recognizable.', """
poly('block',(8,4),(40,4),(40,17),(31,26),(17,26),(8,17),(8,4))
line('diagonal',(8,17),(32,4));join('diagonal','block')
path('hook',(24,26),[('L',(24,30)),('C',(16,36),(17,30),(16,32)),('C',(27,44),(16,42),(21,44)),('C',(36,36),(33,44),(36,41))]);join('hook','block')
""")
design('crown','HRECT_L','crown','Preserve the three-point crown with a low broad base; exact mirroring balances the center peak and side points.', """
poly('crown',(4,12),(15,23),(24,8),(33,23),(44,12),(41,40),(7,40),closed=True)
""")
for name,top in [('cub',6),('cube',10),('cube-shape',8)]:
 design(name,'SQUARE','box','Preserve the isometric box as three broad faces with a shared center junction. Top-face depth differentiates the original variant.',f"""
poly('box',(24,6),(42,{top+10}),(42,32),(24,42),(6,32),(6,{top+10}),closed=True)
poly('seams',(6,{top+10}),(24,{top+20}),(42,{top+10}));line('vertical',(24,{top+20}),(24,42));join('seams','box');join('vertical','seams');join('vertical','box')
""")
design('cupcake','VRECT_L','cake','Retain the cherry-topped cupcake, scalloped frosting and tapered wrapper; reduce tiny creases to one central wrapper fold.', """
circle('cherry',24,12,4)
path('stem',(24,8),[('C',(32,4),(24,4),(28,4))]);join('stem','cherry')
path('frosting',(8,28),[('C',(20,12),(8,21),(14,14)),('A',(28,12),4,4,False),('C',(40,28),(34,14),(40,21)),('C',(30,28),(37,33),(33,33)),('C',(18,28),(27,33),(21,33)),('C',(8,28),(15,33),(11,33))],True);join('frosting','cherry')
poly('wrapper',(12,31),(16,44),(32,44),(36,31));join('wrapper','frosting')
line('fold',(24,31),(24,44));join('fold','wrapper');join('fold','frosting')
""")
design('curtains-open','SQUARE',None,'Preserve two tied-back curtain panels. One mirrored definition owns their drape, tie heights and lower hems.', """
line('rod',(6,6),(42,6))
for side in (-1,1):
 x=lambda d:24+side*d
 path(f'panel-{side}',(x(2),6),[('L',(x(18),6)),('L',(x(18),42)),('L',(x(8),42)),('C',(x(11),25),(x(8),34),(x(10),29)),('C',(x(2),6),(x(5),21),(x(2),13))],True)
 line(f'tie-{side}',(x(18),25),(x(11),25));join(f'tie-{side}',f'panel-{side}');join(f'panel-{side}','rod')
""")
for name,levels,wide in [('data',2,True),('data-servers',2,False),('database',3,False),('database-diagrams',2,True),('database-servers',2,False)]:
 design(name,'VRECT_L','database','Preserve the stacked cylindrical database, with level elliptical rings and exact side contacts. Ring count and rim depth retain its source structure.',f"""
path('top',(8,10),[('A',(40,10),16,6,True),('A',(8,10),16,6,True)],True)
path('body',(8,10),[('L',(8,38)),('A',(40,38),16,6,False),('L',(40,10))]);join('body','top')
for y in {([20,30] if levels==3 else ([24] if wide else [26]))!r}:
 path(f'ring-{{y}}',(8,y),[('A',(40,y),16,{'5' if wide else '6'},False)]);join(f'ring-{{y}}','body')
""")
design('dating-lips','HRECT_L',None,'Keep a cupid-bow mouth with a broad lower lip and slight center dip. Mirror the lip halves for a natural balanced smile.', """
path('lips',(4,24),[('C',(18,8),(9,16),(13,8)),('C',(24,11),(21,8),(22,11)),('C',(30,8),(26,11),(27,8)),('C',(44,24),(35,8),(39,16)),('C',(24,40),(39,34),(33,40)),('C',(4,24),(15,40),(9,34))],True)
path('mouth',(4,24),[('L',(16,24)),('C',(24,26),(20,24),(20,26)),('C',(32,24),(28,26),(28,24)),('L',(44,24))]);join('mouth','lips')
""")
design('death-coffin','VRECT_L',None,'Keep the tapered coffin and central cross; the six straight sides use paired coordinates and generous inner space.', """
poly('coffin',(16,4),(32,4),(40,16),(34,44),(14,44),(8,16),closed=True)
poly('cross',(24,15),(24,20),(24,31));poly('arms',(18,20),(24,20),(30,20));join('cross','arms')
""")
design('delicata-squash','SQUARE',None,'Preserve the diagonal oval squash and single lengthwise rib. A smooth oval with pointed poles replaces the irregular trace.', """
path('squash',(6,42),[('C',(38,10),(6,20),(21,6)),('C',(6,42),(42,25),(27,42))],True)
poly('rib',(6,42),(38,10),(42,6));join('rib','squash')
""")
for name,slant in [('delivery-truck',False),('delivery-truck-delivery',True)]:
 design(name,'HRECT_L','truck','Keep the tall cargo box and short cab, with consistent round wheels and a distinct cab roof profile.',f"""
for x in (12,36):circle(f'wheel-{{x}}',x,35,5)
poly('cargo',(7,35),(4,35),(4,8),(28,8),(28,35),(17,35));join('cargo','wheel-12')
poly('cab',(28,16),({'36' if slant else '38'},16),(44,{'25' if slant else '22'}),(44,35),(41,35));join('cab','cargo');join('cab','wheel-36')
line('sill',(28,35),(31,35));join('sill','cargo');join('sill','wheel-36')
""")
for name,chipped in [('dentistry-tooth',False),('dentistry-tooth-chipped',True)]:
 design(name,'VRECT_L',None,'Keep the broad crown and two long rounded roots. Shared root proportions preserve the tooth identity.'+(' A clear notch on the right marks the chipped edge.' if chipped else ' Both sides mirror smoothly.'),"""
path('tooth',(24,6),[('C',(34,4),(28,6),(30,4)),('C',(40,13),(39,4),(40,7)),
"""+("('L',(38,17)),('L',(34,19)),('L',(39,23))," if chipped else "('C',(36,27),(40,18),(36,22)),")+"""
('C',(30,44),(35,34),(35,44)),('C',(24,28),(29,44),(31,28)),('C',(18,44),(17,28),(19,44)),('C',(12,27),(13,44),(13,34)),('C',(8,13),(12,22),(8,18)),('C',(14,4),(8,7),(9,4)),('C',(24,6),(18,4),(20,6))],True)
""")
design('design-tool-magnet','SQUARE',None,'Keep a broad horseshoe magnet with two equal pole bands. Concentric semicircles and shared verticals repair uneven inner walls.', """
path('magnet',(6,6),[('L',(16,6)),('L',(16,24)),('A',(32,24),8,8,False),('L',(32,6)),('L',(42,6)),('L',(42,24)),('A',(6,24),18,18,True),('L',(6,6))],True)
for x in (6,32):line(f'pole-{x}',(x,16),(x+10,16));join(f'pole-{x}','magnet')
""")
design('diamond-money','HRECT_L','gem','Keep the faceted diamond with a wide shoulder and centered bottom point. Paired facets retain symmetry and clear openings.', """
poly('gem',(14,8),(34,8),(44,22),(24,40),(4,22),closed=True)
poly('across',(4,22),(18,22),(30,22),(44,22));poly('facets',(14,8),(18,22),(24,40),(30,22),(34,8));join('across','gem');join('facets','gem');join('across','facets')
""")
# Visual and clearance refinements after the first contact-sheet review.
design('canoe-paddles','SQUARE',None,'Two broad diagonal paddle blades are mirrored from a single definition, with shared shaft attachment points and an exact central crossing.', """
poly('blade-left',(6,14),(14,6),(22,14),(22,22),(14,22),(6,14))
poly('blade-right',(42,14),(34,6),(26,14),(26,22),(34,22),(42,14))
poly('shaft-left',(22,22),(24,24),(42,42));poly('shaft-right',(26,22),(24,24),(6,42))
join('shaft-left','blade-left');join('shaft-right','blade-right');join('shaft-left','shaft-right')
""")
design('cashew','SQUARE',None,'A smooth crescent cashew retains broad rounded tips, a full outer belly and one scooped inner curve.', """
path('nut',(29,6),[('C',(42,20),(38,6),(42,10)),('C',(19,42),(42,34),(33,42)),('C',(6,30),(10,42),(6,37)),('C',(15,25),(6,24),(10,23)),('C',(25,20),(23,29),(28,24)),('C',(23,12),(23,17),(22,15)),('C',(29,6),(23,8),(25,6))],True)
""")
design('casino-clover','VRECT_L','clover','Keep a three-lobed clover with rounded leaf ends and a narrow central stem. Both side leaves mirror around the shared stem.', """
path('clover',(24,33),[('C',(8,28),(12,40),(8,34)),('C',(17,18),(8,21),(12,17)),('C',(16,11),(14,15),(14,12)),('C',(24,7),(16,4),(20,4)),('C',(32,11),(28,4),(32,4)),('C',(31,18),(34,12),(34,15)),('C',(40,28),(36,17),(40,21)),('C',(24,33),(40,34),(36,40))],True)
line('stem',(24,33),(24,44));join('stem','clover')
""")
design('cat-toy','SQUARE',None,'Keep the round toy and loose string; the open string curls have enough spacing to remain visible at 48 pixels.', """
circle('ball',16,16,10)
path('string',(24,22),[('C',(42,28),(28,27),(42,23)),('C',(31,33),(42,32),(37,33)),('L',(29,33)),('C',(26,42),(23,33),(23,42)),('L',(30,42))]);join('string','ball')
""")
design('cauldron','HRECT_L','cooking-pot','A broad round-bellied cauldron has a flared lip and paired shoulders. Preserve the source rounded cooking vessel.', """
path('pot',(8,8),[('L',(40,8)),('A',(40,16),4,4,True),('L',(44,24)),('C',(24,40),(43,36),(35,40)),('C',(4,24),(13,40),(5,36)),('L',(8,16)),('A',(8,8),4,4,True)],True)
""")
# Preserve natural vessel proportions: the belly, not the base, owns the width.
for name,foot in [('ceramic',16),('ceramic-tool',13)]:
 design(name,'VRECT_L','amphora','A narrow-necked vase with a broad rounded belly and narrower foot. Mirrored tangents keep both shoulders smooth; foot width preserves the variant.',f"""
path('vase',(16,4),[('L',(32,4)),('C',(40,22),(30,10),(40,14)),('C',({48-foot},44),(40,31),({48-foot},35)),('L',({foot},44)),('C',(8,22),({foot},35),(8,31)),('C',(16,4),(8,14),(18,10))],True)
""")
design('chef-gear-biscuits-cup','SQUARE','cup-soda','Two rounded biscuits stand in a tapered cup. The source wide sticks and open upper gap are preserved.', """
poly('cup',(6,22),(42,22),(35,42),(13,42),(6,22))
path('left-biscuit',(14,22),[('L',(8,12)),('C',(10,6),(6,8),(8,6)),('C',(17,9),(13,6),(16,6)),('L',(24,22))]);join('left-biscuit','cup')
path('right-biscuit',(24,22),[('L',(31,9)),('C',(38,6),(32,6),(35,6)),('C',(40,12),(40,6),(42,8)),('L',(34,22))]);join('right-biscuit','cup');join('left-biscuit','right-biscuit')
""")
for name in ('chilli','chilli-jelapeno'):
 k,ref,plan,body=D[name];D[name]=(k,ref,plan,body.replace("('C',(40,8),(44,16),(44,8)),('L',(38,8))","('C',(44,12),(43,18),(44,16)),('C',(40,8),(44,9),(43,8)),('L',(38,8))"))
design('chocolate-box','HRECT_L',None,'A heart-shaped chocolate box retains broad lobes and a clear lower depth band; symmetric curves meet the heart valley and point.', """
path('lid',(24,13),[('C',(14,8),(20,10),(18,8)),('C',(4,16),(8,8),(4,10)),('L',(24,28)),('L',(44,16)),('C',(34,8),(44,10),(40,8)),('C',(24,13),(30,8),(28,10))],True)
poly('depth',(4,16),(4,28),(24,40),(44,28),(44,16));line('seam',(24,28),(24,40));join('depth','lid');join('seam','depth');join('seam','lid')
""")
for name in ('circinus','circinus-state'):
 k,ref,plan,body=D[name];D[name]=(k,ref,plan,body.replace('(40,6)','(42,6)'))
# Fewer, shallower rings keep the database layers clear with the system stroke.
k,ref,plan,body=D['database'];D['database']=(k,ref,plan,body.replace('16,6,False)]);join','16,3,False)]);join'))
for name,orientation in [('clover',0),('clover-symbol',1)]:
 design(name,'SQUARE','clover','Four heart-shaped leaves are mirrored in both axes around one center. A short curved stem keeps the clover readable without uneven lobes.',f"""
leaf=[('L',(13,24)),('C',(6,18),(8,24),(6,22)),('C',(14,12),(6,12),(10,10)),('C',(18,6),(12,8),(13,6)),('C',(24,13),(22,6),(24,8)),('L',(24,24))]
for sx,sy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
 transform=lambda p:(24+sx*(p[0]-24),24+sy*(p[1]-24))
 commands=[]
 for kind,end,*ctrl in leaf:commands.append((kind,transform(end),*[transform(p) for p in ctrl]))
 name=f'leaf-{{sx}}-{{sy}}';path(name,(24,24),commands,True)
 for other in [f'leaf-{{a}}-{{b}}' for a,b in [(-1,-1),(-1,1),(1,-1),(1,1)] if (a,b)<(sx,sy)]:join(name,other)
""" )
# A cog quarter must turn into its neighbor with the same tooth orientation.
for name,notch in [('cog-1',0),('cog-4c6e5052',1)]:
 design(name,'SQUARE','cog','Eight evenly repeated gear teeth retain the original cog silhouette. Paired cardinal and diagonal teeth follow one mirrored quadrant.',f"""
quadrant={([(24,6),(28,6),(30,11),(34,10),(38,14),(37,18),(42,20),(42,24)] if notch==0 else [(24,6),(28,6),(28,11),(32,13),(36,10),(38,12),(35,16),(37,20),(42,20),(42,24)])!r}
turn=lambda p,n:p if n==0 else turn((48-p[1],p[0]),n-1)
points=[]
for n in range(4):points.extend(turn(p,n) for p in quadrant[:-1])
poly('gear',*points,closed=True)
""")
design('chef-gear-mug','SQUARE','coffee','Keep the upright mug with a broad handle and lightly rounded base. Its taller cup body distinguishes it from the low cups.', """
path('cup',(6,6),[('L',(30,6)),('L',(30,14)),('L',(30,28)),('L',(30,34)),('A',(22,42),8,8,True),('L',(14,42)),('A',(6,34),8,8,True),('L',(6,6))],True)
path('handle',(30,14),[('L',(35,14)),('A',(42,21),7,7,True),('A',(35,28),7,7,True),('L',(30,28))]);join('handle','cup')
""")
# Set distinct depths on the remaining cup instead of duplicating the mug.
k,ref,plan,body=D['cup-1'];D['cup-1']=(k,ref,plan,body.replace("('A',(22,40),10,10,True)","('C',(20,40),(32,38),(26,40))").replace("('L',(14,40)),('A',(4,30),10,10,True)","('L',(16,40)),('C',(4,30),(8,40),(4,37))"))
# Place wheel contacts on explicit quarter-circle nodes; keep the body above the tyres.
wheel_code="""
for x in (12,36):
 path(f'wheel-{x}',(x,32),[('A',(x+4,36),4,4,True),('A',(x,40),4,4,True),('A',(x-4,36),4,4,True),('A',(x,32),4,4,True)],True)
 join(f'wheel-{x}','body')
"""
for name,(roof,divider) in cars.items():
 # Lower shoulders meet the body band at y=22; cabin topology stays individual.
 roof=[(x,min(y,24)) for x,y in roof]
 body=f"""
path('body',(4,28),[('L',{roof[0]!r})]+[('L',p) for p in {roof[1:]!r}]+[('L',(44,28)),('A',(40,32),4,4,True),('L',(36,32)),('L',(12,32)),('L',(8,32)),('A',(4,28),4,4,True)],True)
"""+wheel_code
 if name=='car-2':body+="line('belt',(6,20),(32,20));line('pillar',(21,8),(21,20));join('belt','body');join('pillar','body');join('pillar','belt')\n"
 if name in ('car-5e6ba5b0','car-9e5f3201'):body+="line('belt',(9,20),(33,20));join('belt','body')\n" if name=='car-5e6ba5b0' else "line('belt',(11,20),(35,20));join('belt','body')\n"
 if name=='car-transportation':body+="line('handle',(18,20),(23,20))\n"
 design(name,'HRECT_L','car','Keep this compact car roof type and stance. Four exact tyre quadrants meet a smoothly rounded lower body at shared nodes; the wheels retain clear round interiors.',body)
for name,right in [('car-e1ae9ac1',36),('car-retro',38)]:
 design(name,'HRECT_L','car','Retain a rounded vintage cabin with a central pillar and smooth lower body; the longer roof distinguishes the retro variant.',f"""
path('body',(4,26),[('A',(10,20),6,6,True),('L',(24,20)),('L',(38,20)),('A',(44,26),6,6,True),('L',(44,28)),('A',(40,32),4,4,True),('L',(36,32)),('L',(12,32)),('L',(8,32)),('A',(4,28),4,4,True),('L',(4,26))],True)
path('roof',(12,20),[('C',(24,8),(12,13),(17,8)),('C',({right},20),(31,8),({right},13))]);join('roof','body')
line('pillar',(24,8),(24,20));join('pillar','roof');join('pillar','body')
"""+wheel_code)
design('convertible','HRECT_L','car','An open convertible keeps its low cabin and two equal tyres attached at explicit tangent nodes.', """
path('body',(4,18),[('L',(16,18)),('C',(28,18),(18,27),(26,27)),('L',(40,18)),('A',(44,22),4,4,True),('L',(44,28)),('A',(40,32),4,4,True),('L',(36,32)),('L',(12,32)),('L',(8,32)),('A',(4,28),4,4,True),('L',(4,18))],True)
line('windshield',(12,18),(12,8));line('seat',(28,18),(26,8));join('windshield','body');join('seat','body')
"""+wheel_code)
for name,slant in [('delivery-truck',False),('delivery-truck-delivery',True)]:
 design(name,'HRECT_L','truck','Keep the tall cargo compartment and short cab. Round tyres attach cleanly below the body, while a sloped or squared cab preserves the variant.',f"""
path('body',(4,8),[('L',(28,8)),('L',(28,16)),('L',({'36' if slant else '38'},16)),('L',(44,{'24' if slant else '21'})),('L',(44,28)),('A',(40,32),4,4,True),('L',(36,32)),('L',(28,32)),('L',(12,32)),('L',(8,32)),('A',(4,28),4,4,True),('L',(4,8))],True)
line('partition',(28,16),(28,32));join('partition','body')
"""+wheel_code)
design('canoe-paddles','SQUARE',None,'Two broad paddle blades mirror about the central axis with a clear gap between them. Shafts meet at one central crossing.', """
poly('blade-left',(6,14),(14,6),(20,12),(20,20),(12,20),(6,14))
poly('blade-right',(42,14),(34,6),(28,12),(28,20),(36,20),(42,14))
poly('shaft-left',(20,20),(24,24),(42,42));poly('shaft-right',(28,20),(24,24),(6,42))
join('shaft-left','blade-left');join('shaft-right','blade-right');join('shaft-left','shaft-right')
""")
# A single upper arc owns the clover crown extreme.
k,ref,plan,body=D['casino-clover'];D['casino-clover']=(k,ref,plan,body.replace("('C',(24,7),(16,4),(20,4)),('C',(32,11),(28,4),(32,4))","('C',(24,4),(16,6),(20,4)),('C',(32,11),(28,4),(32,6))"))
design('cargo-ship-symbol','SQUARE','ship','Preserve the frontal ship and stepped deckhouse. The deckhouse rests directly on a level gunwale above the low bow waves.', """
poly('cabin',(12,23),(12,14),(19,14),(19,6),(29,6),(29,14),(36,14),(36,23))
poly('hull',(10,39),(6,23),(12,23),(36,23),(42,23),(38,39));join('hull','cabin')
poly('water',(6,42),(10,39),(17,42),(24,39),(31,42),(38,39),(42,42));join('water','hull')
""")
design('ceiling-ball-chandelier-retro','HRECT_L','lamp-ceiling','Three round globes hang at equal spacing from one level arm; matched radii keep the fixture balanced.', """
line('ceiling',(18,8),(30,8));poly('stem',(24,8),(24,20),(24,32));join('stem','ceiling')
poly('arm',(8,32),(8,20),(24,20),(40,20),(40,32));join('arm','stem')
for x in (8,24,40):
 path(f'globe-{x}',(x,32),[('A',(x,40),4,4,True),('A',(x,32),4,4,True)],True);join(f'globe-{x}','stem' if x==24 else 'arm')
""")
design('chef-gear-biscuits-cup','SQUARE','cup-soda','A wide cup holds two rounded biscuit sticks. Exact attachment nodes keep the biscuits visibly seated in the rim.', """
poly('cup',(6,22),(14,22),(24,22),(34,22),(42,22),(35,42),(13,42),(6,22))
path('left-biscuit',(14,22),[('L',(8,12)),('C',(10,6),(6,8),(8,6)),('C',(17,9),(13,6),(16,6)),('L',(24,22))]);join('left-biscuit','cup')
path('right-biscuit',(24,22),[('L',(31,9)),('C',(38,6),(32,6),(35,6)),('C',(40,12),(40,6),(42,8)),('L',(34,22))]);join('right-biscuit','cup');join('left-biscuit','right-biscuit')
""")
design('chef-gear-cookie-bowl','SQUARE',None,'A bitten cookie rises from a broad shallow bowl. One readable bite replaces the crowded cluster of small scallops.', """
path('bowl',(6,25),[('L',(10,25)),('L',(38,25)),('L',(42,25)),('C',(34,36),(41,30),(37,34)),('L',(34,42)),('L',(14,42)),('L',(14,36)),('C',(6,25),(11,34),(7,30))],True)
path('cookie',(10,25),[('C',(26,6),(8,12),(18,6)),('C',(38,17),(25,13),(31,17)),('L',(38,25))]);join('cookie','bowl')
""")
for name,belly in [('chilli',22),('chilli-jelapeno',18)]:
 design(name,'HRECT_L',None,'A curved pepper retains a pointed tip, broad body and a short curved stem; the belly fullness differentiates the two peppers.',f"""
path('pepper',(4,24),[('C',(32,18),(16,27),(24,22)),('C',(40,20),(36,14),(40,16)),('C',({belly},40),(44,28),(34,40)),('C',(4,24),(12,40),(7,31))],True)
path('stem',(40,20),[('C',(44,12),(43,18),(44,15)),('C',(40,8),(44,9),(43,8))]);join('stem','pepper')
""")
# True junction nodes on the corn, hook and curtains preserve connected geometry.
design('corn','VRECT_L',None,'A round-topped cob emerges above paired husks. Both leaves attach at clear shoulder nodes and taper into one shared base.', """
path('cob',(16,25),[('L',(16,12)),('A',(32,12),8,8,True),('L',(32,25))])
path('left',(8,22),[('C',(16,25),(11,22),(14,24)),('C',(24,44),(21,31),(24,37)),('C',(8,22),(11,44),(10,32))],True)
path('right',(40,22),[('C',(32,25),(37,22),(34,24)),('C',(24,44),(27,31),(24,37)),('C',(40,22),(37,44),(38,32))],True)
join('left','cob');join('right','cob');join('left','right')
""")
design('crane-hook','VRECT_L',None,'A compact pulley block supports a smooth open hook. A diagonal block seam and spacious lower hook retain the original mechanism.', """
poly('block',(8,4),(32,4),(40,4),(40,16),(32,23),(24,23),(16,23),(8,16),(8,4))
line('diagonal',(8,16),(32,4));join('diagonal','block')
path('hook',(24,23),[('L',(24,31)),('C',(16,36),(19,31),(16,32)),('C',(26,44),(16,42),(20,44)),('C',(36,36),(32,44),(36,41))]);join('hook','block')
""")
# Extend the wrapper below the frosting, with endpoints split at the real joins.
k,ref,plan,body=D['cupcake'];body=body.replace("('C',(30,28),(37,33),(33,33)),('C',(18,28),(27,33),(21,33)),('C',(8,28),(15,33),(11,33))","('C',(36,31),(39,30),(38,31)),('C',(30,28),(33,31),(32,30)),('C',(24,31),(28,30),(26,31)),('C',(18,28),(22,31),(20,30)),('C',(12,31),(16,30),(15,31)),('C',(8,28),(10,31),(9,30))")
D['cupcake']=(k,ref,plan,body)
design('curtains-open','SQUARE',None,'Two tied-back curtain panels mirror about a clear center opening. Shared tie nodes and generous lower folds preserve the drape.', """
poly('rod',(6,6),(18,6),(30,6),(42,6))
for side in (-1,1):
 x=lambda d:24+side*d
 path(f'panel-{side}',(x(6),6),[('L',(x(18),6)),('L',(x(18),25)),('L',(x(18),42)),('L',(x(8),42)),('C',(x(9),25),(x(8),34),(x(8),29)),('C',(x(6),6),(x(6),20),(x(6),13))],True)
 line(f'tie-{side}',(x(18),25),(x(9),25));join(f'tie-{side}',f'panel-{side}');join(f'panel-{side}','rod')
""")
k,ref,plan,body=D['database'];D['database']=(k,ref,plan,body.replace('[20, 30]','[23, 33]').replace('16,3,False','16,2,False'))
k,ref,plan,body=D['clover-symbol'];D['clover-symbol']=(k,ref,plan+' This variant uses deeper heart notches.',body.replace("('C',(14,12),(6,12),(10,10))","('C',(15,15),(6,10),(11,10))").replace("('C',(18,6),(12,8),(13,6))","('C',(18,6),(12,10),(13,6))"))
design('cog-4c6e5052','SQUARE','cog','A gear has four broad cardinal teeth and four diagonal shoulders. A shared quadrant keeps every tooth evenly spaced.', """
quarter=[(24,6),(29,6),(31,12),(36,12),(36,17),(42,19),(42,24)]
turn=lambda p,n:p if n==0 else turn((48-p[1],p[0]),n-1)
poly('gear',*[turn(p,n) for n in range(4) for p in quarter[:-1]],closed=True)
""")
k,ref,plan,body=D['chef-gear-biscuits-cup'];D['chef-gear-biscuits-cup']=(k,ref,plan,body.replace("poly('cup',(6,22),(14,22),(24,22),(34,22),(42,22),(35,42),(13,42),(6,22))","path('cup',(6,22),[('L',(14,22)),('L',(24,22)),('L',(34,22)),('L',(42,22)),('L',(42,36)),('A',(36,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('L',(6,22))],True)"))
k,ref,plan,body=D['convertible'];D['convertible']=(k,ref,plan,body.replace('(18,27),(26,27)','(18,24),(26,24)'))
k,ref,plan,body=D['corn'];D['corn']=(k,ref,plan,body.replace('(16,25)','(18,25)').replace('(16,12)','(18,10)').replace('(32,12),8,8','(30,10),6,6').replace('(32,25)','(30,25)'))
for name,notch in [('clover',9),('clover-symbol',11)]:
 design(name,'SQUARE','clover','Four heart-shaped leaves meet at the center, preserving the original diagonal leaf divisions. One rotated leaf definition owns all lobes and spacing.',f"""
leaf=[('C',(14,12),(20,20),(14,17)),('C',(19,6),(14,8),(15,6)),('C',(24,{notch}),(22,6),(23,{notch})),('C',(29,6),(25,{notch}),(26,6)),('C',(34,12),(33,6),(34,8)),('C',(24,24),(34,17),(28,20))]
turn=lambda p,n:p if n==0 else turn((48-p[1],p[0]),n-1)
for n in range(4):
 path(f'leaf-{{n}}',(24,24),[(k,turn(e,n),turn(a,n),turn(b,n)) for k,e,a,b in leaf],True)
 for m in range(n):join(f'leaf-{{n}}',f'leaf-{{m}}')
""")
for name in ('clover','clover-symbol'):
 k,ref,plan,body=D[name]
 body=body.replace("('C',(14,12),(20,20),(14,17))","('L',(14,14))").replace("('C',(34,12),(33,6),(34,8)),('C',(24,24),(34,17),(28,20))","('C',(34,14),(33,6),(34,8)),('L',(24,24))")
 body=body.replace("[(k,turn(e,n),turn(a,n),turn(b,n)) for k,e,a,b in leaf]","[(k,turn(e,n),*[turn(p,n) for p in controls]) for k,e,*controls in leaf]")
 D[name]=(k,ref,plan,body)
design('database','VRECT_L','database','Preserve the four-layer database with shallow elliptical rings. The rim and repeated layers have ample spacing for consistent strokes.', """
path('top',(8,8),[('A',(40,8),16,4,True),('A',(8,8),16,4,True)],True)
path('body',(8,8),[('L',(8,42)),('A',(40,42),16,2,False),('L',(40,8))]);join('body','top')
for y in (22,32):path(f'ring-{y}',(8,y),[('A',(40,y),16,2,False)]);join(f'ring-{y}','body')
""")
for name,ry in [('data',6),('data-servers',5)]:
 design(name,'SQUARE','database','Retain the original broad cylindrical database proportions. True elliptical rims and evenly spaced levels replace the irregular tracing.',f"""
path('top',(6,{6+ry}),[('A',(42,{6+ry}),18,{ry},True),('A',(6,{6+ry}),18,{ry},True)],True)
path('body',(6,{6+ry}),[('L',(6,{42-ry})),('A',(42,{42-ry}),18,{ry},False),('L',(42,{6+ry}))]);join('body','top')
path('ring',(6,24),[('A',(42,24),18,{ry},False)]);join('ring','body')
""")
design('cart-e3de8236','HRECT_L','shopping-basket','A broad basket keeps the source taper, with one arched carry handle and rounded lower corners for a distinct conventional basket variant.', """
path('basket',(4,20),[('L',(12,20)),('L',(36,20)),('L',(44,20)),('L',(39,36)),('C',(34,40),(38,39),(36,40)),('L',(14,40)),('C',(9,36),(12,40),(10,39)),('L',(4,20))],True)
path('handle',(12,20),[('A',(36,20),12,12,True)]);join('handle','basket')
""")
design('cart-shopping','HRECT_L','shopping-cart','A wheeled shopping cart keeps its right-facing handle and uses gently rounded lower basket corners. Wheels remain equal and evenly spaced.', """
path('basket',(4,16),[('L',(40,16)),('L',(35,27)),('C',(30,30),(34,29),(32,30)),('L',(15,30)),('C',(11,27),(13,30),(12,29)),('L',(4,16))],True)
line('handle',(40,16),(44,8));join('handle','basket')
self.add_dot('wheel-left',(15,40));self.add_dot('wheel-right',(31,40))
""")
# Soften the angular car shoulders while preserving each source roof profile.
for name,(source_roof,divider) in cars.items():
 roof=[(x,min(y,24)) for x,y in source_roof];commands=[]
 for i,p in enumerate(roof):
  prev=roof[i-1] if i else (4,28);nxt=roof[i+1] if i+1<len(roof) else (44,28)
  def step(a,b):
   dx,dy=b[0]-a[0],b[1]-a[1];m=max(abs(dx),abs(dy))
   return (round(dx/m),round(dy/m)) if m else (0,0)
  u=step(prev,p);v=step(p,nxt)
  a=(p[0]-u[0],p[1]-u[1]);b=(p[0]+v[0],p[1]+v[1])
  if p==prev or p==nxt or u==v:commands.append(('L',p));continue
  commands.extend([('L',a),('C',b,(a[0]+(p[0]-a[0])*2/3,a[1]+(p[1]-a[1])*2/3),(b[0]+(p[0]-b[0])*2/3,b[1]+(p[1]-b[1])*2/3))])
 k,ref,plan,body=D[name]
 before=f"[('L',{roof[0]!r})]+[('L',p) for p in {roof[1:]!r}]"
 body=body.replace(before,repr(commands))
 D[name]=(k,ref,plan+' Small tangent curves soften the shoulders while retaining the original roof shape.',body)
