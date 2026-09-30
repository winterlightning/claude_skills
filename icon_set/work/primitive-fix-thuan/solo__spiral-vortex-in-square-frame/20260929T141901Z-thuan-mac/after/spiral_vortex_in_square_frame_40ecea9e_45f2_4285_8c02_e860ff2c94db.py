"""The rejected vortex closes into a circle and sends a bar through its center. Restore an open inward curl connected to a square frame, with no closed circular loop.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match for the framed spiral; source owns its topology.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='40ecea9e-45f2-4285-8c02-e860ff2c94db'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__spiral-vortex-in-square-frame/20260929T141901Z-thuan-mac/reference/houdini logo_40ecea9e-45f2-4285-8c02-e860ff2c94db.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='spiral-vortex-in-square-frame'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('spiral', 'vortex', 'in', 'square', 'frame')
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

        poly('frame',(6,20),(6,6),(42,6),(42,42),(6,42),(6,34))
        path('spiral',(6,20),[('C',(24,15),(12,12),(20,15)),('A',(33,24),9,9,True),('A',(24,33),9,9,True),('A',(15,24),9,9,True),('C',(24,24),(15,23),(20,24))]);join('spiral','frame')
