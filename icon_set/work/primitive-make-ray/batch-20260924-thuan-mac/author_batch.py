"""Standalone revision authoring; exact source identity is recorded per module."""
import json, re, textwrap, sys, io
from pathlib import Path
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
import cairosvg
SOURCE_ICON_ID = ['d887ebc5-e028-4b29-95eb-d108a07e35c2', '8ee71767-8c7b-4b67-8c9c-982b7a27e635', '95f36efc-1966-49b5-978a-2938622f39c8', '59bf9944-e39e-44d7-a13e-05c98d58e886', 'a4dc687d-cffd-4881-a57d-b884d2cbce23', '9cc63cfd-be10-4af6-b277-92e252919cc7', '3b617167-6bc8-47b6-8ca4-ece9d9067e8d', '4ed91796-017e-538d-8c4d-6f874608ce4f', 'f8b6ea0a-273a-4932-a93b-52454f7fd328', '6b3e7a5a-f418-4efc-be04-216b265ddec8', '439fdf79-7201-4e1e-b530-c3c1c7020eae', 'd9a66ec5-6720-4213-9bfe-b9572cfa84f8', '75f115c6-e249-48a1-aac9-f840b6e89c3e', 'e3f7ad31-1cbe-40ca-b4de-da206b319982', '4ae0f802-0947-49ab-948b-a13314a05022', '7420a5ad-20b8-4125-a020-7f6c31b74aac', '1562f98c-4790-44ea-971c-d68ba4454109', 'afb69f40-6aff-40c4-aa6f-3646708bd0d2', 'd077ca8e-11b1-40d1-a612-b89115575b84', 'e0e5259b-1f4e-49b1-b4fe-796abc5994f0']
SOURCE_PATH = 'icon_set/work/primitive-make-ray/batch-20260924-thuan-mac/claimed-inputs.json'
AUTHOR = 'gpt-6'
ROOT=Path('icon_set/work/primitive-make-ray/batch-20260924-thuan-mac')
items=json.load(open(SOURCE_PATH))
HELPERS='''
        def path(name, start, steps, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                else: self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m); here=end
            self.add_contour(name,*members,closed=closed)
        def poly(name,*pts,closed=False): self.add_polyline(name,*pts,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
'''
D={}
def design(i,key,plan,ref,omit,code):D[i]=(key,plan,ref,omit,textwrap.dedent(code))
design(0,'SQUARE','Mirrored wings and antennae share an elongated striped body; extremes 6,6,42,42.','bug: paired appendages and coherent body outline','Tiny legs omitted to retain open wing/body spacing.', '''
path('body',(18,14),[('A',(30,14),6,6,True),('L',(30,18)),('L',(30,26)),('L',(30,30)),('L',(30,34)),('A',(24,42),6,8,True),('A',(18,34),6,8,True),('L',(18,30)),('L',(18,26)),('L',(18,18)),('L',(18,14))],True)
for side,x in [('left',18),('right',30)]:
    path('wing-'+side,(x,18),[('A',(x,30),12,6,side=='right')]);join('wing-'+side,'body')
    line('antenna-'+side,(x,14),(14 if side=='left' else 34,6));join('antenna-'+side,'body')
for y in (26,34):
    line('band-'+str(y),(18,y),(30,y));join('band-'+str(y),'body')
''')
design(1,'SQUARE','Left-facing bird on a broad semicircular nest, smoothly rounded crown; extremes 6,6,42,42.','bird: continuous crown and belly','Fine nest hatching and tiny eye omitted.', '''
path('bird',(14,26),[('L',(14,20)),('L',(6,14)),('L',(14,14)),('A',(30,14),8,8,True),('A',(34,22),4,8,False),('L',(42,14)),('L',(38,26))])
path('nest',(6,26),[('L',(14,26)),('L',(38,26)),('L',(42,26)),('A',(6,26),18,16,True)],True)
join('bird','nest')
''')
design(2,'VRECT_L','Perched bird has round head, swept breast and long tail; extremes 8,4,40,44.','bird: circular head flowing into breast','Tiny eye and inner wing omitted.', '''
path('bird',(8,36),[('L',(20,16)),('L',(20,12)),('A',(36,12),8,8,True),('L',(40,14)),('L',(36,18)),('A',(22,32),14,14,True),('L',(16,32)),('L',(8,36))],True)
poly('leg',(22,32),(27,44),(40,44));line('perch',(14,44),(27,44));join('leg','bird');join('leg','perch')
''')
design(3,'HRECT_L','Horizontal elliptical airship hull, separate upper/lower tail fins and hanging cabin; extremes 4,8,44,40.','No useful direct Lucide match','No omissions; cabin and two fins retained.', '''
path('hull',(4,22),[('A',(20,12),16,10,True),('A',(36,16),20,10,True),('L',(40,8)),('L',(44,8)),('L',(44,36)),('L',(40,36)),('L',(36,28)),('A',(28,32),12,8,True),('L',(16,32)),('A',(4,22),12,10,True)],True)
poly('cabin',(16,32),(16,40),(28,40),(28,32));join('cabin','hull')
''')
design(4,'HRECT_L','Right-facing boar with curved skull, upright ear, projecting snout and upward tusk; extremes 4,8,44,40.','No useful direct Lucide match','Tiny nostril and eye omitted.', '''
path('head',(10,40),[('A',(4,34),6,6,True),('L',(4,24)),('A',(14,14),10,10,True),('L',(14,8)),('A',(26,16),14,14,True),('A',(36,20),14,14,False),('L',(40,20)),('A',(44,24),4,4,True),('L',(44,28)),('A',(40,32),4,4,True),('L',(34,32)),('L',(28,26)),('L',(24,36)),('L',(32,36)),('L',(24,40)),('L',(10,40))],True)
''')
design(5,'SQUARE','Diagonal axe with a broad crescent blade and shared mounting nodes; extremes 6,6,42,42.','axe: convex blade and distinct handle attachment','Handle reduced to one stroke.', '''
poly('handle',(6,42),(24,24),(32,16))
path('blade',(24,24),[('L',(18,18)),('L',(30,6)),('A',(42,18),12,12,False),('A',(26,38),16,20,True),('A',(24,24),12,16,False)])
join('blade','handle')
''')
design(6,'SQUARE','Three clockwise arrows retain triangular loop with equal stroke width and clear open arrowheads; extremes 6,6,42,42.','recycle: three separated bent arrows','Outlined broad shafts simplified to centerline arrows for clearance.', '''
path('top',(15,14),[('L',(19,8)),('A',(25,8),3,2,True),('L',(32,19))]);poly('top-tip',(23,17),(32,19),(35,10));join('top','top-tip')
path('right',(39,28),[('L',(42,34)),('A',(38,38),4,4,True),('L',(25,38))]);poly('right-tip',(30,32),(25,38),(30,42));join('right','right-tip')
path('left',(16,38),[('L',(10,38)),('A',(6,34),4,4,True),('L',(12,23))]);poly('left-tip',(6,25),(12,23),(15,30));join('left','left-tip')
''')
design(7,'SQUARE','Certificate with lower-right round seal and single notched ribbon; extremes 6,6,42,42.','award: round seal with hanging notched ribbon','One of two text rules omitted.', '''
poly('paper',(26,32),(6,32),(6,6),(42,6),(42,24))
circle('seal',34,24,8);join('paper','seal')
poly('ribbon',(26,24),(26,42),(34,38),(42,42),(42,24));join('ribbon','seal')
line('text',(15,15),(19,15))
''')
design(8,'HRECT_L','Closed horizontal battery and centered lightning stroke with external terminal; extremes 4,8,44,40.','battery-charging: angular bolt and rounded corners','Terminal is a single short stroke.', '''
path('case',(8,8),[('L',(32,8)),('A',(36,12),4,4,True),('L',(36,36)),('A',(32,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
poly('bolt',(24,17),(16,25),(25,25),(18,31));line('terminal',(44,20),(44,28))
''')
for i in (9,10):
 design(i,'SQUARE','Cherry-topped triangular cake slice with a broad layer and rounded lower corners; extremes 6,6,42,42.','cake-slice: continuous wedge silhouette and layer rule','Cherry stem omitted; one layer retained.', '''
path('cake',(6,24),[('L',(20,14)),('L',(28,14)),('L',(42,22)),('L',(42,32)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,32)),('L',(6,24))],True)
circle('cherry',24,10,4);join('cherry','cake')
line('top',(6,24),(42,22));join('top','cake')
line('layer',(6,32),(42,32));join('layer','cake')
''')
design(10,'SQUARE','Cherry-topped layer cake has a curved rear edge and a cherry stem; extremes 6,6,42,42.','cake-slice: curved back and spaced layer','One horizontal layer retained.', """
path('cake',(26,12),[('A',(42,24),16,12,True),('L',(42,33)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,33)),('L',(6,24)),('L',(18,12))])
circle('cherry',22,12,4);join('cherry','cake')
line('stem',(22,8),(26,6));join('stem','cherry')
line('top',(6,24),(42,24));join('top','cake')
line('layer',(6,33),(42,33));join('layer','cake')
""")
design(11,'SQUARE','Chick rises from jagged eggshell; rounded crown and deep bowl share contact nodes; extremes 6,6,42,42.','bird: rounded crown and projecting beak','Tiny eye omitted.', '''
path('chick',(14,30),[('L',(14,18)),('L',(14,16)),('A',(34,16),10,10,True),('L',(42,18)),('L',(34,22)),('L',(34,30))])
path('shell',(6,22),[('L',(14,30)),('L',(24,23)),('L',(34,30)),('L',(42,22)),('A',(6,22),18,20,True)],True)
join('chick','shell')
''')
design(12,'CIRCLE','Two opposing circular sync arrows share radius 20 and diagonal arrowheads.','refresh-cw: two coherent arcs with attached heads','No omissions.', '''
path('upper',(4,24),[('A',(24,4),20,20,True),('A',(40,12),20,20,True)])
poly('upper-tip',(31,12),(40,12),(40,16));join('upper','upper-tip')
path('lower',(44,24),[('A',(24,44),20,20,True),('A',(8,36),20,20,True)])
poly('lower-tip',(17,36),(8,36),(8,32));join('lower','lower-tip')
''')
design(13,'SQUARE','Open circular transform disc with radial sector, handle dot and two directional corner arrows; extremes 6,6,42,42.','refresh-cw: detached directional arrow strokes','No defining element omitted.', '''
path('disc',(32,24),[('A',(16,24),8,8,False),('A',(24,32),8,8,False)])
poly('radial',(42,24),(32,24),(24,24),(34,34));join('radial','disc')
poly('radial-tip',(26,34),(34,34),(34,26));join('radial','radial-tip')
self.add_dot('handle',(42,24));join('handle','radial')
poly('top-arrow',(42,14),(34,6),(34,11));line('top-wing',(34,6),(42,6));join('top-arrow','top-wing')
poly('bottom-arrow',(6,34),(14,42),(14,37));line('bottom-wing',(14,42),(6,42));join('bottom-arrow','bottom-wing')
''')
design(14,'CIRCLE','Clockwise return clock with full circular curvature, open lower gap and diagonal arrowhead.','refresh-cw: circular arrow construction','No omissions.', '''
path('rim',(24,44),[('A',(4,24),20,20,True),('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(36,40),20,20,True)])
poly('tip',(36,32),(36,40),(27,40));join('rim','tip')
poly('hands',(24,13),(24,24),(32,24))
''')
design(15,'SQUARE','Counterclockwise arrival clock uses centered circular rim and inward opening at upper left.','refresh-cw: continuous circular rim and attached head','No omissions.', '''
path('rim',(24,6),[('A',(42,24),18,18,True),('A',(24,42),18,18,True),('A',(6,24),18,18,True)])
poly('tip',(6,34),(6,24),(16,24));join('rim','tip')
poly('hands',(24,15),(24,26),(33,26))
''')
design(16,'HRECT_L','Envelope with symmetric flap, rounded rectangle and a true shared diagonal seam junction; extremes 4,8,44,40.','mail: rounded enclosure with shallow symmetric flap','No omissions; single lower-right back seam retained.', '''
path('outline',(8,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
poly('flap',(4,12),(24,28),(34,20),(44,12));join('flap','outline')
line('seam',(34,20),(44,36));join('seam','flap');join('seam','outline')
''')
design(17,'HRECT_M','Closed eyelid is a circular arc with two radial lashes attached at exact arc points; extremes 4,10,44,38.','eye-closed: continuous lid and radial lashes','Two left-hand lashes retained as in source; deliberate asymmetry.', '''
path('lid',(4,10),[('A',(12,22),20,15,False),('A',(24,25),20,15,False),('A',(44,10),20,15,False)])
line('outer-lash',(12,22),(6,30));line('inner-lash',(24,25),(24,38));join('lid','outer-lash');join('lid','inner-lash')
''')
design(18,'HRECT_M','Mirrored lips use smooth rounded upper lobes and a broad lower arc around one seam; extremes 4,10,44,38.','No useful direct Lucide match','Central seam simplified to a shallow straight stroke.', '''
path('outline',(4,24),[('A',(16,10),12,14,True),('A',(24,13),8,3,True),('A',(32,10),8,3,True),('A',(44,24),12,14,True),('A',(24,38),20,14,True),('A',(4,24),20,14,True)],True)
line('seam',(4,24),(44,24));join('seam','outline')
''')
design(19,'SQUARE','French horn has a circular coil and flared upper-right bell with a single inner tube end; extremes 6,6,42,42.','No useful direct Lucide match','Fine valves and pedestal omitted.', '''
path('tube',(18,29),[('L',(27,29)),('A',(19,42),13,13,True),('A',(6,29),13,13,True),('A',(19,16),13,13,True),('L',(24,16)),('A',(42,6),22,22,False),('L',(42,26)),('A',(24,16),22,22,False)])
''')

