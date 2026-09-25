"""Protective Safety Goggles.

Plan: Safety goggles bounds4,10,44,38. Broad outer rim with nose notch and a separate lens contour; retain open lower rim.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21eee887-28cb-4e25-b739-4d7134cd9a28'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/safety goggles_21eee887-28cb-4e25-b739-4d7134cd9a28.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wraparound-safety-goggles'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wraparound', 'safety', 'goggles')

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

        path('rim',(14,38),[('L',(10,38)),('A',(4,32),6,6,True),('L',(4,18)),('A',(12,10),8,8,True),('L',(36,10)),('A',(44,18),8,8,True),('L',(44,32)),('A',(38,38),6,6,True),('L',(34,38))])
        path('lens',(13,19),[('L',(35,19)),('L',(35,29)),('L',(29,29)),('L',(24,24)),('L',(19,29)),('L',(13,29)),('L',(13,19))],True)
