"""A square smartwatch bearing a dollar currency mark.
Symbol plan: watch: attached symmetric straps; dollar-sign: continuous S curve and crossing vertical stem.
Keyshape: VRECT_L; inspect ink_extremes for the fixed profile envelope.
Reduction: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='22b0de95-e0f5-450b-9f1f-9e0284263be7'
SOURCE_PATH='icon_set/work/todo-references/smart watch square dollar sign_22b0de95-e0f5-450b-9f1f-9e0284263be7.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='smart-watch-square-dollar-sign'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smart', 'watch', 'square', 'dollar', 'sign')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.watch()
        self.dollar()

    def circle(self,name,cx,cy,r):
        points=[(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            member=f'{name}-{i}'
            self.add_arc(member,a,b,radius_x=r);members.append(member)
        self.add_contour(name,*members,closed=True)

    def rounded(self,name,l,t,r,b,rad,breaks=None):
        # One owner for all corner radii and genuine attachment nodes.
        points=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad),(l+rad,t)]
        members=[];breaks=breaks or {}
        for i,(a,z) in enumerate(zip(points,points[1:])):
            if i%2:
                member=f'{name}-{i}';self.add_arc(member,a,z,radius_x=rad);members.append(member)
            else:
                nodes=[a]+breaks.get(i,[])+[z]
                for j,(start,end) in enumerate(zip(nodes,nodes[1:])):
                    if start==end: continue
                    member=f'{name}-{i}-{j}';self.add_line(member,start,end);members.append(member)
        self.add_contour(name,*members,closed=True)

    def wifi(self,name,cx,y,rx,ry):
        self.add_arc(name,(cx-rx,y),(cx+rx,y),radius_x=rx,radius_y=ry)

    def watch(self,circular=False):
        if circular:
            nodes=[(12,19),(19,12),(36,29),(29,36),(12,19)]
            members=[]
            for i,(a,b) in enumerate(zip(nodes,nodes[1:])):
                name=f'case-{i}';self.add_arc(name,a,b,radius_x=13);members.append(name)
            self.add_contour('case',*members,closed=True)
            self.add_polyline('strap-top',(12,19),(6,12),(12,6),(19,12))
            self.add_polyline('strap-bottom',(36,29),(42,36),(36,42),(29,36))
        else:
            self.add_polyline('case',(8,24),(12,20),(20,12),(24,8),(40,24),(36,28),(28,36),(24,40),closed=True)
            self.add_polyline('strap-top',(12,20),(6,14),(14,6),(20,12))
            self.add_polyline('strap-bottom',(36,28),(42,34),(34,42),(28,36))
        self.relate('connect','case','strap-top')
        self.relate('connect','case','strap-bottom')

    def dollar(self,cx=24,cy=24):
        self.add_bezier('dollar-upper',(cx+4,cy-6),((cx,cy-9),(cx-5,cy-8),(cx-5,cy-4)),((cx-5,cy-1),(cx-2,cy),(cx,cy)))
        self.add_bezier('dollar-lower',(cx,cy),((cx+3,cy),(cx+5,cy+1),(cx+5,cy+4)),((cx+5,cy+8),(cx,cy+9),(cx-4,cy+6)))
        self.add_contour('dollar','dollar-upper','dollar-lower')
        self.add_polyline('dollar-stem',(cx,cy-10),(cx,cy),(cx,cy+10))
        self.relate('connect','dollar','dollar-stem')

    def pound(self):
        self.add_arc('pound-hook',(30,19),(20,19),radius_x=5,sweep=False)
        self.add_polyline('pound-stem',(20,19),(20,24),(20,29),(18,32),(31,32))
        self.relate('connect','pound-hook','pound-stem')
        self.add_polyline('pound-bar',(16,24),(20,24),(26,24))
        self.relate('connect','pound-bar','pound-stem')
