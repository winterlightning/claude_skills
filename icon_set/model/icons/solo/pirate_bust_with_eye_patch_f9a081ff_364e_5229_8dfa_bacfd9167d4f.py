"""Pirate with Eye Patch.

Symbol plan: Circular pirate face r12, head covering and diagonal patch, shoulders below with exact detached gap4. Extremes8,4,40,44. Omit tiny exposed eye and extra cap line.
Construction references: Shared human_ref/user.svg: circular face and broad curved open shoulders. Source diagonal eye patch.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9a081ff-364e-5229-8dfa-bacfd9167d4f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/piracy pirate_f9a081ff-364e-5229-8dfa-bacfd9167d4f.svg'
AUTHOR = 'gpt-6'


class PirateBustWithEyePatch(Solo48):
    icon_id = 'pirate-bust-with-eye-patch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('pirate', 'bust', 'with', 'eye', 'patch')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x-r,y), [((x+r,y),r,r,True), ((x-r,y),r,r,True)], True)

        path('head',(12,16),[((36,16),12,12,True),((12,16),12,12,True)],True)
        path('patch',(12,16),[(24,16),(36,16)])
        self.add_bezier('patch-bottom',(12,16),((12,24),(22,24),(24,16)))
        self.relate('connect','head','patch');self.relate('connect','head','patch-bottom');self.relate('connect','patch','patch-bottom')
        self.add_bezier('shoulders',(8,44),((8,38),(16,36),(24,36)),((32,36),(40,38),(40,44)))
