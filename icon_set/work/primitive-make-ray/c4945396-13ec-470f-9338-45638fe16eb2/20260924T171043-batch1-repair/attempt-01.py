"""AWS MediaLive play triangle with three media nodes and scan marks."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c4945396-13ec-470f-9338-45638fe16eb2"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon web service elemental medialive_c4945396-13ec-470f-9338-45638fe16eb2.svg'
AUTHOR = 'gpt-6'


class AmazonElementalMediaLive(Solo48):
    icon_id = "amazon-elemental-medialive"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/media"
    aliases = ("aws-medialive",)
    keywords = ("amazon", "aws", "media", "live", "play", "stream")

    def build(self):
        # Plan: central play triangle, three repeated media nodes and scan arrows.
        # VRECT_L centerline extremes (8,4)-(40,44). Small hexagons simplified to circles.
        self.add_polyline('play',(18,18),(30,25),(18,32),closed=True)
        for name,cx,cy in [('top',24,7),('left',11,41),('right',37,41)]:
            self.add_arc(name+'-upper',(cx-3,cy),(cx+3,cy),radius_x=3)
            self.add_arc(name+'-lower',(cx+3,cy),(cx-3,cy),radius_x=3)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)
        self.add_polyline('scan-left',(8,24),(8,18),(12,16))
        self.add_polyline('scan-right',(40,24),(40,18),(36,16))
        self.add_polyline('scan-bottom',(22,42),(24,44),(26,42))
