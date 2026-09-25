"""Safety Helmet Production Line.

Plan: Retained the hard-hat dome, central ridge and broad brim above a three-roller conveyor. The three small roller rings become dots; the conveyor is taller for safe spacing.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8256681c-9841-4460-b2bb-7c6258a0835b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/product helmet_8256681c-9841-4460-b2bb-7c6258a0835b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hard-hat-above-roller-conveyor'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hard', 'hat', 'above', 'roller', 'conveyor')

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

        path('dome',(15,15),[('A',(24,6),9,9,True),('A',(33,15),9,9,True)])
        poly('brim',(6,15),(15,15),(33,15),(42,15));join('brim','dome');line('ridge',(24,6),(24,15));join('ridge','dome');join('ridge','brim')
        rect('conveyor',6,24,36,18,6)
        for x in (15,24,33):self.add_dot('roller-'+str(x),(x,33))
