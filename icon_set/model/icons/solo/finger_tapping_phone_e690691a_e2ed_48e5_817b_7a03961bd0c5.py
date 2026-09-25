"""A hand enters diagonally from the upper right with its index finger aimed at a thin horizontal phone. Small contact strokes surround the fingertip, and a short divider marks the phone’s right end."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e690691a-e2ed-48e5-817b-7a03961bd0c5'
SOURCE_PATH = 'pictographic-primitives/mobile/force touch tap_e690691a-e2ed-48e5-817b-7a03961bd0c5.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'finger-tapping-phone'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('finger', 'tap', 'phone', 'touch', 'hand', 'gesture', 'screen')

    def build(self):
        # Lucide construction references: pointer, smartphone.
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
        # HRECT_L extremes (4,8)-(44,40). Horizontal phone below a diagonally aimed index finger.
        # Human reference: icon_set/references/human_ref/full_body_ref.png; continuous rounded limb vocabulary.
        # Hand only: no head-to-body measurement applies.
        path('hand',(22,8),[('L',(14,16)),('C',(20,22),(10,20),(16,26)),('L',(28,14)),('C',(36,20),(30,12),(30,20)),('C',(44,8),(42,20),(40,12))])
        rounded('phone',4,32,44,40,4)
