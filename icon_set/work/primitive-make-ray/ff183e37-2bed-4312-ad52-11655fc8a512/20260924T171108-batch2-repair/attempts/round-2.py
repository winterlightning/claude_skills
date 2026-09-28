"""A curled bird profile with a separate upper-right leaf.
Symbol plan: bird: coherent curved silhouette; supplied Bower reference owns the curl, beak and leaf.
Reduction: Short mouth divider omitted; tail represented by one broad curve.
Keyshape: SQUARE; exact bounds are obtained from the model.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='ff183e37-2bed-4312-ad52-11655fc8a512'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/bower logo_ff183e37-2bed-4312-ad52-11655fc8a512.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id='bower-logo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('bower', 'logo')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_bezier('curl',(17,25),((23,25),(25,23),(25,20)),((25,12),(22,6),(18,6)))
        self.add_bezier('back',(18,6),((11,6),(6,16),(6,25)),((6,34),(12,39),(20,39)))
        self.add_contour('bird','curl','back')
        self.add_bezier('beak',(25,20),((28,24),(38,24),(42,24)),((42,30),(36,33),(29,33)))
        self.add_bezier('tail',(29,33),((31,36),(33,38),(35,40)),((33,41),(30,42),(27,42)),((24,42),(22,41),(20,39)))
        self.relate('connect','bird','tail');self.relate('connect','beak','tail');self.relate('connect','bird','beak')
        self.add_bezier('leaf-a',(42,6),((42,12),(42,16),(38,16)))
        self.add_bezier('leaf-b',(38,16),((32,16),(32,6),(42,6)))
        self.add_contour('leaf','leaf-a','leaf-b',closed=True)
    def circle(self,name,cx,cy,r):
        pts=[(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            m=f'{name}-{i}';self.add_arc(m,a,b,radius_x=r);members.append(m)
        self.add_contour(name,*members,closed=True)

    def rounded(self,name,l,t,r,b,rad,breaks=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad),(l+rad,t)]
        members=[];breaks=breaks or {}
        for i,(a,z) in enumerate(zip(pts,pts[1:])):
            if i%2:
                m=f'{name}-{i}';self.add_arc(m,a,z,radius_x=rad);members.append(m)
            else:
                nodes=[a]+breaks.get(i,[])+[z]
                for j,(start,end) in enumerate(zip(nodes,nodes[1:])):
                    if start==end:continue
                    m=f'{name}-{i}-{j}';self.add_line(m,start,end);members.append(m)
        self.add_contour(name,*members,closed=True)


    def browser(self):
        self.rounded('window',8,4,40,44,4,breaks={2:[(40,12)],6:[(8,12)]})
        self.add_line('header',(8,12),(40,12));self.relate('connect','header','window')

    def dollar(self,x,y):
        self.add_bezier('dollar',(x+4,y-6),((x+2,y-7),(x+1,y-7),(x,y-7)),((x-7,y-7),(x-7,y),(x,y)),((x+7,y),(x+7,y+7),(x,y+7)),((x-1,y+7),(x-2,y+7),(x-4,y+6)))
        self.add_line('stem-top',(x,y-8),(x,y-7));self.relate('connect','dollar','stem-top')
        self.add_line('stem-bottom',(x,y+7),(x,y+8));self.relate('connect','dollar','stem-bottom')

    def euro(self,x):
        self.add_bezier('euro',(x+3,22),((x-2,19),(x-8,21),(x-8,28)),((x-8,35),(x-2,37),(x+3,34)))
        self.add_polyline('crossbar',(x-11,28),(x-8,28),(x,28));self.relate('connect','euro','crossbar')
