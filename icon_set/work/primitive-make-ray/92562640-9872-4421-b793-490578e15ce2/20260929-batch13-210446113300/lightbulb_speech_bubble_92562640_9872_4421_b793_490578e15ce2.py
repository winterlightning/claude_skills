"""Faceted speech outline and squat bulb lose the rounded message and bulb silhouette. Round the bubble and give bulb shoulders a clearer taper.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: lightbulb and messages-square: round dome and curved enclosure
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='92562640-9872-4421-b793-490578e15ce2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__lightbulb-speech-bubble/20260929T135357Z-thuan-mac/reference/idea message_92562640-9872-4421-b793-490578e15ce2.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='lightbulb-speech-bubble'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('lightbulb', 'speech', 'bubble')
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

        path('bubble',(14,34),[('L',(10,34)),('A',(6,30),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,30)),('A',(38,34),4,4,True),('L',(22,34)),('L',(14,42)),('L',(14,34))],True)
        path('bulb',(18,20),[('A',(30,20),6,5,True),('C',(28,25),(30,23),(28,23)),('L',(20,25)),('C',(18,20),(20,23),(18,23))],True)

        line('bulb-base',(24,25),(24,34));join('bulb-base','bulb');join('bulb-base','bubble')
