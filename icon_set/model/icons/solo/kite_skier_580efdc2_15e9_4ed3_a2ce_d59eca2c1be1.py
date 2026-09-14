"""A skier leans back on two short upturned skis while reaching toward a kite above the right side. An angular tether connects the hands to the curved triangular kite.

Curved kite, tether, leaning skier and upturned ski end retained. The overlapping skis use one shared silhouette; extra rigging is omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '580efdc2-15e9-4ed3-a2ce-d59eca2c1be1'
SOURCE_PATH = 'pictographic-primitives/sports/kite skiing_580efdc2-15e9-4ed3-a2ce-d59eca2c1be1.svg'
AUTHOR = 'gpt-6'

class KiteSkier(Solo48):
    icon_id = 'kite-skier'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('kite', 'skiing', 'skier', 'snow', 'wind', 'sport')

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skeleton(self,branches):
        parts=[]
        for name,points in branches:
            members=[]
            for index,(a,b) in enumerate(zip(points,points[1:])):
                key=f'{name}-{index}';members.append(key)
                self.add_line(key,a,b);parts.append((key,a,b))
            if len(members)>1:self.add_contour(name,*members)
        for index,(a,p,q) in enumerate(parts):
            for b,r,s in parts[index+1:]:
                if p in (r,s) or q in (r,s):self.relate('connect',a,b)

    def rounded(self,name,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for index,a in enumerate(pts):
            b=pts[(index+1)%8];key=f'{name}-{index}';members.append(key)
            if index%2:self.add_arc(key,a,b,radius_x=r)
            else:self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def weight(self,name,x,y,w,h,r):
        # Expose bar attachment nodes at the midpoint of each vertical wall.
        middle=y+h//2
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,middle),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,middle),(x,y+r)]
        members=[]
        for index,a in enumerate(pts):
            b=pts[(index+1)%len(pts)];key=f'{name}-{index}';members.append(key)
            if index in [1,4,6,9]:self.add_arc(key,a,b,radius_x=r)
            else:self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        self.add_arc('kite-canopy',(26,6),(42,22),radius_x=16)
        self.add_polyline('kite-edges',(42,22),(26,22),(26,6))
        self.relate('connect','kite-canopy','kite-edges-1');self.relate('connect','kite-canopy','kite-edges-2')
        self.circle('head',9,18,3)
        self.skeleton([('tether',[(26,22),(18,28),(14,30)]),('body',[(14,30),(10,34)]),('left-leg',[(10,34),(10,42)]),('right-leg',[(10,34),(18,36),(20,42)]),('skis',[(6,42),(10,42),(20,42),(26,42),(30,38)])])
        for a in ['kite-edges-1','kite-edges-2']:self.relate('connect','tether-0',a)
