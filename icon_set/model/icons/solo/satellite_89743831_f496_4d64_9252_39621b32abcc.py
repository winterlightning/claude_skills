"""Parabolic dish with a diagonal rim, round feed receiver and triangular pedestal. SQUARE centerlines (6,6)-(42,42). A fuller continuous bowl replaces the flattened earlier dish."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '89743831-f496-4d64-9252-39621b32abcc'
SOURCE_PATH = 'pictographic-primitives/tv/satellite_89743831-f496-4d64-9252-39621b32abcc.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='satellite-dish: diagonal bowl and receiver arm'
DESIGN_PLAN='Parabolic dish with a diagonal rim, round feed receiver and triangular pedestal. SQUARE centerlines (6,6)-(42,42). A fuller continuous bowl replaces the flattened earlier dish.'
OMISSIONS='Fine receiver support frame reduced to one arm.'
class Drawing(Solo48):
    icon_id='satellite'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'tv'
    categories = ('tv', 'primitives')
    aliases=()
    keywords=('satellite',)
    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            member=f'{name}-{i}'
            if kind=='L': self.add_line(member,start,end)
            elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
            members.append(member); start=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,cx,cy,r):
        self.path(name,(cx-r,cy),[('A',(cx,cy-r),r,r,True),('A',(cx+r,cy),r,r,True),('A',(cx,cy+r),r,r,True),('A',(cx-r,cy),r,r,True)],True)



    def build(self):
        self.path('dish',(12,6),[('L',(24,18)),('L',(42,36)),('C',(26,36),(37,39),(31,38)),('C',(12,28),(20,34),(15,32)),('C',(6,18),(8,24),(6,22)),('C',(12,6),(6,13),(9,8))],True)
        self.add_polyline('pedestal',(12,28),(6,42),(30,42),(26,36));self.relate('connect','pedestal','dish')
        self.add_line('feed',(24,18),(34,10));self.relate('connect','feed','dish')
        self.circle('receiver',38,10,4);self.relate('connect','feed','receiver')
