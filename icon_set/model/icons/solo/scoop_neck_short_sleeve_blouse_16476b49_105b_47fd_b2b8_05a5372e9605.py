"""Short Sleeve Women's Blouse.

Plan: Retained the scoop neck, short sleeves, fitted waist and shallow curved hem of the blouse.
Construction reference: Lucide shirt: curved neckline and shoulder silhouette, source-specific fitted body.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16476b49-105b-47fd-b2b8-05a5372e9605'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blouse_16476b49-105b-47fd-b2b8-05a5372e9605.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'scoop-neck-short-sleeve-blouse'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('scoop', 'neck', 'short', 'sleeve', 'blouse')

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

        path('blouse',(16,6),[('A',(32,6),8,8,False),('C',(42,18),(38,6),(40,12)),('L',(34,22)),('C',(36,40),(32,28),(34,34)),('C',(24,42),(32,42),(28,42)),('C',(12,40),(20,42),(16,42)),('C',(14,22),(14,34),(16,28)),('L',(6,18)),('C',(16,6),(8,12),(10,6))],True)
