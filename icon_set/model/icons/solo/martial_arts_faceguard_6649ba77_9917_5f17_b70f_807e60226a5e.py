"""An oval protective mask has a thick outer rim surrounding a face grille of horizontal bars and a central vertical divider. Two broad protective flaps spread from its lower sides.

Oval rim, central grille cross and two protective flaps retained; fine horizontal bars reduced to one broad divider.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6649ba77-9917-5f17-b70f-807e60226a5e'
SOURCE_PATH = 'pictographic-primitives/sports/martial arts mask helmet_6649ba77-9917-5f17-b70f-807e60226a5e.svg'
AUTHOR = 'gpt-6'

class MartialArtsFaceguard(Solo48):
    icon_id = 'martial-arts-faceguard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('mask', 'helmet', 'martial', 'fencing', 'protection', 'headgear')

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
        self.add_arc('tl',(24,6),(12,18),radius_x=12,sweep=False)
        self.add_line('left-upper',(12,18),(12,20));self.add_line('left-lower',(12,20),(12,22))
        self.add_arc('bl',(12,22),(24,34),radius_x=12,sweep=False)
        self.add_arc('br',(24,34),(36,22),radius_x=12,sweep=False)
        self.add_line('right-lower',(36,22),(36,20));self.add_line('right-upper',(36,20),(36,18))
        self.add_arc('tr',(36,18),(24,6),radius_x=12,sweep=False)
        self.add_contour('rim','tl','left-upper','left-lower','bl','br','right-lower','right-upper','tr',closed=True)
        self.skeleton([('vertical',[(24,6),(24,20),(24,34)]),('horizontal',[(12,20),(24,20),(36,20)]),('left-flap',[(12,22),(6,34),(14,42),(24,34)]),('right-flap',[(36,22),(42,34),(34,42),(24,34)])])
        for a,bs in [('vertical-0',['tl','tr']),('vertical-1',['bl','br']),('horizontal-0',['left-upper','left-lower']),('horizontal-1',['right-lower','right-upper']),('left-flap-0',['left-lower','bl']),('left-flap-2',['bl','br']),('right-flap-0',['right-lower','br']),('right-flap-2',['bl','br'])]:
         for b in bs:self.relate('connect',a,b)
