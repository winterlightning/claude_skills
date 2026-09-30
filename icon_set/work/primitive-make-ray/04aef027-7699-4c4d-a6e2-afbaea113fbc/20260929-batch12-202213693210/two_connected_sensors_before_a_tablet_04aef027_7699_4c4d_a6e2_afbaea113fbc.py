"""Sensors stacked vertically instead of side by side in front of tablet; restore source arrangement.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: panels-top-left: device rectangle; source sensor placement
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='04aef027-7699-4c4d-a6e2-afbaea113fbc'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-connected-sensors-before-a-tablet/20260929T131521Z-thuan-mac/reference/aws iot services farm ipad_04aef027-7699-4c4d-a6e2-afbaea113fbc.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-connected-sensors-before-a-tablet'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('two', 'connected', 'sensors', 'before', 'a', 'tablet')
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

        path('tablet',(22,14),[('L',(22,6)),('L',(42,6)),('L',(42,34)),('L',(38,34))])
        for x in (6,22):
         box(f'sensor{x}',x,22,x+8,34,2)
         line(f'stem{x}',(x+4,34),(x+4,42));join(f'stem{x}',f'sensor{x}')
        line('bus',(6,42),(42,42))
        for x in (6,22):join('bus',f'stem{x}')
