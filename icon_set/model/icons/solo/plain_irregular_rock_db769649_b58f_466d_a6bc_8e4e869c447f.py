"""Simple Irregular Rock Shape.

Plan: Irregular rounded rock outline retained with a shallow crown and broad lower edge; interior stays empty. Keyshape SQUARE uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db769649-b58f-466d-a6bc-8e4e869c447f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/rock_db769649-b58f-466d-a6bc-8e4e869c447f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-irregular-rock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('plain', 'irregular', 'rock')

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

        path('rock',(24,6),[('C',(34,10),(27,6),(31,8)),('C',(38,16),(37,12),(37,13)),('L',(42,28)),('C',(39,35),(42,31),(40,33)),('L',(36,39)),('C',(30,42),(34,42),(33,42)),('L',(16,41)),('C',(11,38),(13,41),(12,40)),('L',(7,31)),('C',(6,27),(6,30),(6,29)),('C',(8,20),(6,25),(7,22)),('L',(11,13)),('C',(15,10),(12,11),(13,11)),('C',(24,6),(19,8),(21,6))],True)
