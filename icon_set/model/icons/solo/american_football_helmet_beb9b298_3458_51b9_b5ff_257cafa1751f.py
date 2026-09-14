"""A side-view football helmet has a rounded shell, ear opening and projecting face guard.

Kept shell, ear opening and an open face-guard contour with real attachment points.
Source shell and guard; quarter-circle construction, with no useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'beb9b298-3458-51b9-b5ff-257cafa1751f'
SOURCE_PATH = 'pictographic-primitives/sports/american football helmet_beb9b298-3458-51b9-b5ff-257cafa1751f.svg'
AUTHOR = 'gpt-6'

class AmericanFootballHelmet(Solo48):
    icon_id = 'american-football-helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('american', 'football', 'helmet')

    def circle(self, name, x, y, radius):
        self.add_arc(name+'-top',(x-radius,y),(x+radius,y),radius_x=radius)
        self.add_arc(name+'-bottom',(x+radius,y),(x-radius,y),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skeleton(self, branches):
        # Declare only actual shared endpoints in the physical figure.
        segments=[]
        for name,points in branches:
            for index,(a,b) in enumerate(zip(points,points[1:])):
                key=f'{name}-{index}'
                self.add_line(key,a,b);segments.append((key,a,b))
            if len(points)>2:self.add_contour(name,*[f'{name}-{i}' for i in range(len(points)-1)])
        for index,(a,p,q) in enumerate(segments):
            for b,r,s in segments[index+1:]:
                if p in (r,s) or q in (r,s):self.relate('connect',a,b)

    def oval(self,name,x,y,rx,ry):
        self.add_arc(name+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self):
        # A side-view football helmet has a rounded shell, ear opening and projecting face guard.
        self.add_arc('shell-dome',(6,26),(40,26),radius_x=18)
        self.add_line('brow',(40,26),(28,26))
        self.add_line('jaw-upper',(28,26),(28,30))
        self.add_line('jaw-lower',(28,30),(28,34))
        self.add_arc('chin',(28,34),(22,40),radius_x=6)
        self.add_line('base',(22,40),(8,40))
        self.add_arc('back-corner',(8,40),(6,36),radius_x=4)
        self.add_line('back',(6,36),(6,26))
        self.add_contour('shell','shell-dome','brow','jaw-upper','jaw-lower','chin','base','back-corner','back',closed=True)
        self.circle('ear',16,28,3)
        self.add_polyline('guard',(40,26),(42,26),(42,40),(38,40))
        self.add_arc('guard-return',(38,40),(28,30),radius_x=10)
        self.relate('connect','guard-3','guard-return')
        for part in ['brow','shell-dome']:self.relate('connect','guard-1',part)
        for part in ['jaw-upper','jaw-lower']:self.relate('connect','guard-return',part)
