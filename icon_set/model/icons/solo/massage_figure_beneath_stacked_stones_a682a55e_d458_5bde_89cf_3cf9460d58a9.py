"""A reclining person rests face-down with an arm extended toward the left. Three smooth oval stones of decreasing size are stacked above the curved back, forming a separate vertical pile.
Symbol plan: Reclining patient with radius-4 head at (12,36) and neck (24,36). Three horizontal oval stones share x32 and touch at y12 and y20. The separate pile ends 8 centerline units above the rounded body. Omit the extended arm.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: human_ref/full_body_ref.png. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a682a55e-d458-5bde-89cf-3cf9460d58a9'
SOURCE_PATH = 'pictographic-primitives/beauty/hot stone massage point_a682a55e-d458-5bde-89cf-3cf9460d58a9.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'massage-figure-beneath-stacked-stones'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('massage', 'figure', 'beneath', 'stacked', 'stones')

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

        circle('head',12,36,4)
        self.add_line('torso',(24,36),(36,36))
        self.add_arc('body-end',(36,36),(36,44),radius_x=4)
        self.add_line('body-bottom',(36,44),(24,44));self.add_contour('body','torso','body-end','body-bottom')
        for j,(cy,rx) in enumerate([(8,6),(16,7),(24,8)]):
         self.add_arc(f'stone-{j}-right',(32,cy-4),(32,cy+4),radius_x=rx,radius_y=4)
         self.add_arc(f'stone-{j}-left',(32,cy+4),(32,cy-4),radius_x=rx,radius_y=4)
         self.add_contour(f'stone-{j}',f'stone-{j}-right',f'stone-{j}-left',closed=True)
        self.relate('connect','stone-0','stone-1');self.relate('connect','stone-1','stone-2')
        self.mark_human_figure('patient',head='head',torso='torso',torso_junction='start')
