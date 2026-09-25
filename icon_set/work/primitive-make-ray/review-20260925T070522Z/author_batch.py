"""Fresh revisions for the twenty claims in batch.json; no registered outputs."""
import json, re, sys, io
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from icon_set.scripts.primitive_fix import load_icon, render_previews
from PIL import Image, ImageDraw
import cairosvg
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None  # Each input ID is preserved separately in its authored module.
SOURCE_PATH = str(Path(__file__).with_name('batch.json'))
HERE = Path(__file__).parent

HELPERS = '''
        def path(name, start, commands, closed=False):
            here, members = start, []
            for j, (kind, end, *a) in enumerate(commands):
                ident = f'{name}-{j}'
                if kind == 'L': self.add_line(ident, here, end)
                elif kind == 'A': self.add_arc(ident, here, end, radius_x=a[0], radius_y=a[1], sweep=a[2])
                elif kind == 'C': self.add_bezier(ident, here, (a[0], a[1], end))
                here = end
                members.append(ident)
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
'''

# Each entry is a fresh subject-specific design, not a coordinate conversion.
DESIGNS = [
('VRECT_L', 'Pointed stupa over a broad bell dome and plinth. Restore the triangular finial; use mirrored dome arcs and a wider foot.', 'No useful exact local Lucide match; source-specific bell and triangular finial.', '''
        axis = 24
        poly('finial',(axis-6,16),(axis,4),(axis+6,16),closed=True)
        path('dome',(10,36),[('C',(18,16),(10,26),(14,20)),('L',(30,16)),('C',(38,36),(34,20),(38,26))])
        join('finial','dome')
        poly('base',(8,36),(10,36),(38,36),(40,36),(40,44),(8,44),closed=True)
        join('dome','base')
'''),
('SQUARE', 'Two church towers flank a gabled nave. Restore roof seams, round window and arched entry; preserve left cross and source asymmetry.', 'Source architecture; no useful exact local Lucide match.', '''
        poly('outline',(6,42),(6,16),(11,11),(16,16),(16,23),(24,13),(32,23),(32,16),(37,11),(42,16),(42,42),(28,42),(20,42),(6,42))
        for x in (16,32):
            line(f'wall-{x}',(x,23),(x,42));join('outline',f'wall-{x}')
        for l,r in ((6,16),(32,42)):
            line(f'roof-{l}',(l,20),(r,20));join('outline',f'roof-{l}')
        circle('window',24,24,3)
        path('entry',(20,42),[('L',(20,36)),('A',(28,36),4,4,True),('L',(28,42))]);join('entry','outline')
        poly('cross-stem',(11,6),(11,8),(11,11));line('cross-bar',(8,8),(14,8));join('cross-stem','cross-bar');join('cross-stem','outline')
'''),
('VRECT_M', 'A narrow formal necktie with a trapezoidal knot and long tapered blade. Restore slim proportions instead of inflating the knot to fill the keyshape.', 'Source-specific textile silhouette; no useful exact Lucide match.', '''
        axis=24
        poly('knot',(axis-8,4),(axis+8,4),(axis+4,14),(axis-4,14),closed=True)
        poly('blade',(axis-4,14),(axis-10,34),(axis,44),(axis+10,34),(axis+4,14));join('knot','blade')
'''),
('SQUARE', 'Broken diagonal link with two smooth capsule ends and three break rays. Restore round ends and the missing diagonal burst.', 'Lucide unlink original and atomic-debug: round open hooks and detached break rays.', '''
        # Mirror the lower hook across x=y for an equally rounded upper hook.
        for name, swap in [('lower',False),('upper',True)]:
            tr=lambda p: (p[1],p[0]) if swap else p
            path(name,tr((16,24)),[('L',tr((9,31))),('C',tr((6,37)),tr((7,33)),tr((6,35))),('C',tr((11,42)),tr((6,40)),tr((8,42))),('C',tr((18,39)),tr((14,42)),tr((16,41))),('L',tr((26,31)))])
        line('burst-h',(6,16),(10,16));line('burst-v',(16,6),(16,10));line('burst-diagonal',(7,7),(10,10))
'''),
('SQUARE', 'Broken diagonal link with two smooth capsule ends and three break rays. Replace uneven pinched hooks with matched open curves.', 'Lucide unlink original and atomic-debug: round open hooks and detached break rays.', '''
        for name, swap in [('lower',False),('upper',True)]:
            tr=lambda p: (p[1],p[0]) if swap else p
            path(name,tr((16,24)),[('L',tr((9,31))),('C',tr((6,37)),tr((7,33)),tr((6,35))),('C',tr((11,42)),tr((6,40)),tr((8,42))),('C',tr((18,39)),tr((14,42)),tr((16,41))),('L',tr((26,31)))])
        line('burst-h',(6,16),(10,16));line('burst-v',(16,6),(16,10));line('burst-diagonal',(7,7),(10,10))
'''),
('SQUARE', 'Speech bubble with a lightning crack and lower-left tail. Restore a tall bubble and a sharper coherent crack; rounded outer corners.', 'Lucide mail informs rounded enclosure construction; source defines crack and tail.', '''
        path('bubble',(10,6),[('L',(21,6)),('L',(25,13)),('L',(21,17)),('L',(31,28)),('L',(28,17)),('L',(32,14)),('L',(29,6)),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,32)),('A',(38,36),4,4,True),('L',(24,36)),('L',(14,42)),('L',(14,36)),('L',(10,36)),('A',(6,32),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
'''),
('SQUARE', 'Magic cauldron with outlined bubble, sparkle, rounded rim and two small feet. Restore a hollow bubble and a visible rim band.', 'Source-specific vessel; no useful exact Lucide match.', '''
        rect('rim',6,17,42,23,3)
        path('pot',(10,23),[('L',(10,28)),('C',(16,37),(10,32),(12,35)),('C',(24,39),(19,39),(21,39)),('C',(32,37),(27,39),(29,39)),('C',(38,28),(36,35),(38,32)),('L',(38,23))]);join('pot','rim')
        for s in (-1,1):
            line(f'foot-{s}',(24+s*8,37),(24+s*13,42));join(f'foot-{s}','pot')
        circle('bubble',13,8,3)
        poly('spark-v',(34,5),(34,8),(34,11));poly('spark-h',(31,8),(34,8),(37,8));join('spark-v','spark-h')
'''),
('SQUARE', 'Fire burning inside a fireplace with projecting mantel and hearth. Restore the architectural surround and an open teardrop flame.', 'Source-specific fireplace; no useful exact local Lucide match.', '''
        poly('mantel',(6,6),(42,6),(42,12),(38,12),(10,12),(6,12),closed=True)
        poly('hearth',(6,36),(10,36),(38,36),(42,36),(42,42),(6,42),closed=True)
        for x in (10,38):
            line(f'post-{x}',(x,12),(x,36));join(f'post-{x}','mantel');join(f'post-{x}','hearth')
        path('flame',(24,18),[('C',(32,30),(28,22),(32,25)),('C',(24,36),(32,34),(28,36)),('C',(18,30),(20,36),(16,34)),('C',(24,18),(20,27),(23,23))],True);join('flame','hearth')
'''),
('VRECT_L', 'A lit candle stands on a pedestal altar. Restore a tall candle body, plain pedestal sides and a broad foot; flame remains pointed.', 'Source-specific altar; no useful exact local Lucide match.', '''
        path('flame',(24,4),[('C',(28,10),(25,6),(28,8)),('A',(20,10),4,4,True),('C',(24,4),(20,8),(23,6))],True)
        poly('candle',(20,27),(20,19),(28,19),(28,27))
        poly('table',(8,27),(20,27),(28,27),(40,27));join('candle','table')
        poly('pedestal',(12,27),(12,38),(8,44),(40,44),(36,38),(36,27));join('pedestal','table')
        line('base-seam',(12,38),(36,38));join('base-seam','pedestal')
'''),
('HRECT_L', 'A cannon barrel rises above a round carriage wheel and a low support. Restore the long rounded barrel and axle ring.', 'Source-specific cannon silhouette; no useful exact Lucide match.', '''
        path('barrel',(13,28),[('C',(9,21),(9,27),(8,23)),('C',(14,16),(9,18),(11,17)),('L',(44,8)),('L',(44,18)),('L',(32,22))])
        circle('wheel',22,30,10);circle('axle',22,30,3)
        poly('carriage',(12,32),(4,35),(4,40),(22,40));join('wheel','carriage')
'''),
('VRECT_L', 'Playing-card club suit with three equal round lobes and a tapered stem. Restore equal lobe weight and clear inward shoulders.', 'Source-specific club symbol; no useful exact Lucide match.', '''
        path('club',(19,21),[('C',(15,13),(16,18),(15,16)),('C',(24,4),(15,8),(19,4)),('C',(33,13),(29,4),(33,8)),('C',(29,21),(33,16),(32,18)),('C',(40,29),(36,18),(40,23)),('C',(24,34),(40,39),(29,40)),('C',(8,29),(19,40),(8,39)),('C',(19,21),(8,23),(12,18))],True)
        poly('stem',(24,34),(22,44),(26,44),(24,34));join('stem','club')
'''),
('SQUARE', 'A handled carving gouge cuts a bowl beside a curled wood shaving. Restore the visible handle and shaving spiral; retain the bowl foot.', 'Source-specific craft tool; no useful exact local Lucide match.', '''
        path('handle',(6,9),[('A',(12,6),4,4,True),('L',(22,16)),('L',(16,22)),('L',(6,12)),('L',(6,9))],True)
        poly('blade',(19,19),(28,28));join('handle','blade')
        path('bowl',(6,28),[('L',(42,28)),('A',(24,40),18,12,True),('A',(6,28),18,12,True)],True);join('blade','bowl')
        poly('foot',(18,40),(18,44),(30,44),(30,40));join('foot','bowl')
        path('shaving',(34,28),[('C',(42,18),(39,26),(42,22)),('C',(36,12),(42,14),(40,12)),('C',(32,18),(32,12),(30,16)),('C',(36,20),(32,20),(35,21))])
'''),
('HRECT_L', 'A wide round cauldron with a flared lip and smoothly bulging shoulders. Replace angular shoulder transitions with a continuous rounded belly.', 'Source-specific pot silhouette; no useful exact local Lucide match.', '''
        path('pot',(8,8),[('L',(40,8)),('A',(40,16),4,4,True),('C',(44,25),(42,18),(44,22)),('C',(28,40),(44,35),(38,40)),('L',(20,40)),('C',(4,25),(10,40),(4,35)),('C',(8,16),(4,22),(6,18)),('A',(8,8),4,4,True)],True)
'''),
('SQUARE', 'Two interlocked diagonal chain links with smoothly rounded ends and a central connecting stroke. Replace chamfered top and mismatched ends.', 'Lucide unlink original and atomic-debug: open round-ended contours; connector changes unlink to link.', '''
        for name,swap in [('lower',False),('upper',True)]:
            tr=lambda p: (48-p[0],48-p[1]) if swap else p
            path(name,tr((14,23)),[('L',tr((9,28))),('C',tr((6,35)),tr((7,30)),tr((6,32))),('A',tr((13,42)),7,7,not swap),('C',tr((20,39)),tr((16,42)),tr((18,41))),('L',tr((25,34)))])
        line('interlock',(18,30),(30,18))
'''),
('VRECT_L', 'Upright half-charged battery with a centered terminal and equal rounded corners. Repair the lopsided shoulder and inconsistent corner radii.', 'Lucide mail original and atomic-debug: uniform corner arcs; source battery layout.', '''
        path('battery',(18,4),[('L',(30,4)),('L',(30,10)),('L',(34,10)),('A',(40,16),6,6,True),('L',(40,28)),('L',(40,38)),('A',(34,44),6,6,True),('L',(14,44)),('A',(8,38),6,6,True),('L',(8,28)),('L',(8,16)),('A',(14,10),6,6,True),('L',(18,10)),('L',(18,4))],True)
        line('charge-level',(8,28),(40,28));join('battery','charge-level')
'''),
('HRECT_L', 'Rounded cheese or nougat block with three differently sized holes and two open edge bites. Restore rounded corners and outlined interior holes.', 'Lucide mail original and atomic-debug informs rounded perimeter; source supplies holes and bites.', '''
        path('block',(10,8),[('L',(38,8)),('A',(44,14),6,6,True),('L',(38,14)),('A',(38,22),4,4,False),('L',(44,22)),('L',(44,30)),('A',(40,34),4,4,False),('A',(44,38),4,4,False),('L',(44,40)),('L',(10,40)),('A',(4,34),6,6,True),('L',(4,14)),('A',(10,8),6,6,True)],True)
        circle('hole-top',17,19,4);circle('hole-small',13,31,2);circle('hole-bottom',27,31,3)
'''),
('SQUARE', 'Chef toque above a mirrored curled moustache. Restore cuff and pleat detail, smooth three-lobed crown and two open moustache lobes.', 'Lucide chef-hat original and atomic-debug: three lobes over a cuff. human_ref/user.svg inspected; no head or torso in this symbol.', '''
        path('hat',(10,19),[('C',(6,13),(7,18),(6,16)),('C',(16,9),(6,7),(12,6)),('C',(24,6),(18,6),(20,6)),('C',(32,9),(28,6),(30,6)),('C',(42,13),(36,6),(42,7)),('C',(38,19),(42,16),(41,18)),('L',(38,27)),('L',(10,27)),('L',(10,19))],True)
        line('cuff',(10,21),(38,21));join('cuff','hat')
        for x in (18,30):line(f'pleat-{x}',(x,16),(x,21));join(f'pleat-{x}','cuff')
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            path(f'moustache-{side}',p(0,36),[('C',p(10,36),p(3,31),p(7,32)),('C',p(18,34),p(14,39),p(16,36)),('C',p(8,42),p(18,40),p(13,42)),('C',p(0,36),p(4,42),p(1,39))],True)
        join('moustache--1','moustache-1')
'''),
('SQUARE', 'Chef toque above a mirrored curled moustache. Restore the outlined moustache lobes and pleats rather than a shallow wavy stroke.', 'Lucide chef-hat original and atomic-debug: three lobes over a cuff. human_ref/user.svg inspected; no head or torso in this symbol.', '''
        path('hat',(10,19),[('C',(6,13),(7,18),(6,16)),('C',(16,9),(6,7),(12,6)),('C',(24,6),(18,6),(20,6)),('C',(32,9),(28,6),(30,6)),('C',(42,13),(36,6),(42,7)),('C',(38,19),(42,16),(41,18)),('L',(38,27)),('L',(10,27)),('L',(10,19))],True)
        line('cuff',(10,21),(38,21));join('cuff','hat')
        for x in (18,30):line(f'pleat-{x}',(x,16),(x,21));join(f'pleat-{x}','cuff')
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            path(f'moustache-{side}',p(0,36),[('C',p(10,36),p(3,31),p(7,32)),('C',p(18,34),p(14,39),p(16,36)),('C',p(8,42),p(18,40),p(13,42)),('C',p(0,36),p(4,42),p(1,39))],True)
        join('moustache--1','moustache-1')
'''),
('VRECT_L', 'A chess pawn with a round head, curved taper and broad base. Replace angular waist with concave curves and restore the collar.', 'Source-specific pawn; no useful exact local Lucide match.', '''
        path('pawn',(18,20),[('A',(24,4),9,9,True),('A',(30,20),9,9,True),('L',(29,23)),('C',(34,36),(28,28),(30,32)),('L',(36,36)),('A',(40,40),4,4,True),('L',(40,44)),('L',(8,44)),('L',(8,40)),('A',(12,36),4,4,True),('L',(14,36)),('C',(19,23),(18,32),(20,28)),('L',(18,20))],True)
        line('collar',(19,23),(29,23));join('collar','pawn')
        line('base-seam',(14,36),(34,36));join('base-seam','pawn')
'''),
('HRECT_L', 'Closed mail envelope with equal rounded corners and a softly rounded flap tip. Replace angular chamfers and pointed flap.', 'Lucide mail original and atomic-debug: rounded enclosure and curved flap junction.', '''
        path('envelope',(8,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
        path('flap',(4,12),[('L',(20,25)),('C',(28,25),(23,28),(25,28)),('L',(44,12))]);join('flap','envelope')
'''),
]

