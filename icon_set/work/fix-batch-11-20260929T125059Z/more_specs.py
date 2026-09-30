add(11,'SQUARE','The rejected spotlight has a diamond-shaped housing and loses the rounded rear connector and light marks.','Round the back housing while preserving the flared angled reflector and clear light rays.','Lucide flashlight: separate reflector and body with a shared slanted seam.','Reduce the rear connector to a rounded housing end; one ray replaces two.', """
poly('head',((16,23),(24,6),(42,24),(25,32),(16,23)))
path(m,'housing',(16,23),('L',(8,31)),('C',(8,37),(5,34),(6,35)),('L',(11,40)),('C',(17,40),(14,43),(15,42)),('L',(25,32)))
join('housing','head')
line('ray',(35,38),(39,42))
""")
add(12,'VRECT_L','The rejected document is square and compresses the page/chart proportions.','Restore a portrait page and a three-column chart anchored to a baseline.','Lucide chart-column informs equal bar spacing and a shared baseline; file-image informs the clipped page.','Omit tiny top corner fold seam.', """
poly('page',((8,4),(30,4),(40,14),(40,44),(8,44),(8,4)))
poly('baseline',((16,34),(24,34),(32,34)))
for name,x,y in [('tall',16,16),('mid',24,22),('short',32,27)]:
 line(name,(x,y),(x,34));join('baseline',name)
""")
add(13,'VRECT_L','The rejected steam has collapsed into dots and the grease drop is short and flat.','Draw a full teardrop below an open tray and three short S-shaped steam strokes.','Lucide flame informs the teardrop silhouette; repeated steam curves share one definition.','Open tray replaces the closed slot to provide space for a readable drop and steam.', """
poly('tray',((8,4),(8,8),(40,8),(40,4)))
path(m,'drop',(24,16),('C',(30,28),(28,22),(33,24)),('C',(18,28),(28,32),(20,32)),('C',(24,16),(15,24),(20,22)),closed=True)
for n,x in enumerate((14,24,34)):
 path(m,'steam'+str(n),(x,39),('C',(x,44),(x-3,40),(x+3,43)))
""")
add(14,'SQUARE','The rejected frog has pinched eye bulges and tangled forelegs and haunches.','Use a wide frog head with smooth eye bulges over a broad seated body, two simple front legs and rounded haunches.','No useful Lucide animal match; shared mirrored eye and leg definitions preserve the front view.','Omit tiny eyes and mouth, as in the blank reference face; avoid extra foot loops.', """
path(m,'head',(14,26),('C',(10,17),(9,24),(8,20)),('C',(18,6),(9,8),(12,6)),('C',(24,10),(21,6),(22,10)),('C',(30,6),(26,10),(27,6)),('C',(38,17),(36,6),(39,8)),('C',(34,26),(40,20),(39,24)),('L',(14,26)),closed=True)
path(m,'body',(14,26),('C',(6,36),(7,26),(6,31)),('C',(12,42),(6,40),(8,42)),('L',(36,42)),('C',(42,36),(40,42),(42,40)),('C',(34,26),(42,31),(41,26)))
join('head','body')
for n,x in [('left',18),('right',30)]:
 line(n,(x,34),(x,42));join(n,'body')
""")
add(15,'HRECT_L','The rejected helmet face has tiny filled eyes and a smiling jaw, opposite to the reference expression.','Make the helmet broader and flatter, restore hollow eyes and a downturned mouth.','No useful Lucide character match; mirrored helmet corners and paired round eyes.','Omit the separate inner cheek contour to give the eyes and expression room.', """
path(m,'helmet',(4,40),('L',(4,20)),('A',(16,8),12,12,True),('L',(32,8)),('A',(44,20),12,12,True),('L',(44,40)))
circle(m,'left-eye',16,23,3);circle(m,'right-eye',32,23,3)
path(m,'frown',(18,36),('C',(30,36),(20,31),(28,31)))
""")
add(16,'VRECT_L','The rejected landscape page has only a single open mountain peak.','Restore two unequal mountain peaks beneath the sun on a portrait file with a clipped corner.','Lucide file-image supplies page and landscape nesting; unequal peaks match the source.','Keep the mountain ridge open so a small enclosed triangle does not fill in.', """
poly('page',((8,4),(30,4),(40,14),(40,44),(8,44),(8,4)))
circle(m,'sun',20,16,3)
poly('ridge',((16,35),(20,30),(24,34),(29,27),(32,35)))
""")
add(17,'VRECT_L','The rejected cocoa pod reads as a generic pointed leaf and loses its stem and curved pod body.','Restore a short stem and an elongated round-shouldered pod containing three seeds.','Lucide leaf contributes one coherent outer contour; the three seeds use one repeat definition.','Omit the inset cut rim and render seeds as short rounded marks to meet clearance.', """
line('stem',(24,4),(24,8))
path(m,'pod',(24,8),('C',(40,25),(35,8),(40,16)),('C',(24,44),(40,34),(30,42)),('C',(8,25),(18,42),(8,34)),('C',(24,8),(8,16),(13,8)),closed=True)
join('stem','pod')
for n,y in enumerate((17,25,33)):
 line('seed'+str(n),(24,y),(25,y))
""")
add(18,'SQUARE','The rejected taco shell is too narrow and reads as a leaf rather than a broad half-round shell.','Broaden the diagonal shell into a substantial semicircle and keep a scalloped filling edge.','Lucide sandwich informs separate shell and filling owners sharing real endpoints; diagonal orientation follows the reference.','Reduce filling lobes to three large scallops.', """
path(m,'shell',(16,42),('C',(14,20),(8,36),(8,28)),('C',(42,16),(22,10),(34,8)),('L',(16,42)),closed=True)
path(m,'filling',(16,42),('C',(6,32),(7,43),(6,38)),('C',(10,18),(6,25),(6,20)),('C',(22,6),(8,10),(15,6)),('C',(34,10),(28,6),(31,6)),('C',(42,16),(39,9),(42,12)))
join('shell','filling')
""")
add(19,'HRECT_L','The rejected sun has become an internal crescent in the cloud and the weather symbol reads as one lumpy mass.','Separate the exposed upper-left sun from a broad lower cloud and preserve a ray outside both.','Lucide cloud-sun informs overlapping outlines with real contacts; intentionally asymmetric sun placement.','One long ray replaces the crowded small rays.', """
path(m,'cloud',(14,26),('C',(26,16),(14,17),(20,13)),('C',(38,26),(32,13),(38,18)),('C',(44,32),(42,26),(44,29)),('C',(36,40),(44,37),(41,40)),('L',(14,40)),('C',(4,33),(8,40),(4,37)),('C',(14,26),(4,29),(8,26)),closed=True)
path(m,'sun',(14,26),('C',(14,12),(7,24),(7,15)),('C',(26,16),(21,8),(26,11)))
join('sun','cloud')
line('ray',(4,8),(6,10))
""")
add(20,'SQUARE','The rejected masked person resembles a hood and lacks natural shoulders beneath the pointed bandana.','Restore a circular upper head, a pointed face covering and broad shoulder curves.','Shared human bust reference and Lucide user-round: circular head proportions over balanced shoulders; the covering replaces the hidden jaw.','Omit the hair part and facial marks to preserve the large bandana.', """
path(m,'head',(12,24),('L',(12,18)),('A',(36,18),12,12,True),('L',(36,24)))
poly('mask',((12,24),(24,20),(36,24),(30,30),(24,36),(18,30),(12,24)))
join('head','mask')
path(m,'left-shoulder',(18,30),('C',(6,42),(8,30),(6,35)))
path(m,'right-shoulder',(30,30),('C',(42,42),(40,30),(42,35)))
join('mask','left-shoulder');join('mask','right-shoulder')
""")

