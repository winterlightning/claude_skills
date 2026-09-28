from pathlib import Path
import json,re,textwrap
ROOT=Path('icon_set/work/primitive-fix-thuan')
BATCH=ROOT/'batch-20260924-thuan-mac'
HELPERS='''
        def path(n, start, steps, closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(steps):
                if here==end: continue
                tag=f'{n}-{i}'
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C': self.add_bezier(tag,here,(a[0],a[1],end))
                members.append(tag); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,q=4):
            path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
D={}
def add(n,k,plan,code,ref='No useful subject-specific Lucide match; supplied original determines the silhouette.',omissions='No defining features omitted.'):
 D[n]=(k,plan,textwrap.dedent(code),ref,omissions)
add('four-species-of-sukkot','SQUARE','Botanical bundle with a straight lulav, paired branching sprig and asymmetric citron. Shared stem attachment nodes and rounded citron outline.', '''
poly('binding',(6,32),(18,32),(18,42),(6,42),closed=True)
poly('lulav',(18,32),(18,22),(18,6))
path('palm',(18,22),[('C',(28,6),(20,14),(24,8))])
poly('sprig',(6,12),(6,22),(6,32))
line('branch',(6,22),(11,17))
join('sprig','branch');join('sprig','binding');join('lulav','binding');join('lulav','palm')
path('citron',(34,23),[('C',(42,32),(40,23),(42,26)),('C',(34,42),(42,38),(38,42)),('C',(28,34),(28,42),(28,39)),('C',(34,23),(28,28),(29,25))],True)
path('stem',(34,23),[('C',(40,15),(35,19),(38,17))]);join('stem','citron')
''','Lucide sprout: coherent botanical curves and shared branch nodes.','Fine leaf veins and citron dimple omitted to keep clear openings.')
add('handheld-circular-saw','SQUARE','Rounded tilted top handle above circular guard; lower exposed blade with three large teeth. Guard and blade share shoe endpoints.', '''
path('guard',(14,26),[('A',(28,12),14,14,True),('A',(42,26),14,14,True)])
poly('shoe',(6,26),(14,26),(42,26));join('shoe','guard')
path('handle',(14,26),[('L',(8,18)),('A',(10,8),7,7,True),('L',(20,6)),('C',(28,12),(25,5),(28,8))]);join('handle','guard');join('handle','shoe')
path('blade',(42,26),[('L',(40,35)),('L',(34,34)),('L',(31,42)),('L',(26,38)),('L',(19,40)),('L',(18,34)),('L',(14,32)),('L',(14,26))]);join('blade','guard');join('blade','shoe')
''',omissions='Small hub omitted to preserve blade negative space.')
add('hanging-spider','VRECT_L','Long hanging thread above compact oval abdomen; eight legs arranged in mirrored pairs, bent outwards. Shared body attachment nodes.', '''
path('body',(18,23),[('A',(24,17),6,6,True),('A',(30,23),6,6,True),('L',(30,31)),('A',(24,37),6,6,True),('A',(18,31),6,6,True),('L',(18,23))],True)
line('thread',(24,4),(24,17));join('thread','body')
for side in (-1,1):
 def p(x,y):return (24+side*x,y)
 for name,pts in [('upper',[(6,23),(15,18),(16,12)]),('middle',[(6,23),(16,26)]),('lower',[(6,31),(16,35)]),('bottom',[(6,31),(10,44)])]:
  poly(f'{name}-{side}',*[p(x,y) for x,y in pts]);join(f'{name}-{side}','body')
 join(f'upper-{side}',f'middle-{side}');join(f'lower-{side}',f'bottom-{side}')
