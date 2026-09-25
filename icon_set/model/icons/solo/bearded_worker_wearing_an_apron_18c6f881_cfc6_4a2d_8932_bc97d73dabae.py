"""A swept-haired, bearded worker with an apron bib.

VRECT_L (8,4)-(40,44); face centred at24,18, circular jaw r12.
Human user.svg informs rounded open shoulders and circular jaw; Lucide
hat-glasses informs headwear contour economy, not the asymmetric swept hair.
The source supplies hair, beard and apron. Shoulder top34 is exactly4 below
jaw bottom30. Paired apron joins use 6-8-10 points on shoulder arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '18c6f881-cfc6-4a2d-8932-bc97d73dabae'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/avatar butcher barber_18c6f881-cfc6-4a2d-8932-bc97d73dabae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bearded-worker-wearing-an-apron'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('Bearded Man Wearing Apron',)
    keywords = ('worker','beard','body-apron','hair','bust','person','butcher')

    def build(self):
        self.add_bezier('hair',(12,18),((12,0),(26,8),(36,4)),((36,8),(36,12),(36,14)))
        self.add_line('hair-side',(36,14),(36,18))
        self.add_contour('hair-outline','hair','hair-side')
        self.add_bezier('fringe',(12,18),((20,4),(27,18),(36,14)))
        self.add_arc('jaw',(36,18),(12,18),radius_x=12)
        self.add_bezier('beard',(12,18),((16,26),(19,22),(24,22)),((29,22),(32,26),(36,18)))
        self.relate('connect','hair-outline','fringe','jaw','beard')
        top=30+HEAD_BODY_CENTERLINE_GAP
        for side,pts in [('left',[(8,44),(12,36),(18,top)]),('right',[(30,top),(36,36),(40,44)])]:
            for i,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'body-shoulder-{side}-{i}',a,b,radius_x=10)
            self.add_contour('body-'+side,f'body-shoulder-{side}-0',f'body-shoulder-{side}-1')
        self.add_line('body-top',(18,top),(30,top))
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-right','body-top')
        self.relate('connect','jaw','body-top')
        self.add_polyline('body-apron',(12,36),(12,44),(36,44),(36,36))
        self.relate('connect','body-apron','body-left')
        self.relate('connect','body-apron','body-right')
