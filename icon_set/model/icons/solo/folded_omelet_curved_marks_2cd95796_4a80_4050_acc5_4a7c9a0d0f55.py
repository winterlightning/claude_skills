"""Folded Breakfast Omelet.

Plan: Folded half oval omelet, diagonal fold and one broad surface curl; bounds4,8,44,40.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2cd95796-4a80-4050-acc5-4a7c9a0d0f55'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/omelet_2cd95796-4a80-4050-acc5-4a7c9a0d0f55.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'folded-omelet-curved-marks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('folded', 'omelet', 'curved', 'marks')

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

        path('omelet',(8,22),[('L',(36,8)),('C',(44,16),(42,8),(44,8)),('C',(22,40),(44,30),(34,40)),('C',(4,28),(10,40),(4,34)),('C',(8,22),(4,25),(6,23))],True)
        path('fold',(18,29),[('C',(28,29),(20,31),(26,31))])