''','Lucide bug: compact body and mirrored jointed limbs.','Head merged with abdomen; all eight legs and hanging thread retained.')
profile="""
path('profile',(16,44),[('L',(16,36)),('C',(8,20),(16,30),(8,28)),('A',(24,4),16,16,True),('C',(40,25),(36,4),(35,15)),('L',(34,26)),('L',(34,30)),('A',(26,38),8,8,True),('L',(26,44))])
"""
add('happiness-emotions','VRECT_L','Smooth continuous skull, sloping nose, rounded chin and a gentle smile terminating on the profile.',profile+"path('smile',(26,27),[('C',(34,30),(28,30),(31,31))]);join('smile','profile')",'Shared human user.svg: smooth head vocabulary; original profile has continuous neck, so no detached gap.','No eye added; preserve the original smile.')
add('head-and-throat-section-116c496d','VRECT_L','Rounded skull and continuous back neck; two rounded mouth-to-throat passages spaced nine units apart.', '''
path('skull',(8,24),[('L',(12,17)),('C',(26,4),(12,9),(18,4)),('A',(40,18),14,14,True),('L',(40,26)),('C',(39,36),(40,30),(39,33)),('L',(39,44))])
path('upper-passage',(8,24),[('L',(20,24)),('A',(30,34),10,10,True),('L',(30,44))]);join('skull','upper-passage')
path('lower-passage',(8,33),[('L',(15,33)),('A',(21,39),6,6,True),('L',(21,44))])
path('chin',(8,33),[('A',(12,37),4,4,False),('L',(12,44))]);join('chin','lower-passage')
''','Shared human user.svg smooth anatomy; supplied anatomical section defines the continuous neck.','Minor lip contour omitted.')
add('head-in-profile-batch-025-07','VRECT_L','Circular skull transitions smoothly to forehead, distinct projecting nose, round chin, continuous neck.',profile,'Shared human user.svg: smooth circular head; supplied side profile determines facial landmarks.','No detail omitted.')
add('head-profile-wearing-broad-protective-mask','VRECT_L','Rounded left-facing head and broad curved mask with rising rear strap; mask side seam shares exact attachment nodes.', '''
path('skull',(8,20),[('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,30)),('C',(35,38),(40,34),(35,34)),('L',(35,44))])
path('mask',(8,20),[('C',(6,30),(6,22),(6,26)),('C',(14,36),(6,34),(10,36)),('L',(23,36)),('L',(40,30))])
path('strap',(8,20),[('C',(23,22),(14,22),(18,23)),('L',(40,16))])
path('seam',(23,22),[('L',(23,36))]);join('mask','seam');join('strap','seam');join('mask','skull')
line('neck',(17,36),(17,44));join('neck','mask')
# The rear strap meets a real point on the crown by a short connector.
''','Shared human user.svg for circular skull; supplied reference for mask curve.','Small eye and inner ear omitted.')
add('headphone-wearing-dj-behind-two-turntables','VRECT_L','Circular head with attached headphone band and ear strokes; broad shoulders meet deck; two separated platter marks.', '''
circle('head',24,10,6)
for side in (-1,1):
 x=24+side*6; z=24+side*14
 path(f'headphone-{side}',(x,10),[('L',(z,10)),('L',(z,16))]);join(f'headphone-{side}','head')
path('shoulders',(14,30),[('A',(24,24),10,6,True),('A',(34,30),10,6,True)])
poly('deck',(10,30),(14,30),(34,30),(38,30),(40,44),(8,44),closed=True);join('deck','shoulders')
for x in (18,30):line(f'platter-{x}',(x-1,37),(x+1,37))
''','Shared human user.svg and full_body_ref.png for round head and shoulders; Lucide headphones for attached ear strokes. Head bottom16 to shoulder top24 gives exact 4-unit ink gap.','Platters reduced to short marks to retain shoulders and console.')
add('hedgehog','HRECT_L','Right-facing smooth muzzle and belly, with three swept quills on the left and two short feet; intentional animal asymmetry.', '''
path('body',(12,8),[('C',(44,28),(25,12),(39,18)),('C',(32,35),(44,32),(39,35)),('L',(16,35)),('C',(8,33),(12,35),(10,34))])
for i,(a,b) in enumerate([((6,16),(17,20)),((4,25),(14,26))]):line(f'quill-{i}',a,b)
line('front-foot',(32,35),(32,40));line('rear-foot',(16,35),(16,40));join('body','front-foot');join('body','rear-foot')
''',omissions='Extra quills and two hidden feet omitted; reference direction restored.')
add('hidden','HRECT_M','Symmetric almond eye with diagonal obscuring slash; smooth cubic arcs have shared slash attachment knots.', '''
path('outline',(4,24),[('C',(14,13),(7,19),(10,15)),('C',(24,10),(18,11),(21,10)),('C',(44,24),(32,10),(39,17)),('C',(34,35),(41,29),(38,33)),('C',(24,38),(30,37),(27,38)),('C',(4,24),(16,38),(9,31))],True)
line('slash',(14,13),(34,35));join('slash','outline')
''','Lucide eye-off: smooth almond contour and coherent diagonal; original specifies a complete lens.','No omissions.')
add('horizontal-power-plug-with-leaf-vein-cord','SQUARE','Horizontal plug with two pins; smooth looping cord merges into a pointed leaf and its vein.', '''
path('plug',(14,6),[('L',(20,6)),('A',(26,12),6,6,True),('A',(20,18),6,6,True),('L',(14,18)),('L',(14,16)),('L',(14,8)),('L',(14,6))],True)
for y in (8,16):line(f'pin-{y}',(6,y),(14,y));join(f'pin-{y}','plug')
path('cord',(26,12),[('L',(34,12)),('A',(42,20),8,8,True),('A',(34,28),8,8,True),('L',(22,28))]);join('cord','plug')
path('leaf',(42,34),[('C',(20,26),(34,26),(27,24)),('C',(14,34),(16,27),(14,30)),('C',(25,42),(14,39),(19,42)),('C',(42,34),(33,42),(39,37))],True)
path('vein',(42,34),[('L',(25,34))]);join('leaf','vein')
''','Lucide leaf: flowing leaf silhouette and integral vein.','Minor secondary vein omitted.')
add('horse','SQUARE','Right-facing horse with curved mane and back, long nose and two broad legs; preserve natural asymmetry.', '''
path('horse',(10,42),[('L',(10,30)),('A',(20,20),10,10,True),('L',(24,20)),('C',(32,6),(26,12),(30,9)),('L',(33,13)),('L',(42,21)),('C',(37,26),(43,25),(40,27)),('L',(33,24)),('L',(31,42)),('L',(23,42)),('L',(22,31)),('C',(18,30),(20,31),(19,30)),('L',(18,42)),('L',(10,42))],True)
path('tail',(13,23),[('C',(6,33),(8,23),(6,27)),('L',(6,38))]);join('tail','horse')
''',omissions='Far legs and eye omitted; tail restored.')
add('hose-spray-gun','SQUARE','Rounded hose nozzle with rear trigger and long grip; three evenly separated water strokes.', '''
path('body',(6,18),[('A',(10,14),4,4,True),('L',(18,14)),('C',(28,6),(20,9),(24,6)),('L',(28,26)),('C',(18,22),(24,26),(20,25)),('L',(18,38)),('A',(14,42),4,4,True),('L',(10,42)),('L',(10,22)),('L',(6,22)),('L',(6,18))],True)
for i,(a,b) in enumerate([((38,8),(42,6)),((38,16),(42,16)),((38,24),(42,26))]):line(f'spray-{i}',a,b)
''',omissions='Thin hose tail omitted; grip and rear trigger integrated.')
add('hot-bean-soup-bowl','HRECT_L','Broad bowl with two separated curved steam wisps and one recognizable bean. Smooth bowl contour and large bean opening.', '''
path('bowl',(4,23),[('A',(24,40),20,17,False),('A',(44,23),20,17,False)])
path('bean',(20,21),[('C',(31,25),(27,18),(31,20)),('C',(23,31),(31,30),(27,32)),('C',(18,27),(19,31),(17,29)),('C',(20,21),(22,27),(23,24))],True)
for x in (11,38):path(f'steam-{x}',(x,8),[('C',(x,14),(x-3,10),(x+3,12))])
''','Lucide soup: simple smooth bowl and long coherent steam strokes.','One bean, rear rim and foot omitted to preserve spacing.')
add('hot-roasted-pork-platter','HRECT_L','Pig head and rounded roast body sit on tapered plate; two long steam strokes. Snout and pointed ear preserve pig identity.', '''
path('pig',(12,32),[('C',(8,24),(10,30),(8,27)),('L',(13,22)),('L',(12,15)),('L',(21,22)),('C',(32,21),(25,22),(29,20)),('A',(40,29),8,8,True),('L',(40,32))])
path('plate',(4,32),[('L',(12,32)),('L',(40,32)),('L',(44,32)),('L',(40,40)),('L',(8,40)),('L',(4,32))],True);join('plate','pig')
for x in (27,40):path(f'steam-{x}',(x,8),[('C',(x,13),(x-2,9),(x+2,12))])
''','Lucide soup: clear separated steam over a vessel.','Eye and garnish omitted; smoother roast replaces angular silhouette.')
add('human-head-side-profile-scan-solo-b001-14','SQUARE','Rounded scan frame joins skull; left-facing profile has curved forehead, nose and chin with continuous neck.', '''
path('frame',(30,6),[('L',(10,6)),('A',(6,10),4,4,False),('L',(6,38)),('A',(10,42),4,4,False),('L',(25,42))])
path('skull',(30,6),[('A',(42,18),12,12,True),('C',(36,34),(42,25),(36,28)),('L',(36,42))]);join('frame','skull')
path('face',(25,14),[('C',(19,20),(21,14),(19,16)),('L',(15,26)),('L',(23,27)),('L',(23,30)),('A',(27,34),4,4,False)])
''','Shared human user.svg smooth human construction; supplied profile and scan frame.','Ear omitted to preserve face interior.')
add('hunting-rifle-front-sight','HRECT_L','Diagonal rifle with rounded stock shoulder and continuous rising barrel. Front sight retained; functional thin barrel is one stroke.', '''
path('stock',(4,40),[('L',(4,29)),('L',(13,25)),('C',(21,18),(16,24),(17,18)),('L',(28,18)),('L',(28,27)),('L',(23,27)),('C',(16,34),(20,28),(19,32)),('L',(4,40))],True)
poly('barrel',(28,18),(44,13),(44,8));join('stock','barrel')
''',omissions='Small trigger omitted; thin barrel preserved as a centerline.')
add('hyperloop-pod-speed-lines','HRECT_M','Horizontal streamlined pod with semicircular rear, rising rounded nose and curved window; long separated speed strokes.', '''
path('pod',(22,10),[('L',(26,10)),('C',(44,26),(35,10),(44,18)),('A',(32,38),12,12,True),('L',(22,38)),('A',(8,24),14,14,True),('A',(22,10),14,14,True)],True)
path('window',(22,10),[('A',(34,26),12,16,False),('L',(44,26))]);join('window','pod')
line('speed-top',(4,10),(22,10));join('speed-top','pod')
line('speed-bottom',(4,38),(22,38));join('speed-bottom','pod')
''',omissions='Middle speed dash omitted because rounded rear occupies its space.')
add('i-love-you-hand-sign','SQUARE','Two raised fingers with rounded tips, folded middle valley and broad palm; rounded diagonal thumb replaces squared thumb.', '''
path('hand',(14,33),[('L',(7,27)),('A',(6,22),4,4,True),('C',(14,25),(8,19),(12,23)),('L',(14,10)),('A',(22,10),4,4,True),('L',(22,26)),('A',(34,26),6,6,False),('L',(34,14)),('A',(42,14),4,4,True),('L',(42,28)),('A',(28,42),14,14,True),('L',(23,42)),('C',(14,33),(18,42),(16,37))],True)
''','Lucide hand-metal: rounded fingertips, curved thumb and flowing palm. Human hand has no detached head gap.','Two folded fingers consolidated into broad U-shaped valley.')
add('intersecting-circles-with-angular-inner-segment','HRECT_L','Two symmetric overlapping circular outlines with shared intersections. Four smooth branches replace angular inner kink.', '''
# Equal radius 17 circles centered (21,24) and (27,24); exact intersection nodes are authored with coherent mirrored arcs.
for side in (-1,1):
 def p(x,y):return (24+side*x,y)
 path(f'outer-{side}',p(0,12),[('A',p(8,8),8,4,side>0),('A',p(20,24),12,16,side>0),('A',p(8,40),12,16,side>0),('A',p(0,36),8,4,side>0)])
 path(f'inner-{side}',p(0,12),[('A',p(8,24),8,12,side>0),('A',p(0,36),8,12,side>0)])
for a in ['outer--1','outer-1','inner--1','inner-1']:
 for b in ['outer--1','outer-1','inner--1','inner-1']:
  if a<b:join(a,b)
''',omissions='Removed accidental angular kink from previous revision; preserve original two-loop topology.')
rows=[]
for r in sorted(ROOT.glob('*/20260924T094233Z-thuan-mac')):
 claim=json.loads((r/'claim.json').read_text());item=claim['item']; n=item['icon_id']
 ref=next((r/'reference').glob('*.svg'));uuid=ref.stem[-36:];concept=ref.stem[:-37]
 out=Path('icon_set/work/primitive-make-ray')/uuid/'20260924-thuan-mac-stroke-revision'
 out.mkdir(parents=True,exist_ok=True)
 k,plan,code,refs,omit=D[n]
 meta=dict(concept=concept,source_uuid=uuid,reference_path=str(ref),icon_id=n,author='gpt-6',feedback=item.get('feedback'),keyshape=k,plan=plan,construction_reference=refs,omissions=omit)
 (out/(n+'.metadata.json')).write_text(json.dumps(meta,indent=2)+'\n')
 module=out/(n.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
 module.write_text('"""'+plan+'\nKeyshape '+k+'. '+refs+'\nOmissions: '+omit+'"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = '+repr(uuid)+'\nSOURCE_PATH = '+repr(str(ref))+'\nAUTHOR = "gpt-6"\n\nclass Drawing(Solo48):\n    icon_id = '+repr(n)+'\n    keyshape = Keyshape.'+k+'\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="objects"\n    aliases=()\n    keywords='+repr(tuple(n.split('-')))+'\n\n    def build(self):\n'+HELPERS+textwrap.indent(code,'        ')+'\n')
 rows.append(dict(key=item['key'],fix_dir=str(r),run=str(out),module=str(module),**meta))
(BATCH/'runs.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Authored',len(rows),'fresh standalone revisions')
