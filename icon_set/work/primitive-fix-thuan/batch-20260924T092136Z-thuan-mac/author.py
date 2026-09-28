"""Standalone revision authoring; sources are recorded per input in claimed.json."""
from pathlib import Path
import json
SOURCE_ICON_ID = None  # Multiple exact source IDs in claimed.json and each output module.
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/batch-20260924T092136Z-thuan-mac/claimed.json'
AUTHOR = 'gpt-6'
ROOT = Path(__file__).parent
records = json.loads((ROOT/'claimed.json').read_text())
HELPERS = '''
        # Typed continuous paths own their junctions. Repeated parts share parameters.
        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i, (kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                ids.append(ident);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
designs={
 'cup-1':('SQUARE','Lucide coffee: tangent bowl corners and a rounded external handle.','Steam absent in source; no omissions.', '''
        # Body owns bottom radius 10; handle uses an 8-unit semicircle.
        path('body',(6,6),[('L',(32,6)),('L',(32,14)),('L',(32,30)),('L',(32,32)),('A',(22,42),10,10,True),('L',(16,42)),('A',(6,32),10,10,True),('L',(6,6))],True)
        path('handle',(32,14),[('L',(34,14)),('A',(42,22),8,8,True),('A',(34,30),8,8,True),('L',(32,30))])
        join('body','handle')
'''),
 'cute-cat':('SQUARE','Lucide cat: paired pointed ears, rounded cheeks, small separate eyes.','Simplified mouth to one broad smile; no whiskers in source.', '''
        # Mirror ear and cheek construction about x=24; bounds 6,6 to 42,42.
        path('head',(18,14),[('L',(8,6)),('A',(6,8),2,2,False),('L',(8,22)),('C',(24,42),(4,38),(10,42)),('C',(40,22),(38,42),(44,38)),('L',(42,8)),('A',(40,6),2,2,False),('L',(30,14)),('L',(18,14))],True)
        for x in (16,32): self.add_dot('eye-'+str(x),(x,23))
        path('smile',(20,31),[('A',(28,31),5,5,False)])
'''),
 'curved-gauge-indicator-batch-018-15':('HRECT_M','Lucide gauge: coherent arch and a single straight diagonal pointer.','No scale ticks or numerals exist in source; retained crossing tick.', '''
        # Arch is split at the real pointer crossing (40,22); no arrowhead.
        path('arch',(4,38),[('C',(24,10),(4,22),(12,10)),('C',(40,22),(32,10),(37,15)),('C',(44,38),(43,29),(44,33))])
        poly('pointer',(32,28),(40,22),(44,19))
        join('arch','pointer')
'''),
 'curved-gauge-indicator-solo-b017':('HRECT_M','Lucide gauge: coherent arch and a single straight diagonal pointer.','No scale ticks or numerals exist in source; retained crossing tick.', '''
        # Shared arch and pointer attachment; duplicate source, distinct claimed ID.
        path('arch',(4,38),[('C',(24,10),(4,22),(12,10)),('C',(40,22),(32,10),(37,15)),('C',(44,38),(43,29),(44,33))])
        poly('pointer',(32,28),(40,22),(44,19))
        join('arch','pointer')
'''),
 'diagonal-circular-refresh-arrows-batch-020-02':('SQUARE','Lucide refresh-cw: two smooth rotational arcs with open right-angle heads.','None; diagonal opposing arrow arrangement retained.', '''
        # Opposite halves derive by 180-degree rotation; shared radius and head length.
        for i in range(2):
            def p(x,y): return (x,y) if i==0 else (48-x,48-y)
            path(f'arc-{i}',p(6,24),[('A',p(24,6),18,18,True),('C',p(40,14),p(31,6),p(36,9))])
            poly(f'head-{i}',p(40,6),p(40,14),p(32,14))
            join(f'arc-{i}',f'head-{i}')
'''),
 'table-tennis-paddle-and-ball-solo-b016-r02':('SQUARE','Lucide coffee informed tangent contour transitions; no useful exact paddle match.','Rubber seam omitted to preserve paddle face opening; outlined handle and ball retained.', '''
        # Diagonal paddle: large rounded blade, neck, and capsule-ended handle.
        path('paddle',(18,24),[('C',(12,12),(10,22),(8,18)),('C',(26,6),(16,6),(22,6)),('C',(38,18),(34,6),(38,12)),('C',(24,28),(38,26),(32,28)),('L',(12,42)),('A',(6,36),6,6,True),('L',(18,24))],True)
        circle('ball',39,39,3)
