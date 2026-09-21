"""Real Leather Material Symbol.

Plan: Mirror hide outline aroundx24; scalloped top, concave flanks, pointed tail. Bounds6,6,42,42.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e537b18e-1a15-4e6d-99de-df2190456dec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pelt_e537b18e-1a15-4e6d-99de-df2190456dec.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spread-leather-hide'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('spread', 'leather', 'hide')

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

        path('hide',(18,6),[('L',(30,6)),('C',(42,12),(32,16),(36,12)),('C',(42,36),(32,20),(32,28)),('C',(24,42),(32,32),(28,34)),('C',(6,36),(20,34),(16,32)),('C',(6,12),(16,28),(16,20)),('C',(18,6),(12,12),(16,16))],True)
