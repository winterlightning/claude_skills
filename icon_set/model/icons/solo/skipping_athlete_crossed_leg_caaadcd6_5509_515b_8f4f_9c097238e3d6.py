"""A front-facing figure holds both ends of a jump rope near hip height. One leg lifts across the other while the rope forms a rounded loop beneath the body.

Broad rope loop and paired hands retained; compact joined limbs distinguish the lifted knee and inward bent leg poses.
Inspected source rendering; Lucide bike, sword, dumbbell and person-standing informed sparse equipment and figure construction where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'caaadcd6-5509-515b-8f4f-9c097238e3d6'
SOURCE_PATH = 'pictographic-primitives/sports/fitness jumping rope_caaadcd6-5509-515b-8f4f-9c097238e3d6.svg'
AUTHOR = "gpt-6"

class SkippingAthleteCrossedLeg(Solo48):
    icon_id = 'skipping-athlete-crossed-leg'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('skipping', 'rope', 'jumping', 'athlete', 'fitness', 'exercise')

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
        self.circle('head',24,9,3)
        branches=[('torso',[(24,21),(24,27)]),('left-arm',[(24,21),(15,20),(6,22)]),('right-arm',[(24,21),(33,20),(42,22)])]
        branches+=[('left-leg',[(24,27),(26,32)]),('right-leg',[(24,27),(19,31),(22,32)])]
        self.skeleton(branches)
        self.add_arc('rope',(6,22),(42,22),radius_x=18,radius_y=20,sweep=False)
        for a in ['left-arm-1','right-arm-1']:self.relate('connect','rope',a)
