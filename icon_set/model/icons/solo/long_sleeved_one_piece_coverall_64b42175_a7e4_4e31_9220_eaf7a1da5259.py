"""Protective One Piece Coverall.

Plan: Coverall bounds6,6,42,42 with long sleeves, two trouser legs and center closure. Symmetric silhouette; remove small collar triangles.
Construction reference: Lucide shirt: unified clothing silhouette and mirrored sleeves
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64b42175-a7e4-4e31-9220-eaf7a1da5259'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/coverall_64b42175-a7e4-4e31-9220-eaf7a1da5259.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-sleeved-one-piece-coverall'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('long', 'sleeved', 'one', 'piece', 'coverall')

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

        poly('suit',(16,6),(24,10),(32,6),(42,18),(36,24),(34,22),(34,42),(26,42),(24,30),(22,42),(14,42),(14,22),(12,24),(6,18),closed=True)
        line('zip',(24,10),(24,30));join('zip','suit')
