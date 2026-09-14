"""A jump rope arches upward between two matching vertical handles. The long cord forms a smooth inverted U, and both cylindrical handles have softly rounded lower ends.

Mirrored capsule handles and a single continuous arched cord retained.
Inspected source rendering; Lucide bike, sword, dumbbell and person-standing informed sparse equipment and figure construction where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b5a83f3a-1a7a-57ff-a828-af1aa4d4eb1f'
SOURCE_PATH = 'pictographic-primitives/sports/fitness jumping rope_b5a83f3a-1a7a-57ff-a828-af1aa4d4eb1f.svg'
AUTHOR = "gpt-6"

class JumpRope(Solo48):
    icon_id = 'jump-rope'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('rope', 'skipping', 'jump', 'fitness', 'exercise', 'equipment')

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
        self.add_line('cord-left',(10,26),(10,20))
        self.add_arc('cord-top',(10,20),(38,20),radius_x=14)
        self.add_line('cord-right',(38,20),(38,26))
        self.add_contour('cord','cord-left','cord-top','cord-right')
        for name,x in [('left',10),('right',38)]:
         self.add_arc(name+'-a',(x-4,30),(x,26),radius_x=4)
         self.add_arc(name+'-b',(x,26),(x+4,30),radius_x=4)
         self.add_line(name+'-c',(x+4,30),(x+4,38))
         self.add_arc(name+'-d',(x+4,38),(x-4,38),radius_x=4)
         self.add_line(name+'-e',(x-4,38),(x-4,30))
         self.add_contour(name,*[name+'-'+c for c in 'abcde'],closed=True)
         for part in ['a','b']:self.relate('connect','cord-'+name,name+'-'+part)
