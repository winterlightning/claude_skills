"""Three hollow rounded signal bars rise in height from left to right. Below them, a small hollow block sits beneath the first bar, followed by two short horizontal marks under the remaining bars."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5570ecb-4c49-48f0-ae7f-5d75dfcbb9bd'
SOURCE_PATH = 'pictographic-primitives/mobile/dual sim signal_e5570ecb-4c49-48f0-ae7f-5d75dfcbb9bd.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'dual-sim-signal-secondary-low'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('dual-sim', 'signal', 'bars', 'cellular', 'network', 'reception', 'indicator')

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
        # HRECT_L extremes (4,8)-(44,40): repeated width-8 columns and a second row.
        for i,(x,top) in enumerate(((4,16),(20,12),(36,8))):
            self.add_polyline(f'bar-{i}',(x,top),(x+8,top),(x+8,24),(x,24),closed=True)
        self.add_polyline('secondary-active',(4,32),(12,32),(12,40),(4,40),closed=True)
        for i,x in enumerate((20,36)):
            self.add_line(f'secondary-empty-{i}',(x,40),(x+8,40))
