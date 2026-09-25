"""A closed padlock sits inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: Corner fillets reduced to round joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a7f1734e-4fae-4c0a-9d33-80bf4a3da78f'
SOURCE_PATH = 'pictographic-primitives/other/house lock_a7f1734e-4fae-4c0a-9d33-80bf4a3da78f.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id='house-lock'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/buildings'
    aliases=()
    keywords=('house', 'lock')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def house(self):
        # One mirrored envelope, x=24 axis; centerline extremes 6,6,42,42.
        self.add_line('roof-1',(6,18),(24,6))
        self.add_line('roof-2',(24,6),(42,18))
        self.add_line('wall-right',(42,18),(42,40))
        self.add_arc('corner-right',(42,40),(40,42),radius_x=2)
        self.add_line('floor',(40,42),(8,42))
        self.add_arc('corner-left',(8,42),(6,40),radius_x=2)
        self.add_line('wall-left',(6,40),(6,18))
        self.add_contour('house','roof-1','roof-2','wall-right','corner-right','floor','corner-left','wall-left',closed=True)

    def lock_body(self):
        # Shared shackle nodes are vertices in the top rail.
        self.add_polyline('lock-body',(16,26),(19,26),(29,26),(32,26),(32,34),(16,34),closed=True)

    def build(self):

        self.add_polyline('house',(6,18),(24,6),(42,18),(42,42),(6,42),closed=True);self.lock_body()
        self.add_line('shackle-left',(19,26),(19,22))
        self.add_arc('shackle-top',(19,22),(29,22),radius_x=5)
        self.add_line('shackle-right',(29,22),(29,26))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','shackle','lock-body')

# Final visible envelope: (4,4)-(44,44)
# Visual review: Padlock body and rounded shackle remain distinct. Body inner opening is small but legible.

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'fc60f96f0192e3b42a59c0f6ef3c7620e3c8e61ea967c46bb76030471667fe1e', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'a7f1734e-4fae-4c0a-9d33-80bf4a3da78f'}