# Fresh second attempts follow the first full visual comparison.
SPECS[1]['code']="""
circle(m,'face',24,27,9)
path(m,'shoulders',(8,44),('A',(40,44),16,4,True))
join('face','shoulders')
line('hair-left',(15,27),(8,33));line('hair-right',(33,27),(40,33))
join('face','hair-left');join('face','hair-right')
for n,x in enumerate((10,24,38)):
 poly('stress'+str(n),((x+2,4),(x-2,7),(x+2,10)))
"""
SPECS[1]['change']='Restore a larger circular face, flared bob ends, broad shoulders and three distinct zigzag stress marks.'
SPECS[1]['omissions']='Omit the interior center part and neckline to keep the face open.'
SPECS[6]['code']="""
circle(m,'chip',24,19,13)
circle(m,'chip-center',24,19,4)
for name,a,b in [('top',(24,6),(24,15)),('bottom',(24,23),(24,32)),('left',(11,19),(20,19)),('right',(28,19),(37,19))]:
 line(name,a,b);join(name,'chip');join(name,'chip-center')
for name,sign in [('left-hand',-1),('right-hand',1)]:
 x=lambda a:24+sign*a
 path(m,name,(x(7),42),('C',(x(18),38),(x(7),40),(x(18),42)),('L',(x(18),30)))
 line(name+'-thumb',(x(18),38),(x(12),37));join(name,name+'-thumb')
"""
SPECS[7]['code']="""
circle(m,'input-top',7,21,3);circle(m,'input-bottom',7,35,3)
poly('output-left',((20,18),(28,18),(28,29),(20,29),(20,18)))
poly('output-right',((36,18),(44,18),(44,29),(36,29),(36,18)))
path(m,'flow',(4,8),('L',(12,8)),('C',(18,11),(15,8),(16,9)),('C',(18,35),(21,17),(16,27)),('C',(39,40),(20,40),(31,40)),('L',(44,40)))
line('arrow',(44,40),(39,36));join('flow','arrow')
"""
SPECS[9]['code']="""
poly('blade',((27,6),(42,21),(25,38),(10,23),(27,6)))
path(m,'handle',(14,27),('L',(6,35)),('L',(6,38)),('A',(10,42),4,4,False),('L',(13,42)),('L',(22,35)))
join('handle','blade')
circle(m,'hole',26,22,3)
"""
SPECS[10]['code']="""
path(m,'arm',(6,34),('L',(18,22)),('C',(18,14),(14,18),(15,17)),('L',(24,8)),('C',(28,6),(25,6),(26,6)),('C',(31,10),(30,6),(31,8)),('C',(36,14),(35,9),(38,11)),('C',(42,20),(40,13),(42,16)),('C',(40,26),(42,22),(42,24)),('L',(30,34)),('C',(24,34),(28,36),(26,36)),('L',(16,42)))
path(m,'thumb',(31,10),('L',(28,21)),('L',(34,27)))
join('arm','thumb')
"""
SPECS[11]['code']=SPECS[11]['code'].replace("('C',(8,37),(5,34),(6,35))", "('C',(6,35),(6,33),(6,34)),('C',(8,37),(6,36),(7,36))")
SPECS[13]['code']=SPECS[13]['code'].replace('(28,32),(20,32)','(28,30),(20,30)')
SPECS[18]['code']="""
path(m,'shell',(20,42),('C',(18,24),(12,36),(12,30)),('C',(42,20),(25,15),(35,13)),('L',(20,42)),closed=True)
path(m,'filling',(20,42),('C',(6,32),(10,42),(6,39)),('C',(11,20),(6,23),(6,21)),('C',(24,6),(8,10),(16,6)),('C',(34,11),(30,6),(34,6)),('C',(42,20),(40,11),(42,14)))
join('shell','filling')
"""
SPECS[19]['code']=SPECS[19]['code'].replace("line('ray',(4,8),(6,10))", "line('ray',(4,8),(5,8))")
SPECS[20]['code']=SPECS[20]['code'].replace("('C',(6,42),(8,30),(6,35))", "('C',(6,42),(18,35),(6,32))").replace("('C',(42,42),(40,30),(42,35))", "('C',(42,42),(30,35),(42,32))")