'''),
 'couple-standing-with-hair':('SQUARE','Shared human_ref/full_body_ref.png: outlined round heads, open limbs, rounded dress.','Fringe removed at this scale; woman hair sides retained.', '''
        # Equivalent heads: r=5, bottom16; shoulders24 -> exact 4-unit ink gap.
        for who,x in [('man',13),('woman',35)]: circle(who+'-head',x,11,5)
        line('torso',(13,24),(13,32))
        poly('arms',(6,24),(13,24),(20,24))
        poly('legs',(6,42),(13,32),(20,42))
        join('arms','torso');join('legs','torso')
        self.mark_human_figure('man',head='man-head',torso='torso',torso_junction='start')
        path('dress',(35,24),[('C',(42,34),(38,24),(40,30)),('L',(39,34)),('L',(31,34)),('L',(28,34)),('C',(35,24),(30,30),(32,24))],True)
        for x in (31,39):
            line('leg-'+str(x),(x,34),(x,42));join('dress','leg-'+str(x))
        for x in (30,40):
            line('hair-'+str(x),(x,11),(x,16));join('woman-head','hair-'+str(x))
'''),
 'cow-head-wide-muzzle':('SQUARE','Lucide cat informed mirrored facial silhouette; cow reference owns horns, ears and muzzle.','Eyes and nostrils omitted because enclosed bands cannot hold marks with MIC 8.', '''
        # Shared axis24, mirrored horns and leaflike ears; broad capsule muzzle.
        path('face',(16,28),[('L',(16,16)),('L',(32,16)),('L',(32,28))])
        path('muzzle',(16,28),[('L',(32,28)),('A',(39,35),7,7,True),('A',(32,42),7,7,True),('L',(16,42)),('A',(9,35),7,7,True),('A',(16,28),7,7,True)],True)
        join('face','muzzle')
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            path('horn-'+str(side),p(18,6),[('A',p(8,16),10,10,side>0)])
            path('ear-'+str(side),p(8,16),[('L',p(18,16)),('A',p(8,26),10,10,side>0),('L',p(8,16))],True)
            join('face','horn-'+str(side));join('face','ear-'+str(side));join('horn-'+str(side),'ear-'+str(side))
'''),
 'dental-extraction-forceps-open-jaws':('SQUARE','Lucide wrench: open jaws and smoothly flowing tool shoulders.','Handle thickness simplified to two open curved strokes; retains asymmetric curved forceps.', '''
        # Two tool arms cross at a shared mechanical pivot; asymmetric hooked jaws.
        path('arm-front',(18,42),[('C',(30,24),(25,36),(30,30)),('C',(36,6),(28,15),(32,9))])
        path('arm-back',(6,34),[('C',(30,24),(13,26),(23,25)),('C',(42,10),(38,22),(42,18))])
        join('arm-front','arm-back')
'''),
 'crossed-double-wrenches':('SQUARE','Lucide wrench: rounded open jaws and broad diagonal shafts.','Rear shaft is occluded by the complete foreground tool; all four open jaws retained.', '''
        # Diagonal front tool: open curved jaws at opposing ends; rear is a half-turn pair.
        path('front',(30,6),[('A',(24,18),10,10,False),('L',(18,24)),('A',(6,30),10,10,False),('L',(6,36)),('L',(12,30)),('A',(18,36),6,6,True),('L',(12,42)),('L',(18,42)),('A',(24,30),10,10,False),('L',(30,24)),('A',(42,18),10,10,False),('L',(42,12)),('L',(36,18)),('A',(30,12),6,6,True),('L',(36,6)),('L',(30,6))],True)
        for i in range(2):
            def p(x,y):return (x,y) if i==0 else (48-x,48-y)
            path('rear-'+str(i),p(18,24),[('L',p(14,20)),('C',p(6,10),p(6,20),p(6,14)),('L',p(12,16)),('A',p(18,10),6,6,False),('L',p(14,6)),('C',p(24,18),p(22,6),p(26,10))])
            join('front','rear-'+str(i))
''')
}
for rec in records:
    key,ref,omit,body=designs[rec['icon_id']]
    module=Path(rec['run'])/(rec['icon_id'].replace('-','_')+'_'+rec['source_uuid'].replace('-','_')+'.py')
    module.write_text(f'''"""Revision for bad-stroke feedback. {ref}
Omissions: {omit}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {rec['source_uuid']!r}
SOURCE_PATH = {rec['reference_path']!r}
AUTHOR = {AUTHOR!r}
class Revision(Solo48):
    icon_id = {rec['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = {tuple(rec['concept'].split())!r}
    def build(self):
'''+HELPERS+body)
    rec.update(module=str(module),keyshape=key,construction_reference=ref,omissions=omit)
(ROOT/'claimed.json').write_text(json.dumps(records,indent=2)+'\n')
