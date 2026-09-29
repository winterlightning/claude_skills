from author_batch import *
SPECS[1]['body']=SPECS[1]['body'].replace('(14,35),(17,43)','(12,36),(13,43)').replace('((14,31),(15,41),(24,44)),((31,46),(38,42),(38,36))','((17,31),(18,41),(25,44)),((31,46),(36,43),(36,38))')
SPECS[6]['body']=SPECS[6]['body'].replace('((36,23),(40,18),(35,10))','((32,20),(33,21),(34,21)),((39,21),(39,17),(35,10))')+"\nself.relate('connect','brush-head','brush-handle')"
SPECS[10]['body']=SPECS[10]['body'].replace('((17,0),(31,0),(41,7))','((17,1),(31,1),(41,7))')

define(11,'SQUARE','The rider became an angular robot-like torso with a rectangular central block instead of a rounded front wheel.','Restored rounded shoulders, relaxed angled arms, handlebar segments and a narrow capsule-shaped front wheel beneath the rider.', '''
# Detached head: cy9,r5 -> shoulder top22, exactly8 centerline /4 ink.
circle(self,'head',24,9,5)
curve(self,'shoulders',(11,32),((5,30),(11,22),(17,22)),((21,22),(27,22),(31,22)),((37,22),(43,30),(37,32)))
self.add_line('left-arm',(11,32),(8,43));self.add_line('right-arm',(37,32),(40,43))
self.relate('connect','shoulders','left-arm');self.relate('connect','shoulders','right-arm')
rounded(self,'front-wheel',21,30,27,44,3)
self.add_line('left-handlebar',(11,32),(21,32));self.add_line('right-handlebar',(27,32),(37,32))
for side in ('left','right'):
    self.relate('connect',side+'-handlebar',side+'-arm')
    self.relate('connect',side+'-handlebar','front-wheel')
''','human_ref/full_body_ref.png: circular head and smooth upper body; supplied original: centered wheel and paired angled arms','Keep a front-view rider, both handlebars and the narrow front wheel. Compact connected vehicle details preserve meaning at4px stroke; the head gap remains exactly4px.')

define(12,'SQUARE','The bicycle lost its seat tube and complete diamond frame; the heavy simplified triangle made the bike ambiguous.','Restored the complete two-triangle frame, two round wheels, seat post, saddle, fork and curved handlebar.', '''
# Paired equal wheels and a true diamond frame share hub and junction points.
for name,cx in (('rear',12),('front',36)):circle(self,name+'-wheel',cx,34,8)
self.add_polyline('rear-frame',(12,34),(18,20),(24,34),(12,34))
self.add_polyline('front-frame',(18,20),(33,16),(24,34))
self.add_line('fork',(33,16),(36,34))
self.add_line('seat-post',(18,20),(16,14));self.add_line('saddle',(12,14),(20,14))
self.add_polyline('handlebar-stem',(33,16),(31,10),(37,10))
curve(self,'handlebar',(37,10),((42,10),(42,15),(37,17)))
for a,b in [('rear-frame','front-frame'),('front-frame','fork'),('rear-frame','seat-post'),('seat-post','saddle'),('front-frame','handlebar-stem'),('fork','handlebar-stem'),('handlebar-stem','handlebar')]:self.relate('connect',a,b)
# Frame runs genuinely cross the wheel rims, as in a conventional bicycle diagram.
for a,b in [('rear-wheel','rear-frame'),('front-wheel','fork')]:self.relate('connect',a,b)
''','No new Lucide bicycle reference used; original supplies the full diamond frame and two equal circular wheels.','A complete bicycle frame and realistic wheel proportions create compact triangular regions. Preserve these defining structures at4px rather than deleting the seat tube.')

