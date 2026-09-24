"""A right-facing head profile with a detached puzzle piece above its missing upper-left section.

Plan: Asymmetric continuous anatomical profile and detached puzzle piece. SQUARE extremes (6,6)-(42,42). Shared human-reference.md and user.svg inform smooth head construction; this continuous-neck profile is not a detached stick figure, so no head/body gap flag applies. No useful Lucide match for this specific puzzle silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4a264e06-6d44-57cc-8176-d57369c6c0ee'
SOURCE_PATH = 'icon_set/work/todo-references/autism disorder symptoms_4a264e06-6d44-57cc-8176-d57369c6c0ee.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'autism-disorder-symptoms'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('autism', 'disorder', 'symptoms')
    def build(self):
        self.add_line('neck-back',(18,42),(18,36))
        self.add_arc('skull-back',(18,36),(14,26),radius_x=14)
        self.add_line('socket-left',(14,26),(18,26))
        self.add_arc('socket',(18,26),(26,26),radius_x=4,sweep=False)
        self.add_line('socket-right',(26,26),(28,26))
        self.add_arc('puzzle-nub',(28,26),(28,18),radius_x=4,sweep=False)
        self.add_line('forehead-top',(28,18),(28,12))
        self.add_arc('forehead',(28,12),(38,24),radius_x=12)
        self.run('nose',(38,24),(42,30),(38,30),(38,34))
        self.add_arc('jaw',(38,34),(34,38),radius_x=4)
        self.run('neck-front',(34,38),(32,38),(32,42))
        self.add_contour('profile','neck-back','skull-back','socket-left','socket','socket-right','puzzle-nub','forehead-top','forehead','nose-1','nose-2','nose-3','jaw','neck-front-1','neck-front-2')
        self.add_arc('piece-crown',(6,14),(18,6),radius_x=12)
        self.run('piece-top',(18,6),(22,6),(22,10))
        self.add_arc('piece-notch',(22,10),(22,16),radius_x=3,sweep=False)
        self.run('piece-right',(22,16),(22,20),(17,20))
        self.add_arc('piece-tab',(17,20),(11,20),radius_x=3)
        self.run('piece-left',(11,20),(11,16),(6,14))
        self.add_contour('piece','piece-crown','piece-top-1','piece-top-2','piece-notch','piece-right-1','piece-right-2','piece-tab','piece-left-1','piece-left-2',closed=True)

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def roundrect(self,name,x0,y0,x1,y1,r):
        nodes=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        for i,a in enumerate(nodes):
            b=nodes[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

    def run(self,name,*points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f"{name}-{i}",a,b)
