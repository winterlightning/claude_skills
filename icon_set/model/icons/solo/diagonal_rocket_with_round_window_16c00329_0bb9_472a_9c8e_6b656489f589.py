"""Diagonal rocket with a circular window, two angular fins and detached exhaust.
SQUARE extremes (6,6)-(42,42) preserve the source direction. Lucide rocket
contributes tapered body flow and integrated fins. One closed silhouette owns
fins and fuselage, symmetric about x+y=48; window sits on that axis.
Nose seam omitted and flame simplified to one exhaust stroke for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '16c00329-0bb9-472a-9c8e-6b656489f589'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/rocket ship_16c00329-0bb9-472a-9c8e-6b656489f589.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'diagonal-rocket-with-round-window'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ['Launching Space Rocket Ship']
    keywords = ['rocket','space','window','fin','flame','spacecraft']
    def build(self):
        points=[(12,24),(6,28),(6,16),(16,16)]
        for j in range(3): self.add_line(f'left-{j}',points[j],points[j+1])
        self.add_bezier('nose-left',(16,16),((22,8),(34,6),(42,6)))
        self.add_bezier('nose-right',(42,6),((42,14),(40,26),(32,32)))
        right=[(32,32),(32,42),(20,42),(24,36),(12,24)]
        for j in range(4): self.add_line(f'right-{j}',right[j],right[j+1])
        self.add_contour('silhouette',*[f'left-{j}' for j in range(3)],'nose-left','nose-right',*[f'right-{j}' for j in range(4)],closed=True)
        self.add_arc('window-top',(25,20),(31,20),radius_x=3)
        self.add_arc('window-bottom',(31,20),(25,20),radius_x=3)
        self.add_contour('window','window-top','window-bottom',closed=True)
        self.add_line('exhaust',(6,42),(10,38))
