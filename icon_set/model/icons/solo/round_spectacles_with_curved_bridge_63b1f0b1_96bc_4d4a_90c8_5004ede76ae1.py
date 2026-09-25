"""Round Frame Eyeglasses.

Plan: Round spectacles on diagonal, short temples at outer sides; bounds4,8,44,40.
Construction reference: Lucide glasses: circular lenses, curved bridge and temple ends
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63b1f0b1-96bc-4d4a-90c8-5004ede76ae1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/spectacles_63b1f0b1-96bc-4d4a-90c8-5004ede76ae1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-spectacles-with-curved-bridge'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('round', 'spectacles', 'with', 'curved', 'bridge')

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

        circle('left',14,15,7);circle('right',34,33,7)
        path('bridge',(21,15),[('C',(27,33),(31,16),(30,24))]);join('bridge','left');join('bridge','right')
        line('temple-left',(4,15),(7,15));line('temple-right',(41,33),(44,33));join('temple-left','left');join('temple-right','right')
