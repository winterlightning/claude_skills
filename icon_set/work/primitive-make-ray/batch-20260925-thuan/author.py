from pathlib import Path
import json,re,textwrap
SOURCE_ICON_ID = 'batch-metadata-in-each-module'
SOURCE_PATH = 'claims.json'
AUTHOR = 'gpt-6'
ROOT=Path('icon_set/work/primitive-make-ray/batch-20260925-thuan')
helpers='''
        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
# Revisions are independently authored from rendered references; each body owns its shapes.
designs=[
('VRECT_L','Smooth horse neck, distinct muzzle and ear, wider stable pedestal.','No useful exact Lucide match; coherent horse contour.', '''
path('horse',(12,34),[('C',(22,21),(12,28),(23,27)),('L',(15,23)),('C',(8,20),(11,26),(8,23)),('C',(13,13),(8,18),(11,15)),('L',(20,7)),('L',(20,4)),('C',(36,17),(29,7),(36,12)),('C',(34,34),(38,23),(34,29))])
box('base',8,34,40,44,3)
join('horse','base')
'''),
('VRECT_L','Restore tall tapered chess body below the three-point royal crown and larger finial.','Lucide crown: balanced repeated tips.', '''
circle('finial',24,8,4)
path('piece',(12,36),[('L',(16,22)),('L',(12,19)),('L',(12,13)),('L',(19,17)),('L',(24,13)),('L',(29,17)),('L',(36,13)),('L',(36,19)),('L',(32,22)),('L',(36,36)),('A',(40,40),4,4,True),('L',(40,44)),('L',(8,44)),('L',(8,40)),('A',(12,36),4,4,True)],True)
line('base-seam',(12,36),(36,36));join('piece','base-seam')
'''),
('SQUARE','More natural meaty diagonal taper, rounded bone and two clear bite scallops.','Lucide drumstick: broad meat and rounded bone.', '''
path('drumstick',(8,33),[('C',(17,21),(13,31),(14,26)),('C',(29,6),(21,14),(24,6)),('L',(34,6)),('C',(36,15),(32,11),(32,15)),('C',(42,22),(34,20),(37,24)),('C',(23,33),(38,28),(28,30)),('C',(16,41),(19,36),(19,42)),('C',(10,40),(13,44),(11,42)),('C',(6,36),(6,40),(6,38)),('C',(8,33),(6,34),(7,33))],True)
'''),
('HRECT_L','Longer pointed pepper with flowing belly and clean curved stalk.','No useful exact Lucide match; smooth organic silhouette.', '''
path('pepper',(4,26),[('C',(31,18),(17,29),(24,24)),('C',(41,21),(36,13),(41,16)),('C',(23,40),(41,31),(32,40)),('C',(4,26),(13,40),(6,33))],True)
path('stem',(39,17),[('C',(44,12),(42,17),(44,15)),('C',(40,8),(44,10),(43,8))])
'''),
('VRECT_L','Steeper mirrored chevrons restore vertical compression direction.','Lucide chevrons-down-up: paired open angles.', '''
axis=24
for name,edge,tip in [('down',4,20),('up',44,28)]:
    poly(name,(axis-16,edge),(axis,tip),(axis+16,edge))
'''),
('VRECT_L','Equal-angle inward chevrons with a clear central gap.','Lucide chevrons-down-up: paired open angles.', '''
axis=24
for name,edge,tip in [('down',4,20),('up',44,28)]:
    poly(name,(axis-16,edge),(axis,tip),(axis+16,edge))
'''),
('HRECT_L','Restore gently sloping seat back, raised front lip and fine runner supports.','No useful exact Lucide match; smooth coherent sleigh contours.', '''
path('body',(4,8),[('L',(17,10)),('C',(21,18),(21,10),(21,13)),('L',(21,22)),('L',(30,22)),('C',(39,16),(32,17),(35,16)),('L',(39,28)),('L',(12,28)),('A',(4,20),8,8,True),('L',(4,8))],True)
path('runner',(4,40),[('L',(34,40)),('A',(44,30),10,10,False)])
for name,a,b in [('rear',(16,28),(10,40)),('front',(28,28),(34,40))]:
    line(name,a,b);join(name,'body');join(name,'runner')
