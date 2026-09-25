"""Browser advertisement using the exact, unscaled native typeface v2 A and D.
The frame is expanded to (4,4)-(44,44) centerlines to preserve glyph clearance.
This exceeds the approved SOLO48 SQUARE keyshape. No validation rules are waived.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.primitives import Bezier,Point
SOURCE_ICON_ID='24fe2386-b951-48d1-8a50-9d4e65f27e91'
SOURCE_PATH='pictographic-primitives/other/ui webpage ad text_24fe2386-b951-48d1-8a50-9d4e65f27e91.svg'
AUTHOR='gpt-6'
TYPEFACE_SOURCE='icon_set/typeface/glyphs-v2.json'
GLYPH_PROVENANCE={'A': {'source_path': 'Letters/new/A.svg', 'svg_sha256': '958cc5c66707801c397be5d2ab77f3acfe8b4d828d20846827d30369d71b9c05'}, 'D': {'source_path': 'Letters/new/D.svg', 'svg_sha256': '81d4ead52b6a385f2ec5f17b91748e14ed0c9832884948a0cba5b70c43b4b0bc'}}
class Drawing(Solo48):
    icon_id='ui-webpage-ad-text'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=('advertisement window',)
    keywords=('ad','advertisement','browser','typeface v2')
    def build(self):
        # Browser owns a joined header; native glyphs are translated, never scaled.
        pts=[(8,4),(40,4),(44,8),(44,40),(40,44),(8,44),(4,40),(4,8)]
        ids=[]
        for i,p in enumerate(pts):
            q=pts[(i+1)%8];n=f'frame-{i}';ids.append(n)
            if i%2:self.add_arc(n,p,q,radius_x=4)
            else:self.add_line(n,p,q)
        self.add_contour('frame',*ids,closed=True)
        self.add_line('header',(4,12),(44,12))
        self.relate('connect','frame','header')
        self.primitives.append(Bezier('A-0-0',Point(*(12.0, 35.9998)),Point(*(12.000060000000001, 23.99994)),(((12.0, 35.9998),(12.000060000000001, 27.99984),(12.000060000000001, 23.99994)),)))
        self.primitives.append(Bezier('A-0-1',Point(*(12.000060000000001, 23.99994)),Point(*(20.0, 23.99993)),(((12.000060000000001, 20.00003),(20.0, 20.0),(20.0, 23.99993)),)))
        self.primitives.append(Bezier('A-0-2',Point(*(20.0, 23.99993)),Point(*(20.0, 35.9999)),(((20.0, 25.42069),(20.0, 35.9999),(20.0, 35.9999)),)))
        self.add_contour('A-0',*['A-0-0', 'A-0-1', 'A-0-2'],closed=False)
        self.add_line('A-1-0',(12.0, 31.0701),(20.0, 31.0701))
        self.add_contour('A-1',*['A-1-0'],closed=False)
        self.add_line('D-0-0',(28.0, 21.0),(31.25788, 21.0))
        self.primitives.append(Bezier('D-0-1',Point(*(31.25788, 21.0)),Point(*(36.0, 28.5)),(((33.8769, 21.0),(36.0, 24.35786),(36.0, 28.5)),)))
        self.primitives.append(Bezier('D-0-2',Point(*(36.0, 28.5)),Point(*(31.25788, 36.0)),(((36.0, 32.6421),(33.8769, 36.0),(31.25788, 36.0)),)))
        self.add_line('D-0-3',(31.25788, 36.0),(28.0, 36.0))
        self.add_line('D-0-4',(28.0, 36.0),(28.0, 21.0))
        self.add_contour('D-0',*['D-0-0', 'D-0-1', 'D-0-2', 'D-0-3', 'D-0-4'],closed=True)
        self.relate('connect','A-0','A-1')

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '398d3a872adfdc9fb093f8c6084bc63933136de78be88c8ced82976aa2a658dc', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '24fe2386-b951-48d1-8a50-9d4e65f27e91'}
