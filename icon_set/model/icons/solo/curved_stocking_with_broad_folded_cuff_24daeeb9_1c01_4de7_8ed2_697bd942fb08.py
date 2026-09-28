"""Festive Christmas Stocking.

Plan: Stocking with broad folded cuff and rounded left-pointing toe, bounds8,4,40,44. Omit heel patch to keep broad foot opening.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24daeeb9-1c01-4de7-8ed2-697bd942fb08'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stocking_24daeeb9-1c01-4de7-8ed2-697bd942fb08.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-stocking-with-broad-folded-cuff'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('curved', 'stocking', 'with', 'broad', 'folded', 'cuff')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        poly('cuff',(20,4),(40,4),(40,14),(20,14),closed=True)
        path('sock',(20,14),[('L',(20,24)),('C',(8,36),(20,29),(8,28)),('A',(16,44),8,8,False),('C',(40,28),(26,44),(40,36)),('L',(40,14))]);join('sock','cuff')
