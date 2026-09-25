"""A curved bow carries a horizontal arrow pointing right.

Kept the bow and arrow as one physical archery subject. No string was present in the reference.
Lucide bow-arrow informed a coherent curved bow and straight arrow; source keeps its horizontal orientation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9765457f-3e30-4835-b25c-e413e4bbcd41'
SOURCE_PATH = 'pictographic-primitives/sports/archery_9765457f-3e30-4835-b25c-e413e4bbcd41.svg'
AUTHOR = 'gpt-6'

class ArcheryBowAndArrow(Solo48):
    icon_id = 'archery-bow-and-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('archery', 'bow', 'and', 'arrow')

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
        # A curved bow carries a horizontal arrow pointing right.
        self.add_arc('bow-upper',(6,6),(24,24),radius_x=18)
        self.add_arc('bow-lower',(24,24),(6,42),radius_x=18)
        self.add_contour('bow','bow-upper','bow-lower')
        self.skeleton([('shaft',[(6,24),(24,24),(42,24)]),('arrowhead',[(34,16),(42,24),(34,32)])])
        for bow in ['bow-upper','bow-lower']:
            for shaft in ['shaft-0','shaft-1']:self.relate('connect',bow,shaft)
