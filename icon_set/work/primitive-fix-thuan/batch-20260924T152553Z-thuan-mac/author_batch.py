from pathlib import Path
import json,re,textwrap,shutil
from icon_set.scripts.primitive_fix import load_icon,render_previews
AUTHOR='gpt-6'
SOURCE_ICON_ID=None # Multi-input orchestration; each authored module retains its exact source ID.
SOURCE_PATH=None
ROOT=Path('icon_set/work/primitive-fix-thuan')
BATCH=ROOT/'batch-20260924T152553Z-thuan-mac'
HELPERS='''
        def path(n,start,steps,closed=False):
            p=start; members=[]
            for i,step in enumerate(steps):
                m=f"{n}-{i}"
                if len(step)==2:
                    self.add_line(m,p,step);p=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(m,p,end,radius_x=rx,radius_y=ry,sweep=sweep);p=end
                members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[((x,y-r),r,r,True),((x+r,y),r,r,True),((x,y+r),r,r,True),((x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(a,b): self.relate('connect',a,b)
'''
# Each entry owns an independently composed symbol plan and geometry.
DESIGNS={
'rhinoceros-facing-right':('HRECT_L','Heavy rhino silhouette with rounded back, two broad legs, low muzzle and rising horn. No useful Lucide match. Inner leg seams omitted.', '''
path('rhino',(4,40),[(4,22),((18,8),14,14,True),(26,8),((32,14),6,6,True),(35,20),(44,12),(44,26),((38,32),6,6,True),(32,30),(32,40),(24,40),(24,30),(12,30),(12,40),(4,40)],True)
'''),
'right-facing-head-with-curled-breath-lines':('SQUARE','Circular rear skull, continuous neck, rounded open mouth and two outward breath curls. Human user.svg informs skull flow; preserve attached anatomical neck.', '''
path('head',(6,42),[(6,18),((18,6),12,12,True),((30,18),12,12,True),(30,20),(33,24),(25,24),((25,34),5,5,False),(27,34),((22,39),5,5,True),(22,42)])
path('breath-upper',(41,20),[((42,25),3,3,True),(39,27)])
path('breath-lower',(36,36),[(39,36),((42,39),3,3,True),((39,42),3,3,True)])
'''),
'right-facing-human-profile':('VRECT_L','Circular skull and smooth quarter-circle shoulder; continuous neck remains anatomical. Human user.svg informs circular skull and rounded shoulder. No detached head.', '''
path('profile',(24,44),[(24,28),((12,16),12,12,True),((24,4),12,12,True),((36,16),12,12,True),(40,22),(34,24),(34,32),(32,32)])
path('shoulder',(8,44),[((24,28),16,16,True)])
join('profile','shoulder')
'''),
'road-crossing-horizontal-line':('HRECT_L','Mirrored straight tapering road sides, a full width overpass and two center dashes; remove kinks in rejected road edges. No useful exact Lucide match.', '''
poly('left',(8,40),(12,24),(16,8))
poly('right',(40,40),(36,24),(32,8))
poly('bridge',(4,24),(12,24),(36,24),(44,24))
join('bridge','left');join('bridge','right')
line('dash-top',(24,8),(24,16));line('dash-bottom',(24,32),(24,40))
'''),
'rocket-passing-above-a-globe':('SQUARE','Diagonal pointed rocket with two fins above a curved globe, short exhaust and continent seam. Lucide rocket informs coherent pointed fuselage.', '''
path('rocket',(17,21),[(29,9),(42,6),(39,19),(27,31),(17,21)],True)
poly('fin-left',(17,21),(8,21),(13,16),(22,16));join('fin-left','rocket')
poly('fin-right',(27,31),(27,39),(32,34),(32,26));join('fin-right','rocket')
line('exhaust',(6,32),(10,28))
path('globe',(16,34),[((30,42),14,14,False),((42,30),12,12,False)])
'''),
'rolled-parchment-wavy-mark':('VRECT_L','Upright scroll with rounded rolled top and lower curl, one visible wave. Lucide scroll informs split shared boundaries and rolled-end construction.', '''
path('sheet',(12,4),[(30,4),((36,10),6,6,True),(36,34),(40,34),(40,38),((34,44),6,6,True),(18,44),((12,38),6,6,True),(12,20)])
path('top-roll',(8,20),[(8,8),((16,8),4,4,True),(16,20),(12,20),(8,20)],True)
join('sheet','top-roll')
path('lower-curl',(24,34),[(24,38),((30,44),6,6,False)]);join('lower-curl','sheet')
line('lip',(24,34),(36,34));join('lip','sheet');join('lip','lower-curl')
path('wave',(21,24),[((25,24),3,3,True),((29,24),3,3,False)])
'''),
'rolled-sheet-with-loose-end':('HRECT_L','Horizontal cylinder with open spiral front and a loose sheet extending to lower right; circle and cylinder use shared tangent extrema. Lucide cylinder informs barrel.', '''
path('spiral',(17,23),[((13,19),4,4,True),((19,13),6,6,True),((27,21),8,8,True),((16,32),11,11,True),((4,20),12,12,True),((16,8),12,12,True)])
path('barrel',(16,8),[(32,8),((44,20),12,12,True),((32,32),12,12,True),(16,32)])
join('spiral','barrel')
poly('flap',(16,32),(24,40),(44,40),(36,32));join('flap','barrel');join('flap','spiral')
'''),
'roller-coaster-ferris-wheel':('SQUARE','Ferris wheel with radial spokes and splayed supports beside a smooth descending coaster track. Lucide ferris-wheel informs radial wheel.', '''
circle('wheel',30,18,12)
poly('spoke-v',(30,6),(30,18),(30,30));poly('spoke-h',(18,18),(30,18),(42,18))
join('spoke-v','wheel');join('spoke-h','wheel');join('spoke-v','spoke-h')
poly('support',(24,42),(30,30),(36,42));join('support','wheel');join('support','spoke-v')
path('track',(6,42),[(6,30),((14,30),4,4,True),((26,42),12,12,False),(42,42)])
join('track','support')
'''),
'rotating-valve-handle':('SQUARE','Centered horizontal valve handle and stem above a broad base, flanked by opposite rotation arrows. Lucide rotate-cw informs curved directional arrows.', '''
path('handle',(19,14),[(29,14),((29,22),4,4,True),(24,22),(19,22),((19,14),4,4,True)],True)
line('stem',(24,22),(24,38));join('stem','handle')
poly('base',(14,42),(14,38),(24,38),(34,38),(34,42));join('base','stem')
path('left-arrow',(12,6),[((6,18),15,15,False),(6,28),(12,28)])
poly('left-head',(6,20),(6,28),(14,28));join('left-head','left-arrow')
path('right-arrow',(36,36),[((42,24),15,15,False),(42,6),(34,6)])
poly('right-head',(34,6),(42,6),(42,14));join('right-head','right-arrow')
'''),
'round-antenna-on-splayed-legs':('SQUARE','Circular antenna with horizontal divider, two splayed supports, balanced curved signal arcs. Lucide radio-tower informs paired arcs and splayed support.', '''
circle('dish',24,21,9)
poly('divider',(15,21),(24,21),(33,21));join('divider','dish')
poly('legs',(16,42),(24,30),(32,42));join('legs','dish')
path('signal-left',(10,6),[((6,24),25,25,False),((10,34),18,18,False)])
path('signal-right',(38,6),[((42,24),25,25,True),((38,34),18,18,True)])
'''),
'round-baby-head-with-one-curl':('CIRCLE','Closed circular baby face, integrated ears and one top curl; Lucide baby informs circular face and curl; human user.svg supplies circular anatomy. Facial dots omitted because source is blank.', '''
path('head',(6,20),[((24,4),18,18,True),((42,20),18,18,True),(44,20),((44,28),4,4,True),(42,28),((24,44),18,18,True),((6,28),18,18,True),(4,28),((4,20),4,4,True),(6,20)],True)
path('curl',(24,4),[((30,10),6,6,True),((24,16),6,6,True),((18,10),6,6,True)]);join('curl','head')
'''),
'round-bodied-hen':('HRECT_L','Smooth broad hen body with rounded head, beak, tail and two separate feet; Lucide bird informs flowing neck and body. Tiny comb seam omitted.', '''
path('hen',(4,16),[(12,24),(24,24),(24,16),((32,8),8,8,True),((40,16),8,8,True),(44,20),(40,24),(40,28),((28,40),12,12,True),(20,40),((4,24),16,16,True),(4,16)],True)
'''),
'round-bottom-flask-solo':('VRECT_L','Round flask with straight neck, distinct rolled lip and exact tangent circular bulb. Lucide flask-round informs circular bulb and upright neck. No liquid line because reference is empty.', '''
path('bulb',(18,16),[(18,4),(30,4),(30,16),((40,30),16,16,True),((24,44),16,14,True),((8,30),16,14,True),((18,16),16,16,True)],True)
line('lip-left',(14,4),(18,4));line('lip-right',(30,4),(34,4));join('lip-left','bulb');join('lip-right','bulb')
'''),
'round-gift-with-tied-ribbon':('CIRCLE','Round gift with horizontal and vertical ribbon and mirrored broad bow loops. Lucide gift informs matched bow lobes, avoiding overlapped knotted strokes.', '''
circle('box',24,24,20)
poly('ribbon-h',(4,24),(24,24),(44,24));poly('ribbon-v',(24,24),(24,44));join('ribbon-h','box');join('ribbon-v','box');join('ribbon-h','ribbon-v')
path('bow-left',(24,24),[(16,22),((16,12),5,5,True),((24,20),8,8,True),(24,24)],True)
path('bow-right',(24,24),[(24,20),((32,12),8,8,True),((32,22),5,5,True),(24,24)],True)
for a in ['bow-left','bow-right']:
 join(a,'ribbon-h');join(a,'ribbon-v')
join('bow-left','bow-right')
'''),
'round-hatbox-with-loop-handle':('VRECT_L','Cylinder with oval lid and broad semicircular loop handle seated at actual shared lid endpoints. Lucide cylinder informs equal curved top and bottom.', '''
path('lid',(8,24),[((24,16),16,8,True),((40,24),16,8,True),((24,32),16,8,True),((8,24),16,8,True)],True)
path('body',(8,24),[(8,36),((24,44),16,8,False),((40,36),16,8,False),(40,24)]);join('body','lid')
path('handle',(16,17),[(16,12),((32,12),8,8,True),(32,17)])
'''),
'round-lantern':('VRECT_L','Circular lantern globe divided by centered ribs; arched top handle and separate base. Circular joins split at exact nodes. No useful Lucide lamp match for this globe lantern.', '''
circle('globe',24,26,16)
poly('vertical',(24,10),(24,26),(24,42));poly('horizontal',(8,26),(24,26),(40,26))
join('vertical','globe');join('horizontal','globe');join('vertical','horizontal')
path('handle',(16,12),[(16,8),((24,4),8,4,True),((32,8),8,4,True),(32,12)])
poly('base',(16,40),(16,44),(32,44),(32,40))
'''),
'round-meatball-with-short-curved-marks':('CIRCLE','Circular meatball with four curved texture strokes arranged rotationally around center. Lucide cookie informs sparse internal texture; restore reference arcs instead of dots.', '''
circle('ball',24,24,20)
for i,(a,b) in enumerate([((15,22),(20,16)),((26,14),(32,19)),((34,26),(29,32)),((22,34),(16,29))]):
 self.add_arc(f'texture-{i}',a,b,radius_x=8,sweep=True)
'''),
'rounded-armchair-with-inset-seat-cushion':('SQUARE','Rounded armchair with thick arms, inset seat and two feet; Lucide armchair informs one coherent lower silhouette and tangent corners.', '''
path('back',(14,20),[(14,12),((20,6),6,6,True),(28,6),((34,12),6,6,True),(34,20)])
path('chair',(14,28),[(14,22),((6,22),4,4,False),(6,34),((10,38),4,4,False),(38,38),((42,34),4,4,False),(42,22),((34,22),4,4,False),(34,28),(14,28)],True)
join('back','chair')
line('foot-left',(10,38),(10,42));line('foot-right',(38,38),(38,42));join('foot-left','chair');join('foot-right','chair')
'''),
'rounded-camping-caravan':('HRECT_L','Rounded caravan with upright doorway, window opening, one wheel and tow bar. Lucide caravan informs continuous shell broken at the wheel.', '''
path('shell',(11,35),[(4,35),(4,20),((16,8),12,12,True),(28,8),((40,20),12,12,True),(40,35),(21,35)])
circle('wheel',16,35,5);join('shell','wheel')
poly('door',(28,35),(28,19),(40,19));join('door','shell')
line('window',(12,19),(19,19))
line('tow',(40,35),(44,35));join('tow','shell')
'''),
'rounded-car-under-sun':('SQUARE','Complete rounded side car with two wheels below sun; Lucide car informs wheel breaks and roof slope. Tiny window seam and fine sun rays omitted.', '''
path('body',(9,37),[(6,37),(6,30),((12,24),6,6,True),(18,18),(24,18),(32,24),(36,24),((42,30),6,6,True),(42,37),(39,37)])
circle('rear-wheel',14,37,5);circle('front-wheel',34,37,5)
line('sill',(19,37),(29,37));join('sill','rear-wheel');join('sill','front-wheel');join('body','rear-wheel');join('body','front-wheel')
circle('sun',37,9,3)
''')}

