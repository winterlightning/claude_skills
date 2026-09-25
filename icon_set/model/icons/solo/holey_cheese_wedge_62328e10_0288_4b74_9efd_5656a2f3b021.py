"""Cheese wedge with a curved rind, shallow sloped top seam and two open circular holes.
Keyshape HRECT_L: exact SOLO48 contract envelope.
Construction: No useful local Lucide cheese match; source governs wedge and round perforations
Omissions: Three holes reduced to two; small edge bite omitted for clearance.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '62328e10-0288-4b74-9efd-5656a2f3b021'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/cheddar_62328e10-0288-4b74-9efd-5656a2f3b021.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='holey-cheese-wedge'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('holey', 'cheese', 'wedge')
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

        path('wedge',(4,18),[('L',(26,8)),('C',(44,14),(34,8),(40,10)),('L',(44,40)),('L',(4,40)),('L',(4,18))],True)
        line('top-seam',(4,18),(44,14));join('top-seam','wedge')
        for i,(x,y) in enumerate(((16,28),(32,27))):ellipse(f'hole-{i}',x,y,3,3)
