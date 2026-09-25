"""face woozy.
Open circular face, uneven mouth and closed eyes; a six-ray asterisk preserves the floating-star cue.
Square fits face and floating star; intentional facial asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fe974dc7-4d81-41d1-9dba-73ed68ac785f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/face woozy_fe974dc7-4d81-41d1-9dba-73ed68ac785f.svg'
AUTHOR = 'gpt-6'

class WoozyFaceFloatingStar(Solo48):
    icon_id = 'woozy-face-floating-star'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('Woozy Face with Floating Star',)
    keywords = tuple('woozy face with floating star'.split())

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
        self.add_arc('face-ne',(24,6),(42,24),radius_x=18)
        self.add_arc('face-se',(42,24),(24,42),radius_x=18)
        self.add_arc('face-sw',(24,42),(6,24),radius_x=18)
        self.add_contour('face','face-ne','face-se','face-sw')
        for x in (18,30):
            self.add_arc('eye-'+str(x),(x-2,19),(x+2,19),radius_x=2,sweep=False)
        self.add_polyline('mouth',(18,31),(22,29),(26,31),(30,29))
        self.add_polyline('star-h',(6,9),(9,9),(12,9))
        self.add_polyline('star-d1',(8,6),(9,9),(10,12))
        self.add_polyline('star-d2',(8,12),(9,9),(10,6))
        self.relate('connect','star-h','star-d1')
        self.relate('connect','star-h','star-d2')
        self.relate('connect','star-d1','star-d2')

# Repair plan: Open circular face, uneven mouth and closed eyes; a six-ray asterisk preserves the floating-star cue.
# Omissions: Five-point star outline reduced to six rays; face upper-left arc opened.
# Construction references: No useful local Lucide smile match.
# Keyshape and proportions: Square fits face and floating star; intentional facial asymmetry.
