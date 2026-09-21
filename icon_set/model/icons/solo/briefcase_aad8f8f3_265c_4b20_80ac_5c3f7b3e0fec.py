"""Professional Handheld Briefcase.

Plan: Briefcase bounds4,8,44,40, top handle and centered latch. Seam splits at latch. Rounded case corners.
Construction reference: Lucide briefcase: continuous rounded housing and centered handle
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aad8f8f3-265c-4b20-80ac-5c3f7b3e0fec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/toolbox_aad8f8f3-265c-4b20-80ac-5c3f7b3e0fec.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'briefcase'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('briefcase',)

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

        path('case',(8,16),[('L',(16,16)),('L',(32,16)),('L',(40,16)),('A',(44,20),4,4,True),('L',(44,28)),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,28)),('L',(4,20)),('A',(8,16),4,4,True)],True)
        poly('handle',(16,16),(16,8),(32,8),(32,16));join('handle','case')
        poly('latch',(20,24),(28,24),(28,32),(20,32),closed=True)
        line('seam-left',(4,28),(20,28));line('seam-right',(28,28),(44,28))
        for seam in ('seam-left','seam-right'):join(seam,'case');join(seam,'latch')
