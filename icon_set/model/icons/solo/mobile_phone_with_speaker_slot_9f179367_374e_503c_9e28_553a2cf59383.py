"""A tall slim phone has a rounded rectangular outline and a short centred speaker slot near its upper edge. Its otherwise empty front has no separate lower bezel or visible button."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f179367-374e-503c-9e28-553a2cf59383'
SOURCE_PATH = 'pictographic-primitives/mobile/mobile phone_9f179367-374e-503c-9e28-553a2cf59383.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'mobile-phone-with-speaker-slot'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('phone', 'mobile', 'screen', 'speaker', 'device', 'smartphone', 'handset')

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
        rounded('body',8,4,40,44,4,split_y=None)
        self.add_line('speaker',(20,13),(28,13))