'''),
('SQUARE','Restore separate chisel blade and handle above a flowing carved wood surface.','No exact Lucide match; rounded tool grip and coherent wood contour.', '''
path('handle',(26,16),[('L',(35,7)),('A',(41,13),4,4,True),('L',(32,22)),('L',(26,16))],True)
path('blade',(26,22),[('L',(19,29)),('A',(13,23),4,4,True),('L',(20,16)),('L',(26,22))],True)
path('wood',(6,32),[('L',(13,32)),('C',(24,36),(18,32),(18,36)),('C',(36,30),(29,36),(29,30)),('L',(42,30)),('L',(42,42)),('L',(6,42)),('L',(6,32))],True)
'''),
('SQUARE','Smaller circular hinge and longer splayed compass legs; deliberate diagonal posture.','Lucide drafting-compass: circular hinge and braced legs.', '''
circle('hinge',32,14,7)
line('grip',(37,9),(40,6))
poly('left-leg',(26,18),(18,24),(6,33))
poly('right-leg',(32,21),(29,30),(25,42))
line('brace',(18,24),(29,30));join('brace','left-leg');join('brace','right-leg')
'''),
('SQUARE','Rebalance drafting compass around smaller hinge and longer pointed legs.','Lucide drafting-compass: circular hinge and braced legs.', '''
circle('hinge',32,14,7)
line('grip',(37,9),(40,6))
poly('left-leg',(26,18),(18,24),(6,33))
poly('right-leg',(32,21),(29,30),(25,42))
line('brace',(18,24),(29,30));join('brace','left-leg');join('brace','right-leg')
'''),
('VRECT_L','Restore broad rounded shoulder block with circular detached head and exact 4px ink gap.','human_ref/user.svg: round head and broad smooth shoulders.', '''
circle('head',24,12,8)
path('body',(8,44),[('L',(8,38)),('A',(18,28),10,10,True),('L',(30,28)),('A',(40,38),10,10,True),('L',(40,44)),('L',(8,44))],True)
'''),
('CIRCLE','Extend the open circular ring and balance a crisp check inside it.','Lucide circle-check-big: open ring and independent check.', '''
path('ring',(44,24),[('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True),('C',(33,6),(28,4),(30,5))])
poly('check',(16,23),(24,31),(42,12))
'''),
('VRECT_L','Restore rounded document, square checkbox rows and visible horizontal text strokes.','Lucide mail rounded enclosure; repeated checklist rows from source.', '''
box('page',8,4,40,44,3)
for y in (16,32):
    poly(f'box-{y}',(15,y-3),(21,y-3),(21,y+3),(15,y+3),closed=True)
    line(f'text-{y}',(29,y),(33,y))
'''),
('VRECT_M','Slender champagne neck with rounded cap, flowing shoulders and rounded bottle base.','Lucide bottle-wine: narrow neck and flowing shoulders.', '''
path('bottle',(19,13),[('L',(19,9)),('A',(29,9),5,5,True),('L',(29,13)),('C',(38,29),(29,21),(38,22)),('L',(38,40)),('A',(34,44),4,4,True),('L',(14,44)),('A',(10,40),4,4,True),('L',(10,29)),('C',(19,13),(10,22),(19,21))],True)
line('cap-seam',(19,13),(29,13));join('cap-seam','bottle')
line('base-seam',(10,35),(38,35))
'''),
('SQUARE','Larger circular key bow, full length terminal tooth and balanced inner tooth.','Lucide key: round bow joined to a single shaft.', '''
path('bow',(25,26),[('A',(28,33),10,10,True),('A',(18,43),10,10,True),('A',(8,33),10,10,True),('A',(18,23),10,10,True),('A',(25,26),10,10,True)],True)
poly('shaft',(25,26),(31,20),(40,11),(45,16))
line('inner-tooth',(31,20),(36,25));join('bow','shaft');join('shaft','inner-tooth')
'''),
('SQUARE','Restore grand piano silhouette, level keyboard edge and distinct even keys and legs.','Lucide piano: smooth lid shoulder and repeated keys.', '''
path('lid',(10,26),[('L',(10,10)),('A',(14,6),4,4,True),('L',(20,6)),('C',(32,17),(25,6),(25,17)),('L',(36,17)),('A',(42,23),6,6,True),('L',(42,26))])
poly('keyboard',(10,26),(42,26),(42,36),(6,36),(6,31),(10,26),closed=True)
join('keyboard','lid')
for x in (16,24,32):
    line(f'key-{x}',(x,26),(x,31))
for x in (12,36):
    line(f'leg-{x}',(x,36),(x,42))
'''),
('SQUARE','Round both sponge pores and soften the asymmetric waisted silhouette.','No useful exact Lucide match; smooth organic outline.', '''
path('sponge',(22,6),[('C',(34,17),(31,6),(31,13)),('C',(42,28),(37,21),(42,21)),('C',(29,42),(42,36),(34,42)),('C',(17,32),(23,42),(23,34)),('C',(6,21),(9,30),(6,29)),('C',(22,6),(6,13),(15,6))],True)
circle('large-pore',19,18,3)
circle('small-pore',31,29,3)
'''),
('VRECT_L','Flowing nose, readable lips and natural chin with larger clear ear opening.','human_ref/user.svg supports smooth anatomy; no exact Lucide facial-profile match.', '''
path('face',(17,4),[('C',(8,20),(17,11),(8,16)),('C',(13,23),(8,23),(11,23)),('C',(12,29),(12,25),(11,27)),('C',(14,32),(12,31),(14,31)),('L',(14,35)),('C',(21,40),(14,40),(17,40)),('C',(37,30),(30,40),(37,36))])
path('ear',(30,13),[('C',(40,14),(30,5),(40,5)),('C',(33,23),(40,20),(37,23))])
path('neck',(27,39),[('C',(31,44),(29,40),(30,42))])
'''),
('HRECT_M','Shallower graceful eyelid with five fanned lashes and exact shared attachment nodes.','Lucide eye-closed: broad continuous lid and radial lashes.', '''
path('lid',(4,13),[('C',(10,20),(6,16),(8,18)),('C',(24,25),(14,23),(19,25)),('C',(38,20),(29,25),(34,23)),('C',(44,13),(40,18),(42,16))])
for j,(a,b) in enumerate([((10,20),(5,25)),((16,23),(12,32)),((24,25),(24,35)),((32,23),(36,32)),((38,20),(43,25))]):
    line(f'lash-{j}',a,b)
'''),
('HRECT_M','Rounded envelope corners and gently rounded flap tip restore the source construction.','Lucide mail: soft enclosure corners and continuous flap.', '''
box('envelope',4,10,44,38,3)
path('flap',(5,12),[('L',(21,25)),('C',(27,25),(23,27),(25,27)),('L',(43,12))])
''')]
manifest=[]
for index,(claim,design) in enumerate(zip(json.loads((ROOT/'claims.json').read_text()),designs)):
 p=Path(claim);item=json.loads((p/'claim.json').read_text())['item'];ref=next((p/'reference').glob('*.svg'))
 uid=ref.stem[-36:];concept=ref.stem[:-37];ident=item['icon_id'];keyshape,note,lucide,body=design
 run=Path('icon_set/work/primitive-make-ray')/uid/'20260925T0712-thuan-fix';run.mkdir(parents=True,exist_ok=False)
 metadata=dict(concept=concept,source_uuid=uid,reference_path=str(ref))
 (run/f'{ident}.metadata.json').write_text(json.dumps(metadata,indent=2))
 module=run/(ident.replace('-','_')+'_'+uid.replace('-','_')+'.py')
 content=f'''"""{note}\nPlan: coherent named contours and repeated dimensions. {keyshape} natural subject envelope.\nConstruction reference: {lucide}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {uid!r}\nSOURCE_PATH = {str(ref)!r}\nAUTHOR = 'gpt-6'\n\nclass Drawing(Solo48):\n    icon_id = {ident!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = 'objects'\n    aliases = ()\n    keywords = {tuple(concept.split())!r}\n\n    def build(self):\n'''+helpers+textwrap.indent(textwrap.dedent(body),'        ')
 module.write_text(content)
 manifest.append(dict(index=index+1,key=item['key'],run=str(run),module=str(module),note=note,reference=lucide,**metadata))
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))
print('Authored',len(manifest))
