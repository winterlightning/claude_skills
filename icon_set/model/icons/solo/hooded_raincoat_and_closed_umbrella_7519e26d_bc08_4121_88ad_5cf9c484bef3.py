"""Raincoat and Umbrella.

Plan: Hooded coat and closed umbrella, bounds6,6,42,42. Keep coherent rainwear pair. Coat center seam and hood; umbrella remains separate.
Construction reference: Lucide shirt: coherent garment outline; source rainwear pair
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7519e26d-bc08-4121-88ad-5cf9c484bef3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/rain coat umbrella_7519e26d-bc08-4121-88ad-5cf9c484bef3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hooded-raincoat-and-closed-umbrella'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('hooded', 'raincoat', 'and', 'closed', 'umbrella')

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

        path('coat',(8,14),[('A',(24,14),8,8,True),('L',(24,18)),('L',(26,24)),('L',(26,42)),('L',(6,42)),('L',(6,24)),('L',(8,18)),('L',(8,14))],True)
        poly('hood',(8,18),(16,26),(24,18));line('seam',(16,26),(16,42));join('hood','coat');join('hood','seam');join('seam','coat')
        poly('umbrella',(34,18),(42,18),(38,42),closed=True);line('tip',(38,10),(38,18));join('tip','umbrella')
