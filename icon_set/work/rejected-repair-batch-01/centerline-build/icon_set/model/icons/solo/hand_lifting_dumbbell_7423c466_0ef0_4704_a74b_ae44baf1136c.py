"""An upright forearm ends in a fist wrapped around the center of a horizontal dumbbell. Four rounded knuckles sit above the grip, between two tall rectangular end weights.

Kept the fist wrapped around a horizontal dumbbell and the upright forearm. Merged four knuckles into a rounded crown; simplified end weights to strokes to leave hand clearance.
Source gripping hand; Lucide dumbbell informed bilateral end weights and the shared grip axis.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7423c466-0ef0-4704-a74b-ae44baf1136c'
SOURCE_PATH = 'pictographic-primitives/sports/dumbbell lift_7423c466-0ef0-4704-a74b-ae44baf1136c.svg'
AUTHOR = 'gpt-6'

class HandLiftingDumbbell(Solo48):
    icon_id = 'hand-lifting-dumbbell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('dumbbell', 'hand', 'lifting', 'strength', 'fitness', 'weight')

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
        self.skeleton([
         ('left-weight',[(6,6),(6,18),(6,26)]),
         ('right-weight',[(42,6),(42,18),(42,26)]),
         ('left-bar',[(6,18),(16,18)]),
         ('right-bar',[(32,18),(42,18)])])
        points=[(16,42),(19,28),(16,22),(16,18),(16,16)]
        for i,(a,b) in enumerate(zip(points,points[1:])):self.add_line(f'hand-left-{i}',a,b)
        self.add_arc('knuckles-left',(16,16),(20,12),radius_x=4)
        self.add_line('knuckles',(20,12),(28,12))
        self.add_arc('knuckles-right',(28,12),(32,16),radius_x=4)
        points=[(32,16),(32,18),(32,22),(29,28),(32,42)]
        for i,(a,b) in enumerate(zip(points,points[1:])):self.add_line(f'hand-right-{i}',a,b)
        self.add_contour('hand',*[f'hand-left-{i}' for i in range(4)],'knuckles-left','knuckles','knuckles-right',*[f'hand-right-{i}' for i in range(4)])
        for part in ['hand-left-2','hand-left-3']:self.relate('connect','left-bar-0',part)
        for part in ['hand-right-0','hand-right-1']:self.relate('connect','right-bar-0',part)
