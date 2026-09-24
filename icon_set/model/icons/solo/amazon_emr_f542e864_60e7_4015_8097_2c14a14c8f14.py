'A plus-marked circular source hub branching to square data nodes.\nPlan: HRECT_L makes room for the source hub and destination column.\nReduction: Reduced four repeated destination squares to two; retained the plus, circular hub and branching links.\nConstruction: No useful direct Lucide match; supplied reference governs the node network.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "f542e864-60e7-4015-8097-2c14a14c8f14"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon emr_f542e864-60e7-4015-8097-2c14a14c8f14.svg'
AUTHOR = 'gpt-6'


class AmazonEmr(Solo48):
    icon_id = 'amazon-emr'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/cloud"
    aliases = ("elastic-mapreduce",)
    keywords = ("amazon", "aws", "emr", "data", "cluster", "nodes")

    def build(self):
        # Plan: plus-marked circular source with two mirrored square destinations.
        # Four repeated destinations reduced to two to preserve legal open squares.
        # HRECT_L centerlines (4,8)-(44,40); hub attaches at its right apex.
        self.add_arc('hub-top',(4,24),(26,24),radius_x=11)
        self.add_arc('hub-bottom',(26,24),(4,24),radius_x=11)
        self.add_contour('hub','hub-top','hub-bottom',closed=True)
        self.add_polyline('plus-horizontal',(13,24),(15,24),(17,24))
        self.add_polyline('plus-vertical',(15,22),(15,24),(15,26))
        self.relate('connect','plus-horizontal','plus-vertical')
        for name,y in [('top',12),('bottom',36)]:
            self.add_polyline(name+'-node',(36,y),(36,y-4),(44,y-4),(44,y+4),(36,y+4),closed=True)
            self.add_line(name+'-link',(26,24),(36,y))
            self.relate('connect','hub',name+'-link')
            self.relate('connect',name+'-node',name+'-link')
        self.relate('connect','top-link','bottom-link')
