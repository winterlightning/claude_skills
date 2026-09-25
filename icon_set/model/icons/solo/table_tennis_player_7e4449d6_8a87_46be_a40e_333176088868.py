"""An athlete leans toward a table edge on the right, holding a small oval paddle in a bent forward arm. A small ball hangs just above the table beside the player.

Held paddle, small airborne ball and cropped table edge retained. Table is deliberately abbreviated, with a single supporting leg.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7e4449d6-8a87-46be-a40e-333176088868'
SOURCE_PATH = 'pictographic-primitives/sports/ping pong player_7e4449d6-8a87-46be-a40e-333176088868.svg'
AUTHOR = 'gpt-6'

class TableTennisPlayer(Solo48):
    icon_id = 'table-tennis-player'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('table', 'tennis', 'paddle', 'player', 'ball', 'sport')

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
        self.circle('head',16,9,3)
        self.add_arc('paddle-right',(32,11),(32,19),radius_x=4)
        self.add_arc('paddle-left',(32,19),(32,11),radius_x=4)
        self.add_contour('paddle','paddle-right','paddle-left',closed=True)
        self.circle('ball',40,27,2)
        self.skeleton([('body',[(18,22),(16,32)]),('left-arm',[(18,22),(10,22),(6,28)]),('playing-arm',[(18,22),(26,26),(32,19)]),('left-leg',[(16,32),(6,42)]),('right-leg',[(16,32),(24,36),(22,42)]),('table',[(34,38),(38,38),(42,38)]),('table-leg',[(38,38),(38,42)])])
        for a in ['paddle-right','paddle-left']:self.relate('connect','playing-arm-1',a)
