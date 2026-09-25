"""Professional Staff Member Profile.

Plan: Staff bust: circular head r8 at24,12; shoulder top24 gives 0 ink gap. V-neck jacket with center seam; bounds8,4,40,44.
Construction reference: human_ref/user.svg: circular head and broad curved shoulders; current avatar touching-ink rule
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7715f374-5876-4cec-a72c-1210559373d8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crewmember_7715f374-5876-4cec-a72c-1210559373d8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-in-v-neck-jacket'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'in', 'v', 'neck', 'jacket')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member='shoulder-top' if name=='body' and index==2 else f"{name}-{index}"
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

        path('head',(24,4),[('A',(32,12),8,8,True),('A',(24,20),8,8,True),('A',(16,12),8,8,True),('A',(24,4),8,8,True)],True)
        path('body',(8,44),[('L',(8,36)),('A',(20,24),12,12,True),('L',(28,24)),('A',(40,36),12,12,True),('L',(40,44))]);join('head','body')
        poly('collar',(12,28),(24,38),(36,28));line('seam',(24,38),(24,44));join('collar','body');join('collar','seam')
