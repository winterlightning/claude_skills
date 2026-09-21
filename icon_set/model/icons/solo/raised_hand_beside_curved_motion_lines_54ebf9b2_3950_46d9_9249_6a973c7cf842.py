"""Hand Massaging Pressure Point.

Plan: HRECT_L, centerline extremes (4, 8, 44, 40); 48 x 48, stroke 4.
All four fingertips and the thumb are retained in the raised hand. Auxiliary motion arcs are omitted to keep correct anatomy and spacing.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54ebf9b2-3950-46d9-9249-6a973c7cf842'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/massage point_54ebf9b2-3950-46d9-9249-6a973c7cf842.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'raised-hand-beside-curved-motion-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('raised', 'hand', 'beside', 'curved', 'motion', 'lines')

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

        path('hand',(12,40),[('L',(12,32)),('C',(4,26),(8,30),(4,28)),('L',(4,24)),('A',(12,24),4,4,True),('L',(12,14)),('A',(20,14),4,4,True),('L',(20,12)),('A',(28,12),4,4,True),('L',(28,14)),('A',(36,14),4,4,True),('L',(36,18)),('A',(44,18),4,4,True),('L',(44,26)),('C',(36,32),(44,28),(40,30)),('L',(36,40))])
