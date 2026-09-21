"""Protective Kitchen Oven Mitt.

Plan: Oven mitt bounds8,4,40,44 with broad curved fingers, left thumb and8-high cuff. Shared seam at y36.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '917e7d44-3b6e-481c-a5a6-f77338e659f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mitten_917e7d44-3b6e-481c-a5a6-f77338e659f6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oven-mitt-with-wide-wrist-cuff'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('oven', 'mitt', 'with', 'wide', 'wrist', 'cuff')

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

        path('mitt',(16,36),[('L',(8,28)),('C',(8,20),(8,26),(8,22)),('C',(16,20),(10,16),(13,18)),('L',(16,16)),('A',(40,16),12,12,True),('L',(40,36)),('L',(16,36))],True)
        path('cuff',(16,36),[('L',(40,36)),('L',(40,40)),('A',(36,44),4,4,True),('L',(20,44)),('A',(16,40),4,4,True),('L',(16,36))],True);join('mitt','cuff')
