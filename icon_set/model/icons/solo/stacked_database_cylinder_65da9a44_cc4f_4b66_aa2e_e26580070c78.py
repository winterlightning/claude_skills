from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65da9a44-cc4f-4b66-aa2e-e26580070c78'
SOURCE_PATH = 'pictographic-primitives/servers/database_65da9a44-cc4f-4b66-aa2e-e26580070c78.svg'
AUTHOR = 'gpt-6-astra'


class StackedDatabaseCylinder(Solo48):
    icon_id = 'stacked-database-cylinder'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "servers"
    categories = ("primitives", "servers")
    aliases = ()
    keywords = ('database', 'storage', 'data', 'cylinder', 'stack', 'server', 'disk')

    def build(self) -> None:
        # VRECT_L centerlines (8,4)-(40,44); coaxial ellipses share radii.
        left, right = 8, 40
        rx, ry = 16, 5
        self.add_arc("top-back", (left,9), (right,9), radius_x=rx, radius_y=ry)
        self.add_arc("top-front", (right,9), (left,9), radius_x=rx, radius_y=ry)
        self.add_contour("top", "top-back", "top-front", closed=True)
        self.add_polyline("left-side", (left,9), (left,19), (left,29), (left,39))
        self.add_polyline("right-side", (right,9), (right,19), (right,29), (right,39))
        for index,y in enumerate((19,29,39)):
            self.add_arc(f"tier-{index}", (right,y), (left,y), radius_x=rx, radius_y=ry)
            self.relate("connect", f"tier-{index}", "left-side")
            self.relate("connect", f"tier-{index}", "right-side")
        self.relate("connect", "top", "left-side")
        self.relate("connect", "top", "right-side")