SPECS[2]['code']="""
box(m,'board',4,8,44,40,4)
oval(m,'knot',24,24,5,4)
path(m,'grain-left',(4,17),('C',(19,24),(13,17),(10,24)))
path(m,'grain-right',(29,24),('C',(44,31),(38,24),(35,31)))
join('board','grain-left');join('board','grain-right');join('knot','grain-left');join('knot','grain-right')
"""
SPECS[2]['omissions']='One flowing grain stream joins the knot; omit extra parallel bands that would crowd it.'
SPECS[7]['code']="""
circle(m,'input-top',7,21,3);circle(m,'input-bottom',7,35,3)
line('output-left',(32,16),(32,24));line('output-right',(44,16),(44,24))
path(m,'flow',(4,8),('L',(10,8)),('C',(19,20),(19,8),(19,14)),('L',(19,28)),('C',(44,36),(19,36),(30,36)))
poly('arrow',((38,32),(44,36),(38,40)));join('flow','arrow')
"""
SPECS[7]['omissions']='Two input circles replace three; output rectangles become compact solid bars, preserving their pair and position; one rightward arrow remains.'
SPECS[9]['code']="""
poly('blade',((26,6),(42,22),(26,38),(10,22),(26,6)))
path(m,'handle',(14,26),('L',(6,34)),('L',(6,38)),('A',(10,42),4,4,False),('L',(14,42)),('L',(22,34)))
join('handle','blade')
circle(m,'hole',26,22,3)
"""
SPECS[9]['change']='Give the blade a clearly hollow hanging hole and a rounded diagonal handle, with sufficient blade width around the hole.'
SPECS[9]['omissions']='Omit the tiny handle rivet; broaden the blade to keep its hanging hole open at 48 pixels.'
SPECS[18]['code']=SPECS[18]['code'].replace('(12,36),(12,30)','(13,36),(13,30)')

