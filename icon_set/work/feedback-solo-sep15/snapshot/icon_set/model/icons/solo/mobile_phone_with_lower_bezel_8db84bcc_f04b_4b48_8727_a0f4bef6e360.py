"""A tall phone has smoothly rounded corners, a short speaker slot near the top, and a horizontal divider above its lower bezel. The broad central screen area remains empty."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8db84bcc-f04b-4b48-8727-a0f4bef6e360'
SOURCE_PATH = 'pictographic-primitives/mobile/mobile phone 1_8db84bcc-f04b-4b48-8727-a0f4bef6e360.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'mobile-phone-with-lower-bezel'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/mobile'
    aliases = ()
    keywords = ('phone', 'mobile', 'screen', 'speaker', 'bezel', 'device', 'smartphone')

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
        rounded('body',8,4,40,44,4,split_y=36)
        self.add_line('bezel',(8,36),(40,36))
        self.relate('connect','body','bezel')
        self.add_line('speaker',(20,13),(28,13))
