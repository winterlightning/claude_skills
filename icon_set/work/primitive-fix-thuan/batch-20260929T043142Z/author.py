from pathlib import Path
import sys,json,datetime,io,re
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw
import cairosvg
BATCH=Path(__file__).parent
ITEMS=json.loads((BATCH/'items.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID=[re.search(r'[0-9a-f-]{36}$',Path(i['ref']).stem).group() for i in ITEMS]
SOURCE_PATH=[i['ref'] for i in ITEMS]
HELPERS='''
    def path(self, name, start, commands, closed=False):
        members=[]
        at=start
        for n,c in enumerate(commands):
            ident=f"{name}-{n}"
            if c[0]=='L':
                end=c[1]; self.add_line(ident,at,end)
            else:
                _,end,rx,ry,sweep,*large=c
                self.add_arc(ident,at,end,radius_x=rx,radius_y=ry,sweep=sweep,large_arc=bool(large and large[0]))
            members.append(ident); at=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

    def box(self,name,l,t,r,b,rad=2):
        self.path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
'''
DESIGNS={}
def design(n,key,problem,change,code,ref='no useful exact Lucide match; coherent circular arcs and shared parameters'):
    DESIGNS[n]=(key,problem,change,code,ref)

design(0,'HRECT_L','The arrows are distorted into a narrow S rather than following one round cycle.','Restored a common circular orbit, counterclockwise direction and distinct arrow tips.', '''
        # Two arcs share a circular center; opposite arrowheads are mirrored.
        self.path('upper',(39,16),[('A',(24,7),17,17,False),('A',(7,24),17,17,False)])
        self.add_polyline('upper-tip',(4,18),(7,24),(13,20))
        self.relate('connect','upper','upper-tip')
        self.path('lower',(9,32),[('A',(24,41),17,17,False),('A',(41,24),17,17,False)])
        self.add_polyline('lower-tip',(35,28),(41,24),(44,30))
        self.relate('connect','lower','lower-tip')
''','refresh-ccw: common orbit and tangent arrowhead attachments')
design(1,'HRECT_L','The solid bars make a Roman numeral rather than the reference railing with broad outlined rails.','Restored two rounded outlined rails with three evenly spaced upright supports.', '''
        # Two identical rails and one evenly spaced upright series.
        self.box('top-rail',4,8,44,16,2)
        self.box('bottom-rail',4,32,44,40,2)
        for n,x in enumerate((12,24,36)):
            p=f'post-{n}'; self.add_line(p,(x,16),(x,32))
            self.relate('connect',p,'top-rail'); self.relate('connect',p,'bottom-rail')
''')
design(2,'SQUARE','The cloud is flattened and every rain streak has the same short length.','Restored a tall central cloud lobe and three slanted rain streaks with a longer middle streak.', '''
        # Cloud owns three rounded lobes and a flat base; rain is a detached series.
        self.path('cloud',(12,28),[('A',(12,16),6,6,True),('L',(14,16)),('A',(34,16),10,10,True),('L',(36,16)),('A',(36,28),6,6,True),('L',(12,28))],True)
        for n,(x,y) in enumerate(((15,40),(27,42),(39,40))):
            self.add_line(f'rain-{n}',(x,36),(x-3,y))
''','cloud-rain: distinct cloud lobe and detached rain strokes')
design(3,'SQUARE','The moon is an open C stroke and the cloud silhouette is angular.','Restored a closed crescent behind a rounded cloud and three diagonal precipitation strokes.', '''
        # The cloud occludes the lower left moon; the visible crescent retains two edges.
        self.path('moon',(44,4),[('A',(44,24),10,10,False),('A',(44,4),4,10,True)],True)
        self.path('cloud',(12,32),[('A',(12,18),7,7,True),('A',(28,20),8,8,True),('A',(28,32),6,6,True),('L',(12,32))],True)
        for n,x in enumerate((14,24,34)):
            self.add_line(f'rain-{n}',(x,40),(x-3,44))
''','cloud-rain: smooth cloud shoulders and separated weather marks')
HAND='''
        # Four finger caps share 6-unit pitch; palm keeps an open wrist and thumb crease.
        self.path('silhouette',(15,44),[
            ('L',(15,40)),('L',(8,30)),('A',(7,26),7,7,True),('L',(7,22)),
            ('A',(13,22),3,3,True),('L',(13,10)),('A',(19,10),3,3,True),
            ('L',(19,7)),('A',(25,7),3,3,True),('L',(25,9)),
            ('A',(31,9),3,3,True),('L',(31,13)),('A',(37,13),3,3,True),
            ('L',(37,29)),('A',(33,40),17,17,True),('L',(33,44))])
        for n,(x,y) in enumerate(((19,10),(25,9),(31,13))):
            p=f'finger-seam-{n}'; self.add_line(p,(x,y),(x,21)); self.relate('connect',p,'silhouette')
        self.path('thumb-crease',(13,22),[('L',(13,27)),('A',(22,34),9,9,True)])
        self.relate('connect','thumb-crease','silhouette')
'''
for n in (4,5,6):
    design(n,'VRECT_L','The wrist and thumb anatomy were shortened or lost, so the raised hand reads as a mitten or wave.','Restored four graduated fingers, a separate thumb fold, a tall palm and an open wrist.',HAND,'hand: graduated finger caps and shared finger seams; supplied hand reference owns wrist proportions')
design(7,'SQUARE','The lower palm and wrist are absent, and only three fingers remain.','Rebuilt the complete diagonal open hand with four fingers, thumb, palm crease and wrist.', '''
        # An inclined hand retains all four finger tips and the reference wrist opening.
        self.path('hand',(9,42),[('L',(12,35)),('L',(6,26)),('A',(11,22),3,3,True),('L',(15,27)),('L',(24,8)),('A',(30,10),3,3,True),('L',(27,17)),('L',(32,6)),('A',(38,8),3,3,True),('L',(32,22)),('L',(38,12)),('A',(43,15),3,3,True),('L',(36,28)),('L',(40,22)),('A',(44,26),3,3,True),('L',(35,39)),('L',(27,44))])
        self.path('thumb-fold',(15,27),[('A',(23,35),9,9,True)])
        self.relate('connect','hand','thumb-fold')
''','hand: rounded caps and full palm silhouette, deliberately tilted as supplied')
design(8,'VRECT_L','The folded fingers became edge bumps and the crossing thumb disappeared.','Restored two separated raised fingers, two curled knuckles, and a thumb crossing the palm.', '''
        # V fingers form the upper silhouette; folded fingers and thumb form the lower hand.
        self.path('hand',(14,24),[('L',(9,8)),('A',(15,6),3,3,True),('L',(23,24)),('L',(29,6)),('A',(35,8),3,3,True),('L',(30,25)),('L',(35,27)),('A',(37,31),4,4,True),('L',(37,34)),('A',(12,36),13,13,True),('L',(9,29)),('A',(14,24),4,4,True)],True)
        self.add_line('folded-fingers',(14,24),(18,33)); self.relate('connect','folded-fingers','hand')
        self.path('thumb',(34,29),[('L',(22,26)),('A',(20,31),3,3,False),('L',(27,34))])
''','hand: connected rounded finger construction; asymmetry preserves the V gesture')
design(9,'SQUARE','The wrist ornament sits outside the arm and the palm became a jagged outline.','Rebuilt a diagonal closed hand, a continuous wrist band and a central circular rakhi ornament.', '''
        # The arm runs diagonally; the bracelet crosses it at the wrist.
        self.path('outer',(27,4),[('L',(36,12)),('L',(43,17)),('L',(34,27)),('A',(32,36),10,10,True),('L',(25,43)),('A',(20,39),3,3,True)])
        self.path('lower',(20,39),[('A',(15,40),3,3,True),('L',(10,35)),('A',(6,30),4,4,True),('L',(16,18)),('L',(23,10))])
        self.add_line('finger-1',(15,32),(11,36)); self.relate('connect','finger-1','lower')
        self.add_line('finger-2',(25,33),(20,39)); self.relate('connect','finger-2','outer'); self.relate('connect','finger-2','lower')
        self.circle('rakhi',29,16,5)
        self.add_line('band-left',(21,10),(25,13)); self.relate('connect','band-left','rakhi')
        self.add_line('band-right',(33,19),(39,22)); self.relate('connect','band-right','rakhi')
''','hand: rounded knuckle silhouettes; intentional diagonal wrist arrangement')

design(10,'SQUARE','The bowl lost its foot, round contents and hanging noodles; one chopstick floats separately.','Restored two full chopsticks, a lifted noodle bundle, bowl contents and a foot under the curved bowl.', '''
        # Bowl, foot, noodles and chopsticks are separate physical components.
        self.path('bowl',(4,26),[('L',(44,26)),('A',(4,26),20,14,True)],True)
        self.add_polyline('foot',(17,40),(17,44),(31,44),(31,40))
        self.relate('connect','bowl','foot')
        self.add_line('chopstick-top',(10,9),(44,4))
        self.add_line('chopstick-bottom',(17,13),(44,11))
        self.add_line('noodle-left',(18,8),(18,26))
        self.add_line('noodle-right',(24,7),(24,26))
        self.relate('connect','noodle-left','bowl'); self.relate('connect','noodle-right','bowl')
        self.path('food-left',(8,26),[('A',(14,19),7,7,True)])
        self.path('food-right',(28,26),[('A',(40,26),6,6,True)])
        self.relate('connect','food-left','bowl'); self.relate('connect','food-right','bowl')
''','soup: coherent curved bowl and pedestal foot; supplied reference owns chopsticks and hanging noodles')

BERRY='''
        # Berry is a tapered cluster of six visible drupelets, with no hidden overlapping outlines.
        self.circle('middle',24,22,6)
        self.path('left',(19,18),[('A',(8,23),7,7,False),('A',(13,30),7,7,False),('A',(19,27),7,7,False)])
        self.path('right',(29,18),[('A',(40,23),7,7,True),('A',(35,30),7,7,True),('A',(29,27),7,7,True)])
        self.path('lower-left',(13,30),[('A',(24,37),8,8,False)])
        self.path('lower-right',(35,30),[('A',(24,37),8,8,True)])
        self.add_line('fruit-seam',(24,28),(24,37)); self.relate('connect','fruit-seam','middle'); self.relate('connect','fruit-seam','lower-left'); self.relate('connect','fruit-seam','lower-right')
        self.path('tip',(18,38),[('A',(30,38),6,6,False)])
'''
design(11,'VRECT_L','The raspberry became a three-lobed blank outline with no drupelet pattern.','Restored six rounded berry segments in a tapered cluster beneath two pointed leaves.', '''
        # A mirrored pair of leaves crowns the characteristic raspberry cluster.
        self.path('leaf-left',(23,16),[('A',(10,4),13,13,False),('A',(23,16),13,13,False)],True)
        self.path('leaf-right',(25,16),[('A',(38,4),13,13,True),('A',(25,16),13,13,True)],True)
'''+BERRY,'grape: distinct rounded fruit units; supplied raspberry reference owns the upright tapered cluster')
design(12,'VRECT_L','The repeated bumps read as a cog or flower rather than a raspberry made of round drupelets.','Restored a layered tapered berry, a pointed side leaf and a curved stem.', '''
        # Curved upright stem and one leaf retain the natural asymmetric crown.
        self.path('stem',(25,17),[('A',(33,4),18,18,True)])
        self.path('leaf',(24,15),[('A',(11,5),13,13,False),('A',(24,15),13,13,False)],True)
'''+BERRY,'grape: rounded drupelets and a distinct stem, with the supplied asymmetric leaf retained')
design(13,'VRECT_L','The fruit has only two oversized lobes and a tiny base, losing the clustered berry structure.','Restored a tapered six-segment berry and three individually legible pointed leaves.', '''
        # Three leaves are arranged around the center axis; fruit owns its repeated segments.
        self.path('leaf-center',(24,16),[('A',(24,3),9,9,True),('A',(24,16),9,9,True)],True)
        self.path('leaf-left',(20,16),[('A',(8,7),12,12,False),('A',(20,16),12,12,False)],True)
        self.path('leaf-right',(28,16),[('A',(40,7),12,12,True),('A',(28,16),12,12,True)],True)
'''+BERRY,'grape: visible rounded fruit segments; reference supplies three-leaf crown')
design(14,'VRECT_L','The booklet lost its angled rear cover and both text rules, and its star is cramped.','Restored an angled rear leaf, a clear rating star, and one text line on the front cover; one of the two source rules is omitted for legibility.', '''
        # Front cover owns star and centered text; the rear leaf projects above it.
        self.add_polyline('back',(14,10),(35,4),(35,12))
        self.box('cover',10,12,38,44,1)
        self.relate('connect','back','cover')
        self.add_polyline('star',(24,18),(27,24),(33,24),(28,28),(30,34),(24,31),(18,34),(20,28),(15,24),(21,24),closed=True)
        self.add_line('text-1',(20,38),(28,38))
''','no useful exact Lucide match; rounded enclosure and one coherent star contour')
design(15,'SQUARE','The tail is enclosed like a handle and the broad snake head lacks eyes and a forked tongue.','Restored an S-shaped snake with a separate segmented rattle, a broad head, eyes and a forked tongue.', '''
        # One continuous tubular body ends in a widened head; the rattle is a detached series.
        self.path('snake',(5,26),[('L',(5,33)),('A',(23,33),9,9,False),('L',(23,16)),('A',(31,16),4,4,True),('L',(31,21)),('L',(26,25)),('A',(34,38),15,15,False),('A',(44,25),15,15,False),('L',(39,21)),('L',(39,16)),('A',(17,16),11,11,False),('L',(17,33)),('A',(11,33),3,3,True),('L',(11,26)),('A',(5,26),3,3,False)],True)
        self.add_dot('eye-left',(32,27)); self.add_dot('eye-right',(38,27))
        self.add_polyline('tongue',(35,38),(35,42),(32,45)); self.relate('connect','tongue','snake')
        self.add_line('fork',(35,42),(38,45)); self.relate('connect','fork','tongue')
        for n,y in enumerate((19,13,7)):
            self.add_line(f'rattle-{n}',(6+n,y),(10-n,y)) if n<2 else self.add_dot(f'rattle-{n}',(8,y))
''','no useful exact Lucide match; concentric body bends and minimal facial marks')
design(16,'SQUARE','The handshake was reduced to an X above a bowl-shaped outline.','Restored opposing cuffs, a crossing thumb, interlocking hands and a house roof above.', '''
        # Roof stands separately over two hands; their meeting seam identifies a handshake.
        self.add_polyline('roof',(4,19),(24,4),(44,19))
        self.box('cuff-left',5,25,11,38,1)
        self.box('cuff-right',37,25,43,38,1)
        self.path('left-hand',(11,28),[('L',(18,25)),('L',(23,26))])
        self.path('right-hand',(37,28),[('L',(29,24)),('A',(24,25),5,5,False),('L',(19,29)),('A',(24,31),4,4,False),('L',(27,29)),('L',(34,36)),('A',(30,40),3,3,True),('L',(26,36))])
        self.path('fingers',(11,36),[('L',(21,44)),('A',(25,42),3,3,False),('A',(30,40),3,3,False)])
        self.relate('connect','left-hand','cuff-left'); self.relate('connect','right-hand','cuff-right'); self.relate('connect','fingers','cuff-left'); self.relate('connect','right-hand','fingers')
''','handshake: crossing thumb and rounded finger joints; reference supplies house roof')
design(17,'SQUARE','The calculator became a generic device with a display and two dots, losing the arithmetic operators.','Restored a four-cell arithmetic calculator with plus, minus, multiply and equals in front of a house.', '''
        # The calculator occludes the lower-left house; its 2x2 series owns the four operators.
        self.add_polyline('roof',(20,14),(32,4),(44,14))
        self.add_polyline('house',(42,19),(42,29),(37,29))
        self.box('calculator',4,16,35,44,3)
        self.add_line('plus-h',(10,24),(14,24)); self.add_line('plus-v',(12,22),(12,26)); self.relate('connect','plus-h','plus-v')
        self.add_line('minus',(25,24),(29,24))
        self.add_line('times-a',(10,34),(14,38)); self.add_line('times-b',(14,34),(10,38)); self.relate('connect','times-a','times-b')
        for n,y in enumerate((33,38)): self.add_line(f'equals-{n}',(25,y),(29,y))
''','calculator: rounded body and aligned keypad; operators follow the supplied reference')
design(18,'VRECT_L','The house has no doorway and the pointing hand has a floating mitten silhouette without a wrist.','Restored a house with a doorway above a complete pointing hand, including bent fingers and wrist.', '''
        # Small house is separate above the pointing fingertip; the full hand keeps its wrist opening.
        self.add_polyline('roof',(26,14),(28,12),(36,4),(44,12),(46,14))
        self.add_polyline('house',(28,12),(28,20),(44,20),(44,12))
        self.relate('connect','roof','house')
        self.add_polyline('door',(33,20),(33,14),(39,14),(39,20)); self.relate('connect','door','house')
        self.path('hand',(14,44),[('L',(14,40)),('L',(7,31)),('A',(12,28),3,3,True),('L',(15,32)),('L',(15,21)),('A',(21,21),3,3,True),('L',(21,28)),('A',(27,28),3,3,True),('A',(33,29),3,3,True),('L',(33,36)),('A',(31,40),8,8,True),('L',(31,44))])
        self.add_line('fold-1',(21,28),(21,32)); self.relate('connect','fold-1','hand')
        self.add_line('fold-2',(27,28),(27,32)); self.relate('connect','fold-2','hand')
''','hand: rounded finger caps and coherent thumb; supplied reference owns the pointing gesture and house')
design(19,'SQUARE','The eye merged with the triangle sides and lost its lower eyelid and outlined iris.','Restored a complete almond eye enclosed by a triangular outline; the iris is a solid pupil to keep the eye open and clear at 48px.', '''
        # Triangle owns one complete eye; both lids share the same mirrored endpoints.
        self.add_polyline('triangle',(24,4),(46,44),(2,44),closed=True)
        self.path('eye',(15,31),[('A',(33,31),10,10,True),('A',(15,31),10,10,True)],True)
        self.add_dot('pupil',(24,31))
''','eye: paired circular lid arcs and an outlined circular iris')

def generate(indices):
    runs=json.loads((BATCH/'runs.json').read_text()) if (BATCH/'runs.json').exists() else {}
    for n in indices:
        r=ITEMS[n]; key,problem,change,code,ref=DESIGNS[n]
        stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        out=ROOT/'icon_set/work/primitive-make-ray'/SOURCE_ICON_ID[n]/(stamp+'-meaning-fix')
        out.mkdir(parents=True)
        meta=dict(concept=Path(r['ref']).stem[:-37],source_uuid=SOURCE_ICON_ID[n],reference_path=r['ref'],icon_id=r['icon_id'],author=AUTHOR,original_vs_rejected=problem,feedback=r['feedback'],changes=change,lucide_reference=ref,keyshape=key)
        (out/(r['icon_id']+'.metadata.json')).write_text(json.dumps(meta,indent=2))
        module=out/(r['icon_id'].replace('-','_')+'_'+SOURCE_ICON_ID[n].replace('-','_')+'.py')
        module.write_text(f'"""{change}\nPlan and comparison: {problem}\nConstruction reference: {ref}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={SOURCE_ICON_ID[n]!r}\nSOURCE_PATH={r["ref"]!r}\nAUTHOR={AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id={r["icon_id"]!r}\n    keyshape=Keyshape.{key}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="objects/general"\n    aliases=()\n    keywords=()\n'+HELPERS+'\n    def build(self):\n'+code)
        icon=load_icon(module); report=icon.validate_icon(); svg=icon.to_svg()
        (out/(r['icon_id']+'.svg')).write_text(svg)
        (out/'validation.txt').write_text(report.describe())
        render_previews(svg,r['icon_id'],48,out)
        cairosvg.svg2png(url=str(ROOT/r['ref']),write_to=str(out/'original.png'),output_width=384,output_height=384,background_color='white')
        g=gate(module); (out/'gate.json').write_text(json.dumps(g,indent=2))
        (out/'review-notes.md').write_text(f'# {r["key"]}\n\nOriginal versus rejected: {problem}\n\nFeedback: {r["feedback"]}\n\nRevision: {change}\n\nConstruction: {ref}\n\nVisual review pending.\n')
        runs[str(n)]={'dir':str(out.relative_to(ROOT)),'module':str(module.relative_to(ROOT)),'metadata':meta}
        print(n,r['icon_id'],report.status,'gate',g['status'],len(g['errors']),len(g['warnings']),flush=True)
        (BATCH/'runs.json').write_text(json.dumps(runs,indent=2))
    sheet(indices,runs)

def sheet(indices,runs):
    for start in range(0,len(indices),5):
        subset=indices[start:start+5]; im=Image.new('RGB',(1000,200*len(subset)),'#e5e5e5'); d=ImageDraw.Draw(im)
        for j,n in enumerate(subset):
            r=ITEMS[n]; out=ROOT/runs[str(n)]['dir']; y=j*200
            d.text((8,y+4),f"{n} {r['icon_id']}",fill='black')
            orig=Image.open(out/'original.png').resize((150,150)); im.paste(orig,(10,y+30))
            for k,theme in enumerate(('light','dark')):
                im.paste(Image.open(out/f'preview-{theme}-384.png').resize((150,150)),(210+k*360,y+30))
                im.paste(Image.open(out/f'preview-{theme}-48.png'),(380+k*360,y+70))
        im.save(BATCH/f'after-{subset[0]}.png')

if __name__=='__main__':
    generate([int(x) for x in sys.argv[1:]])
