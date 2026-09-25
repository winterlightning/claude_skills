"""amazon-web-service-game-tech: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7558136-8e09-4d56-8e82-dd4c66e81553'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon web service game tech_a7558136-8e09-4d56-8e82-dd4c66e81553.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AmazonWebServiceGameTech(Solo48):
    icon_id = 'amazon-web-service-game-tech'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('amazon', 'web', 'service', 'game', 'tech', '_uncategorized_02')

    def build(self):
        # Plan: HRECT_L (4,8)-(44,40); mirrored shoulders and grips; smooth tangent joins throughout.
        # Reference: Lucide gamepad-2: flowing controller silhouette and paired grips.
        axis = 24
        # Mirrored shoulders and grips are generated from the same left-side definition.
        for side,mirror in [('left',False),('right',True)]:
            def p(x,y):return (2*axis-x,y) if mirror else (x,y)
            self.add_arc(side+'-shoulder',p(4,18),p(12,8),radius_x=8,radius_y=10,sweep=not mirror)
            self.add_bezier(side+'-top',p(12,8),(p(16,8),p(16,12),p(20,12)))
            self.add_line(side+'-wall',p(4,34),p(4,18))
            self.add_arc(side+'-heel',p(10,40),p(4,34),radius_x=6,sweep=not mirror)
            self.add_bezier(side+'-grip',p(18,30),(p(14,30),p(14,40),p(10,40)))
        # Orient right side in the reverse direction to close the contour.
        from dataclasses import replace
        from ...primitives import Arc,Bezier
        for i,q in enumerate(self.primitives):
            if q.element_id.startswith('right'):
                if isinstance(q,Bezier):
                    c1,c2,end=q.segments[0]
                    self.primitives[i]=Bezier(q.element_id,q.end,q.start,((c2,c1,q.start.as_tuple()),))
                elif isinstance(q,Arc):self.primitives[i]=replace(q,start=q.end,end=q.start,sweep=not q.sweep)
                else:self.primitives[i]=replace(q,start=q.end,end=q.start)
        self.add_line('top',(20,12),(28,12))
        self.add_line('underside',(30,30),(18,30))
        self.add_contour('outline','left-shoulder','left-top','top','right-top','right-shoulder','right-wall','right-heel','right-grip','underside','left-grip','left-heel','left-wall',closed=True)
