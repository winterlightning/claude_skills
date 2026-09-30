"""Stick figure replaces source profile bust; restore head/neck/shoulder profile beside suitcase.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Shared human user.svg: smooth head and shoulders; luggage: rounded case
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3b255cf1-988c-4c5f-ad89-86c99e9ec069'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__traveler-beside-suitcase/20260929T131521Z-thuan-mac/reference/foreigner_3b255cf1-988c-4c5f-ad89-86c99e9ec069.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='traveler-beside-suitcase'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('traveler', 'beside', 'suitcase')
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

        path('person',(6,42),[('L',(6,29)),('C',(12,22),(6,25),(9,23)),('L',(12,19)),('C',(10,12),(10,18),(10,15)),('A',(22,12),6,6,True),('L',(25,17)),('L',(21,17)),('L',(21,22)),('C',(23,31),(23,25),(23,27)),('L',(23,42))])
        box('suitcase',32,26,42,42,2)
        poly('handle',(34,26),(34,18),(42,18),(42,26));join('handle','suitcase')
