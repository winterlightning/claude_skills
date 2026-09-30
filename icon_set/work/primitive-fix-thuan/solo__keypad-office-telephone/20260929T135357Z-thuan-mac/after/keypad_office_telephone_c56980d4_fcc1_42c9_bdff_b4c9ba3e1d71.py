"""Rejected receiver is a plain arch and keypad has only two dots. Restore handset end pads and a three-key row.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: phone: receiver terminals; grip: equal keypad series
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c56980d4-fcc1-42c9-bdff-b4c9ba3e1d71'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__keypad-office-telephone/20260929T135357Z-thuan-mac/reference/phone office_c56980d4-fcc1-42c9-bdff-b4c9ba3e1d71.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='keypad-office-telephone'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('keypad', 'office', 'telephone')
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

        path('receiver',(6,18),[('L',(6,14)),('C',(24,6),(6,7),(15,6)),('C',(42,14),(33,6),(42,7)),('L',(42,18)),('L',(34,18)),('L',(31,15)),('L',(17,15)),('L',(14,18)),('L',(6,18))],True)
        path('base',(8,26),[('L',(40,26)),('L',(42,42)),('L',(6,42)),('L',(8,26))],True)
        for x in (16,24,32):self.add_dot(f'key{x}',(x,34))