define(13,'VRECT_L','The cliff became a jagged zigzag and the climber had a tiny head with an unnatural bent body.','Restored the smooth curving cliff, a proportionate head, an extended reaching arm and a bent climbing knee.', '''
# Head(16,11),r5 -> actual torso junction(16,24):4px visible clearance; upper torso tangent vertical.
circle(self,'head',16,11,5)
curve(self,'torso',(16,24),((16,28),(13,32),(16,34)))
self.add_polyline('reaching-arm',(16,24),(24,24),(35,19))
self.add_line('rear-leg',(16,34),(12,44))
curve(self,'front-leg',(16,34),((20,32),(24,28),(27,33)),((29,36),(31,40),(34,44)))
curve(self,'cliff',(38,4),((40,10),(38,15),(35,19)),((34,23),(32,28),(29,31)))
for part in ('reaching-arm','rear-leg','front-leg'):self.relate('connect','torso',part)
self.relate('connect','rear-leg','front-leg');self.relate('connect','reaching-arm','cliff')
self.mark_human_figure('climber',head='head',torso='torso-curve',torso_junction='start')
''','human_ref/full_body_ref.png: outlined head, coherent limbs and bent knee; original supplies curved cliff','Retain the natural curve of the cliff, exact4px head gap and a readable climbing action. The natural scene envelope and compact bent-leg spacing are intentional.')