def main():
    rows=json.loads((HERE/'batch.json').read_text())
    for i,(row,design) in enumerate(zip(rows,DESIGNS)):
        keyshape,plan,ref,body=design
        source=Path(row['ref']); uuid=re.search(r'[a-f0-9-]{36}$',source.stem).group()
        concept=source.stem[:-37]
        out=ROOT/'icon_set/work/primitive-make-ray'/uuid/f'20260925T070522Z-thuan-revision-{i:02}'
        out.mkdir(parents=True,exist_ok=False)
        ident=row['key'].split('/')[1]
        metadata={'concept':concept,'source_uuid':uuid,'reference_path':row['ref'],'icon_id':ident,'author':AUTHOR,'feedback':'Manual fix request'}
        (out/f'{ident}.metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
        module=out/(ident.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
        module.write_text(f'"""{plan}\nConstruction: {ref}\nFresh standalone revision; original preserved.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {uuid!r}\nSOURCE_PATH = {row["ref"]!r}\nAUTHOR = {AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id = {ident!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(ident.split("-"))!r}\n\n    def build(self):\n'+HELPERS+body)
        icon=load_icon(module); svg=icon.to_svg();report=icon.validate_icon()
        (out/f'{ident}.svg').write_text(svg)
        (out/'validation.txt').write_text(report.describe())
        render_previews(svg,ident,48,out)
        cairosvg.svg2png(url=str(source),write_to=str(out/'reference.png'),output_width=192,output_height=192)
        row.update(run=str(out.relative_to(ROOT)),module=str(module.relative_to(ROOT)),plan=plan,construction_reference=ref,keyshape=keyshape)
        print(i,ident,report.status,len(report.errors),len(report.warnings),flush=True)
    (HERE/'batch.json').write_text(json.dumps(rows,indent=2)+'\n')

if __name__=='__main__': main()
