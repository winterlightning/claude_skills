"""Closed eyelid is a circular arc with two radial lashes attached at exact arc points; extremes 4,10,44,38.
Construction: eye-closed: continuous lid and radial lashes
Reduction: Two left-hand lashes retained as in source; deliberate asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'afb69f40-6aff-40c4-aa6f-3646708bd0d2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__closed-eye-with-eyelashes/20260924T111346Z-thuan-mac/reference/eyelid_afb69f40-6aff-40c4-aa6f-3646708bd0d2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-eye-with-eyelashes'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('closed', 'eye', 'with', 'eyelashes')
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                else: self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m); here=end
            self.add_contour(name,*members,closed=closed)
        def poly(name,*pts,closed=False): self.add_polyline(name,*pts,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('lid',(4,10),[('A',(12,22),20,15,False),('A',(24,25),20,15,False),('A',(44,10),20,15,False)])
        line('outer-lash',(12,22),(6,30));line('inner-lash',(24,25),(24,38));join('lid','outer-lash');join('lid','inner-lash')
