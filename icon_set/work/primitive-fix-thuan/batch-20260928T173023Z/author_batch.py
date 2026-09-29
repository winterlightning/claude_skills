"""Fresh primitive-make-ray bad-stroke revisions, with exact input provenance."""
from pathlib import Path
import sys,json,re,textwrap,importlib.util,shutil
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from PIL import Image,ImageDraw
BATCH=Path(__file__).parent
claims=json.loads((BATCH/'claims.json').read_text())
SOURCE_ICON_ID={r['index']:re.search(r'([a-f0-9-]{36})\.svg$',r['reference']).group(1) for r in claims}
SOURCE_PATH={r['index']:r['reference'] for r in claims}
AUTHOR='gpt-6'
old=BATCH.parent/'batch-20260928T171810Z/author_batch.py'
spec=importlib.util.spec_from_file_location('prior_geometry_helpers',old);prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
HELPERS=prior.HELPERS+'''
    def bubble(self):
        self.path('bubble',(22,38),[('L',(22,44)),('C',(40,22),(33,39),(40,31)),('C',(24,4),(40,12),(33,4)),('C',(8,21),(15,4),(8,11)),('C',(22,38),(8,31),(14,37))],True)
    def file(self):
        self.path('page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.path('fold',(28,4),[('L',(28,12)),('A',(32,16),4,4,False),('L',(40,16))]);self.relate('connect','page','fold')
'''
BODIES={
0:'''# Equal tall cups and a tangent elliptical headband.
self.path('band',(8,28),[('L',(8,24)),('A',(40,24),16,20,True),('L',(40,28))])
for side,left in [('left',8),('right',30)]:
    self.path(side+'-cup',(left,28),[('A',(left+10,28),5,5,True),('L',(left+10,39)),('A',(left,39),5,5,True),('L',(left,28))],True)
    self.relate('connect','band',side+'-cup')
''',
1:'''# A slashed C currency sign, not punctuation; smooth circular C with an exact slash attachment.
self.circle('ring',24,24,20)
self.path('c',(31,16),[('A',(25,14),10,10,False),('A',(15,24),10,10,False),('A',(19,32),10,10,False),('A',(25,34),10,10,False),('A',(31,32),10,10,False)])
self.add_polyline('slash',(16,36),(19,32),(31,16));self.relate('connect','c','slash')
''',
2:'''# Circular clockwise return stroke; hands share the true center (24,24).
self.path('return',(24,44),[('A',(4,24),20,20,True),('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(36,40),20,20,True)])
self.add_polyline('arrow',(36,32),(36,40),(44,40));self.relate('connect','return','arrow')
self.add_polyline('hands',(24,13),(24,24),(33,24))
''',
3:'''# Rotated bell: two smooth mirrored curve halves meet tangentially at the blade root.
self.path('guard',(8,24),[('C',(24,24),(12,20),(20,20)),('C',(24,40),(28,28),(28,36)),('L',(16,32)),('L',(8,24))],True)
self.add_line('blade',(24,24),(44,4));self.relate('connect','guard','blade')
self.add_line('grip',(16,32),(4,44));self.relate('connect','guard','grip')
''',
4:'''# Closed nib with distinct cap, diagonal slit and one coherent flourish.
self.path('nib',(16,28),[('L',(21,14)),('C',(31,11),(23,10),(27,10)),('L',(38,4)),('L',(44,10)),('L',(37,17)),('C',(30,25),(38,22),(35,24)),('L',(16,28))],True)
self.add_line('cap-seam',(31,11),(37,17));self.relate('connect','nib','cap-seam')
self.add_line('slit',(16,28),(26,18));self.relate('connect','nib','slit')
self.path('flourish',(16,28),[('L',(8,28)),('A',(4,32),4,4,False),('A',(8,36),4,4,False),('L',(29,36)),('A',(29,44),4,4,True),('L',(4,44))]);self.relate('connect','nib','flourish')
''',
5:'''# Four distinct suits. Heart lobes are broad and mirrored around x35.
self.add_polyline('diamond',(12,4),(20,13),(12,22),(4,13),closed=True)
self.path('club',(31,12),[('C',(35,4),(29,7),(31,4)),('C',(39,12),(39,4),(41,7)),('C',(43,18),(43,10),(45,14)),('C',(35,18),(41,22),(37,21)),('C',(27,18),(33,21),(29,22)),('C',(31,12),(25,14),(27,10))],True)
self.add_line('club-stem',(35,18),(35,22));self.relate('connect','club','club-stem')
self.path('spade',(12,28),[('C',(4,37),(8,32),(4,34)),('C',(12,40),(4,42),(9,43)),('C',(20,37),(15,43),(20,42)),('C',(12,28),(20,34),(16,32))],True)
self.add_line('spade-stem',(12,40),(12,44));self.relate('connect','spade','spade-stem')
self.path('heart',(35,31),[('C',(27,32),(33,25),(27,27)),('C',(35,44),(27,36),(32,41)),('C',(43,32),(38,41),(43,36)),('C',(35,31),(43,27),(37,25))],True)
''',
6:'''# Four quadrant layout: apple, two curved arrows and gabled carton.
self.path('apple',(13,10),[('C',(5,13),(9,7),(5,9)),('C',(13,24),(4,22),(10,25)),('C',(21,13),(16,25),(22,22)),('C',(13,10),(21,9),(17,7))],True)
self.add_polyline('stem',(13,10),(13,7),(13,4));self.relate('connect','apple','stem')
self.path('leaf',(13,7),[('C',(19,5),(15,5),(17,5))]);self.relate('connect','stem','leaf')
self.path('upper-arrow',(42,19),[('C',(27,8),(40,12),(34,8))])
self.add_polyline('upper-head',(32,4),(27,8),(32,12));self.relate('connect','upper-arrow','upper-head')
self.path('lower-arrow',(4,28),[('C',(18,40),(4,35),(10,40))])
self.add_polyline('lower-head',(14,36),(18,40),(14,44));self.relate('connect','lower-arrow','lower-head')
self.add_polyline('carton',(28,44),(28,32),(32,26),(40,26),(44,32),(44,44),(36,44),closed=True)
self.add_polyline('carton-fold',(32,26),(36,32),(36,44));self.relate('connect','carton','carton-fold')
''',
7:'''self.bubble()
# The complete @ curl retains the lower terminal omitted in the rejected version.
self.circle('at-counter',23,20,4)
self.path('at-curl',(26,31),[('C',(14,21),(17,34),(14,28)),('C',(24,11),(14,14),(17,11)),('C',(34,21),(31,11),(34,14)),('C',(27,22),(34,27),(27,27)),('L',(27,20)),('L',(27,17))])
self.relate('connect','at-counter','at-curl')
''',
8:'''self.bubble()
self.box('camera',14,14,27,28,3,{2:[(27,18),(27,24)]})
self.add_polyline('lens',(27,18),(34,14),(34,28),(27,24));self.relate('connect','camera','lens')
''',
9:'''# Round bulb dome, smoothly narrowing shoulders and a rounded attached socket.
self.path('bulb',(10,18),[('A',(24,4),14,14,True),('A',(38,18),14,14,True),('C',(31,33),(38,26),(31,27)),('L',(31,35)),('L',(29,35)),('L',(19,35)),('L',(17,35)),('L',(17,33)),('C',(10,18),(17,27),(10,26))],True)
self.path('socket',(19,35),[('L',(19,40)),('A',(23,44),4,4,False),('L',(25,44)),('A',(29,40),4,4,False),('L',(29,35))]);self.relate('connect','bulb','socket')
''',
10:'''self.file()
self.path('bulb',(17,23),[('A',(31,23),7,7,True),('C',(28,31),(31,27),(28,28)),('L',(20,31)),('C',(17,23),(20,28),(17,27))],True)
self.add_line('socket',(21,38),(27,38))
''',
11:'''# Natural pin with a smooth rounded tip; stripe and inner fold meet exact shared nodes.
self.path('pin',(9,19),[('A',(24,4),15,15,True),('A',(33,7),15,15,True),('A',(39,19),15,15,True),('C',(33,31),(39,23),(37,26)),('C',(30,35),(32,32),(31,33)),('C',(24,44),(27,40),(26,44)),('C',(18,35),(22,44),(21,40)),('C',(15,31),(17,33),(16,32)),('C',(9,19),(11,26),(9,23))],True)
self.add_polyline('stripe',(15,31),(24,19),(33,7));self.relate('connect','pin','stripe')
self.path('inner-fold',(24,19),[('C',(29,24),(28,20),(32,21)),('L',(18,35))]);self.relate('connect','stripe','inner-fold');self.relate('connect','pin','inner-fold')
''',
12:'''# Double-storey lowercase g with true circular upper bowl and oval descender.
self.node('upper-bowl',16,14,10,[(-6,8)])
self.add_line('ear',(16,4),(29,4));self.relate('connect','upper-bowl','ear')
self.path('lower-loop',(5,36),[('A',(16,28),11,8,True),('A',(27,36),11,8,True),('A',(16,44),11,8,True),('A',(5,36),11,8,True)],True)
self.path('neck',(10,22),[('C',(16,28),(7,27),(10,28))]);self.relate('connect','neck','upper-bowl');self.relate('connect','neck','lower-loop')
self.add_polyline('plus-h',(32,22),(38,22),(44,22));self.add_polyline('plus-v',(38,16),(38,22),(38,28));self.relate('connect','plus-h','plus-v')
''',
13:'''# Restore seven waveform strokes; one shared 5u pitch keeps the narrow gaps even.
self.circle('badge',24,24,20)
for i,(x,top,bottom) in enumerate([(9,23,25),(14,16,32),(19,22,30),(24,10,38),(29,20,28),(34,16,32),(39,23,25)]):
    self.add_line(f'wave-{i}',(x,top),(x,bottom))
''',
14:'''self.file()
self.box('slide',14,22,34,37,3,{2:[(34,28)],6:[(14,28)]})
self.add_line('slide-header',(14,28),(34,28));self.relate('connect','slide','slide-header')
''',
15:'''# Rounded camera, two hollow controls, proper lens wedge, and a separate capsule microphone.
self.box('body',4,20,32,40,4,{0:[(24,20)],2:[(32,26),(32,34)]})
self.add_polyline('lens',(32,26),(44,20),(44,40),(32,34));self.relate('connect','body','lens')
for i,x in enumerate((12,24)):self.circle(f'control-{i}',x,30,3)
self.path('microphone',(34,4),[('L',(41,4)),('A',(41,10),3,3,True),('L',(34,10)),('A',(31,7),3,3,True),('A',(34,4),3,3,True)],True)
self.path('mount',(24,20),[('L',(24,11)),('A',(28,7),4,4,True),('L',(31,7))]);self.relate('connect','body','mount');self.relate('connect','mount','microphone')
''',
16:'''# Smooth rounded body; the two lens roots land on split side-wall nodes.
self.box('body',4,12,32,36,5,{2:[(32,19),(32,29)]})
self.add_polyline('lens',(32,19),(44,12),(44,36),(32,29));self.relate('connect','body','lens')
''',
17:'''# Shared shoulder shape and circular U-neck; preserve the natural rounded shoulder slopes.
self.path('shirt',(18,6),[('A',(30,6),6,6,False),('C',(38,12),(34,6),(36,8)),('L',(42,22)),('L',(34,25)),('L',(34,42)),('L',(14,42)),('L',(14,25)),('L',(6,22)),('L',(10,12)),('C',(18,6),(12,8),(14,6))],True)
for x in (14,34):
    self.add_line(f'sleeve-seam-{x}',(x,18),(x,25));self.relate('connect','shirt',f'sleeve-seam-{x}')
''',
18:'''# Smooth rear cap and gently rounded horn corners; waveform is a coherent symmetric curve.
self.path('horn',(14,17),[('L',(30,6)),('C',(34,8),(32,4),(34,5)),('L',(34,40)),('C',(30,42),(34,43),(32,44)),('L',(14,31)),('L',(14,17))],True)
self.path('rear',(14,17),[('L',(8,17)),('A',(4,21),4,4,False),('L',(4,27)),('A',(8,31),4,4,False),('L',(14,31))]);self.relate('connect','horn','rear')
self.path('sound-wave',(40,14),[('C',(44,24),(42,16),(44,20)),('C',(40,34),(44,28),(42,32))])
''',
19:'''# Two blade teeth and the source's open grip notch, with smooth rounded handle corners.
self.path('blade',(4,14),[('L',(10,6)),('C',(14,6),(11,4),(12,4)),('L',(30,22)),('L',(23,29)),('L',(18,34)),('L',(16,31)),('L',(16,24)),('L',(10,24)),('L',(10,17)),('L',(4,17)),('L',(4,14))],True)
self.path('handle',(30,22),[('L',(42,34)),('C',(42,38),(44,36),(44,36)),('L',(36,44)),('C',(32,44),(35,45),(33,45)),('L',(26,38)),('L',(29,35)),('L',(23,29))]);self.relate('connect','blade','handle')
'''
}
NOTES={
0:('The narrow cups and blunt band junctions lost the broad earmuff shape.','Widened both tall cups and rebuilt the band with a smooth arc and shared attachment points.'),
1:('The slashed currency C had lumpy terminals and an uneven curved outline.','Rebuilt the C from coherent circular arcs and aligned the diagonal slash to exact C nodes.'),
2:('The return arrow was blocky and the hands were short and visually off-center.','Restored a longer circular return stroke, an open lower gap and hands meeting at the true clock center.'),
3:('The guard was pinched and its joins distorted the semicircular bell.','Rebuilt a balanced curved bell with a smooth blade-root junction and aligned diagonal grip.'),
4:('The nib and writing stroke merged into a heavy hook, losing the pen silhouette.','Restored the pointed nib, cap seam and slit, with a separate smooth writing flourish attached at the tip.'),
5:('The heart was a narrow wedge and the other suit lobes were cramped.','Redrew all four symbols; the heart now has broad matched lobes, a clear notch and a centered tip.'),
6:('The cycle arrows were angular hooks; the carton fold was missing.','Rebuilt curved directional arrows, shaped the apple and restored a gabled carton with a side fold.'),
7:('The at-sign had a tiny counter and an incomplete lower curl; the bubble tail was squared off.','Enlarged the counter, completed the curl and restored the round bubble with its flowing pointed tail.'),
8:('The camera was a square block and the bubble tail had a flat, angular join.','Rounded the camera body and rebuilt the bubble/tail contour and lens attachment.'),
9:('The bulb neck and socket formed a square block with abrupt shoulder joins.','Drew smooth mirrored shoulders and a rounded socket joined to the bulb neck.'),
10:('The page had sharp corners and lost its fold; the bulb shoulder was jagged.','Restored rounded page corners, folded corner and smooth bulb contours with a separate base stroke.'),
11:('The pin had an angular tip and blunt stripe junctions.','Restored a rounded tapered pin with exact stripe/fold attachment nodes and a smooth inner bend.'),
12:('The upper g bowl was squared and flattened, and the lower loop was undersized.','Restored a circular upper bowl, broader oval descender, curved neck and evenly formed plus.'),
13:('The seven-stroke podcast mark was reduced to three thick bars.','Restored all seven evenly spaced waveform strokes inside the circular badge.'),
14:('The page fold was missing and the inner slide looked like a heavy equal-row table.','Restored the folded rounded page and a smooth slide frame with a shallower header row.'),
15:('The microphone became a solid T bar and the camera controls lost their openings.','Restored an outlined capsule microphone, curved mount, hollow controls and clean rounded camera body.'),
16:('Angular fitted segments produced visible notches on the camera body.','Replaced those segments with a coherent rounded rectangle and exact lens-root joins.'),
17:('The neck and shoulders were stiff and boxy.','Restored a circular U-neck, smooth paired shoulders and clean sleeve seams.'),
18:('The rear cap and horn had stepped, angular stroke joins.','Restored rounded rear corners and horn tips, plus one continuous sound-wave curve.'),
19:('The handle became a closed wedge and lost its grip notch.','Restored the notched grip, two blade teeth and rounded handle transitions.')}
REFS={0:'Lucide headphones',1:'No useful direct Lucide match; supplied currency-sign silhouette',2:'Lucide clock-arrow-down and earlier rotate-cw construction',3:'No useful direct Lucide bell-guard match; supplied silhouette',4:'Lucide pen-tool',5:'Lucide heart, club and spade',6:'Lucide apple and milk',7:'Lucide at-sign',8:'Lucide video',9:'Lucide lightbulb',10:'Lucide file and lightbulb',11:'Lucide map-pin',12:'No direct Lucide brand match; circular and oval letter construction',13:'Repeated waveform construction; supplied source pattern',14:'Lucide file',15:'Lucide video',16:'Lucide video',17:'Lucide shirt',18:'Lucide volume-1',19:'No useful direct Lucide saw match; source outline and notch'}
SHAPES={i:'SQUARE' for i in range(20)}
SHAPES.update({0:'VRECT_L',1:'CIRCLE',2:'CIRCLE',7:'VRECT_L',8:'VRECT_L',9:'VRECT_M',10:'VRECT_L',11:'VRECT_L',13:'CIRCLE',14:'VRECT_L',16:'HRECT_M',18:'HRECT_L'})
OMISSIONS={4:'Tiny nib vent fork reduced to one slit.',6:'Tiny carton top lip omitted to keep the gable open.',15:'Secondary carrying handle omitted to separate the microphone mount.'}
def author(indices=None,rev=1):
 for rec in claims:
    i=rec['index']
    if indices is not None and i not in indices:continue
    sid=SOURCE_ICON_ID[i];ref=Path(rec['reference']);concept=ref.stem[:-37]
    run=Path('icon_set/work/primitive-make-ray')/sid/f'20260928T173023Z-fix-{i:02d}-r{rev}';run.mkdir(parents=True,exist_ok=False)
    (run/(rec['icon_id']+'.metadata.json')).write_text(json.dumps(dict(concept=concept,source_uuid=sid,reference_path=str(ref)),indent=2))
    before,change=NOTES[i];shape=SHAPES[i]
    (run/'review.json').write_text(json.dumps(dict(before_problem=before,feedback=rec['feedback'],changes=change,construction_reference=REFS[i],omissions=OMISSIONS.get(i,'None')),indent=2))
    module=run/(rec['icon_id'].replace('-','_')+'_'+sid.replace('-','_')+'.py')
    doc=f'{before} {change}\nSymbol plan: typed contours, shared radii and exact attachment nodes; paired features use common dimensions.\nConstruction: {REFS[i]}. Keyshape {shape}; any proportional departure is recorded as an exact-drawing exception.'
    source=f'{doc!r}\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={sid!r}\nSOURCE_PATH={str(ref)!r}\nAUTHOR="gpt-6"\nPARENT_MODULE={str(next((Path(rec["fix"])/"before").glob("*.py")))!r}\nclass Drawing(Solo48):\n    icon_id={rec["icon_id"]!r}\n    keyshape=Keyshape.{shape}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="primitives-generate"\n    aliases=()\n    keywords={tuple(concept.split())!r}\n'+HELPERS+'\n    def build(self):\n'+textwrap.indent(BODIES[i],'        ')
    module.write_text(source);icon=load_icon(module);svg=icon.to_svg();(run/(rec['icon_id']+'.svg')).write_text(svg);report=icon.validate_icon();(run/'validation.txt').write_text(report.describe());render_previews(svg,rec['icon_id'],48,run)
    for kind in ('original','before'):shutil.copyfile(Path(rec['fix'])/(kind+'.png'),run/(kind+'.png'))
    rec.update(run=str(run),module=str(module),note=change);print(i,rec['icon_id'],report.status,len(report.errors),len(report.warnings),flush=True)
 (BATCH/'authored.json').write_text(json.dumps(claims,indent=2))
def sheets():
 for start in range(0,len(claims),5):
    im=Image.new('RGB',(840,5*230),'#ddd');d=ImageDraw.Draw(im)
    for row,rec in enumerate(claims[start:start+5]):
        y=row*230;run=Path(rec['run']);d.text((8,y+2),f"{rec['index']} {rec['icon_id']}",fill='black')
        for col,name in enumerate(['original.png','before.png','preview-light-384.png','preview-dark-384.png']):
            pic=Image.open(run/name).convert('RGB');pic.thumbnail((174,174));im.paste(pic,(8+col*206,y+26))
        for col,theme in enumerate(['light','dark']):im.paste(Image.open(run/f'preview-{theme}-48.png').convert('RGB'),(420+col*206,y+178))
    im.save(BATCH/f'after-{start//5}.png')
if __name__=='__main__':author();sheets()
