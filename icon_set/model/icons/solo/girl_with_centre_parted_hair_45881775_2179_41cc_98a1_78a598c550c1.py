"""A small front-facing girl has a round blank face beneath centrally parted hair curling outward at the sides. Her simple body has short sleeves and a long tapered lower section.
Symbol plan: Circular face with outward hair curls, smooth broad dress and paired legs. Shared head radius 6; body top y24 yields exact 4-unit ink gap. Omit the interior hair part, duplicate hair cap and sleeves; keep the circular face and symmetric outward hair curls.
Keyshape: VRECT_L, centerline extremes (8,4)-(40,44).
Construction reference: human_ref/full_body_ref.png; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '45881775-2179-41cc-98a1-78a598c550c1'
SOURCE_PATH = 'pictographic-primitives/avatars/girl full body_45881775-2179-41cc-98a1-78a598c550c1.svg'
AUTHOR = 'gpt-6'
SOURCE_CATEGORY = 'avatars'

class BatchSolo(Solo48):
    icon_id = 'girl-with-centre-parted-hair'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('girl', 'with', 'centre', 'parted', 'hair')

    def build(self):

        def segments(name, *points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def rect(name, l,t,r,b, radius=0):
            if not radius:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            q=radius
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z: continue
                part=f'{name}-{j}'
                if j%2: self.add_arc(part,a,z,radius_x=q)
                else: self.add_line(part,a,z)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        def axes():
            self.add_line('axis-y',(6,6),(6,38))
            self.add_arc('axis-corner',(6,38),(10,42),radius_x=4,sweep=False)
            self.add_line('axis-x',(10,42),(42,42))
            self.add_contour('axes','axis-y','axis-corner','axis-x')

        circle('head',24,10,6)
        self.add_arc('hair-left',(18,10),(8,20),radius_x=10)
        self.add_arc('hair-right',(40,20),(30,10),radius_x=10)
        self.relate('connect','hair-left','head')
        self.relate('connect','hair-right','head')
        self.add_arc('shoulder-left',(12,36),(24,24),radius_x=12)
        self.add_arc('shoulder-right',(24,24),(36,36),radius_x=12)
        segments('hem',(36,36),(28,36),(20,36),(12,36))
        self.add_contour('dress','shoulder-left','shoulder-right','hem-1','hem-2','hem-3',closed=True)
        for x in (20,28):
         self.add_line(f'leg-{x}',(x,36),(x,44))
         self.relate('connect',f'leg-{x}','dress')
