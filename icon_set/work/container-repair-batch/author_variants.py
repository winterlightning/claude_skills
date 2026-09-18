"""Review variants; SOURCE_ICON_ID/SOURCE_PATH inherited per source, AUTHOR gpt-6."""
import ast,json,re,textwrap
from pathlib import Path
from icon_set.scripts.create_variant import prepare_variant
OUT=Path(__file__).parent
plans={}
def plan(n,key,center,reason,body):plans[n]=(key,center,reason,textwrap.dedent(body).strip())
plan('open-handle-shopping-basket','SQUARE',[32,40],'Deepen the basket and shorten the open handles, retaining taper.', '''
poly('basket',(2,18),(62,18),(54,62),(10,62),closed=True)
for x,tip in ((14,22),(50,42)):
 line(f'handle-{x}',(x,18),(tip,2));join('basket',f'handle-{x}')
''')
plan('arched-handle-shopping-basket','SQUARE',[32,40],'Deepen the basket body while retaining the arched handle and rim.', '''
poly('basket',(6,18),(12,62),(52,62),(58,18))
line('rim',(2,18),(62,18));join('rim','basket')
path(self,'handle',(6,18),[('L',(16,6)),('A',(24,2),10,10,True),('L',(40,2)),('A',(48,6),10,10,True),('L',(58,18))]);join('handle','basket');join('handle','rim')
''')
plan('awning-storefront-container','SQUARE',[32,40],'Raise the awning and broaden the storefront opening.', '''
path(self,'awning',(2,10),[('L',(8,2)),('L',(56,2)),('L',(62,10)),('A',(42,10),10,6,True),('A',(22,10),10,6,True),('A',(2,10),10,6,True)],True)
poly('shop',(12,16),(12,62),(52,62),(52,16));join('shop','awning')
''')
plan('bottom-fold-note-container','SQUARE',[30,30],'Reduce the folded corner to leave the central paper area clear.', '''
poly('paper',(2,2),(62,2),(62,50),(50,62),(2,62),closed=True)
poly('fold',(50,62),(50,50),(62,50));join('fold','paper')
''')
plan('cargo-delivery-truck-container','SQUARE',[23,25],'Broaden and deepen the cargo box; keep a compact cab and both wheels.', '''
path(self,'body',(8,55),[('L',(2,55)),('L',(2,2)),('L',(44,2)),('L',(44,55)),('L',(22,55))])
path(self,'cab',(44,24),[('L',(52,24)),('A',(62,34),10,10,True),('L',(62,55)),('L',(61,55))]);join('body','cab')
line('windshield',(52,34),(62,34));join('windshield','cab')
line('axle',(44,55),(47,55));join('body','axle')
for x in (15,54):ellipse(self,f'wheel-{x}',x,55,7)
join('body','wheel-15');join('cab','wheel-54');join('axle','wheel-54')
''')
plan('delivery-van-container','SQUARE',[24,25],'Increase van body height, retaining the stepped roof, sloping windshield and wheels.', '''
path(self,'body',(8,55),[('L',(2,55)),('L',(2,2)),('L',(40,2)),('L',(40,18)),('L',(48,18)),('L',(62,34)),('L',(62,55)),('L',(61,55))])
line('sill',(22,55),(47,55));line('window',(51,34),(62,34));join('window','body')
for x in (15,54):
 ellipse(self,f'wheel-{x}',x,55,7);join('body',f'wheel-{x}');join('sill',f'wheel-{x}')
''')
plan('digital-video-camera','HRECT_XL',[25,32],'Taller camera body and a narrower attached lens wedge.', '''
rect(self,'body',2,6,48,58,6)
poly('lens',(48,22),(62,14),(62,50),(48,42));join('body','lens')
''')
plan('closed-padlock-container','VRECT_XL',[32,40],'Raise the body top and shorten the shackle while keeping the closed lock.', '''
rect(self,'body',6,18,58,62,5)
path(self,'shackle',(20,18),[('L',(20,14)),('A',(44,14),12,12,True),('L',(44,18))]);join('shackle','body')
''')
plan('unlocked-security-padlock','VRECT_XL',[32,40],'Raise the lock body and use a smaller open shackle, retaining a clear opening.', '''
rect(self,'body',6,18,58,62,5)
path(self,'shackle',(20,18),[('L',(20,12)),('A',(40,12),10,10,True)]);join('shackle','body')
''')
plan('double-concentric-circles','CIRCLE',[32,32],'Increase the inner circle by one grid unit while retaining two concentric rings.', '''
ellipse(self,'outer-ring',32,32,30)
ellipse(self,'inner-ring',32,32,22)
''')
plan('double-speech-bubbles','SQUARE',[26,24],'Deepen the front message while preserving both speech tails and the rear bubble.', '''
path(self,'front',(6,2),[('L',(46,2)),('A',(50,6),4,4,True),('L',(50,42)),('A',(46,46),4,4,True),('L',(22,46)),('L',(10,54)),('L',(10,46)),('L',(6,46)),('A',(2,42),4,4,True),('L',(2,6)),('A',(6,2),4,4,True)],True)
path(self,'rear',(50,30),[('L',(58,30)),('A',(62,34),4,4,True),('L',(62,52)),('L',(58,52)),('L',(58,62)),('L',(44,54)),('L',(34,54)),('A',(30,50),4,4,True),('L',(30,46))]);join('front','rear')
''')
plan('film-frame-container','SQUARE',[32,32],'Retain both rows of film perforations; remove the redundant horizontal dividers.', '''
rect(self,'frame',2,2,62,62,6)
for y in (10,54):
 for x in (14,30,46):line(f'perforation-{x}-{y}',(x,y),(x+4,y))
''')
plan('gas-station-fuel-pump','SQUARE',[25,39],'Widen the pump body and shorten its display to open the lower panel.', '''
rect(self,'body',2,2,48,62,4)
rect(self,'display',10,10,40,18,2)
path(self,'hose',(48,46),[('L',(51,46)),('A',(58,39),7,7,False),('L',(58,16)),('L',(62,8))]);join('body','hose')
''')
plan('gift-box-container','SQUARE',[32,40],'Use a compact bow and thin lid above a taller gift box.', '''
rect(self,'lid',2,12,62,20,2)
path(self,'box',(6,20),[('L',(6,56)),('A',(12,62),6,6,False),('L',(52,62)),('A',(58,56),6,6,False),('L',(58,20))]);join('box','lid')
for side in (-1,1):
 def p(x,y):return (32+side*x,y)
 path(self,f'bow-{side}',p(0,12),[('L',p(10,2)),('A',p(18,10),8,8,side>0),('L',p(0,12))],True)
 join(f'bow-{side}','lid')
join('bow--1','bow-1')
''')
plan('hanging-pennant-banner','VRECT_XL',[32,33],'Widen the banner while keeping the cord and pointed lower edge.', '''
line('rod',(6,12),(58,12));poly('cord',(10,12),(32,2),(54,12))
poly('banner',(10,12),(10,50),(32,62),(54,50),(54,12))
join('rod','cord');join('rod','banner');join('cord','banner')
''')
plan('hanging-shop-signboard','SQUARE',[27,38],'Taller hanging sign with a shorter suspension and unchanged support.', '''
rect(self,'panel',2,16,52,60,3)
path(self,'support',(2,2),[('L',(56,2)),('A',(62,8),6,6,True),('L',(62,62))])
for x in (12,44):
 line(f'hanger-{x}',(x,2),(x,16));join('support',f'hanger-{x}');join('panel',f'hanger-{x}')
''')
plan('industrial-factory-with-smokestacks','SQUARE',[32,41],'Raise the factory roof and shorten the twin smokestacks to deepen the main building.', '''
poly('building',(2,62),(2,18),(18,18),(32,10),(46,18),(62,18),(62,62),closed=True)
poly('stack-left',(4,18),(6,2),(14,2),(18,18));poly('stack-right',(46,18),(50,2),(58,2),(60,18))
join('building','stack-left');join('building','stack-right')
''')
plan('liquid-soap-dispenser-bottle','VRECT_XL',[32,40],'Broaden the bottle body while retaining the pump and sloping shoulders.', '''
path(self,'bottle',(26,12),[('L',(38,12)),('L',(41,18)),('L',(52,18)),('A',(58,24),6,6,True),('L',(58,56)),('A',(52,62),6,6,True),('L',(12,62)),('A',(6,56),6,6,True),('L',(6,24)),('A',(12,18),6,6,True),('L',(23,18)),('L',(26,12))],True)
line('stem',(32,12),(32,2));path(self,'pump',(40,2),[('L',(24,2)),('A',(18,8),6,6,False)]);join('stem','bottle');join('stem','pump')
''')
plan('open-book-container','HRECT_XL',[41,32],'Give the right page more width, keeping a narrower visible left page and curved binding.', '''
path(self,'outline',(2,6),[('A',(20,12),18,6,True),('A',(62,6),42,6,True),('L',(62,52)),('A',(20,58),42,6,False),('A',(2,52),18,6,False),('L',(2,6))],True)
line('spine',(20,12),(20,58));join('spine','outline')
''')
plan('open-envelope-with-letter','SQUARE',[32,25],'Lower the envelope fold so the letter has more visible height.', '''
path(self,'envelope',(62,38),[('L',(62,56)),('A',(56,62),6,6,True),('L',(8,62)),('A',(2,56),6,6,True),('L',(2,38))])
poly('fold',(2,38),(22,48),(42,48),(62,38));join('envelope','fold')
path(self,'paper',(10,42),[('L',(10,6)),('A',(14,2),4,4,True),('L',(50,2)),('A',(54,6),4,4,True),('L',(54,42))]);join('paper','fold')
for side,x,ex in [('left',10,2),('right',54,62)]:
 line('back-'+side,(ex,38),(x,30));join('back-'+side,'paper');join('back-'+side,'envelope');join('back-'+side,'fold')
for n,a,b in [('left',(22,48),(16,54)),('right',(42,48),(48,54))]:line('seam-'+n,a,b);join('seam-'+n,'fold')
''')
plan('oval-speech-bubble','HRECT_XL',[32,30],'Increase oval height, preserving the wide elliptical bubble and lower-left tail.', '''
path(self,'outline',(2,30),[('A',(32,6),30,24,True),('A',(62,30),30,24,True),('A',(32,54),30,24,True),('A',(14,49),30,24,True),('L',(6,58)),('L',(8,44)),('A',(2,30),30,24,True)],True)
''')
plan('panoramic-360-degree-virtual-reality-view','HRECT_XL',[32,32],'Narrow the folded side panels while retaining the curved panoramic outline.', '''
path(self,'outline',(2,16),[('A',(62,16),30,10,True),('L',(62,48)),('A',(2,48),30,10,True),('L',(2,16))],True)
poly('panel-left',(2,16),(10,20),(10,55));poly('panel-right',(62,16),(54,20),(54,55));join('panel-left','outline');join('panel-right','outline')
''')
plan('photo-camera-container','SQUARE',[32,37],'Enlarge the lens and camera body while preserving the raised top housing.', '''
path(self,'body',(8,10),[('L',(18,10)),('L',(24,2)),('L',(40,2)),('L',(46,10)),('L',(56,10)),('A',(62,16),6,6,True),('L',(62,56)),('A',(56,62),6,6,True),('L',(8,62)),('A',(2,56),6,6,True),('L',(2,16)),('A',(8,10),6,6,True)],True)
ellipse(self,'lens',32,37,19)
''')
plan('propane-gas-cylinder-tank','VRECT_XL',[32,33],'Widen and deepen the tank body; shorten the valve neck and base.', '''
rect(self,'tank',6,10,58,54,8)
line('cap',(18,2),(46,2))
for x in (24,40):line(f'neck-{x}',(x,2),(x,10));join('cap',f'neck-{x}');join('tank',f'neck-{x}')
path(self,'foot',(18,54),[('L',(10,62)),('L',(54,62)),('L',(46,54))]);join('tank','foot')
''')
plan('rectangular-picture-frame','SQUARE',[32,32],'Broaden the frame, keeping a uniform eight-unit centerline border.', '''
poly('outer',(2,2),(62,2),(62,62),(2,62),closed=True)
poly('inner',(10,10),(54,10),(54,54),(10,54),closed=True)
''')
plan('right-pointing-label-tag','HRECT_XL',[26,32],'Increase tag height while retaining its pointed right end.', '''
path(self,'outline',(7,6),[('L',(44,6)),('L',(62,32)),('L',(44,58)),('L',(7,58)),('A',(2,53),5,5,True),('L',(2,11)),('A',(7,6),5,5,True)],True)
''')
plan('round-bottom-chemistry-flask','VRECT_XL',[32,36],'Widen the round bulb and shorten the neck while retaining the flask silhouette.', '''
path(self,'vessel',(24,2),[('L',(24,12)),('A',(6,36),18,24,False),('A',(58,36),26,26,False),('A',(40,12),18,24,False),('L',(40,2))])
line('rim',(20,2),(44,2));join('rim','vessel')
''')
plan('search-magnifying-glass','SQUARE',[28,28],'Enlarge the lens slightly while retaining the diagonal handle.', '''
ellipse(self,'lens',28,28,26)
line('handle',(44,48),(62,62));join('lens','handle')
''')
plan('simple-folded-booklet','VRECT_XL',[32,38],'Widen the front cover while retaining the sloping rear cover.', '''
poly('front',(6,14),(58,14),(58,62),(6,62),closed=True)
poly('rear',(6,14),(54,2),(54,14));join('front','rear')
''')
plan('smartphone-front-camera-flash','VRECT_L',[32,40],'Move the camera band upward, keeping the lens and flash rays.', '''
path(self,'body',(48,10),[('A',(54,16),6,6,True),('L',(54,56)),('A',(48,62),6,6,True),('L',(16,62)),('A',(10,56),6,6,True),('L',(10,16)),('A',(16,10),6,6,True)])
line('divider',(10,20),(54,20));join('divider','body');self.add_dot('camera',(32,12))
line('ray-top',(32,2),(32,4));line('ray-left',(21,2),(23,4));line('ray-right',(43,2),(41,4));line('ray-west',(19,12),(23,12));line('ray-east',(41,12),(45,12))
''')
plan('soft-boiled-egg-in-cup','VRECT_XL',[32,28],'Widen the egg crown and lower the cup rim while retaining an egg-shaped top.', '''
self.add_arc('egg-crown',(8,46),(56,46),radius_x=24,radius_y=44)
line('cup-rim',(6,46),(58,46));self.add_arc('cup-bowl',(58,46),(6,46),radius_x=26,radius_y=16)
join('egg-crown','cup-rim');join('cup-bowl','cup-rim')
''')
plan('square-artboard-with-corner-indicators','SQUARE',[32,32],'Increase the artboard area and shorten the external indicator ticks.', '''
poly('artboard',(10,10),(54,10),(54,54),(10,54),closed=True)
for n,p in enumerate((10,54)):
 line(f'top-{n}',(p,2),(p,4));line(f'bottom-{n}',(p,60),(p,62));line(f'left-{n}',(2,p),(4,p));line(f'right-{n}',(60,p),(62,p))
''')
plan('stacked-browser-windows','SQUARE',[36,33],'Remove the secondary header divider while retaining its indicator and the rear window.', '''
rect(self,'front',10,2,62,52,6)
line('indicator',(20,10),(24,10))
path(self,'back',(10,14),[('L',(8,14)),('A',(2,20),6,6,False),('L',(2,56)),('A',(8,62),6,6,False),('L',(46,62)),('A',(52,56),6,6,False),('L',(52,52))]);join('back','front')
''')
plan('takeaway-cup-with-straw-container','VRECT_XL',[32,40],'Broaden the tapered cup body, retaining the lid and straw.', '''
poly('cup',(6,18),(58,18),(52,62),(12,62),closed=True)
line('rim',(6,10),(58,10));line('straw',(32,2),(32,10));join('rim','straw')
for x in (6,58):line(f'lid-{x}',(x,10),(x,18));join(f'lid-{x}','rim');join(f'lid-{x}','cup')
''')
# Start with geometric edits to these more shape-sensitive originals.
# Sedan and towel ring retain their distinctive proportions pending pair review.
rows=[]
sources=json.loads((OUT/'sources.json').read_text())
for source in sources:
 n=source['name']
 if n not in plans:continue
 key,center,reason,body=plans[n];dest,vid,original=prepare_variant(n,'container','Room for native 32-unit sub-icons')
 tree=ast.parse(original);cls=next(a for a in tree.body if isinstance(a,ast.ClassDef) and any(isinstance(t,ast.Assign) and any(isinstance(z,ast.Name) and z.id=='icon_id' for z in t.targets) for t in a.body))
 # Retain exact source metadata from the original file.
 metadata={}
 for a in tree.body:
  if isinstance(a,ast.Assign):
   for target in a.targets:
    if isinstance(target,ast.Name) and target.id in ('SOURCE_ICON_ID','SOURCE_PATH'):metadata[target.id]=ast.literal_eval(a.value)
 metadata.setdefault('SOURCE_ICON_ID',None);metadata.setdefault('SOURCE_PATH',None)
 srcid=metadata['SOURCE_ICON_ID']
 if srcid:dest=dest.with_name(dest.stem+'_'+srcid.replace('-','_')+'.py')
 text='"""'+reason+'\nConstruction: shared body/attachment coordinates, integer grid, 4-unit stroke.\nLucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.\n"""\nfrom ...keyshapes import Keyshape\nfrom ._base import Container64\nfrom ._construction import path, rounded_rect as rect, ellipse\n'
 for k,v in metadata.items():text+=f'{k} = {v!r}\n'
 text+="AUTHOR = 'gpt-6'\n\n"+f'class {cls.name}(Container64):\n    icon_id = {vid!r}\n    variant_of = {n!r}\n    variant_label = "Room for native 32-unit sub-icons"\n    keyshape = Keyshape.{key}\n    aliases = ()\n    keywords = ()\n\n    def build(self):\n        line, poly = self.add_line, self.add_polyline\n        def join(a,b): self.relate("connect",a,b)\n'+textwrap.indent(body,'        ')+'\n'
 dest.write_text(text);rows.append({'parent':n,'variant':vid,'module':str(dest),'center':center,'reason':reason})
(OUT/'variants.json').write_text(json.dumps(rows,indent=2));print('Authored',len(rows),'repair variants')
