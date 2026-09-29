"""Restore long flowing hair, a seated torso, supporting arm and a sweeping fish tail ending in two fin lobes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '346b37cf-28b6-4072-96cc-679789ce5ec7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-mermaid-with-raised-tail/20260929T085457Z-thuan-mac/reference/fantasy medieval mermaid 2_346b37cf-28b6-4072-96cc-679789ce5ec7.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'seated-mermaid-with-raised-tail'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('fantasy medieval mermaid 2',)
    # Symbol plan: Restore long flowing hair, a seated torso, supporting arm and a sweeping fish tail ending in two fin lobes.
    # Construction: human_ref/full_body_ref.png

    def path(self, name, start, *segments, closed=False):
        ids = []
        point = start
        for j, segment in enumerate(segments):
            eid = f"{name}-{j}"
            if len(segment) == 2:
                self.add_line(eid, point, segment)
                end = segment
            else:
                end, rx, ry, sweep, large = segment
                self.add_arc(eid, point, end, radius_x=rx, radius_y=ry,
                             sweep=sweep, large_arc=large)
            ids.append(eid)
            point = end
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), ((x+r,y),r,r,True,False),
                  ((x-r,y),r,r,True,False), closed=True)

    def oval(self, name, x, y, rx, ry):
        self.path(name, (x-rx,y), ((x+rx,y),rx,ry,True,False),
                  ((x-rx,y),rx,ry,True,False), closed=True)

    def box(self, name, x1,y1,x2,y2,r=3):
        self.path(name, (x1+r,y1), (x2-r,y1),
                  ((x2,y1+r),r,r,True,False), (x2,y2-r),
                  ((x2-r,y2),r,r,True,False), (x1+r,y2),
                  ((x1,y2-r),r,r,True,False), (x1,y1+r),
                  ((x1+r,y1),r,r,True,False), closed=True)

    def build(self):

        # One flowing silhouette; profile face and hair remain continuous anatomy.
        self.path('hair', (10,25), ((8,17),7,9,True,False), (10,13), (10,10),
                  ((22,4),8,7,True,False), ((26,8),5,4,True,False),
                  ((17,11),8,4,True,False), (17,17), ((13,23),5,7,True,False))
        self.path('face-neck', (24,10), (25,15), (22,17), (22,21),
                  ((27,28),7,8,False,False), (31,30))
        self.path('body-tail', (13,24), (12,36), ((25,44),15,9,False,False),
                  ((39,27),15,18,False,False))
        self.path('tail-top', (18,32), ((35,29),14,7,False,False), (35,25))
        self.path('fin', (35,25), ((29,17),7,8,True,False),
                  ((36,21),10,8,True,False), ((42,17),9,8,False,False),
                  ((39,27),6,10,True,False))
        self.path('support-arm', (10,27), (8,40), (8,44))
        self.relate('connect','body-tail','tail-top') if False else None
     
