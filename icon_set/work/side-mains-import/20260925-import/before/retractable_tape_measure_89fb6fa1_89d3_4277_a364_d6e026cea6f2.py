"""Retractable Measuring Tape Tool.

Plan: Housing and strip share a base junction. Centerline bounds 4,8,44,40. Drop fine strip graduations; retain housing hub.
Construction reference: ruler.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89fb6fa1-89d3-4277-a364-d6e026cea6f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/tape measure_89fb6fa1-89d3-4277-a364-d6e026cea6f2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'retractable-tape-measure'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('retractable', 'tape', 'measure')

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

        path('housing',(28,28),[('L',(28,40)),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,20)),('A',(16,8),12,12,True),('A',(28,20),12,12,True),('L',(28,28))],True)
        poly('strip',(28,28),(44,28),(44,40),(28,40));join('housing','strip')
        circle('hub',16,23,3)
