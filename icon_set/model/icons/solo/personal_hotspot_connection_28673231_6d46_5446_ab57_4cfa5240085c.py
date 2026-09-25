"""Two broad oblong chain links overlap diagonally, with the upper link shifted left and the lower link shifted right. Each open contour curves around the other, forming a compact interlocking pair."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28673231-6d46-5446-ab57-4cfa5240085c'
SOURCE_PATH = 'pictographic-primitives/mobile/personal hotspot connection_28673231-6d46-5446-ab57-4cfa5240085c.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'personal-hotspot-connection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('chain', 'link', 'connection', 'hotspot', 'network', 'interlocking', 'pair')

    def build(self):
        # Lucide construction references: link.
        # Typed paths own continuous joins; repeated shapes share dimensions.
        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                ident = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(ident, here, end)
                elif kind == 'C':
                    self.add_bezier(ident, here, (args[0],args[1],end))
                else:
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def rounded(name,x0,y0,x1,y1,r,split_y=None):
            right = [('L',(x1,split_y))] if split_y is not None else []
            left = [('L',(x0,split_y))] if split_y is not None else []
            path(name,(x0+r,y0),[
                ('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),
                *right,('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),
                ('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),
                *left,('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        # HRECT_L extremes (4,8)-(44,40): repeated vertical links with a shared bridge.
        # Each bridge crossing is split at an actual contour endpoint.
        for name,x in (('left-link',4),('right-link',28)):
            path(name,(x+8,8),[('A',(x+16,16),8,8,True),('L',(x+16,24)),('L',(x+16,32)),('A',(x+8,40),8,8,True),('A',(x,32),8,8,True),('L',(x,24)),('L',(x,16)),('A',(x+8,8),8,8,True)],True)
        self.add_polyline('bridge',(12,24),(20,24),(28,24),(36,24))
        self.relate('connect','left-link','bridge')
        self.relate('connect','right-link','bridge')
