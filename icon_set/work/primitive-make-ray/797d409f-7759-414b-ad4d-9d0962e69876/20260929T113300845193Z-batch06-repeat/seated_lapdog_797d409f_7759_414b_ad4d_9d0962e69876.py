"""The rejected dog had a sharp triangular ear and angular back. Restored a rounded upright ear, flowing shoulder and softer muzzle while retaining the seated legs and raised tail.
Plan: Lucide dog: smooth muzzle and ears; supplied reference owns the seated profile. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='797d409f-7759-414b-ad4d-9d0962e69876'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__seated-lapdog/20260929T112716Z-thuan-mac/reference/lapdog_797d409f-7759-414b-ad4d-9d0962e69876.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='seated-lapdog'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                members.append(member);here=end
            self.add_contour(name,*members,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*pts): self.add_polyline(name,*pts)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r): path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('dog',(24,6),[('C',(30,14),(28,6),(29,10)),('L',(34,14)),('C',(42,20),(38,18),(42,18)),('C',(34,28),(42,26),(38,28)),('L',(34,38)),('A',(38,42),4,4,False),('L',(24,42)),('L',(18,42)),('A',(10,34),8,8,True),('C',(22,18),(10,26),(20,25)),('C',(24,6),(24,14),(22,9))],True)
        path('tail',(10,34),[('A',(6,26),4,8,True),('L',(6,20))]);join('tail','dog')
        line('front-leg',(24,30),(24,42));join('front-leg','dog')
