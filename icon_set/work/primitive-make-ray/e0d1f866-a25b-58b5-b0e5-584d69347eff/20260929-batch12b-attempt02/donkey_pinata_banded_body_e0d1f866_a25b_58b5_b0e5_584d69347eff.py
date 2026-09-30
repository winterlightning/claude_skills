"""Rejected pinata has square joints and a narrow triangular leg opening. Round the back and hooves while preserving ear, donkey muzzle and horizontal band.
Plan: HRECT_L; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e0d1f866-a25b-58b5-b0e5-584d69347eff'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__donkey-pinata-banded-body/20260929T132613Z-thuan-mac/reference/pinata_e0d1f866-a25b-58b5-b0e5-584d69347eff.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='donkey-pinata-banded-body'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pinata',)
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                kind,end,*args=step; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end; members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b): self.relate('connect',a,b)

        def box(name,l,t,r,b,rad=0):
            if not rad:self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('outline',(4,36),[('L',(4,24)),('L',(4,20)),('A',(8,16),4,4,True),('L',(24,16)),('L',(28,8)),('L',(34,12)),('L',(44,14)),('L',(44,24)),('L',(36,24)),('L',(36,40)),('L',(28,40)),('L',(26,32)),('L',(16,32)),('L',(14,40)),('L',(8,40)),('A',(4,36),4,4,True)],True)
        self.add_line('band',(4,24),(36,24));join('band','outline')
