"""A reclining person lies horizontally with a circular head at the right. Two small stones sit above the back, while three wavy vertical heat lines rise over the treatment area.
Symbol plan: Reclining patient with radius-4 head at (40,32), torso neck (28,32), and two equal stones resting directly on the back. A rounded open body outline clarifies the reclining pose. Two matched steam trails replace three; omit the arm.
Keyshape: HRECT_L; centerline extremes (4,8)-(44,40).
Construction reference: human_ref/full_body_ref.png. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'adb175ef-3f15-412e-aca0-3c0b32f9b52e'
SOURCE_PATH = 'pictographic-primitives/beauty/hot stone massage person_adb175ef-3f15-412e-aca0-3c0b32f9b52e.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'hot-stone-massage-with-steam'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    aliases = ()
    keywords = ('hot', 'stone', 'massage', 'with', 'steam')

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

        circle('head',40,32,4)
        self.add_line('torso',(28,32),(24,32));self.add_line('back',(24,32),(8,32))
        self.add_arc('body-end',(8,32),(8,40),radius_x=4,sweep=False)
        self.add_line('body-bottom',(8,40),(28,40))
        self.add_contour('body','torso','back','body-end','body-bottom')
        for j,x in enumerate((8,24)):
         self.add_arc(f'stone-{j}-right',(x,24),(x,32),radius_x=4)
         self.add_arc(f'stone-{j}-left',(x,32),(x,24),radius_x=4)
         self.add_contour(f'stone-{j}',f'stone-{j}-right',f'stone-{j}-left',closed=True)
         self.relate('connect',f'stone-{j}','body')
         self.add_bezier(f'steam-{j}',(x+2,8),((x-4,10),(x+6,12),(x,15)))
        self.mark_human_figure('patient',head='head',torso='torso',torso_junction='start')
