from pathlib import Path
import json,textwrap,sys,shutil
SOURCE_ICON_ID = None
SOURCE_PATH = 'batch.json'
AUTHOR = 'gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch.json').read_text())
HELPERS='''
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def bez(n,a,*segs): self.add_bezier(n,a,*segs)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,k=2):
            pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k),(l+k,t)]
            names=[]
            for i,(a,z) in enumerate(zip(pts,pts[1:])):
                if a==z: continue
                m=n+str(i); names.append(m)
                if i%2: arc(m,a,z,k)
                else: line(m,a,z)
            contour(n,*names,closed=True)
'''
DESIGNS={
0:('VRECT_L','Lucide grape and leaf: coherent lobes, internal berry cells and pointed leaf.', '''
arc('top-left',(24,24),(8,24),8,s=False)
arc('left-side',(8,24),(16,32),8,s=False)
arc('base',(16,36),(32,36),8,s=False)
line('lower-left',(16,32),(16,36))
line('lower-right',(32,36),(32,32))
arc('right-side',(32,32),(40,24),8,s=False)
arc('top-right',(40,24),(24,24),8,s=False)
contour('berry','top-left','left-side','lower-left','base','lower-right','right-side','top-right',closed=True)
poly('cells',(16,32),(24,24),(32,32));join('cells','berry')
bez('leaf',(24,16),((24,8),(32,4),(40,4)),((40,12),(36,16),(32,16)))
join('leaf','berry')
'''),
1:('VRECT_L','No exact Lucide corn match; leaf supplies smooth pointed contours.', '''
arc('cob-top',(16,12),(32,12),8)
line('cob-right',(32,12),(32,31));line('cob-left',(16,31),(16,12))
contour('cob','cob-left','cob-top','cob-right')
for y in (14,22):
    line('kernels-'+str(y),(16,y),(32,y));join('kernels-'+str(y),'cob')
bez('husk-left',(24,44),((10,44),(8,36),(8,26)),((18,28),(24,34),(24,44)))
bez('husk-right',(24,44),((24,34),(30,28),(40,26)),((40,36),(38,44),(24,44)))
join('husk-left','husk-right');join('cob','husk-left');join('cob','husk-right')
'''),
2:('SQUARE','Lucide thumbs-up: smooth thumb transition and continuous palm contour.', '''
poly('wrist',(14,24),(6,24),(6,40),(14,40))
bez('thumb-rise',(14,24),((20,20),(22,13),(22,6)))
arc('thumb-tip',(22,6),(30,14),8)
line('thumb-inner',(30,14),(28,22))
line('fingers-top',(28,22),(36,22))
arc('fingers-round',(36,22),(42,28),6)
line('fingers-side',(42,28),(42,34))
arc('palm-corner',(42,34),(34,42),8)
bez('palm',(34,42),((24,42),(18,40),(14,40)))
contour('hand','thumb-rise','thumb-tip','thumb-inner','fingers-top','fingers-round','fingers-side','palm-corner','palm')
join('wrist','hand')
line('crease',(33,32),(42,32));join('crease','hand')
'''),
3:('SQUARE','Lucide cable: unequal connectors with protruding ends and coherent S-shaped cord.', '''
box('plug-left',6,10,14,22,2)
line('tip-left',(10,6),(10,10));join('tip-left','plug-left')
line('cord-a',(10,22),(10,35));arc('cord-b',(10,35),(24,35),7,s=False)
line('cord-c',(24,35),(24,13));arc('cord-d',(24,13),(38,13),7)
line('cord-e',(38,13),(38,28))
contour('cord','cord-a','cord-b','cord-c','cord-d','cord-e')
box('plug-right',34,28,42,38,2)
line('tip-right',(38,38),(38,42))
join('tip-right','plug-right');join('cord','plug-left');join('cord','plug-right')
'''),
4:('SQUARE','Lucide calculator: evenly spaced keypad marks and rounded display.', '''
box('display',26,6,42,14,2)
line('stem',(34,14),(34,22));join('stem','display')
poly('body',(6,34),(12,22),(34,22),(36,22),(42,34),(42,42),(6,42),closed=True)
join('stem','body')
line('drawer',(6,34),(42,34));join('drawer','body')
for x in (18,28): self.add_dot('key-'+str(x),(x,26))
''')}
if (ROOT/'designs_extra.json').exists():
 DESIGNS.update({int(k):tuple(v) for k,v in json.loads((ROOT/'designs_extra.json').read_text()).items()})
for i,(shape,refs,code) in DESIGNS.items():
 if len(sys.argv)>1 and i not in [int(x) for x in sys.argv[1:]]:continue
 r=rows[i]
 if r.get('run'):
  old=Path(r['run']);num=int(old.name.rsplit('r',1)[-1])+1
 else:num=1
 run=Path('icon_set/work/primitive-make-ray')/r['source_uuid']/f'20260929-batch02-r{num}'
 run.mkdir(parents=True,exist_ok=False);r['run']=str(run)
 (run/(r['id']+'.metadata.json')).write_text(json.dumps({'concept':r['concept'],'source_uuid':r['source_uuid'],'reference_path':r['reference']},indent=2))
 (run/'review-before.txt').write_text(r['wrong']+'\nNo written feedback or reason recorded.\n'+r['change'])
 name=r['id'].replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py'
 txt=f'"""{r["change"]}\nSymbol plan: {refs}\nKeyshape {shape}; exact contract bounds.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {r["source_uuid"]!r}\nSOURCE_PATH = {r["reference"]!r}\nAUTHOR = "gpt-6"\n\nclass Drawing(Solo48):\n    icon_id = {r["id"]!r}\n    keyshape = Keyshape.{shape}\n    category = "objects"\n    human_construction = "bust"\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    aliases = ()\n    keywords = ()\n    def build(self):\n'+HELPERS+textwrap.indent(textwrap.dedent(code),'        ')
 (run/name).write_text(txt)

(ROOT/'batch.json').write_text(json.dumps(rows,indent=2))
