"""A bunting stage with a tilted microphone on a short tripod.

HRECT_L extrema (4,8)-(44,40). Pennant tips repeat about x=24; the mic is
deliberately offset, as in the source. Lucide mic-vocal informs head/arm join.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a37d9a40-16b7-4abd-b2f5-962b0ceb5244"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_12/concert microphone_a37d9a40-16b7-4abd-b2f5-962b0ceb5244.svg'
AUTHOR = "gpt-6"


class ConcertStageWithSinger(Solo48):
    icon_id = "concert-stage-with-singer"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music/performance"
    aliases = ("concert microphone", "stage with microphone")
    keywords = ("bunting", "tripod", "stand", "pennants")

    def build(self) -> None:
        self.add_polyline("stage",(4,40),(4,8),(24,8),(44,8),(44,40))
        self.add_polyline("pennants",(4,8),(14,18),(24,8),(34,18),(44,8))
        self.relate("connect","stage","pennants")
        points=[(14,29),(17,26),(20,29),(17,32),(14,29)]
        parts=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            name=f"mic-{i}"
            self.add_arc(name,a,b,radius_x=3,radius_y=3,sweep=True)
            parts.append(name)
        self.add_contour("microphone",*parts,closed=True)
        self.add_line("angled-arm",(20,29),(29,29))
        self.add_line("stand",(29,29),(29,35))
        self.add_polyline("feet",(23,40),(29,35),(35,40))
        self.relate("connect","microphone","angled-arm")
        self.relate("connect","angled-arm","stand")
        self.relate("connect","stand","feet")
