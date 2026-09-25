"""Royal Crown.

Plan: Royal three-lobed crown with detached finial; bounds6,6,42,42. Curved lobes above single broad band.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd921d83-82b1-4990-b10c-2e0fbc4dd8cc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/diadem_bd921d83-82b1-4990-b10c-2e0fbc4dd8cc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-lobed-crown-with-round-finial'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'lobed', 'crown', 'with', 'round', 'finial')

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

        path('crown',(10,34),[('L',(6,26)),('C',(18,22),(6,18),(12,16)),('C',(30,22),(18,12),(30,12)),('C',(42,26),(36,16),(42,18)),('L',(38,34)),('L',(38,42)),('L',(10,42)),('L',(10,34))],True)
        line('band',(10,34),(38,34));join('band','crown');self.add_dot('finial',(24,6))
