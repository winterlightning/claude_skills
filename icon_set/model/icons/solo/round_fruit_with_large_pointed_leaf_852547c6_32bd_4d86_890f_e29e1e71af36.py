"""Round Fruit with Leaf.

Plan: Round fruit beneath rightward leaf; bounds8,4,40,44. Leaf vein omitted.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '852547c6-32bd-4d86-890f-e29e1e71af36'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/currant_852547c6-32bd-4d86-890f-e29e1e71af36.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-fruit-with-large-pointed-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('round', 'fruit', 'with', 'large', 'pointed', 'leaf')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('fruit',(24,22),[('C',(40,33),(34,22),(40,26)),('C',(24,44),(40,40),(32,44)),('C',(8,33),(16,44),(8,40)),('C',(24,22),(8,26),(14,22))],True)
        line('stem',(24,22),(24,12));join('stem','fruit')
        path('leaf',(24,12),[('C',(40,4),(24,4),(32,4)),('C',(24,12),(40,12),(34,12))],True);join('stem','leaf')
