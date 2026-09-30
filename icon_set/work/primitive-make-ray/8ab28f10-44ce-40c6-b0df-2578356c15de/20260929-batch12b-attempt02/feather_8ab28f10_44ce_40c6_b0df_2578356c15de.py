"""Rejected feather has a broad leaf-like closed vane and loses the open notch. Restore the long pointed vane, visible open notch and diagonal quill.
Plan: VRECT_L; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8ab28f10-44ce-40c6-b0df-2578356c15de'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__feather/20260929T132613Z-thuan-mac/reference/feather_8ab28f10-44ce-40c6-b0df-2578356c15de.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='feather'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('feather',)
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

        path('vane',(14,36),[('C',(8,26),(10,34),(8,30)),('C',(36,4),(8,17),(25,8)),('C',(40,18),(40,8),(40,12)),('L',(34,22))])
        path('vane-lower',(36,30),[('C',(14,36),(30,38),(20,40))]);join('vane','vane-lower')
        self.add_polyline('quill',(8,44),(14,36),(26,21));join('quill','vane');join('quill','vane-lower')
