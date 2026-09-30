"""The rejected tree closes the roots with a bottom bar and omits both side branches. Restore outward branches, open flared roots, narrow eyes and a shallow smile.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match for this character trunk.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0e2497bc-6381-4694-8d17-9da0fe023c2e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__smiling-tree-trunk-batch-086/20260929T141901Z-thuan-mac/reference/mario tree_0e2497bc-6381-4694-8d17-9da0fe023c2e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='smiling-tree-trunk-batch-086'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('smiling', 'tree', 'trunk', 'batch', '086')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('trunk',(4,40),[('C',(11,30),(8,40),(11,36)),('L',(11,20)),('L',(11,8)),('C',(24,8),(15,14),(20,14)),('C',(37,8),(28,14),(33,14)),('L',(37,20)),('L',(37,30)),('C',(44,40),(37,36),(40,40))])
        path('branch-left',(4,8),[('C',(11,20),(4,18),(6,20))]);join('branch-left','trunk')
        path('branch-right',(44,8),[('C',(37,20),(44,18),(42,20))]);join('branch-right','trunk')
        for x in (20,28):line('eye'+str(x),(x,21),(x,22))
        path('smile',(20,31),[('A',(28,31),4,3,False)])
