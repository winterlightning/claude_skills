"""Fidget Spinner Toy.

Plan: Three rounded lobes and broad waists around bearing. Bounds6,6,42,42. Center bearing radius3 with9u clearance.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae6c0f5f-dc86-48e7-a739-7c4c0a7b3ac0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/spinner_ae6c0f5f-dc86-48e7-a739-7c4c0a7b3ac0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-lobed-fidget-spinner-with-center-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('three', 'lobed', 'fidget', 'spinner', 'with', 'center', 'ring')

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

        path('spinner',(14,18),[('C',(24,6),(12,10),(18,6)),('C',(34,18),(30,6),(36,10)),('C',(38,27),(32,23),(34,25)),('C',(42,35),(42,29),(42,31)),('C',(34,42),(42,39),(38,42)),('C',(24,38),(30,42),(27,38)),('C',(14,42),(21,38),(18,42)),('C',(6,35),(10,42),(6,39)),('C',(10,27),(6,31),(6,29)),('C',(14,18),(14,25),(16,23))],True)
        circle('bearing',24,27,2)
