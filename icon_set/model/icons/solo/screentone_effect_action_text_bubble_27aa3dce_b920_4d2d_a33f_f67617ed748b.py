from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='27aa3dce-b920-4d2d-a33f-f67617ed748b'
SOURCE_PATH='icon_set/work/todo-references/screentone effect action text bubble_27aa3dce-b920-4d2d-a33f-f67617ed748b.svg'
AUTHOR='gpt-6'
PLAN='Empty comic action bubble with inward-curving edges and six detached action rays. Opposite sides mirror around (24,24).'
CONSTRUCTION_REFERENCES='No useful exact Lucide match; source provides the concave burst and ray pattern.'
OMISSIONS='Ray lengths reduced to preserve surrounding space; all six rays retained.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='screentone-effect-action-text-bubble'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases=()
    keywords=('screentone', 'effect', 'action', 'text', 'bubble')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8];part=f'{name}-{i}';members.append(part)
            if i%2:self.add_arc(part,a,b,radius_x=r)
            else:self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def magnifier(self):
        # The handle node (30,33) is exactly radius 15 from (21,21).
        pts=[(6,21),(21,6),(36,21),(30,33),(6,21)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_arc(f'lens-{i}',a,b,radius_x=15)
        self.add_contour('lens',*(f'lens-{i}' for i in range(4)),closed=True)
        self.add_line('handle',(30,33),(42,42));self.relate('connect','lens','handle')

    def score(self,y):
        self.add_arc('two-top',(12,y+4),(20,y+4),radius_x=4)
        self.add_polyline('two-bottom',(20,y+4),(12,y+12),(20,y+12));self.relate('connect','two-top','two-bottom')
        for i,cy in enumerate((y+3,y+11)):self.add_dot(f'colon-{i}',(25,cy))
        self.box('zero',31,y,8,12,4)

    def terminal(self):
        self.box('screen',6,6,36,28,3)
        self.add_line('stand',(24,34),(24,42));self.relate('connect','screen','stand')
        self.add_polyline('foot',(16,42),(24,42),(32,42));self.relate('connect','stand','foot')
        for i,y in enumerate((18,26)):self.add_line(f'equals-{i}',(31,y),(35,y))

    def send(self,direction):
        self.box('panel',6,6,36,36,4)
        if direction=='left':
            self.add_polyline('head',(23,17),(16,24),(23,31));self.add_line('shaft',(16,24),(33,24))
        else:
            self.add_polyline('head',(25,17),(32,24),(25,31));self.add_line('shaft',(32,24),(15,24))
        self.relate('connect','head','shaft')

    def build(self):
        self.add_bezier('burst',(6,24),((10,23),(12,20),(10,16)),((14,18),(17,15),(18,13)),((22,17),(26,17),(30,13)),((31,15),(34,18),(38,16)),((36,20),(38,23),(42,24)),((38,25),(36,28),(38,32)),((34,30),(31,33),(30,35)),((26,31),(22,31),(18,35)),((17,33),(14,30),(10,32)),((12,28),(10,25),(6,24)))
        for name,a,b in [('top',(24,6),(24,7)),('bottom',(24,41),(24,42)),('nw',(8,6),(9,7)),('ne',(39,7),(40,6)),('sw',(8,42),(9,41)),('se',(39,41),(40,42))]:self.add_line('ray-'+name,a,b)

KEYSHAPE_REASON='The complete composition uses centerline extremes (6,6)–(42,42).'
FINAL_REDUCTIONS='Ray lengths reduced to preserve surrounding space; all six rays retained.'
