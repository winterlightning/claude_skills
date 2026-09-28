from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc729e7d-4470-50b7-9ed9-55ce7e4c2157'
SOURCE_PATH = 'pictographic-primitives/servers/server_dc729e7d-4470-50b7-9ed9-55ce7e4c2157.svg'
AUTHOR = 'gpt-6-astra'


class ThreeUnitServerStack(Solo48):
    icon_id = 'three-unit-server-stack'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "servers"
    categories = ("servers", "other", "primitives-generate")
    aliases = ()
    keywords = ('server', 'rack', 'hardware', 'storage', 'network', 'stack', 'indicator')

    def build(self) -> None:
        # VRECT_L centerlines (8,4)-(40,44); three bays share a rounded case.
        left, right, top, bottom, radius = 8, 40, 4, 44, 4
        self.add_line("top", (left+radius,top), (right-radius,top))
        self.add_arc("tr", (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line("right", (right,top+radius), (right,bottom-radius))
        self.add_arc("br", (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line("bottom", (right-radius,bottom), (left+radius,bottom))
        self.add_arc("bl", (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line("left-1", (left,bottom-radius), (left,31))
        self.add_line("left-2", (left,31), (left,17))
        self.add_line("left-3", (left,17), (left,top+radius))
        self.add_arc("tl", (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour("case", "top", "tr", "right", "br", "bottom", "bl", "left-1", "left-2", "left-3", "tl", closed=True)
        for n,y in enumerate((17,31)):
            self.add_line(f"bay-{n}", (left,y), (22,y))
            self.relate("connect", "case", f"bay-{n}")
        for n,y in enumerate((13,24,35)):
            self.add_dot(f"indicator-{n}", (31,y))
