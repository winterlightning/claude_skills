"""Author isolated SOLO48 revisions; retain all claimed source identities."""
import json,re,textwrap,sys
from pathlib import Path
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
import cairosvg
ROOT=Path('icon_set/work/primitive-make-ray/batch-20260924T115443-thuan-mac')
SOURCE_PATH=str(ROOT/'items.json')
items=json.loads(Path(SOURCE_PATH).read_text())
SOURCE_ICON_ID=[re.search(r'[0-9a-f-]{36}$',Path(i['ref']).stem)[0] for i in items]
AUTHOR='gpt-6'
HELPERS='''
        def path(name,start,steps,closed=False):
            here=start;members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
                else:self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m);here=end
            self.add_contour(name,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
'''
D={}
def design(i,key,plan,ref,omit,code):D[i]=(key,plan,ref,omit,textwrap.dedent(code))
design(0,'HRECT_L','A side-view electric streetcar with two window panes, equal wheels and a roof trolley pole. Extrema 4,8,44,40.','bus: equal wheels and divided glazing','Window frames integrated into the upper body band.', '''
path('body',(4,18),[('A',(8,14),4,4,True),('L',(24,14)),('L',(40,14)),('A',(44,18),4,4,True),('L',(44,24)),('L',(44,32)),('L',(34,32)),('L',(14,32)),('L',(4,32)),('L',(4,24)),('L',(4,18))],True)
for x in (14,34):circle('wheel-'+str(x),x,36,4);join('wheel-'+str(x),'body')
poly('window-sill',(4,24),(24,24),(44,24));line('window-divider',(24,14),(24,24));join('window-sill','body');join('window-divider','body');join('window-divider','window-sill')
line('trolley-pole',(24,14),(34,8));join('trolley-pole','body')
''')
design(1,'HRECT_L','A right-facing turkey has a scalloped fan, long neck, pointed beak and two legs. Extrema 4,8,44,40.','No exact Lucide turkey; circular scallops and continuous bird outline','Fine feather dividers and tiny eye omitted.', '''
path('body',(18,30),[('A',(24,20),6,10,True),('L',(30,20)),('L',(30,12)),('A',(38,12),4,4,True),('L',(44,16)),('L',(38,20)),('L',(38,28)),('A',(30,36),8,8,True),('L',(22,36)),('A',(18,30),4,6,True)],True)
path('fan',(18,30),[('L',(8,30)),('A',(4,26),4,4,True),('A',(8,22),4,4,True),('A',(4,18),4,4,True),('A',(8,14),4,4,True),('A',(14,8),6,6,True),('A',(20,14),6,6,True),('L',(24,20))]);join('fan','body')
for x in (22,30):line('leg-'+str(x),(x,36),(x,40));join('leg-'+str(x),'body')
''')
flower="""
path('bloom',(24,4),[('C',(30,12),(28,4),(30,8)),('C',(40,16),(36,9),(40,10)),('C',(34,24),(40,21),(38,24)),('C',(32,32),(38,28),(37,32)),('C',(24,28),(28,32),(26,30)),('C',(16,32),(22,30),(20,32)),('C',(14,24),(11,32),(10,28)),('C',(8,16),(10,24),(8,22)),('C',(18,12),(8,10),(12,9)),('C',(24,4),(18,8),(20,4))],True)
line('stem',(24,28),(24,44));join('stem','bloom')
self.add_dot('centre',(24,19))
"""
design(2,'VRECT_L','Five distinct curved petals sit on a central stem with mirrored leaf strokes. Extrema 8,4,40,44.','flower and flower-2: five coherent lobes and paired foliage','Seed ring reduced to a dot; secondary leaf edges omitted for spacing.',flower+"""
path('leaves',(8,39),[('C',(24,44),(14,39),(19,42)),('C',(40,39),(29,42),(34,39))]);join('stem','leaves')
""")
design(3,'VRECT_L','Five distinct rounded petals above a vertical stem and a left-facing leaf. Extrema 8,4,40,44.','flower-2: connected stem and a single leaf','Small flower centre omitted; all five petals retained.', """
path('bloom',(28,4),[('C',(34,11),(33,4),(34,7)),('C',(40,15),(38,9),(40,10)),('C',(35,21),(40,19),(38,21)),('C',(34,26),(39,24),(38,26)),('C',(28,22),(31,26),(30,25)),('C',(22,26),(26,25),(25,26)),('C',(21,21),(18,26),(17,24)),('C',(16,15),(18,21),(16,19)),('C',(22,11),(16,10),(18,9)),('C',(28,4),(22,7),(23,4))],True)
line('stem',(28,22),(28,44));join('stem','bloom')
path('leaf',(28,44),[('L',(18,44)),('A',(8,34),10,10,True),('L',(8,32)),('A',(28,44),20,12,True)],True);join('stem','leaf')
""")
design(4,'HRECT_L','Five equal-width panpipes descend in four-unit steps below a broad binding. Extrema 4,8,44,40.','No useful Lucide panpipe match; equal tube parameters and rounded ends','No tubes omitted.', '''
path('binding',(4,16),[('L',(4,11)),('A',(7,8),3,3,True),('L',(41,8)),('A',(44,11),3,3,True),('L',(44,16)),('L',(36,16)),('L',(28,16)),('L',(20,16)),('L',(12,16)),('L',(4,16))],True)
steps=[('L',(4,36))]
for i in range(5):
    x=4+i*8;y=36-i*4
    steps.append(('A',(x+8,y),4,4,False))
    steps.append(('L',(x+8,y-4 if i<4 else 16)))
path('pipes',(4,16),steps);join('pipes','binding')
for i in range(1,5):
    x=4+i*8;bottom=36-i*4
    line('wall-'+str(i),(x,16),(x,bottom));join('wall-'+str(i),'binding');join('wall-'+str(i),'pipes')
''')
design(5,'SQUARE','Bare foot and ankle profile has a broad instep, rounded toes, subtle sole arch and rounded heel. Extrema 6,6,42,42.','footprints: continuous anatomical outline; shared human reference reviewed, no detached head applies','Toe separations omitted for side profile.', '''
path('foot',(30,6),[('L',(30,16)),('C',(22,28),(30,22),(28,25)),('C',(10,33),(16,31),(14,33)),('A',(6,37),4,4,False),('A',(11,42),5,5,False),('C',(24,40),(16,42),(18,40)),('C',(34,42),(29,40),(30,42)),('A',(42,34),8,8,False),('C',(38,20),(42,29),(38,25)),('L',(38,6))])
''')
design(6,'VRECT_L','A sole-facing foot with rounded toe lobes receives three evenly spaced acupuncture needles with circular heads. Extrema 8,4,40,44.','footprints: rounded toe/heel contour; human reference reviewed, no head/body gap applies','Smallest toe divisions reduced to three clear lobes.', '''
path('foot',(24,40),[('A',(20,44),4,4,True),('L',(16,44)),('A',(8,36),8,8,True),('L',(8,9)),('A',(18,9),5,5,True),('A',(24,9),3,3,True),('A',(30,9),3,3,True)])
for i,(a,y) in enumerate([((20,20),16),((22,28),28),((24,40),40)]):
    line('needle-'+str(i),a,(36,y));circle('head-'+str(i),38,y,2);join('needle-'+str(i),'head-'+str(i))
join('needle-2','foot')
''')
design(7,'SQUARE','A diagonal football travels between upright goalposts above a central post; two trail marks show motion. Extrema 6,6,42,42.','No useful Lucide goal-post match; original arrangement retained','Ball laces omitted.', '''
line('left-upright',(6,6),(6,18))
poly('goal',(42,6),(42,28),(32,28),(22,28));line('post',(32,28),(32,42));poly('base',(22,42),(32,42),(42,42));join('post','goal');join('post','base')
path('ball',(22,18),[('A',(32,8),8,8,True),('A',(22,18),8,8,True)],True)
line('trail-low',(6,42),(8,37));line('trail-high',(11,29),(14,25))
''')
design(8,'SQUARE','Four card suits in a two-by-two grid: diamond, club, spade and heart. Extrema 6,6,42,42.','club, spade and heart: continuous outlines with explicit stems','Fine lobe curvature simplified to circular/elliptical arcs.', '''
poly('diamond',(13,6),(20,13),(13,20),(6,13),closed=True)
path('club',(32,10),[('A',(38,10),3,4,True),('A',(42,15),4,5,True),('A',(35,17),4,4,True),('A',(28,15),4,4,True),('A',(32,10),4,5,True)],True)
line('club-stem',(35,17),(35,21));join('club-stem','club')
path('spade',(13,29),[('L',(7,35)),('A',(13,38),4,4,False),('A',(19,35),4,4,False),('L',(13,29))],True)
line('spade-stem',(13,38),(13,42));join('spade-stem','spade')
path('heart',(35,32),[('A',(28,33),4,4,False),('L',(35,42)),('L',(42,33)),('A',(35,32),4,4,False)],True)
''')
design(9,'SQUARE','Front-facing car beneath three spray streams has a broad windshield and paired tires. Extrema 6,6,42,42.','car-front: symmetric windshield and rounded body corners','Headlamps omitted to retain clear cabin/body bands; spray reduced to three long strokes.', '''
path('body',(6,30),[('L',(12,22)),('L',(36,22)),('L',(42,30)),('L',(42,35)),('A',(39,38),3,3,True),('L',(36,38)),('L',(12,38)),('L',(9,38)),('A',(6,35),3,3,True),('L',(6,30))],True)
line('windshield',(6,30),(42,30));join('windshield','body')
for x in (12,36):line('tire-'+str(x),(x,38),(x,42));join('tire-'+str(x),'body')
for x in (12,24,36):line('spray-'+str(x),(x,6),(x-1,13))
''')
design(10,'HRECT_L','Rounded six-tooth gear connects to a three-way branching line. Extrema 4,8,44,40.','settings: rounded teeth instead of angular mitres','Tiny central dot omitted.', '''
path('gear',(12,17),[('A',(16,10),4,7,True),('A',(20,17),4,7,True),('C',(28,17),(24,15),(28,12)),('C',(23,24),(28,21),(24,22)),('C',(28,31),(24,26),(28,27)),('C',(20,31),(28,36),(24,33)),('C',(16,38),(20,36),(19,38)),('C',(12,31),(13,38),(12,36)),('C',(4,31),(8,33),(4,36)),('C',(9,24),(4,27),(8,26)),('C',(4,17),(8,22),(4,21)),('C',(12,17),(4,12),(8,15))],True)
poly('spine',(44,8),(38,8),(38,24),(38,40),(44,40));poly('arm',(23,24),(38,24),(44,24));join('arm','gear');join('arm','spine')
''')
design(11,'HRECT_L','Flared megaphone with a rounded rear chamber, broad mouth rim and angled handgrip. Extrema 4,8,44,40.','megaphone: continuous horn and attached grip','Small driver cap behind the mouth omitted.', '''
path('rear',(8,16),[('L',(16,16)),('L',(16,28)),('L',(8,28)),('A',(4,24),4,4,True),('L',(4,20)),('A',(8,16),4,4,True)],True)
poly('horn',(16,16),(36,8),(36,32),(16,28));join('horn','rear')
poly('rim',(36,8),(44,8),(44,32),(36,32));join('rim','horn')
poly('grip',(8,28),(11,40),(21,40),(16,28));join('grip','rear');join('grip','horn')
''')
design(12,'HRECT_L','Kettledrum with an elliptical bowl, three splayed supports and two sloping mallets. Extrema 4,8,44,40.','drum: smooth elliptical body and diagonal mallets','Drumhead rear ellipse omitted for spacing.', '''
path('bowl',(4,23),[('L',(44,23)),('A',(36,31),20,10,True),('A',(24,33),20,10,True),('A',(12,31),20,10,True),('A',(4,23),20,10,True)],True)
for n,a,b in [('left',(12,31),(9,40)),('centre',(24,33),(24,40)),('right',(36,31),(39,40))]:line('leg-'+n,a,b);join('leg-'+n,'bowl')
circle('mallet-left',14,11,3);circle('mallet-right',34,11,3)
line('handle-left',(4,8),(11,11));line('handle-right',(44,8),(37,11));join('handle-left','mallet-left');join('handle-right','mallet-right')
''')
design(13,'SQUARE','Chef knife with a broad curved blade and a rounded diagonal grip at the heel. Extrema 6,6,42,42.','pocket-knife: rounded grip construction; supplied chef blade controls silhouette','Rivet dots omitted.', '''
path('blade',(6,6),[('L',(30,24)),('L',(22,32)),('C',(6,6),(12,24),(6,16))],True)
path('handle',(30,24),[('L',(40,34)),('C',(42,38),(42,35),(42,36)),('A',(38,42),4,4,True),('L',(32,42)),('L',(22,32))]);join('handle','blade')
''')
design(14,'SQUARE','Diagonal kitchen masher has a rounded head with an oval face division and a broad handle. Extrema 6,6,42,42.','No direct Lucide masher match; quarter-circle head and equal-width handle','Tiny surface texture omitted.', '''
path('tool',(6,30),[('A',(18,18),12,12,True),('L',(26,18)),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,14)),('L',(30,26)),('L',(30,30)),('A',(18,42),12,12,True),('A',(6,30),12,12,True)],True)
path('face',(6,30),[('A',(18,42),12,12,True)]);join('face','tool')
''')
for i in (15,16):
 crown_y=20 if i==15 else 18;ry=crown_y-8
 design(i,'HRECT_L','Symmetric kraken silhouette with a rounded crown and two smoothly curled tentacle tips. Extrema 4,8,44,40.','No useful Lucide kraken match; mirrored arcs and shared radii','No source features omitted; open bottom retained.',f'''
path('kraken',(4,28),[('A',(6,30),2,2,True),('L',(6,36)),('A',(14,36),4,4,False),('L',(14,{crown_y})),('A',(24,8),10,{ry},True),('A',(34,{crown_y}),10,{ry},True),('L',(34,36)),('A',(42,36),4,4,False),('L',(42,30)),('A',(44,28),2,2,True)])
''')
design(17,'VRECT_L','A broad dairy can has a rounded lid, straight neck, sloping shoulders and rounded lower corners. Extrema 8,4,40,44.','milk: continuous neck-to-shoulder outline and rounded body','Fine wire side handles omitted.', '''
path('lid',(12,12),[('L',(12,8)),('A',(16,4),4,4,True),('L',(32,4)),('A',(36,8),4,4,True),('L',(36,12)),('L',(32,12)),('L',(16,12)),('L',(12,12))],True)
path('can',(16,12),[('L',(16,20)),('L',(8,28)),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,28)),('L',(32,20)),('L',(32,12))]);join('can','lid')
line('shoulder-rule',(16,20),(32,20));join('shoulder-rule','can')
''')
design(18,'HRECT_L','A seated right-facing lizard has a smoothly swept back, broad head, bent foreleg and curled tail. Extrema 4,8,44,40.','No useful direct Lucide match; original reptile silhouette and coherent supported cubic contours','Tiny toe marks omitted.', '''
path('outline',(22,40),[('C',(4,30),(10,40),(4,38)),('C',(24,15),(4,23),(15,16)),('C',(34,8),(29,14),(27,8)),('C',(44,14),(40,8),(44,10)),('C',(35,20),(44,18),(39,20)),('L',(30,30)),('L',(36,30))])
path('tail',(22,40),[('C',(13,34),(17,39),(13,38)),('C',(22,28),(13,30),(18,28)),('L',(24,28)),('L',(24,34)),('L',(29,34))]);join('tail','outline')
''')
design(19,'SQUARE','Long diagonal kitchen knife has a broad rounded cutting tip and an aligned rounded handle. Extrema 6,6,42,42.','pocket-knife: rounded grip; supplied blade controls long curved tip','No essential features omitted.', '''
path('blade',(20,26),[('L',(42,6)),('L',(42,10)),('A',(30,34),12,24,True),('L',(26,36)),('L',(20,26))],True)
path('handle',(20,26),[('L',(10,34)),('A',(6,38),4,4,False),('A',(10,42),4,4,False),('L',(26,36))]);join('handle','blade')
''')

