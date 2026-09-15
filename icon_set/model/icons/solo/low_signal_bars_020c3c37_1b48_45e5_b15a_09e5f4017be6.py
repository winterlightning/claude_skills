"""Two hollow signal bars rise from a shared baseline, with the second taller than the first. Two short horizontal marks continue the row to the right, indicating the remaining empty positions."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '020c3c37-1b48-45e5-b15a-09e5f4017be6'
SOURCE_PATH = 'pictographic-primitives/mobile/signal low_020c3c37-1b48-45e5-b15a-09e5f4017be6.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'low-signal-bars'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/mobile'
    aliases = ()
    keywords = ('signal', 'low', 'bars', 'reception', 'cellular', 'network', 'strength')

    def build(self):
        # Lucide construction references: signal.
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
        # HRECT_L extremes (4,8)-(44,40). Two width-8 active bars, two empty dots.
        for i,(x,top) in enumerate(((4,24),(20,8))):
            self.add_polyline(f'bar-{i}',(x,top),(x+8,top),(x+8,40),(x,40),closed=True)
        for i,x in enumerate((36,44)):
            self.add_dot(f'empty-{i}',(x,40))
