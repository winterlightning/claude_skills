"""Rejected square windows became horizontal dashes. Restore two outlined square windows beneath the gable; omit the secondary doorway to give the paired windows enough space.
Plan: HRECT_L; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='947154d2-ba94-40d8-86da-58585ad61c10'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__gabled-house-paired-windows/20260929T132937Z-thuan-mac/reference/proprietor_947154d2-ba94-40d8-86da-58585ad61c10.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='gabled-house-paired-windows'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('proprietor',)
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

        self.add_polyline('house',(4,18),(24,8),(44,18),(44,40),(4,40),closed=True)
        for name,x in [('left',12),('right',28)]:box('window-'+name,x,24,x+8,32,0)