def author(i):
 it=items[i];key,plan,ref,omit,code=D[i];uuid=SOURCE_ICON_ID[i];concept=Path(it['ref']).stem[:-37]
 run=Path('icon_set/work/primitive-make-ray')/uuid/'20260924T120000Z-thuan-mac-revision'
 run.mkdir(parents=True,exist_ok=True)
 if (run/'result.json').exists():raise RuntimeError('Completed run: use a fresh run ID')
 it.update(run=str(run),uuid=uuid,concept=concept,plan=plan,lucide=ref,omissions=omit)
 (run/(it['id']+'.metadata.json')).write_text(json.dumps({'concept':concept,'source_uuid':uuid,'reference_path':it['ref']},indent=2))
 module=run/(it['id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py');it['module']=str(module)
 module.write_text(f'"""{plan}\nConstruction: {ref}\nReduction: {omit}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={uuid!r}\nSOURCE_PATH={it["ref"]!r}\nAUTHOR={AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id={it["id"]!r}\n    keyshape=Keyshape.{key}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="objects"\n    aliases=()\n    keywords={tuple(it["id"].split("-"))!r}\n    def build(self):\n'+HELPERS+textwrap.indent(code,'        '))
 icon=load_icon(module);report=icon.validate_icon();(run/'validation.txt').write_text(report.describe());(run/(it['id']+'.svg')).write_text(icon.to_svg());render_previews(icon.to_svg(),it['id'],48,run)
 cairosvg.svg2png(url=it['ref'],write_to=str(run/'reference.png'),output_width=240,output_height=240)
 print(i,it['id'],report.describe())
if __name__=='__main__':
 for i in list(map(int,sys.argv[1:])) or range(20):author(i)
 (ROOT/'items.json').write_text(json.dumps(items,indent=2))
