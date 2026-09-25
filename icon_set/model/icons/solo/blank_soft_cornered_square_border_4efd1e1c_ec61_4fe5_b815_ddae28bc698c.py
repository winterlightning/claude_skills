"""Blank Soft-Cornered Square Border.
Standalone border geometry; nested edges define one frame, no independent glyph.
SQUARE envelope x6..42/y6..42; bilateral symmetry about x24.
Lucide square original/atoms inform tangent quarter-circle corners and closed contour.
Reference supplies the nested-border arrangement. Curves receive generous clearance.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '4efd1e1c-ec61-4fe5-b815-ddae28bc698c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/square k_4efd1e1c-ec61-4fe5-b815-ddae28bc698c.svg'
AUTHOR = 'gpt-6-astra'
class AuthoredFrame(Solo48):
    icon_id = 'blank-soft-cornered-square-border'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('Simple Rounded Square Shape',)
    keywords = ('square', 'frame', 'outline', 'border')
    def build(self):
        def rect(prefix,x0,y0,x1,y1,r):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            ids=[]
            for i,a in enumerate(pts):
                b=pts[(i+1)%8];ident=f'{prefix}-{i}';ids.append(ident)
                if i%2:self.add_arc(ident,a,b,radius_x=r)
                else:self.add_line(ident,a,b)
            self.add_contour(prefix,*ids,closed=True)
        rect('outer',6,6,42,42,5)
