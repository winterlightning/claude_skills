"""Five equal circular beads on a U-shaped cord; larger bead openings replace the tiny rejected loops.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: No useful exact Lucide necklace match; source supplies five beads and U arrangement.
Omissions: U is deepened to fit five beads and strict clearance.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ed4699f6-a912-4876-9b67-eba4703923e0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bead_ed4699f6-a912-4876-9b67-eba4703923e0.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='curved-string-of-beads'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('curved', 'string', 'of', 'beads')
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

        centers=((10,10),(10,28),(24,38),(38,28),(38,10));radius=4
        for i,(x,y) in enumerate(centers):ellipse(f'bead-{i}',x,y,radius,radius)
        links=(((10,14),(10,24)),((14,28),(20,38)),((28,38),(34,28)),((38,24),(38,14)))
        for i,(a,b) in enumerate(links):
         line(f'cord-{i}',a,b);join(f'cord-{i}',f'bead-{i}');join(f'cord-{i}',f'bead-{i+1}')
