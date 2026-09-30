from pathlib import Path
import json, re, datetime, sys
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts.build_gate import gate
BASE=Path(__file__).parent
rows=json.loads((BASE/'claims.json').read_text())
HELPERS='''
    def path(self,n,start,ops,closed=False):
        here=start; members=[]
        for i,(kind,end,*args) in enumerate(ops):
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,here,end)
            elif kind=='A': self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
            members.append(m); here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
'''
SPECS=[
('SQUARE','The rejected insect has an angular head and drooping wings; restore a round head, oval wings and a segmented abdomen. No written feedback.','Lucide bug: paired antennae and organized body parts. Legs and one stripe omitted for clearance.', '''
        self.circle('head',24,10,4)
        self.add_line('antenna-left',(20,10),(16,6)); self.relate('connect','antenna-left','head')
        self.add_line('antenna-right',(28,10),(32,6)); self.relate('connect','antenna-right','head')
        self.path('body',(24,14),[('C',(30,24),(29,14),(30,18)),('L',(30,32)),('C',(24,42),(30,37),(27,41)),('C',(18,32),(21,41),(18,37)),('L',(18,24)),('C',(24,14),(18,18),(19,14))],True)
        self.relate('connect','head','body')
        self.add_line('stripe',(18,32),(30,32));self.relate('connect','stripe','body')
        self.add_line('thorax-end',(18,24),(30,24));self.relate('connect','thorax-end','body')
        self.path('wing-left',(18,24),[('C',(6,23),(12,17),(6,17)),('C',(18,32),(6,30),(11,34))]);self.relate('connect','wing-left','body')
        self.path('wing-right',(30,24),[('C',(42,23),(36,17),(42,17)),('C',(30,32),(42,30),(37,34))]);self.relate('connect','wing-right','body')
        for side in ('left','right'):
            self.relate('connect',f'wing-{side}','thorax-end')
            self.relate('connect',f'wing-{side}','stripe')
        self.add_polyline('leg-left',(18,32),(10,38),(8,42));self.add_polyline('leg-right',(30,32),(38,38),(40,42))
        for side in ('left','right'):
            self.relate('connect',f'leg-{side}','body');self.relate('connect',f'leg-{side}',f'wing-{side}');self.relate('connect',f'leg-{side}','stripe')
'''),
('SQUARE','The rejected cloud has a pinched upright lobe and very short rain marks; restore a broad smooth cloud and diagonal rainfall with exposed sun. No written feedback.','Lucide cloud-sun-rain: coherent cloud lobes and detached rain. Two clear rays replace the finer ray series.', '''
        self.path('cloud',(10,30),[('A',(6,26),4,4,True),('A',(10,22),4,4,True),('A',(17,15),7,7,True),('A',(24,22),7,7,True),('A',(24,30),4,4,True),('L',(10,30))],True)
        self.path('sun',(24,22),[('A',(32,14),8,8,True),('A',(40,22),8,8,True),('A',(32,30),8,8,True),('L',(24,30))]);self.relate('connect','sun','cloud')
        self.add_dot('ray-top',(32,6))
        self.add_line('ray-diagonal',(40,6),(42,8))
        for x in (14,24,34):self.add_line(f'rain-{x}',(x,38),(x-3,42))

'''),
('VRECT_L','The rejected hill is a shallow flattened strip; restore a tall rounded hill beneath the partly hidden sun. No written feedback.','Lucide sunrise: separated radial rays and partial sun. Reference hill restored; only three main rays retained.', '''
        self.path('hill',(8,44),[('C',(12,32),(8,40),(10,35)),('C',(24,28),(15,29),(20,28)),('C',(36,32),(28,28),(33,29)),('C',(40,44),(38,35),(40,40)),('L',(8,44))],True)
        self.path('sun',(12,32),[('A',(36,32),12,12,True)]);self.relate('connect','sun','hill')
        self.add_line('ray-top',(24,4),(24,8))
        self.add_line('ray-left',(8,15),(10,17))
        self.add_line('ray-right',(38,17),(40,15))
'''),
('SQUARE','The rejected sun looks like a small loop attached to the cloud; restore a larger visible solar arc while preserving lightning and snow. No written feedback.','Lucide cloud-sun: sun partially hidden by the cloud. Fine rays omitted; two snow pellets retained.', '''
        self.path('cloud',(10,34),[('A',(6,30),4,4,True),('C',(16,26),(6,26),(16,32)),('A',(26,16),10,10,True),('A',(36,26),10,10,True),('C',(42,32),(40,26),(42,28))])
        self.path('sun',(16,26),[('A',(6,16),10,10,True),('A',(16,6),10,10,True),('A',(26,16),10,10,True)]);self.relate('connect','sun','cloud')
        self.add_polyline('bolt',(27,26),(22,34),(34,34),(26,42))
        self.add_dot('snow-left',(7,42));self.add_dot('snow-right',(41,42))

'''),
('SQUARE','The rejected face has one eye and a tiny round mouth; restore two eyes and the broad worried open mouth beside the sweat drop. No written feedback.','No useful exact Lucide face match; circular face arcs and mirrored mouth. Fine brows omitted; outline opens behind sweat.', '''
        self.path('face',(24,6),[('A',(6,24),18,18,False),('A',(24,42),18,18,False),('C',(40,34),(32,42),(38,39))])
        self.path('sweat',(38,6),[('L',(42,18)),('A',(34,18),4,4,True),('L',(38,6))],True)
        self.add_dot('eye-left',(17,17));self.add_dot('eye-right',(25,17))
        self.path('mouth',(18,31),[('A',(30,31),6,6,True),('L',(18,31))],True)
''')]
def author(indices):
    manifest=json.loads((BASE/'runs.json').read_text()) if (BASE/'runs.json').exists() else {}
    for idx in indices:
        r=rows[idx]; key=r['key'].split('/')[1]; ref=Path(r['ref']);uuid=re.search(r'[0-9a-f-]{36}$',ref.stem).group();concept=ref.stem[:-37]
        shape,finding,construction,body=SPECS[idx]
        stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ-batch08')
        out=ROOT/'icon_set/work/primitive-make-ray'/uuid/stamp;out.mkdir(parents=True)
        metadata=dict(concept=concept,source_uuid=uuid,reference_path=r['ref'])
        (out/f'{key}.metadata.json').write_text(json.dumps(metadata,indent=2))
        (out/'review-before.txt').write_text(finding+'\n'+construction+'\n')
        import shutil
        shutil.copy(BASE/f'actual-{idx+1}-ref.png',out/'reference.png');shutil.copy(BASE/f'actual-{idx+1}-before.png',out/'before.png')
        source=f'''"""{finding}\nSymbol plan: {construction}\nKeyshape {shape}, authored on the SOLO48 integer grid with 4-unit strokes.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={uuid!r}\nSOURCE_PATH={r['ref']!r}\nAUTHOR='gpt-6'\nclass Drawing(Solo48):\n    icon_id={key!r}\n    keyshape=Keyshape.{shape}\n    semantic_role='MAIN'\n    semantic_kind='noun'\n    category='primitives-generate'\n    aliases=()\n    keywords={tuple(key.split('-'))!r}\n'''+HELPERS+'\n    def build(self):\n'+body
        module=out/(key.replace('-','_')+'_'+uuid.replace('-','_')+'.py');module.write_text(source)
        icon=load_icon(module);report=icon.validate_icon();(out/'validation.txt').write_text(report.describe())
        svg=icon.to_svg();(out/f'{key}.svg').write_text(svg);render_previews(svg,key,48,out)
        g=gate(module,out/'gate');(out/'gate.json').write_text(json.dumps(g,indent=2))
        print(idx+1,key,report.describe(),g,flush=True)
        manifest[str(idx)]=str(out.relative_to(ROOT));(BASE/'runs.json').write_text(json.dumps(manifest,indent=2))
if __name__=='__main__':author([int(a)-1 for a in sys.argv[1:]] or list(range(5)))
