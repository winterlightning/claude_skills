"""Briefcase. Retains the identifying silhouette and visible features.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide briefcase-business: tangent rounded corners and attached top handle; source requires a plain case.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b850201-571a-4a5c-bee3-706213011447'
SOURCE_PATH = 'pictographic-primitives/symbol/case_6b850201-571a-4a5c-bee3-706213011447.svg'
AUTHOR = 'gpt-6'


class BriefcasePlain(Solo48):
    icon_id = 'briefcase-plain'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('briefcase', 'case', 'bag', 'work', 'business', 'job', 'portfolio', 'luggage')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_line('case-top-1', (8, 18), (16, 18))
        self.add_line('case-top-2', (16, 18), (32, 18))
        self.add_line('case-top-3', (32, 18), (40, 18))
        self.add_arc('case-ne', (40, 18), (44, 22), radius_x=4, radius_y=4, sweep=True)
        self.add_line('case-right', (44, 22), (44, 36))
        self.add_arc('case-se', (44, 36), (40, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('case-bottom-1', (40, 40), (8, 40))
        self.add_arc('case-sw', (8, 40), (4, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('case-left', (4, 36), (4, 22))
        self.add_arc('case-nw', (4, 22), (8, 18), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('case', 'case-top-1', 'case-top-2', 'case-top-3', 'case-ne', 'case-right', 'case-se', 'case-bottom-1', 'case-sw', 'case-left', 'case-nw', closed=True)
        self.add_line('handle-left', (16, 18), (16, 12))
        self.add_arc('handle-nw', (16, 12), (20, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_line('handle-top', (20, 8), (28, 8))
        self.add_arc('handle-ne', (28, 8), (32, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('handle-right', (32, 12), (32, 18))
        self.add_contour('handle', 'handle-left', 'handle-nw', 'handle-top', 'handle-ne', 'handle-right')
        self.relate("connect", 'case', 'handle')
