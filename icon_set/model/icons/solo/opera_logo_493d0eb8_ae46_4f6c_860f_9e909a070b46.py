"""A large circle holds a tall narrow oval ring at its centre, like a capital O viewed at an angle.

Symbol plan: Radius20 circle enclosing an upright ellipse rx8 ry11; radial extremes (4,4)-(44,44).
Review notes: Preserves round outside and tall elliptical counter. Earlier Lucide circle construction informs paired arcs; the ellipse is intentionally not made circular.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '493d0eb8-ae46-4f6c-860f-9e909a070b46'
SOURCE_PATH = 'pictographic-primitives/logos/opera logo_493d0eb8-ae46-4f6c-860f-9e909a070b46.svg'
AUTHOR = 'gpt-6'

class OperaLogo(Solo48):
    icon_id = 'opera-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('opera', 'browser', 'letter-o', 'logo', 'brand', 'web', 'internet')

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
        ring('outer',24,24,20)
        self.add_arc('inner-top',(16,24),(32,24),radius_x=8,radius_y=11)
        self.add_arc('inner-bottom',(32,24),(16,24),radius_x=8,radius_y=11)
        self.add_contour('inner','inner-top','inner-bottom',closed=True)
