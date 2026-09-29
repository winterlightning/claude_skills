from pathlib import Path
import json,sys,textwrap,hashlib
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
BATCH=Path(__file__).parent
ITEMS=json.loads((BATCH/'items.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH=None
HELPERS='''
        # Typed path helpers own continuous contours, repeated radii and real junctions.
        def path(name,start,commands,closed=False):
            here=start;members=[]
            for i,c in enumerate(commands):
                kind,end,*args=c; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C':
                    c1,c2=args
                    self.add_bezier(ident,here,(c1,c2,end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
DESIGNS={
1:('VRECT_L','Rebuild a flowing headcloth around a circular face, with broad round shoulders and a central robe seam.','human_ref/user.svg; Lucide user-round', '''
path('veil',(8,34),[('L',(12,16)),('A',(36,16),12,12,True),('L',(40,34))])
path('face',(16,16),[('A',(32,16),8,8,False),('A',(16,16),8,8,True)],True)
path('shoulders',(8,44),[('L',(8,41)),('A',(20,29),12,12,True),('L',(28,29)),('A',(40,41),12,12,True),('L',(40,44))])
line('robe',(24,29),(24,44));join('robe','shoulders')
'''),
2:('VRECT_L','One symmetric outlined chevron with a constant diagonal band.','Lucide mountain: coherent line joins', '''
poly('chevron',(8,24),(28,4),(40,4),(20,24),(40,44),(28,44),closed=True)
'''),
3:('HRECT_L','Two equal circular loops, each with one tangent tail; rotational symmetry about the canvas center.','Lucide circle: circular arcs', '''
circle('upper-loop',12,16,8);circle('lower-loop',36,32,8)
line('upper-tail',(12,8),(44,8));line('lower-tail',(36,40),(4,40))
join('upper-loop','upper-tail');join('lower-loop','lower-tail')
'''),
4:('VRECT_M','Mirror top corner radii and center the bookmark notch.','Lucide bookmark: paired circular top corners', '''
path('bookmark',(10,44),[('L',(10,8)),('A',(14,4),4,4,True),('L',(34,4)),('A',(38,8),4,4,True),('L',(38,44)),('L',(24,34)),('L',(10,44))],True)
'''),
5:('SQUARE','Three equal circle nodes; bond endpoints use exact 3-4-5 circle points.','Lucide circle: equal circular nodes', '''
for n,x,y in [('top',24,11),('left',11,37),('right',37,37)]:
    path(n,(x-3,y+4),[('A',(x-5,y),5,5,True),('A',(x,y-5),5,5,True),('A',(x+5,y),5,5,True),('A',(x+3,y+4),5,5,True),('A',(x-3,y+4),5,5,True)],True)
line('left-bond',(21,15),(14,33));line('right-bond',(27,15),(34,33));line('base-bond',(16,37),(32,37))
join('top','left-bond');join('top','right-bond');join('left','left-bond');join('right','right-bond');join('left','base-bond');join('right','base-bond')
'''),
6:('HRECT_L','Rounded wallet with a capsule clasp and an occluded right wall.','Lucide wallet: rounded body and continuous tab', '''
path('body',(40,19),[('L',(40,12)),('A',(36,8),4,4,False),('L',(8,8)),('A',(4,12),4,4,False),('L',(4,36)),('A',(8,40),4,4,False),('L',(36,40)),('A',(40,36),4,4,False),('L',(40,29))])
path('tab',(33,19),[('L',(41,19)),('A',(44,22),3,3,True),('L',(44,26)),('A',(41,29),3,3,True),('L',(33,29)),('A',(33,19),5,5,True)],True)
join('body','tab')
'''),
7:('SQUARE','Smooth crescent with an independent equal-arm cancel mark.','No useful exact match; circular arc construction', '''
path('crescent',(28,6),[('A',(6,24),22,18,False),('A',(28,42),22,18,False),('A',(18,24),22,22,True),('A',(28,6),22,22,True)],True)
poly('cross-a',(34,20),(38,24),(42,28));poly('cross-b',(34,28),(38,24),(42,20));join('cross-a','cross-b')
'''),
8:('HRECT_L','Two clean angular mountain peaks, one partial foreground ridge.','Lucide mountain: coherent angular contour', '''
poly('outline',(4,40),(16,20),(20,25),(30,8),(44,40),closed=True)
line('ridge',(20,25),(25,31));join('outline','ridge')
'''),
9:('VRECT_L','One rounded sheet with three equally spaced text rows.','Lucide bookmark: matched quarter-circle corners', '''
rounded('paper',8,4,40,44,4)
for i,x1 in enumerate([31,31,27]):line('text-'+str(i),(17,14+8*i),(x1,14+8*i))
'''),
10:('HRECT_L','Smooth dome and four visible sweeping tentacles, mirrored about x=24.','No useful exact Lucide match; shared smooth curve construction', '''
path('body',(4,30),[('C',(14,30),(4,36),(11,37)),('C',(12,20),(14,27),(12,25)),('A',(36,20),12,12,True),('C',(34,30),(36,25),(34,27)),('C',(44,30),(37,37),(44,36))])
path('left-arm',(20,32),[('C',(8,40),(18,38),(14,40))])
path('right-arm',(28,32),[('C',(40,40),(30,38),(34,40))])
'''),
11:('HRECT_L','An asymmetrical tapered chilli with a continuous curved stalk.','No useful exact match; natural asymmetric silhouette', '''
path('pepper',(4,27),[('C',(31,18),(15,32),(23,20)),('C',(39,22),(34,16),(39,18)),('C',(24,40),(43,32),(31,40)),('C',(4,27),(14,40),(7,35))],True)
path('stem',(37,18),[('C',(44,8),(43,18),(44,12))]);join('stem','pepper')
'''),
12:('SQUARE','Diagonal pen with parallel barrel edges, symmetric round cap and an open triangular nib.','Lucide bookmark: coherent round joins', '''
path('pen',(6,42),[('L',(11,27)),('L',(30,8)),('A',(40,18),7,7,True),('L',(21,37)),('L',(6,42))],True)
'''),
13:('SQUARE','A true circle behind an aligned square; the hidden quadrant is omitted.','Lucide circle: cardinal quarter arcs', '''
path('circle',(32,20),[('A',(19,7),13,13,False),('A',(6,20),13,13,False),('A',(19,33),13,13,False),('L',(20,33))])
poly('square',(20,33),(20,20),(32,20),(42,20),(42,42),(20,42),(20,33),closed=True);join('circle','square')
'''),
14:('CIRCLE','True circular pie outline with two radial cuts sharing the exact center.','Lucide circle: equal-radius circular arcs', '''
path('pie',(24,4),[('A',(44,24),20,20,True),('A',(36,40),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
poly('slice',(24,4),(24,24),(36,40));join('slice','pie')
'''),
15:('SQUARE','A three-tier swirl with shared horizontal seams and a single broad curled top.','No useful exact match; smooth capsule base and coherent swirl', '''
path('base',(13,28),[('L',(35,28)),('A',(35,42),7,7,True),('L',(13,42)),('A',(13,28),7,7,True)],True)
path('middle',(13,28),[('C',(17,18),(8,26),(10,18)),('L',(31,18)),('C',(35,28),(38,18),(40,26))]);join('middle','base')
path('top',(17,18),[('C',(23,6),(12,11),(28,13)),('C',(31,18),(34,8),(38,17))]);join('top','middle')
'''),
16:('HRECT_M','A centered play triangle beside a regular three-row playlist.','Lucide mountain: simple coherent triangular contour', '''
poly('play',(4,10),(20,24),(4,38),closed=True)
for i,x1 in enumerate([44,40,44]):line('row-'+str(i),(29,14+10*i),(x1,14+10*i))
'''),
17:('HRECT_L','Mirrored basket handles, a straight rim and evenly spaced interior slots.','Lucide wallet: coherent rounded enclosure', '''
path('basket',(4,21),[('L',(44,21)),('L',(38,37)),('C',(34,40),(37,40),(36,40)),('L',(14,40)),('C',(10,37),(12,40),(11,40)),('L',(4,21))],True)
line('left-handle',(10,21),(16,8));line('right-handle',(38,21),(32,8));join('basket','left-handle');join('basket','right-handle')
line('left-slot',(19,29),(19,32));line('right-slot',(29,29),(29,32))
'''),
18:('SQUARE','Symmetric circular cranium with smooth cheek transitions and mirrored slanted eyes.','Lucide skull: circular cranium and paired cheeks; human_ref/user.svg anatomy', '''
path('skull',(15,42),[('L',(15,38)),('C',(6,24),(15,32),(6,37)),('A',(42,24),18,18,True),('C',(33,38),(42,37),(33,32)),('L',(33,42))])
line('left-eye',(15,24),(19,26));line('right-eye',(33,24),(29,26));line('tooth',(24,40),(24,42))
'''),
19:('HRECT_L','Two triangular mountains with one clean shared baseline and one continuous foreground slope.','Lucide mountain: intentional angular peaks', '''
poly('outer',(4,40),(16,20),(20,26),(30,8),(44,40),(30,40),closed=True)
line('ridge',(20,26),(30,40));join('outer','ridge')
'''),
20:('SQUARE','Three rotating arrow strokes with coherent circular arcs and simple two-arm heads.','Lucide refresh-cw: smooth arcs with shared arrowhead nodes', '''
path('top-arc',(36,14),[('A',(14,12),16,16,False)])
poly('top-head',(17,6),(14,12),(21,14));join('top-arc','top-head')
path('left-arc',(8,19),[('A',(6,26),17,17,False),('A',(14,40),17,17,False)])
poly('left-head',(7,42),(14,40),(12,33));join('left-arc','left-head')
path('right-arc',(24,42),[('A',(40,23),19,19,False)])
poly('right-head',(34,28),(40,23),(42,30));join('right-arc','right-head')
'''),
}

def author(n,version=1):
 r=ITEMS[n-1];shape,plan,refs,body=DESIGNS[n]
 run=ROOT/'icon_set/work/primitive-make-ray'/r['uuid']/f'20260928T172849Z-fix-{n:02d}-r{version}'
 run.mkdir(parents=True,exist_ok=False)
 meta=dict(concept=r['concept'],source_uuid=r['uuid'],reference_path=r['ref'])
 (run/(r['key'].split('/')[1]+'.metadata.json')).write_text(json.dumps(meta,indent=2))
 code=f'''"""{plan}\nReference comparison: {r['comparison']}\nConstruction reference: {refs}.\nSOLO48 keyshape {shape}; uniform 4-unit strokes; explicit coherent symbol ownership.\n"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={r['uuid']!r}
SOURCE_PATH={r['ref']!r}
AUTHOR={AUTHOR!r}

class Drawing(Solo48):
    icon_id={r['key'].split('/')[1]!r}
    keyshape=Keyshape.{shape}
    semantic_role='MAIN'
    semantic_kind='noun'
    category={'avatars' if n==1 else 'objects'!r}
    aliases=()
    keywords={tuple(r['concept'].split())!r}

    def build(self):
'''+HELPERS+textwrap.indent(textwrap.dedent(body).strip()+'\n','        ')
 module=run/(r['key'].split('/')[1].replace('-','_')+'_'+r['uuid'].replace('-','_')+'.py')
 module.write_text(code)
 (run/'comparison-review.txt').write_text(r['comparison']+'\nFeedback: '+r['feedback']+'\nPlan: '+plan+'\n')
 import shutil
 shutil.copyfile(ROOT/r['ref'],run/'reference.svg')
 return run,module

def inspect(run,module):
 icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
 (run/(icon.icon_id+'.svg')).write_text(svg);(run/'validation.txt').write_text(report.describe())
 render_previews(svg,icon.icon_id,48,run)
 g=gate(module);(run/'gate.json').write_text(json.dumps(g,indent=2))
 print(run.name,icon.icon_id,report.status,g['status'],flush=True)
 for msg in list(report.errors)+list(report.warnings)+g['errors']+g['warnings']:print(' ',msg,flush=True)
 return g
if __name__=='__main__':
 for n in map(int,sys.argv[1:] or range(1,21)):
  run,module=author(n);inspect(run,module)
