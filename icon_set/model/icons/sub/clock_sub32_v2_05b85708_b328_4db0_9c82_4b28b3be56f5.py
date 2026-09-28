"""Independent 32px profile of clock.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '05b85708-b328-4db0-9c82-4b28b3be56f5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/office/clock_05b85708-b328-4db0-9c82-4b28b3be56f5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('05b85708-b328-4db0-9c82-4b28b3be56f5', 'pictographic-primitives/office/clock_05b85708-b328-4db0-9c82-4b28b3be56f5.svg'), ('4ab76b4c-c88a-4586-b84f-4ffd7244d650', 'pictographic-primitives/office/clock_4ab76b4c-c88a-4586-b84f-4ffd7244d650.svg'), ('9f37004b-ad82-4bff-ba0a-63d3fdc12e97', 'pictographic-primitives/office/clock_9f37004b-ad82-4bff-ba0a-63d3fdc12e97.svg'), ('e7f654f6-570d-40dd-84e5-be7ff0923e87', 'pictographic-primitives/office/clock_e7f654f6-570d-40dd-84e5-be7ff0923e87.svg'), ('282df875-ad80-4f27-9f87-f3b69a27f229', 'pictographic-primitives/office/clock_282df875-ad80-4f27-9f87-f3b69a27f229.svg'))
PROFILE_SOURCE_KEYS = ('solo/clock', 'solo/clock-4ab76b4c', 'solo/clock-9f37004b', 'solo/clock-e7f654f6', 'solo/clock-office')
SOLO_SOURCE_ICON_IDS = ('clock', 'clock-4ab76b4c', 'clock-9f37004b', 'clock-e7f654f6', 'clock-office')
REFERENCE_EXPORT_SHA256 = '67967de3ce3da04a245c136daacce4ac2b999fd318a8e7fa7ed24de1c16aa015'

class DrawingVariant2(Sub32):
    icon_id = 'clock-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'office'
    categories = ('office', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular clock with connected upright minute hand and right-facing hour hand. Construction reference: clock."""
        circle(self, 'frame', 16, 16, 14)
        self.add_polyline('hands', (16, 9), (16, 16), (21, 16))

def box(s, n, l, t, r, b, k=3):
    points = [(l + k, t), (r - k, t), (r, t + k), (r, b - k), (r - k, b), (l + k, b), (l, b - k), (l, t + k)]
    members = []
    for i, p in enumerate(points):
        q = points[(i + 1) % 8]
        name = f'{n}-{i}'
        if i % 2:
            s.add_arc(name, p, q, radius_x=k)
        else:
            s.add_line(name, p, q)
        members.append(name)
    s.add_contour(n, *members, closed=True)

def circle(s, n, cx, cy, r):
    s.add_arc(n + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
    s.add_arc(n + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
    s.add_contour(n, n + '-top', n + '-bottom', closed=True)