def main():
 overrides=BATCH/"revisions.json"
 if overrides.exists(): DESIGNS.update(json.loads(overrides.read_text()))
 ledger=[]
 for claim in sorted(ROOT.glob('*/20260924T152553Z-thuan-mac/claim.json')):
  data=json.loads(claim.read_text());item=data['item'];id=item['icon_id'];ref=next((claim.parent/'reference').glob('*.svg'));uuid=re.search(r'[0-9a-f-]{36}$',ref.stem).group();concept=ref.stem[:-37]
  run=Path('icon_set/work/primitive-make-ray')/uuid/'20260924T153200Z-thuan-mac-revision';run.mkdir(parents=True,exist_ok=True)
  key,plan,body=DESIGNS[id]
  meta={'concept':concept,'source_uuid':uuid,'reference_path':str(ref),'icon_id':id,'author':AUTHOR,'feedback':item.get('feedback'),'plan':plan}
  (run/f'{id}.metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
  shutil.copyfile(ref,run/'reference.svg')
  module=run/(id.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
  module.write_text(f'"""{plan}\nKeyshape {key}; exact SOLO48 extremes from contract."""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={uuid!r}\nSOURCE_PATH={str(ref)!r}\nAUTHOR={AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id={id!r}\n    keyshape=Keyshape.{key}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="objects/reference"\n    aliases=()\n    keywords={tuple(id.split('-'))!r}\n    def build(self):\n'+HELPERS+textwrap.indent(textwrap.dedent(body).strip()+'\n','        '))
  try:
   icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg();(run/f'{id}.svg').write_text(svg);(run/'validation.txt').write_text(report.describe());render_previews(svg,id,48,run)
   print(id,report.status,len(report.errors),len(report.warnings),flush=True)
   if report.status!='valid' or report.warnings: print(report.describe(),flush=True)
  except Exception as e: print(id,type(e).__name__,str(e),flush=True)
  ledger.append({'id':id,'key':item['key'],'run':str(run),'module':str(module),'claim':str(claim.parent),'plan':plan})
 (BATCH/'ledger.json').write_text(json.dumps(ledger,indent=2)+'\n')
if __name__=='__main__':main()
