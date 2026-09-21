"""Female Reproductive Organs.

Plan: Uterus with symmetric curled tubes and narrow cervix, bounds4,8,44,40. Simplify inner line and curl depth.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86618c56-cce5-4113-85c4-9bc9db68900a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/ovary_86618c56-cce5-4113-85c4-9bc9db68900a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'uterus-curled-fallopian-tubes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('uterus', 'curled', 'fallopian', 'tubes')

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

        path('organ',(16,12),[('C',(24,8),(19,10),(20,8)),('C',(32,12),(28,8),(29,10)),('C',(44,16),(40,4),(44,10)),('C',(36,24),(44,22),(40,26)),('C',(36,16),(32,22),(34,16)),('C',(30,28),(32,18),(32,24)),('L',(28,40)),('L',(20,40)),('L',(18,28)),('C',(12,16),(16,24),(16,18)),('C',(12,24),(14,16),(16,22)),('C',(4,16),(8,26),(4,22)),('C',(16,12),(4,10),(8,4))],True)
