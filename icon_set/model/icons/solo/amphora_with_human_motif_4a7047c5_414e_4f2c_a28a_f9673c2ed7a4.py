from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a7047c5-414e-4f2c-a28a-f9673c2ed7a4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/culture/batch-03/chinese urn_4a7047c5-414e-4f2c-a28a-f9673c2ed7a4.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'amphora-with-human-motif'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('amphora', 'urn', 'vase', 'pottery', 'handles', 'figure', 'ceramic', 'decoration')

    def build(self):
        # Plan: broad symmetric urn with integrated handles, central human decoration with exact detached gap.
        # Centerline envelope: (6,6)-(42,42). Reference: Lucide amphora mirrored vessel; human_ref/full_body_ref.png for decoration.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        # human_ref/full_body_ref.png: head bottom 18, torso starts 26, exactly 4u ink gap.
        self.add_line('rim',(14,6),(34,6))
        for side in (-1,1):
            def p(x,y):return(24+side*x,y)
            name=str(side)
            self.add_line('neck-'+name,p(10,6),p(10,20));join('neck-'+name,'rim')
            path('handle-'+name,p(10,8),p(18,8),p(18,20),p(10,20));join('handle-'+name,'neck-'+name)
            self.add_bezier('body-'+name,p(10,20),(p(10,23),p(18,24),p(18,28)),(p(18,35),p(8,39),p(8,42)))
            join('body-'+name,'neck-'+name);join('body-'+name,'handle-'+name)
        self.add_line('foot',(16,42),(32,42))
        for side in (-1,1):join('foot','body-'+str(side))
        circle('head',24,16,2)
        self.add_line('torso',(24,26),(24,31))
        self.add_line('arms',(20,26),(28,26));join('torso','arms')
        path('legs',(21,34),(24,31),(27,34));join('legs','torso')
        self.mark_human_figure('decoration',head='head',torso='torso',torso_junction='start')
