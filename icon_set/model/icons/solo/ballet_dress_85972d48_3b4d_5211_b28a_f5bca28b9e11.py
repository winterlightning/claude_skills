"""A sleeveless ballet dress has narrow shoulder straps, a notched neckline, and a fitted waist. The skirt spreads broadly into a tutu with a softly scalloped lower hem.

Kept straps, notched neckline, fitted waist and a flared tutu. Reduced the many small hem lobes to three shared broad scallops.
Source dress silhouette; Lucide shirt informed one coherent garment outline and deliberate neckline corners.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85972d48-3b4d-5211-b28a-f5bca28b9e11'
SOURCE_PATH = 'pictographic-primitives/sports/dancing ballet dress_85972d48-3b4d-5211-b28a-f5bca28b9e11.svg'
AUTHOR = 'gpt-6'

class BalletDress(Solo48):
    icon_id = 'ballet-dress'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('ballet', 'dress', 'tutu', 'dance', 'costume', 'garment')

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
        self.add_polyline('bodice',(16,12),(24,18),(32,12),(36,18),(32,28),(16,28),(12,18),closed=True)
        self.add_line('left-strap',(16,6),(16,12))
        self.add_line('right-strap',(32,6),(32,12))
        for part in ['bodice-1','bodice-7']:self.relate('connect','left-strap',part)
        for part in ['bodice-2','bodice-3']:self.relate('connect','right-strap',part)
        self.add_line('skirt-left',(16,28),(6,38))
        for i,x in enumerate([6,18,30]):self.add_arc(f'hem-{i}',(x,38),(x+12,38),radius_x=6,radius_y=4,sweep=False)
        self.add_line('skirt-right',(42,38),(32,28))
        self.add_contour('skirt','skirt-left','hem-0','hem-1','hem-2','skirt-right')
        for part in ['bodice-5','bodice-6']:self.relate('connect','skirt-left',part)
        for part in ['bodice-4','bodice-5']:self.relate('connect','skirt-right',part)
