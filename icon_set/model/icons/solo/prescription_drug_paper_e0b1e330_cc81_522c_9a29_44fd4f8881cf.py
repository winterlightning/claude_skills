"""prescription drug paper: fresh SOLO48 repair.
Plan: Rounded page, R bowl and stem, descending leg crossing the X at a shared node.
Keyshape: VRECT_L. Portrait page accommodates a larger Rx monogram.
Omissions: Text rules omitted to give the Rx monogram adequate clearance.
Construction reference: file-text: rounded document enclosure; supplied Rx reference: connected monogram.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e0b1e330-cc81-522c-9a29-44fd4f8881cf'
SOURCE_PATH = 'pictographic-primitives/health/prescription drug paper_e0b1e330-cc81-522c-9a29-44fd4f8881cf.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/prescription_drug_paper_e0b1e330_cc81_522c_9a29_44fd4f8881cf.py'

class Drawing(Solo48):
    icon_id = 'prescription-drug-paper'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('prescription', 'drug', 'paper')

    def build(self):
        self.box('paper', 8, 4, 40, 44, 4)
        self.add_line('r-stem', (17, 22), (17, 13))
        self.add_line('r-top', (17, 13), (22, 13))
        self.add_arc('r-bowl', (22, 13), (22, 21), radius_x=4)
        self.add_line('r-return', (22, 21), (17, 21))
        self.add_contour('r', 'r-stem', 'r-top', 'r-bowl', 'r-return')
        self.add_polyline('r-leg', (22, 21), (27, 30), (30, 35))
        self.add_polyline('x-cross', (31, 26), (27, 30), (22, 35))
        self.relate('connect', 'r', 'r-leg')
        self.relate('connect', 'r-leg', 'x-cross')

    def box(self, name, left, top, right, bottom, r=3):
        points = [(left + r, top), (right - r, top), (right, top + r), (right, bottom - r), (right - r, bottom), (left + r, bottom), (left, bottom - r), (left, top + r)]
        members = []
        for i, a in enumerate(points):
            b = points[(i + 1) % 8]
            part = f'{name}-{i}'
            if i % 2:
                self.add_arc(part, a, b, radius_x=r)
            else:
                self.add_line(part, a, b)
            members.append(part)
        self.add_contour(name, *members, closed=True)

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '8b8b9c1b9e7fc733f1d73fc9f5491773600c1f1dd6fdfa27eb2cc3b8ebb45a7b', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'e0b1e330-cc81-522c-9a29-44fd4f8881cf'}
