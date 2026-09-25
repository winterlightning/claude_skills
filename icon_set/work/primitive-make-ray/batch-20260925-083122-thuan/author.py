from pathlib import Path
import json,textwrap,ast
ROOT=Path('icon_set/work/primitive-make-ray/batch-20260925-083122-thuan')
AUTHOR='gpt-6'
claims=json.loads((ROOT/'claims.json').read_text())
SOURCE_PATHS=[str(next((Path(p)/'reference').glob('*.svg'))) for p in claims]
SOURCE_ICON_IDS=[Path(p).stem[-36:] for p in SOURCE_PATHS]
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
designs=[
('VRECT_L','Restore organic branching antlers and a flowing deer profile with pointed ear and long muzzle.','No useful exact Lucide deer match; source profile and smooth shared branch nodes.', 'Omit the eye and one fine antler tine; retain three clear tips.', '''
path('head',(10,44),[('L',(18,28)),('C',(8,20),(11,28),(9,24)),('L',(15,20)),('C',(23,24),(19,20),(21,22)),('C',(31,24),(26,21),(28,22)),('C',(40,29),(34,26),(38,28)),('C',(35,35),(40,33),(39,35)),('L',(30,35)),('C',(26,44),(26,35),(26,39))])
path('antler',(23,24),[('C',(20,15),(23,20),(22,18)),('C',(18,4),(18,12),(18,8))])
path('left-tine',(20,15),[('C',(8,4),(11,14),(8,11))]);join('left-tine','antler')
path('right-tine',(23,24),[('C',(28,17),(23,20),(25,18)),('C',(36,4),(35,15),(36,10))]);join('right-tine','antler');join('antler','head');join('right-tine','head')
'''),
('VRECT_L','Restore a broad circular rotation loop with a clear arrow and smooth sweeping internal curve.','Lucide rotate-cw: coherent curved loop and open arrowhead.', 'No defining feature omitted; intentional open upper-right loop retained.', '''
path('loop',(36,13),[('C',(42,26),(40,17),(42,21)),('C',(39,36),(42,30),(41,33)),('C',(24,44),(35,41),(30,44)),('A',(6,26),18,18,True),('C',(12,12),(6,20),(8,15)),('C',(28,10),(17,8),(23,10))])
poly('arrow',(22,4),(28,10),(22,16));join('arrow','loop')
path('sweep',(12,12),[('C',(39,36),(15,25),(27,35))]);join('sweep','loop')
'''),
('SQUARE','Restore the jagged torn seam and diagonal top tape seam on the perspective parcel.','Lucide box: shared perspective corners and clean joined faces.', 'Short tape end simplified; retain the defining jagged tear.', '''
poly('outline',(24,6),(42,15),(42,33),(24,42),(6,33),(6,15),(14,11),closed=True)
poly('lid',(6,15),(24,24),(32,20),(42,15));join('lid','outline')
line('tape',(14,11),(32,20));join('tape','outline');join('tape','lid')
poly('tear',(24,24),(24,31),(29,29),(32,36));join('tear','lid')
line('bottom-seam',(24,39),(24,42));join('bottom-seam','outline')
'''),
('SQUARE','Restore three swept tines on each antler and smooth mirrored beams.','No useful exact Lucide match; mirrored shared curves follow the supplied antlers.', 'None; three side tines per beam retained.', '''
axis=24
for side in (-1,1):
    def pt(x,y):return (axis+side*(x-axis),y)
    name='left' if side==1 else 'right'
    # A single beam definition owns both mirrored instances.
    path(name+'-beam',pt(12,6),[('L',pt(12,14)),('C',pt(15,24),pt(12,18),pt(13,21)),('C',pt(20,36),pt(18,28),pt(20,32)),('L',pt(20,42))])
    for j,(a,b,c,d) in enumerate([((12,14),(6,10),(8,14),(6,13)),((15,24),(6,20),(10,24),(8,23)),((20,36),(10,32),(15,36),(12,35))]):
        path(f'{name}-tine-{j}',pt(*a),[('C',pt(*b),pt(*c),pt(*d))]);join(name+'-beam',f'{name}-tine-{j}')
'''),
('HRECT_L','Round the donkey muzzle and rump, preserve its upright ear and two clear legs.','Lucide rabbit supports smooth animal silhouette; preserve the supplied donkey logo posture.', 'No facial marks or hidden legs added; source silhouette retained.', '''
path('donkey',(4,21),[('C',(10,14),(4,19),(8,17)),('L',(10,8)),('C',(17,14),(14,9),(16,10)),('C',(22,18),(19,16),(20,18)),('L',(34,18)),('C',(40,25),(38,18),(40,20)),('L',(40,40)),('L',(32,40)),('L',(31,29)),('L',(23,29)),('L',(22,40)),('L',(14,40)),('L',(14,25)),('L',(10,22)),('C',(4,21),(7,26),(4,25))],True)
path('tail',(40,25),[('C',(44,32),(42,27),(43,30))]);join('tail','donkey')
'''),
('SQUARE','Restore a smooth diagonal capsule handle and oval mirror joined by a thin angled neck.','Lucide search: clean mirror/head and handle junction; original oval retained.', 'Reflective marks omitted as in the source; oval perspective retained.', '''
path('mirror',(6,36),[('C',(14,30),(6,32),(10,30)),('C',(20,32),(17,30),(19,31)),('C',(22,36),(21,33),(22,34)),('C',(14,42),(22,40),(18,42)),('C',(6,36),(10,42),(6,40))],True)
path('grip',(26,20),[('L',(36,10)),('C',(42,16),(40,6),(46,12)),('L',(32,26)),('C',(26,26),(30,28),(28,28)),('C',(26,20),(24,24),(24,22))],True)
line('neck',(20,32),(26,26));join('neck','mirror');join('neck','grip')
'''),
('VRECT_L','Restore recognizable land detail within the tilted desk globe and a rounded pedestal.','Lucide earth: simplified continent boundary inside a circle; globe provides circular construction.', 'Fine coastline detail reduced to one broad continuous land boundary.', '''
# Concentric ball/support and tilted axial connections retain the desk-globe silhouette.
path('globe',(26,4),[('A',(40,18),14,14,True),('A',(26,32),14,14,True),('A',(12,18),14,14,True),('A',(26,4),14,14,True)],True)
path('support',(12,4),[('C',(6,18),(8,8),(6,12)),('A',(26,38),20,20,False),('C',(40,32),(32,38),(37,36))])
line('axis-top',(12,4),(16,8))
line('axis-bottom',(36,28),(40,32))
path('land',(26,4),[('C',(20,11),(26,9),(20,7)),('C',(25,16),(20,15),(25,12)),('C',(26,25),(28,20),(29,25)),('C',(20,20),(22,25),(23,20)),('C',(12,18),(18,20),(17,18))]);join('land','globe')
line('post',(26,38),(26,44));join('post','support')
path('base',(14,46),[('A',(18,42),4,4,True),('L',(34,42)),('A',(38,46),4,4,True),('L',(14,46))],True)
'''),
('HRECT_L','Enlarge the tape hub and lower the cutter deck so the dispenser reads as a roll on a weighted base.','No useful exact Lucide tape match; concentric roll and hub with a stepped connected housing.', 'Fine cutting teeth omitted; roll, open hub and cutter deck retained.', '''
path('roll',(4,21),[('A',(17,8),13,13,True),('A',(30,21),13,13,True),('A',(29,26),13,13,True),('A',(17,34),13,13,True),('A',(4,21),13,13,True)],True)
circle('hub',17,21,5)
poly('body',(4,21),(4,40),(44,40),(44,26),(29,26));join('body','roll')
''')]
manifest=[]
for index,(claim,design) in enumerate(zip(claims,designs),1):
 p=Path(claim);item=json.loads((p/'claim.json').read_text())['item'];ref=next((p/'reference').glob('*.svg'));uid=ref.stem[-36:];concept=ref.stem[:-37];ident=item['icon_id']
 keyshape,note,lucide,omissions,body=design
 run=Path('icon_set/work/primitive-make-ray')/uid/'20260925T083122-thuan-fix';run.mkdir(parents=True,exist_ok=False)
 metadata=dict(concept=concept,source_uuid=uid,reference_path=str(ref));(run/f'{ident}.metadata.json').write_text(json.dumps(metadata,indent=2))
 module=run/(ident.replace('-','_')+'_'+uid.replace('-','_')+'.py')
 content=f'''"""{note}\nPlan: named coherent contours; repeated elements share parameters.\nKeyshape: {keyshape} for the subject's natural orientation.\nConstruction: {lucide}\nReduction: {omissions}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {uid!r}\nSOURCE_PATH = {str(ref)!r}\nAUTHOR = 'gpt-6'\n\nclass Drawing(Solo48):\n    icon_id = {ident!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = {item['category']!r}\n    aliases = ()\n    keywords = {tuple(concept.split())!r}\n\n    def build(self):\n'''+helpers+textwrap.indent(textwrap.dedent(body),'        ')
 module.write_text(content)
 manifest.append(dict(index=index,key=item['key'],run=str(run),module=str(module),note=note,reference=lucide,omissions=omissions,**metadata))
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2));print('Authored',len(manifest))
