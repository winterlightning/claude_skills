"""Mirrored outlined up arrow with a broad head and softly rounded stem base.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction: arrow-big-up: continuous outline and rounded stem corners
Omissions: None.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__arrow-thick-top-symbol/20260924T142441Z-thuan-mac/reference/arrow thick top_e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='arrow-thick-top-symbol-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'symbol'
    aliases=()
    keywords=('arrow', 'thick', 'top', 'symbol')
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

        path('arrow',(24,4),[('L',(40,24)),('L',(30,24)),('L',(30,41)),('A',(27,44),3,3,True),('L',(21,44)),('A',(18,41),3,3,True),('L',(18,24)),('L',(8,24)),('L',(24,4))],True)
