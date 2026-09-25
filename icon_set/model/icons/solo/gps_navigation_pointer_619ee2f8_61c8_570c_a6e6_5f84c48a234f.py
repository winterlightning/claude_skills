"""A hollow navigation pointer aims diagonally toward the upper right. Two long straight outer edges meet at a sharp tip, while a deep inward notch separates the shorter trailing points at the left and bottom."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '619ee2f8-61c8-570c-a6e6-5f84c48a234f'
SOURCE_PATH = 'pictographic-primitives/mobile/gps location compass_619ee2f8-61c8-570c-a6e6-5f84c48a234f.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'gps-navigation-pointer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('gps', 'navigation', 'pointer', 'direction', 'location', 'compass', 'arrow')

    def build(self):
        # Lucide construction references: navigation.
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
        # SQUARE extremes (6,6)-(42,42): one directional concave polygon.
        self.add_polyline('pointer',(6,22),(42,6),(26,42),(22,26),closed=True)
