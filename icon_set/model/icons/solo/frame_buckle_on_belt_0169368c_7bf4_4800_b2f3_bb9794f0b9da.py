"""Rectangular Waist Belt Buckle.

Plan: Buckle and straps; one open frame and inward prong remove redundant nested contour. Bounds4,10,44,38.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0169368c-7bf4-4800-b2f3-bb9794f0b9da'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/buckle_0169368c-7bf4-4800-b2f3-bb9794f0b9da.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'frame-buckle-on-belt'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('frame', 'buckle', 'on', 'belt')

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

        path('buckle',(16,10),[('L',(32,10)),('A',(36,14),4,4,True),('L',(36,18)),('L',(36,30)),('L',(36,34)),('A',(32,38),4,4,True),('L',(16,38)),('A',(12,34),4,4,True),('L',(12,30)),('L',(12,24)),('L',(12,18)),('L',(12,14)),('A',(16,10),4,4,True)],True)
        poly('strap-left',(12,18),(4,18),(4,30),(12,30));poly('strap-right',(36,18),(44,18),(44,30),(36,30));line('prong',(12,24),(24,24))
        for x in ('strap-left','strap-right','prong'):join(x,'buckle')
