"""A fingertip reaches a selection target below a chevron.

SOLO48 VRECT_L; Lucide reference: pointer: finger silhouette and touch target.
Symbol plan: source composition reduced to named outlines and shared geometry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b5fa4080-f0f6-4340-bf42-bbc85e2598c9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_19/finger tap_b5fa4080-f0f6-4340-bf42-bbc85e2598c9.svg'
AUTHOR = 'gpt-6'

class FingerTapSelectionGesture(Solo48):
    icon_id = 'finger-tap-selection-gesture'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'gestures/touch'
    aliases = ('Finger Tap Selection Gesture',)
    keywords = tuple('finger tap selection gesture'.split())

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
        self.add_polyline('chevron',(16,4),(24,12),(32,4))
        self.add_arc('tap-arch',(8,29),(24,21),radius_x=16,radius_y=14,sweep=True)
        self.add_arc('tap-arch-right',(24,21),(40,29),radius_x=16,radius_y=14,sweep=True)
        self.add_arc('finger-tip',(20,34),(28,34),radius_x=4,sweep=True)
        self.add_line('finger-left',(20,34),(20,44))
        self.add_line('finger-right',(28,34),(28,44))