SPECS[1]['code']="""
circle(m,'face',24,24,10)
path(m,'shoulders',(8,44),('A',(40,44),16,6,True));join('face','shoulders')
line('hair-left',(14,24),(8,30));line('hair-right',(34,24),(40,30))
join('face','hair-left');join('face','hair-right')
for name,s in [('left',-1),('right',1)]:
 x=lambda a:24+s*a
 poly('stress-'+name,((x(12),4),(x(16),7),(x(12),10),(x(16),13)))
"""
SPECS[1]['change']='Restore a larger circular face, flared bob ends, broad shoulders and two distinct zigzag stress marks.'
SPECS[1]['omissions']='Reduce three stress marks to two; omit the interior center part and neckline.'
SPECS[13]['code']="""
poly('tray',((8,4),(8,6),(40,6),(40,4)))
path(m,'drop',(24,14),('C',(30,26),(28,20),(33,22)),('C',(18,26),(28,29),(20,29)),('C',(24,14),(15,22),(20,20)),closed=True)
for n,x in enumerate((14,24,34)):
 path(m,'steam'+str(n),(x+1,37),('C',(x,40),(x-2,38),(x-2,39)),('C',(x+1,44),(x+2,41),(x+2,43)))
"""
SPECS[19]['omissions']='One short ray replaces the crowded small rays.'
SPECS[4]['change']='Round the muzzle, belly and forward foot, with a clear curved back and upturned tail.'
SPECS[4]['omissions']='Omit tiny facial marks, saddle inset and small arm to keep the compact silhouette open.'
SPECS[8]['change']='Add an explicit handle collar and a flowing straw fan beside a rounded dust puff.'
SPECS[8]['omissions']='Omit narrow internal bristles; dust reduced to a single puff.'

SPECS[1]['code']="""
circle(m,'face',24,27,8)
path(m,'shoulders',(8,44),('A',(40,44),16,5,True));join('face','shoulders')
line('hair-left',(16,27),(8,33));line('hair-right',(32,27),(40,33))
join('face','hair-left');join('face','hair-right')
for name,s in [('left',-1),('right',1)]:
 x=lambda a:24+s*a
 poly('stress-'+name,((x(12),4),(x(16),8),(x(12),16),(x(16),20)))
"""
SPECS[13]['code']=SPECS[13]['code'].replace('(14,24,34)','(12,24,36)')
