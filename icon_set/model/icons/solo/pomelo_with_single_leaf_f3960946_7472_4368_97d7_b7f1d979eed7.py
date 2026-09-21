"""Pomelo Fruit with Leaf.

Plan: Pomelo body below a single right-pointing leaf, bounds8,4,40,44. Integrate stem to the body; broad asymmetric leaf retained.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3960946-7472-4368-97d7-b7f1d979eed7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pomelo_f3960946-7472-4368-97d7-b7f1d979eed7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pomelo-with-single-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('pomelo', 'with', 'single', 'leaf')

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

        path('fruit',(24,21),[('C',(40,30),(32,21),(40,23)),('C',(24,44),(40,38),(33,44)),('C',(8,30),(15,44),(8,38)),('C',(24,21),(8,23),(16,21))],True)
        line('stem',(24,21),(24,12));join('stem','fruit')
        path('leaf',(24,12),[('C',(40,4),(24,4),(32,4)),('C',(24,12),(38,12),(31,12))],True);join('stem','leaf')
