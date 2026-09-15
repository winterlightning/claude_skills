"""The capital letters LTE form one horizontal row. The L has a long lower foot, the T has a broad top bar, and the E has three horizontal arms extending to the right."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e4774df-ef53-5eda-941a-67a7eac299a4'
SOURCE_PATH = 'pictographic-primitives/mobile/lte_1e4774df-ef53-5eda-941a-67a7eac299a4.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'lte-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/mobile'
    aliases = ()
    keywords = ('lte', 'text', 'cellular', 'network', 'mobile', 'letters', 'data')

    def build(self):
        # Lucide construction references: none.
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
        # HRECT_L extremes (4,8)-(44,40). Three letters with eight-unit interletter gaps.
        self.add_polyline('l',(4,8),(4,40),(12,40))
        self.add_polyline('t-bar',(20,8),(24,8),(28,8))
        self.add_line('t-stem',(24,8),(24,40))
        self.relate('connect','t-bar','t-stem')
        self.add_polyline('e',(44,8),(36,8),(36,24),(36,40),(44,40))
        self.add_line('e-arm',(36,24),(44,24))
        self.relate('connect','e','e-arm')
