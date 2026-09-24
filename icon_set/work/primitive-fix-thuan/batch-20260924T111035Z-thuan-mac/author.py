from pathlib import Path
import json,re,textwrap,sys,shutil
ROOT=Path.cwd();sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
AUTHOR='gpt-6'
SOURCE_ICON_ID=[re.search(r'[0-9a-f-]{36}$',next((Path(r)/'reference').glob('*.svg')).stem).group() for r in json.loads(Path(__file__).with_name('claims.json').read_text())]
SOURCE_PATH=[str(next((Path(r)/'reference').glob('*.svg'))) for r in json.loads(Path(__file__).with_name('claims.json').read_text())]
HELPERS='''
        def path(name,start,commands,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*pts,closed=False):self.add_polyline(name,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
'''
D={}
def design(i,key,notes,body,ref='No useful exact Lucide match; supplied reference controls the silhouette.',omissions='None'):
 D[i]=(key,notes,textwrap.dedent(body).strip(),ref,omissions)
design(0,'HRECT_M','Restore horizontal long shaft, broad curved point and bent tail. Point owns shared shaft attachment at (28,24).', '''
poly('shaft',(4,28),(4,24),(28,24))
path('point',(28,24),[('L',(28,10)),('C',(44,24),(34,10),(40,18)),('C',(28,38),(40,30),(34,38)),('L',(28,24))],True)
join('shaft','point')
''')
design(1,'SQUARE','Rotate the five-pointed star toward the diagonal shaft; a longer 45-degree wand ends at a star valley.', '''
poly('star',(25,6),(32,12),(41,8),(37,18),(42,26),(32,25),(28,34),(25,25),(16,23),(24,17),closed=True)
line('wand',(6,42),(25,25));join('wand','star')
''','Lucide wand: single diagonal shaft; source five-point star retained.')
design(2,'VRECT_L','Round skull, mask bottom and neck transitions; restore two sides of the mask strap as one loop.', '''
path('head',(20,44),[('C',(17,36),(20,40),(19,38)),('L',(10,32)),('L',(8,24)),('L',(13,18)),('C',(26,4),(13,10),(18,4)),('C',(40,18),(34,4),(40,10)),('C',(35,32),(40,24),(37,28)),('C',(34,44),(33,36),(33,39))])
path('mask',(8,24),[('L',(21,24)),('A',(25,28),4,4,True),('L',(25,32)),('A',(21,36),4,4,True),('L',(17,36))])
path('strap',(21,24),[('L',(30,19)),('C',(29,25),(31,18),(31,22)),('L',(25,32))])
join('head','mask');join('mask','strap')
''', 'Human reference user.svg: smooth head and shoulder vocabulary; continuous-neck profile from source.','Fine mask folds omitted.')
design(3,'HRECT_M','Level the hull and restore rising bow with smoothly rounded stern; cabin endpoints meet split gunwale.', '''
path('hull',(4,24),[('L',(16,24)),('L',(34,24)),('L',(44,24)),('C',(30,38),(40,32),(37,38)),('L',(12,38)),('A',(8,34),4,4,True),('L',(4,24))],True)
path('cabin',(16,24),[('L',(16,10)),('L',(26,10)),('A',(30,14),4,4,True),('L',(34,24))])
join('hull','cabin')
''')
design(4,'SQUARE','Round lower board corners and restore stripes to raised clap rail. Shared rail attachment points prevent overshooting ends.', '''
poly('raised',(6,16),(22,11),(36,6),(40,14),(26,19),(10,24),closed=True)
line('stripe-a',(22,11),(26,19));join('stripe-a','raised')
path('board',(10,24),[('L',(42,24)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,24)),('L',(10,24))],True)
join('raised','board')
''','Lucide clapperboard: curved board corners, striped tilted upper rail.','Lower duplicate striped band omitted to preserve board opening.')
design(5,'VRECT_M','Restore a tall treble clef with narrow upper loop, rounded lower spiral and smoothly hooked stem.', '''
path('clef',(18,38),[('C',(25,44),(18,42),(20,44)),('C',(30,38),(29,44),(31,42)),('L',(22,10)),('C',(27,4),(21,6),(23,4)),('C',(32,11),(31,4),(34,7)),('C',(20,23),(30,16),(24,20)),('C',(10,31),(14,26),(10,27)),('C',(23,36),(10,35),(17,36)),('C',(38,28),(33,36),(38,33)),('C',(27,22),(38,24),(33,22)),('C',(21,28),(22,22),(20,24))])
''',omissions='None; source upper loop, central curl and bottom hook retained.')
design(6,'SQUARE','Replace angular vane with a flowing curved feather; preserve a broad notch and diagonal quill.', '''
path('vane',(12,36),[('C',(28,10),(12,23),(19,15)),('C',(38,6),(32,8),(35,6)),('A',(42,10),4,4,True),('C',(38,22),(42,15),(40,20)),('L',(32,24)),('L',(37,28)),('C',(12,36),(27,34),(20,36))],True)
poly('shaft',(6,42),(12,36),(24,24));join('shaft','vane')
''','Lucide feather: diagonal shaft within coherent vane; source notch and organic silhouette retained.','Upper fine notch omitted to keep clear shaft spacing.')
design(7,'VRECT_L','Restore the source crescent with smooth outer arc and open concave bowl; keep asymmetric pointed ends.', '''
path('moon',(30,4),[('A',(8,24),22,20,False),('A',(28,44),20,20,False),('C',(40,36),(34,44),(39,40)),('C',(20,20),(27,38),(20,32)),('C',(30,4),(20,14),(24,8))],True)
''','Lucide moon: one convex-to-concave closed contour.')
design(8,'SQUARE','Restore upright hooked pruning blade and open counterblade with two separated rounded handles.', '''
path('blade',(22,26),[('C',(24,14),(17,21),(23,17)),('L',(30,6)),('C',(30,22),(33,13),(34,18)),('C',(22,26),(28,26),(24,27))],True)
path('counter',(30,22),[('L',(42,17)),('C',(27,32),(41,27),(36,31)),('L',(30,38)),('C',(24,42),(32,42),(26,42)),('L',(20,31)),('L',(22,26))])
path('handle',(22,26),[('L',(11,39)),('C',(6,34),(8,42),(6,38)),('L',(17,23)),('L',(22,26))],True)
join('blade','counter');join('blade','handle');join('counter','handle')
''','Lucide scissors: smooth handle turns and coherent blade/handle runs.','Tiny pivot hole omitted.')
for i in [9,10,11]:
 vertical=i!=9
 design(i,'SQUARE','Shorten oversized chevrons, restore distinct shafts and maintain balanced clearance around the divider.',f'''
def point(x,y):return (y,x) if {vertical!r} else (x,y)
line('divider',point(24,6),point(24,42))
for side in (-1,1):
    tip=24+side*18; shoulder=24+side*10; inner=24+side*8
    name='left' if side==-1 else 'right'
    poly(name+'-head',point(shoulder,16),point(tip,24),point(shoulder,32))
    line(name+'-shaft',point(tip,24),point(inner,24));join(name+'-head',name+'-shaft')
''','Lucide move-horizontal / move-vertical: 45-degree chevrons and separate straight shafts.')
design(12,'SQUARE','Rebuild two smooth diagonal oblong rings; shared crossing nodes make overlapping contours intentional.', '''
a=(17,17);b=(31,31)
path('lower',a,[('C',(27,21),(21,17),(24,18)),('C',b,(29,24),(31,27)),('L',(23,39)),('C',(16,42),(21,41),(19,42)),('C',(6,32),(10,42),(6,38)),('C',(9,25),(6,29),(7,27)),('L',a)],True)
path('upper',a,[('L',(25,9)),('C',(32,6),(27,7),(29,6)),('C',(42,16),(38,6),(42,10)),('C',(39,23),(42,19),(41,21)),('L',b),('C',(21,27),(27,31),(24,30)),('C',a,(19,24),(17,21))],True)
join('upper','lower')
''','Lucide link: rounded diagonal ring ends; closed overlap retained from source.')
for i in [13,14]:
 design(i,'SQUARE','Broaden the foreground shoulders and stagger rear body height to restore overlap and foreground hierarchy. Circular heads keep exact 4-unit detached gap.', '''
circle('front-head',14,12,6);circle('rear-head',34,13,5)
path('front-body',(6,42),[('L',(6,34)),('A',(14,26),8,8,True),('L',(18,26)),('A',(26,34),8,8,True),('L',(26,38)),('L',(26,42)),('L',(6,42))],True)
path('rear-body',(26,34),[('C',(34,26),(26,29),(29,26)),('A',(42,34),8,8,True),('L',(42,38)),('L',(26,38))])
join('front-body','rear-body')
''','human_ref/user.svg: circular heads, broad rounded shoulders; Lucide users: overlapping foreground hierarchy.','No defining features omitted.')
design(15,'SQUARE','Separate broad muzzle from tapered face at shared nodes and redraw symmetric horns with clean tips.', '''
path('face',(18,34),[('C',(16,25),(17,32),(16,29)),('L',(16,17)),('L',(32,17)),('L',(32,25)),('C',(30,34),(32,29),(31,32))])
path('muzzle',(18,34),[('L',(30,34)),('A',(30,42),4,4,True),('L',(18,42)),('A',(18,34),4,4,True)],True)
join('face','muzzle')
for s in (-1,1):
 def p(x,y):return (24+s*x,y)
 n='horn-left' if s==-1 else 'horn-right'
 path(n,p(8,17),[('C',p(18,6),p(15,17),p(18,13)),('C',p(8,25),p(18,22),p(15,25))])
 join(n,'face')
''',omissions='Small side ears omitted; raised horns and wide muzzle retained.')
design(16,'SQUARE','Restore a symmetric parabola with steeper sides and evenly angled axis arrow. Split true intersections.', '''
poly('vertical',(24,6),(24,24),(24,36),(24,42))
poly('horizontal',(6,36),(24,36),(42,36));join('vertical','horizontal')
path('curve',(6,8),[('C',(24,24),(12,20),(18,24)),('C',(42,8),(30,24),(36,20))])
join('curve','vertical')
poly('arrow',(36,30),(42,36),(36,42));join('arrow','horizontal')
''',omissions='None')
for i in [17,18,19]:
 design(i,'VRECT_L','Smooth circular cranium, rounded chin and continuous neck; retain source facing direction and open neck base.', f'''
def p(x,y):return (48-x,y) if {i==17!r} else (x,y)
path('profile',p(32,44),[('C',p(34,30),p(29,37),p(32,34)),('C',p(40,18),p(38,25),p(40,23)),('A',p(26,4),14,14,{i==17!r}),('A',p(12,18),14,14,{i==17!r}),('L',p(8,26)),('L',p(13,27)),('L',p(13,32)),('A',p(18,37),5,5,{i==17!r}),('L',p(23,37)),('L',p(23,44))])
''','Human reference user.svg: circular head vocabulary; continuous-neck source profile, no detached gap.','Fine lip serrations omitted to avoid crowded strokes.')

