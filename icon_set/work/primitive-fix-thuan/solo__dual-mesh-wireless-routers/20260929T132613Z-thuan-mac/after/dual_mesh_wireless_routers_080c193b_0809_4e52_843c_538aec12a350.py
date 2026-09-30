"""Rejected routers are shallow trapezoids and smallest wifi arc is a blob. Restore two upright rounded router towers under two clear signal arcs.
Plan: VRECT_L; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='080c193b-0809-4e52-843c-538aec12a350'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__dual-mesh-wireless-routers/20260929T132613Z-thuan-mac/reference/mesh wifi router_080c193b-0809-4e52-843c-538aec12a350.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='dual-mesh-wireless-routers'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('mesh', 'wifi', 'router')
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

        box('router-left',8,27,20,44,3);box('router-right',28,27,40,44,3)
        path('wifi-outer',(8,10),[('A',(40,10),16,6,True)])
        path('wifi-inner',(15,18),[('A',(33,18),9,5,True)])
