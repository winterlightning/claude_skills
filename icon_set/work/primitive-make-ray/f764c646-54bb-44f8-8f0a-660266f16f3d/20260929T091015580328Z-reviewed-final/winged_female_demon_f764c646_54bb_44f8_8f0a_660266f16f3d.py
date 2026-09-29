"""Restore two horns, detached bat wings, a flared dress and an independent curved arrow tail."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f764c646-54bb-44f8-8f0a-660266f16f3d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__winged-female-demon/20260929T085457Z-thuan-mac/reference/succubus_f764c646-54bb-44f8-8f0a-660266f16f3d.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'winged-female-demon'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Retain two horns, separate bat wings, flared dress, two legs and an independent arrow tail. Local wing and tail proximity is needed for the complete fantasy silhouette. Head-to-dress-top ink gap is 4: 23-(10+5)-4=4.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '51102cfb11d6e266100846bf81f908e07e9f89f1237d2a768d9e016c9c3ea905'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('succubus',)
    # Symbol plan: Restore two horns, detached bat wings, a flared dress and an independent curved arrow tail.
    # Construction: human_ref/full_body_ref.png: flared female silhouette; original reference: horns, bat wings and arrow tail.

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

        self.circle('head',24,10,5)
        self.path('left-horn',(20,6),(18,3))
        self.path('right-horn',(28,6),(30,3))
        self.path('dress',(18,26),(15,38),(33,38),(30,26),((18,26),6,3,False,False),closed=True)
        self.add_line('left-leg',(20,38),(20,44))
        self.add_line('right-leg',(28,38),(28,44))
        self.path('left-wing',(13,25),(10,20),(5,21),(4,12),((14,15),12,6,True,False))
        self.path('right-wing',(35,25),(38,20),(43,21),(44,12),((34,15),12,6,False,False))
        self.path('tail',(33,35),((42,29),9,7,False,False),(43,26))
        self.path('tail-point',(38,28),(43,26),(45,31))
        self.relate('connect','tail','tail-point')
        self.relate('connect','head','left-horn')
        self.relate('connect','head','right-horn')
        self.relate('connect','dress','left-leg')
        self.relate('connect','dress','right-leg')
     