def write(i):
 it=items[i];key,plan,ref,omit,code=D[i];uuid=re.search(r'[0-9a-f-]{36}$',Path(it['ref']).stem)[0];concept=Path(it['ref']).stem[:-37]
 run=Path('icon_set/work/primitive-make-ray')/uuid/'20260924T112000Z-thuan-mac-revision';run.mkdir(parents=True,exist_ok=True)
 if (run/'result.json').exists(): raise RuntimeError('Completed run is immutable; select a fresh run ID')
 it.update(run=str(run),uuid=uuid,concept=concept,plan=plan,lucide=ref,omissions=omit)
 (run/(it['id']+'.metadata.json')).write_text(json.dumps({'concept':concept,'source_uuid':uuid,'reference_path':it['ref']},indent=2))
 module=run/(it['id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py')
 module.write_text(f'"""{plan}\nConstruction: {ref}\nReduction: {omit}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {uuid!r}\nSOURCE_PATH = {it["ref"]!r}\nAUTHOR = {AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id = {it["id"]!r}\n    keyshape = Keyshape.{key}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(it["id"].split("-"))!r}\n    def build(self):\n'+HELPERS+textwrap.indent(code,'        '))
 it['module']=str(module)
 return it
if __name__=='__main__':
 selected=list(map(int,sys.argv[1:])) or list(range(20))
 if (ROOT/'items.json').exists():items=json.loads((ROOT/'items.json').read_text())
 for i in selected:
  it=write(i);icon=load_icon(it['module']);report=icon.validate_icon();run=Path(it['run']);(run/'validation.txt').write_text(report.describe());(run/(it['id']+'.svg')).write_text(icon.to_svg());render_previews(icon.to_svg(),it['id'],48,run)
  cairosvg.svg2png(url=it['ref'],write_to=str(run/'reference.png'),output_width=240,output_height=240)
  print(i,it['id'],report.describe())
 (ROOT/'items.json').write_text(json.dumps(items,indent=2))
