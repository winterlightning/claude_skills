"""A front-facing person appears behind an open laptop, with a circular head and arched shoulders. The laptop has a tapered lid with a central circular mark and rests on a horizontal base.
Lucide user head and shoulder arch; laptop tapered lid. Symmetric front-facing composition. Central lid logo omitted to keep the shallow lid clear.
Keyshape VRECT_L; centerline extremes (8,6)-(40,42). Tall envelope fits the upright subject. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c890eda1-538b-5186-a443-949e56ec3dfe'
SOURCE_PATH = 'pictographic-primitives/work/employee_c890eda1-538b-5186-a443-949e56ec3dfe.svg'
AUTHOR = 'gpt-6'


class EmployeeBehindLaptop(Solo48):
    icon_id = 'employee-behind-laptop'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('employee', 'laptop', 'person', 'computer', 'work', 'office')

    def build(self) -> None:
        self.add_arc('head-top', (18, 10), (30, 10), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (30, 10), (18, 10), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulders', (10, 32), (38, 32), radius_x=14, radius_y=7, sweep=True, large_arc=False)
        self.add_polyline('laptop', (8, 32), (40, 32), (36, 42), (12, 42), closed=True)
        self.relate("connect", 'shoulders', 'laptop')
        self.add_line('base', (8, 42), (40, 42))
        self.relate("connect", 'base', 'laptop')
