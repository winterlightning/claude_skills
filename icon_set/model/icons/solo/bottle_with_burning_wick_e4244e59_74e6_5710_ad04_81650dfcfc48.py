"""Rounded bottle with a narrow neck and a flowing burning cloth wick, with a pointed fluttering end.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction: cooking-pot: tangent rounded body corners; source governs asymmetric wick
Omissions: Mouth collar omitted to preserve 8-unit neck opening.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e4244e59-74e6-5710-ad04-81650dfcfc48'
SOURCE_PATH = 'pictographic-primitives/war/bomb fire bottle_e4244e59-74e6-5710-ad04-81650dfcfc48.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='bottle-with-burning-wick'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/war'
    aliases=()
    keywords=('bottle', 'with', 'burning', 'wick')
    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; here=start
            for i,step in enumerate(steps):
                tag=f'{name}-{i}'; kind,end,*args=step
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(tag,here,(args[0],args[1],end))
                here=end;members.append(tag)
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('bottle',(12,44),[('A',(8,40),4,4,True),('L',(8,29)),('C',(14,20),(8,25),(14,24)),('L',(14,14)),('L',(24,14)),('L',(24,20)),('C',(30,29),(24,24),(30,25)),('L',(30,40)),('A',(26,44),4,4,True),('L',(12,44))],True)
        path('wick',(19,14),[('C',(27,4),(19,8),(21,4)),('C',(40,16),(35,4),(32,14)),('L',(35,20)),('C',(27,12),(29,20),(29,17))]);join('wick','bottle')
