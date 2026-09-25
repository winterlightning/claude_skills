"""Two equal circles overlap side by side, their shared middle forming a pointed lens shape.

Symbol plan: Two equal overlapping round loops, resolved as an outer perimeter plus two lens boundaries. Mirrored at x24; radial maximum20.
Review notes: Keeps two equal round loops and the shared lens. Smooth mirrored curves use the current model Bezier API to put crossings exactly on integer nodes. Lucide circle informs rounded silhouette; no false connection between untouched loops is used.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01e83e84-cb07-474d-a528-0d359864f77f'
SOURCE_PATH = 'pictographic-primitives/logos/mastercard logo_01e83e84-cb07-474d-a528-0d359864f77f.svg'
AUTHOR = 'gpt-6'

class MastercardLogo(Solo48):
    icon_id = 'mastercard-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('mastercard', 'payment', 'credit-card', 'circles', 'logo', 'brand', 'finance')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        # Shared intersection nodes avoid overlapping complete closed-loop primitives.
        top,bottom=(24,15),(24,33)
        self.add_bezier('outer-left',top,((22,13),(19,12),(16,12)),((9,12),(4,17),(4,24)),((4,31),(9,36),(16,36)),((19,36),(22,35),bottom))
        self.add_bezier('outer-right',bottom,((26,35),(29,36),(32,36)),((39,36),(44,31),(44,24)),((44,17),(39,12),(32,12)),((29,12),(26,13),top))
        self.add_contour('perimeter','outer-left','outer-right',closed=True)
        for side,sgn in [('left',-1),('right',1)]:
            x=lambda value:24+sgn*value
            self.add_bezier('lens-'+side,top,((x(4),18),(x(6),20),(x(6),24)),((x(6),28),(x(4),30),bottom))
            for outer in ['outer-left','outer-right']:self.relate('connect','lens-'+side,outer)
        self.relate('connect','lens-left','lens-right')
