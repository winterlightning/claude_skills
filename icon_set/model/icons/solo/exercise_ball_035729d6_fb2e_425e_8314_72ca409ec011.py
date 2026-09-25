"""A large circular exercise ball is divided by two sweeping curved surface lines. The curves run from the upper edge toward the lower left, suggesting the round volume of the ball.

Circular envelope and two broad sweeping seams retained; seams use shared radii and opposite placements to suggest volume.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '035729d6-fb2e-425e-8314-72ca409ec011'
SOURCE_PATH = 'pictographic-primitives/sports/pilates ball_035729d6-fb2e-425e-8314-72ca409ec011.svg'
AUTHOR = 'gpt-6'

class ExerciseBall(Solo48):
    icon_id = 'exercise-ball'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('ball', 'pilates', 'exercise', 'fitness', 'equipment', 'training')

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
        pts=[(24,4),(44,24),(24,44),(4,24)]
        for i in range(4):self.add_arc(f'ball-{i}',pts[i],pts[(i+1)%4],radius_x=20)
        self.add_contour('ball',*[f'ball-{i}' for i in range(4)],closed=True)
        self.add_arc('upper-seam',(24,4),(4,24),radius_x=20)
        self.add_arc('lower-seam',(44,24),(24,44),radius_x=20,sweep=False)
        for a,bs in [('upper-seam',[0,2,3]),('lower-seam',[0,1,2])]:
         for b in bs:self.relate('connect',a,f'ball-{b}')
