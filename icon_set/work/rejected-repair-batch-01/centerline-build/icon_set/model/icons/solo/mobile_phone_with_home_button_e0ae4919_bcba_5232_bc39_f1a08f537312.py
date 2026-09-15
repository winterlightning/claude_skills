"""A tall rounded phone has a small mark near its top and a horizontal divider above the lower bezel. A short centred home-button mark sits beneath the divider on the front face."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0ae4919-bcba-5232-bc39-f1a08f537312'
SOURCE_PATH = 'pictographic-primitives/mobile/mobile phone_e0ae4919-bcba-5232-bc39-f1a08f537312.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'mobile-phone-with-home-button'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/mobile'
    aliases = ()
    keywords = ('phone', 'mobile', 'screen', 'home-button', 'bezel', 'device', 'smartphone')

    def build(self):
        # Lucide construction references: smartphone.
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
        # VRECT_L extremes (8,4)-(40,44): shared radius-4 corners and x=24 axis.
        rounded('body',8,4,40,44,4,split_y=26)
        self.add_line('bezel',(8,26),(40,26))
        self.relate('connect','body','bezel')
        self.add_dot('speaker',(24,13))
        self.add_line('home-button',(22,35),(26,35))
