"""Safety Ear Protection Plug.

Plan: Diagonal earplug with broad cap and rounded narrow stem; bounds6,6,42,42.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa80ee75-79eb-4074-ab4b-851ef4258d0a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/earplug_aa80ee75-79eb-4074-ab4b-851ef4258d0a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tapered-earplug-with-narrow-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tapered', 'earplug', 'with', 'narrow', 'stem')

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

        path('cap',(16,22),[('L',(30,8)),('C',(36,6),(32,6),(34,6)),('C',(42,12),(40,6),(42,8)),('C',(40,18),(42,14),(41,16)),('L',(30,36)),('L',(26,32)),('L',(20,26)),('L',(16,22))],True)
        path('stem',(20,26),[('L',(8,34)),('C',(6,38),(6,36),(6,37)),('C',(10,42),(6,40),(8,42)),('C',(14,40),(12,42),(13,41)),('L',(26,32))]);join('stem','cap')