if __name__=='__main__':
 runs=json.loads(Path(__file__).with_name('claims.json').read_text()); manifest=[]
 for i,r in enumerate(runs):
  fix=Path(r);item=json.loads((fix/'claim.json').read_text())['item'];ref=Path(SOURCE_PATH[i]);uuid=SOURCE_ICON_ID[i];concept=ref.stem[:-37];key,notes,body,construction,omissions=D[i]
  out=Path('icon_set/work/primitive-make-ray')/uuid/f'20260924T111035Z-thuan-mac-fix-{i:02}'
  out.mkdir(parents=True,exist_ok=True)
  meta={'concept':concept,'source_uuid':uuid,'reference_path':str(ref),'icon_id':item['icon_id'],'author':AUTHOR,'feedback':item['feedback']}
  (out/(item['icon_id']+'.metadata.json')).write_text(json.dumps(meta,indent=2)+'\n')
  mod=out/(item['icon_id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py')
  code=f'''"""{notes}\nConstruction: {construction}\nOmissions: {omissions}\nKeyshape {key}: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uuid!r}
SOURCE_PATH = {str(ref)!r}
AUTHOR = {AUTHOR!r}
class Drawing(Solo48):
    icon_id = {item['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = {tuple(item['icon_id'].split('-'))!r}
    def build(self):
'''+HELPERS+'\n'+textwrap.indent(body,'        ')+'\n'
  mod.write_text(code)
  shutil.copyfile(ref,out/'reference.svg')
  import cairosvg
  cairosvg.svg2png(url=str(ref),write_to=str(out/'reference.png'),output_width=384,output_height=384,background_color='white')
  icon=load_icon(mod);report=icon.validate_icon();svg=icon.to_svg();(out/(item['icon_id']+'.svg')).write_text(svg)
  (out/'validation.txt').write_text(report.describe())
  render_previews(svg,item['icon_id'],48,out)
  print(i,item['icon_id'],report.describe(),flush=True)
  manifest.append({'i':i,'fix':str(fix),'out':str(out),'module':str(mod),'key':item['key'],'notes':notes,'construction':construction,'omissions':omissions})
 Path('icon_set/work/primitive-fix-thuan/batch-20260924T111035Z-thuan-mac/manifest.json').write_text(json.dumps(manifest,indent=2))
