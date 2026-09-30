"""The rejected amulet is flattened with a pin-like top and a tiny flat inset. Restore an upright pendant, open suspension loop and taller pointed teardrop.
Plan: VRECT_M exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6da45d5c-e173-48d2-b3a9-55d622031360'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__oval-amulet-with-teardrop-inset/20260929T135704Z-thuan-mac/reference/amulet_6da45d5c-e173-48d2-b3a9-55d622031360.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='oval-amulet-with-teardrop-inset'
    keyshape=Keyshape.VRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('oval', 'amulet', 'with', 'teardrop', 'inset')
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

        path('pendant',(20,12),[('L',(28,12)),('C',(38,28),(34,12),(38,20)),('C',(24,44),(38,37),(32,44)),('C',(10,28),(16,44),(10,37)),('C',(20,12),(10,20),(14,12))],True)
        path('loop',(20,12),[('L',(20,8)),('A',(28,8),4,4,True),('L',(28,12))]);join('loop','pendant')
        path('drop',(24,21),[('C',(30,32),(27,24),(30,29)),('C',(18,32),(30,38),(18,38)),('C',(24,21),(18,29),(21,24))],True)
