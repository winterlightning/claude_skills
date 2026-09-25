"""A horned standing devil with a curling arrow tail. Simplify body to a figure silhouette; the tail intentionally extends right."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08403821-8001-5c1f-9788-1e4dc890984f'
SOURCE_PATH = 'pictographic-primitives/religion/devil_08403821-8001-5c1f-9788-1e4dc890984f.svg'
AUTHOR = 'gpt-6'


class DevilFigureWithTail(Solo48):
    icon_id = 'devil-figure-with-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('devil', 'demon', 'figure', 'horn', 'tail', 'arrowhead')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Live square centerline extremes (6,6)-(42,42).
        self.add_arc('head-top',(8,12),(20,12),radius_x=6)
        self.add_arc('head-bottom',(20,12),(8,12),radius_x=6)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('horn-left',(8,12),(6,6))
        self.add_line('horn-right',(20,12),(22,6))
        self.relate('connect','head','horn-left');self.relate('connect','head','horn-right')
        self.add_arc('shoulders',(6,35),(22,35),radius_x=8)
        self.add_polyline('body',(22,35),(20,42),(8,42),(6,35))
        self.relate('connect','shoulders','body')
        self.add_line('tail-base',(22,35),(26,35))
        self.add_arc('tail-curl',(26,35),(34,27),radius_x=8,sweep=False)
        self.add_line('tail-tip',(34,27),(42,18))
        self.add_contour('tail','tail-base','tail-curl','tail-tip')
        self.add_polyline('arrow',(33,18),(42,18),(42,27))
        self.relate('connect','tail','arrow');self.relate('connect','tail','body');self.relate('connect','tail','shoulders')
