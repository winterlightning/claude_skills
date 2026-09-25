"""Roasted Coffee Bean.

Plan: Diagonal oval coffee bean with flowing end-to-end seam; bounds6,6,42,42.
Construction reference: Lucide bean: coherent cubic silhouette and flowing seam; preserve source oval
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b19900b-2f50-4eb1-8024-c7cb4c3c1ae7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bean_0b19900b-2f50-4eb1-8024-c7cb4c3c1ae7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-oval-coffee-bean'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('diagonal', 'oval', 'coffee', 'bean')

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

        path('bean',(12,42),[('C',(6,30),(6,42),(6,35)),('C',(34,6),(6,17),(20,6)),('C',(42,18),(40,6),(42,11)),('C',(12,42),(42,31),(27,42))],True)
        path('seam',(12,42),[('C',(26,24),(16,31),(23,29)),('C',(34,6),(30,19),(30,12))]);join('seam','bean')
