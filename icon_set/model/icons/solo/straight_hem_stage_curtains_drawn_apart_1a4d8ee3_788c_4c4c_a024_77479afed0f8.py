'Two tall curtains hang from a shared straight top edge and gather toward opposite sides at mid height. Curving inner edges open onto a blank center above straight horizontal lower hems.\nPlan: Paired stage curtains gathering at the sides; smooth opposing curves from a shared top rail. Remove inner fold lines.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a4d8ee3-788c-4c4c-a024-77479afed0f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/curtain_1a4d8ee3-788c-4c4c-a024-77479afed0f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'straight-hem-stage-curtains-drawn-apart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('straight', 'hem', 'stage', 'curtains', 'drawn', 'apart')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        path('left',(6,6),[('L',(20,6)),('C',(6,28),(20,19),(15,25)),('C',(16,42),(14,29),(16,36)),('L',(6,42)),('L',(6,6))],True)
        path('right',(42,6),[('L',(28,6)),('C',(42,28),(28,19),(33,25)),('C',(32,42),(34,29),(32,36)),('L',(42,42)),('L',(42,6))],True)
        line('rail',(20,6),(28,6));join('rail','left');join('rail','right')
