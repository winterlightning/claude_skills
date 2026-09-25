"""Sweeping swift bird silhouette with three angular feather tips. Omit the surrounding circle to give the bird and feather gaps the full square envelope."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3981b3ac-7804-4133-9218-902547a433cd'
SOURCE_PATH = 'pictographic-primitives/logos/swift logo_3981b3ac-7804-4133-9218-902547a433cd.svg'
AUTHOR = 'gpt-6'

class SwiftBirdLogo(Solo48):
    icon_id = 'swift-bird-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('swift', 'apple', 'programming', 'language', 'bird', 'logo', 'brand')

    def build(self):
        # Plan: Sweeping swift bird silhouette with three angular feather tips. Omit the surrounding circle to give the bird and feather gaps the full square envelope.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        nodes=[(6,24),(18,28),(12,14),(28,24),(24,6)]
        for j,a in enumerate(nodes[:-1]):self.add_line('feather-'+str(j),a,nodes[j+1])
        self.add_bezier('back',(24,6),((36,14),(40,23),(36,31)),((40,34),(42,38),(42,42)),((34,36),(31,40),(24,40)),((14,40),(8,38),(6,36)))
        self.add_line('tip',(6,36),(6,24))
        self.add_contour('bird',*[f'feather-{j}' for j in range(4)],'back','tip',closed=True)

