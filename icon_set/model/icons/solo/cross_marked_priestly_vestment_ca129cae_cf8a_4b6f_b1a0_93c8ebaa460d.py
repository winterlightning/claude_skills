"""Priest Vestment with Cross.

Plan: Priestly garment with integral central cross. Bounds6,6,42,42. Simplify neck and sleeve folds while retaining sleeves and cross.
Construction reference: Lucide shirt: unified garment outline; integral religious emblem
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca129cae-cf8a-4b6f-b1a0-93c8ebaa460d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/chasuble_ca129cae-cf8a-4b6f-b1a0-93c8ebaa460d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cross-marked-priestly-vestment'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cross', 'marked', 'priestly', 'vestment')

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

        poly('garment',(16,6),(24,10),(32,6),(36,8),(42,24),(38,28),(38,42),(10,42),(10,28),(6,24),(12,8),closed=True)
        poly('cross-stem',(24,19),(24,27),(24,33));poly('cross-arm',(18,27),(24,27),(30,27));join('cross-stem','cross-arm')
