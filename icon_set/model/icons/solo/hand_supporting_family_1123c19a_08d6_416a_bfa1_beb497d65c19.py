"""family hold.
Two adults and a smaller child sit over a curved supporting palm.
Horizontal family group; asymmetric palm curve. Adult head bottom14 to shoulder22 and child bottom18 to shoulder26 each give 4 ink clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1123c19a-08d6-416a-bfa1-beb497d65c19'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/family hold_1123c19a-08d6-416a-bfa1-beb497d65c19.svg'
AUTHOR = 'gpt-6'

class HandSupportingFamily(Solo48):
    icon_id = 'hand-supporting-family'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('Hand Supporting Family',)
    keywords = tuple('hand supporting family'.split())

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
        # Human user.svg: head and shoulders with exact detached gap.
        for x in (10,38):
            self.ring('head-'+str(x),x,11,3)
            self.add_arc('body-'+str(x),(x-4,26),(x+4,26),radius_x=4)
        self.ring('child',24,16,2)
        self.add_arc('child-body',(22,28),(26,28),radius_x=2)
        self.add_bezier('palm',(4,36),((14,36),(18,40),(26,40)),((32,40),(38,36),(44,34)))

# Repair plan: Two adults and a smaller child sit over a curved supporting palm.
# Omissions: Wrist cuff and separate fingers omitted.
# Construction references: human_ref/user.svg: circular heads and open shoulders.
# Keyshape and proportions: Horizontal family group; asymmetric palm curve. Adult head bottom14 to shoulder22 and child bottom18 to shoulder26 each give 4 ink clearance.
