"""A standing therapist bends one arm over a reclining person to hold a round herbal compress against the back. The patient's circular head rests at the right of a horizontal body.
Symbol plan: Standing therapist and reclining patient with equal radius-4 circular heads. Therapist torso starts at (8,24); patient torso starts at (28,36), proving exact 4-unit head gaps. Compress is a radius-4 circle physically touching the back; omit bed and clothing outlines.
Keyshape: HRECT_L; centerline extremes (4,8)-(44,40).
Construction reference: human_ref/full_body_ref.png; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7dc22fbf-39be-4ccf-911b-cf43b14058ef'
SOURCE_PATH = 'pictographic-primitives/beauty/herbal compress people_7dc22fbf-39be-4ccf-911b-cf43b14058ef.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'therapist-applying-herbal-compress'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    aliases = ()
    keywords = ('therapist', 'applying', 'herbal', 'compress')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        circle('therapist-head',8,12,4)
        self.add_line('therapist-torso',(8,24),(8,36))
        self.add_line('arm',(8,24),(24,28))
        self.relate('connect','arm','therapist-torso')
        self.add_arc('compress-a',(24,28),(24,36),radius_x=4)
        self.add_arc('compress-b',(24,36),(24,28),radius_x=4)
        self.add_contour('compress','compress-a','compress-b',closed=True)
        self.relate('connect','compress','arm')
        circle('patient-head',40,36,4)
        self.add_line('patient-torso',(28,36),(24,36))
        self.add_line('patient-body',(24,36),(16,36))
        self.add_contour('patient','patient-torso','patient-body')
        self.relate('connect','patient','compress')
        self.mark_human_figure('therapist',head='therapist-head',torso='therapist-torso',torso_junction='start')
        self.mark_human_figure('patient',head='patient-head',torso='patient-torso',torso_junction='start')
