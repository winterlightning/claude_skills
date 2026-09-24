"""An ear listening to two sound waves.

SOLO48 VRECT_L; Lucide reference: ear: outer curve and inner fold.
Symbol plan: source composition reduced to named outlines and shared geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4317946e-a563-47b7-9c3d-e830b878ecc6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/ear listen_4317946e-a563-47b7-9c3d-e830b878ecc6.svg'
AUTHOR = 'gpt-6'

class EarWithSoundWaves(Solo48):
    icon_id = 'ear-with-sound-waves-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'senses/hearing'
    aliases = ('Ear with Sound Waves',)
    keywords = tuple('ear with sound waves'.split())

    def ring(self, name, x, y, r):
        self.add_arc(name+'-ne',(x,y-r),(x+r,y),radius_x=r,sweep=True)
        self.add_arc(name+'-se',(x+r,y),(x,y+r),radius_x=r,sweep=True)
        self.add_arc(name+'-sw',(x,y+r),(x-r,y),radius_x=r,sweep=True)
        self.add_arc(name+'-nw',(x-r,y),(x,y-r),radius_x=r,sweep=True)
        self.add_contour(name,*(name+'-'+s for s in ('ne','se','sw','nw')),closed=True)

    def box(self, name, x1, y1, x2, y2):
        self.add_polyline(name,(x1,y1),(x2,y1),(x2,y2),(x1,y2),closed=True)

    def round_box(self, name, x1, y1, x2, y2, r):
        parts=[]
        def line(s,a,b):
            n=name+'-'+s; self.add_line(n,a,b); parts.append(n)
        def arc(s,a,b):
            n=name+'-'+s; self.add_arc(n,a,b,radius_x=r,sweep=True); parts.append(n)
        line('top',(x1+r,y1),(x2-r,y1))
        arc('ne',(x2-r,y1),(x2,y1+r))
        line('right',(x2,y1+r),(x2,y2-r))
        arc('se',(x2,y2-r),(x2-r,y2))
        line('bottom',(x2-r,y2),(x1+r,y2))
        arc('sw',(x1+r,y2),(x1,y2-r))
        line('left',(x1,y2-r),(x1,y1+r))
        arc('nw',(x1,y1+r),(x1+r,y1))
        self.add_contour(name,*parts,closed=True)

    def heart(self,name,x,y):
        self.add_arc(name+'-left',(x,y-2),(x-6,y-4),radius_x=4,radius_y=4,sweep=False)
        self.add_arc(name+'-left-side',(x-6,y-4),(x-6,y+2),radius_x=4,radius_y=4,sweep=False)
        self.add_line(name+'-left-tip',(x-6,y+2),(x,y+8))
        self.add_line(name+'-right-tip',(x,y+8),(x+6,y+2))
        self.add_arc(name+'-right-side',(x+6,y+2),(x+6,y-4),radius_x=4,radius_y=4,sweep=False)
        self.add_arc(name+'-right',(x+6,y-4),(x,y-2),radius_x=4,radius_y=4,sweep=False)
        self.add_contour(name,*(name+s for s in ('-left','-left-side','-left-tip','-right-tip','-right-side','-right')),closed=True)

    def build(self) -> None:
        self.add_arc('ear-crown',(8,22),(26,6),radius_x=16,radius_y=16,sweep=True)
        self.add_arc('ear-back',(26,6),(33,31),radius_x=17,radius_y=17,sweep=True)
        self.add_polyline('ear-lobe',(33,31),(27,42),(20,42),(16,37))
        self.add_arc('inner',(17,27),(25,20),radius_x=8,sweep=False)
        self.add_arc('wave-one',(37,17),(37,31),radius_x=7,sweep=True)
        self.add_arc('wave-two',(42,12),(42,36),radius_x=12,sweep=True)