define(14,'VRECT_M','The mountain pose had rigid bent arms and an artificial waist bar instead of relaxed arms and close-set legs.','Restored a neutral upright torso, gently hanging arms and close-set feet in a calm standing pose.', '''
# Human reference proportions; head bottom14, upper torso22 ->4px ink gap.
circle(self,'head',24,9,5)
self.add_line('torso',(24,22),(24,32))
curve(self,'left-arm',(24,22),((18,22),(17,29),(17,35)))
curve(self,'right-arm',(24,22),((30,22),(31,29),(31,35)))
self.add_line('left-leg',(24,32),(21,44));self.add_line('right-leg',(24,32),(27,44))
for part in ('left-arm','right-arm','left-leg','right-leg'):self.relate('connect','torso',part)
self.relate('connect','left-arm','right-arm');self.relate('connect','left-leg','right-leg')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: round head and coherent limbs; original: narrow neutral standing posture','Mountain pose should remain narrow and relaxed with close-set feet; preserve this natural envelope rather than spreading the arms to fill the keyshape.')

define(15,'VRECT_L','The skewered olive became a short bent stroke and the garnish lost its round fruit shape.','Restored a distinct outlined olive, diagonal skewer and clean V-shaped martini bowl on a slender stem.', '''
self.add_polyline('bowl',(4,10),(44,10),(24,32),closed=True)
self.add_line('stem',(24,32),(24,44));self.add_line('base',(15,44),(33,44))
self.relate('connect','bowl','stem');self.relate('connect','stem','base')
curve(self,'olive',(23,21),((19,16),(25,10),(30,13)),((36,17),(29,25),(23,21)),closed=True)
self.add_line('skewer-upper',(36,4),(30,13));self.add_line('skewer-lower',(23,21),(20,25))
self.relate('connect','olive','skewer-upper');self.relate('connect','olive','skewer-lower');self.relate('connect','bowl','skewer-upper')
''','Original supplies triangular bowl and skewered olive; geometric circles/curves and shared stem junctions follow the common authoring guide.','The diagonal skewer and oval olive must remain visible inside the bowl. Preserve compact garnish spacing and the wide martini rim at4px stroke.')

GLASSES='''
# Avatar construction: circular head/jaw r17; lower extreme37 and shoulder top41 are4 centerline units apart, so the ink touches.
circle(self,'head',24,20,17)
curve(self,'ear-left',(7,20),((2,17),(3,27),(9,28)))
curve(self,'ear-right',(41,20),((46,17),(45,27),(39,28)))
self.relate('connect','head','ear-left');self.relate('connect','head','ear-right')
for side,cx in (('left',17),('right',31)):circle(self,'lens-'+side,cx,19,4)
self.add_line('bridge',(21,19),(27,19))
self.add_line('temple-left',(7,20),(13,19));self.add_line('temple-right',(35,19),(41,20))
for side in ('left','right'):
    self.relate('connect','bridge','lens-'+side)
    self.relate('connect','temple-'+side,'lens-'+side)
    self.relate('connect','temple-'+side,'head')
self.add_arc('shoulders',(4,46),(44,46),radius_x=20,radius_y=5)
self.relate('connect','head','shoulders')
'''
for i in (16,17):
 define(i,'VRECT_L','The glasses merged into the head outline like goggles, and the ears and human bust proportions were lost.','Restored separate lens circles, a short bridge and temple arms, visible ears and a broad shoulder curve.',GLASSES,'human_ref/user.svg: circular face and broad shoulders; original: round eyeglasses, ears and frontal bust','Preserve facial glass rims, ears and shoulder contact within48px. The large circular head keeps the glasses visually separated from the face outline, with4px strokes and exact touching-ink bust construction.')
 SPECS[i]['human_construction']='bust'

define(18,'SQUARE','The bow tie became a large crossing X attached to the torso and the hat was too blocky.','Restored a smaller two-lobed bow tie, rounded hat crown, separate brim and circular jaw above broad shoulders.', '''
# Circular jaw r8 centered(24,13): lower extreme21; shoulder ellipse top25 gives exact touching ink.
self.add_arc('jaw',(32,13),(16,13),radius_x=8)
self.add_line('hat-left',(16,13),(16,9));self.add_arc('hat-tl',(16,9),(21,4),radius_x=5)
self.add_line('hat-top',(21,4),(27,4));self.add_arc('hat-tr',(27,4),(32,9),radius_x=5)
self.add_line('hat-right',(32,9),(32,13));self.add_contour('hat','hat-left','hat-tl','hat-top','hat-tr','hat-right')
self.add_line('brim',(12,13),(36,13));self.relate('connect','hat','brim');self.relate('connect','jaw','brim')
self.add_arc('shoulders',(4,44),(44,44),radius_x=20,radius_y=19)
self.relate('connect','jaw','shoulders')
self.add_polyline('bow-left',(16,31),(24,35),(16,39),closed=True)
self.add_polyline('bow-right',(32,31),(32,39),(24,35),closed=True)
self.relate('connect','bow-left','bow-right')
''','human_ref/user.svg: circular jaw and broad shoulders; original supplies the hat and separate bow-tie lobes','Preserve two bow-tie lobes beneath the hat and circular face, keeping them separate from the shoulders at48px. Compact bow interiors are intentional with4px strokes.')
SPECS[18]['human_construction']='bust'

define(19,'HRECT_M','The horizontal kitchen knife was changed into a diagonal curved dagger.','Restored a horizontal straight-backed chef blade with a curved cutting edge and a rounded capsule handle.', '''
# Natural horizontal profile, with a shared heel and no decorative details.
self.add_polyline('blade-top-heel',(4,18),(28,18),(28,26),(28,30))
curve(self,'cutting-edge',(28,30),((13,30),(7,28),(4,18)))
# The top/heel polyline is already a joined path; connect the smooth cutting edge at both ends.
self.relate('connect','blade-top-heel','cutting-edge')
self.add_line('handle-top',(28,18),(40,18))
self.add_arc('handle-end',(40,18),(40,26),radius_x=4)
self.add_line('handle-bottom',(40,26),(28,26))
self.add_contour('handle','handle-top','handle-end','handle-bottom')
self.relate('connect','blade-top-heel','handle')
''','No useful local chef-knife match used; original supplies the horizontal silhouette, straight spine and curved cutting edge.','Preserve the narrow horizontal chef-knife proportions instead of bending or widening it to fill the keyshape. The drawing retains4px strokes and a clear8-unit handle interior.')

def make(i):
 runs=sorted((REPO/'icon_set/work/primitive-make-ray'/BATCH[i]['uuid']).glob('20260929T094854Z-gpt6-*'))
 attempt=f'{int(runs[-1].name[-2:])+1:02d}' if runs else '01'
 out=write(i,attempt)
 if SPECS[i].get('human_construction'):
    p=next(out.glob('*.py'));p.write_text(p.read_text().replace('    aliases = ()','    human_construction = "bust"\n    aliases = ()'))
 return out
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
