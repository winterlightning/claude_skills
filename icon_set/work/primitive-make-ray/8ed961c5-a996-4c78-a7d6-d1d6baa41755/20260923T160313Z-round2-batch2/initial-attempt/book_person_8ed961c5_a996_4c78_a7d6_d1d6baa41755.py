"""A book carrying a circular head over curved arms and a torso.
Plan: book-user: book cover and pages; human_ref/user.svg and full_body_ref.png: circular head and coherent human strokes.
Reduction: None; book, head, raised arms and torso retained.
Author geometry backwards from the exact VRECT_L envelope.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='8ed961c5-a996-4c78-a7d6-d1d6baa41755'
SOURCE_PATH='icon_set/work/todo-references/book person_8ed961c5-a996-4c78-a7d6-d1d6baa41755.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='book-person'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('book', 'person')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.rounded('book',8,4,40,44,4,breaks={2:[(40,36)],6:[(8,36)]})
        self.add_line('pages',(8,36),(40,36));self.relate('connect','pages','book')
        self.circle('head',24,15,3)
        self.add_arc('arm-left',(16,25),(24,28),radius_x=8,radius_y=3,sweep=False)
        self.add_arc('arm-right',(24,28),(32,25),radius_x=8,radius_y=3,sweep=False)
        self.add_contour('arms','arm-left','arm-right')
        self.add_polyline('torso',(24,26),(24,28),(24,30));self.relate('connect','arms','torso')
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
        # Head bottom18, torso start26 => exact8 centerline /4 ink; front-facing axis x24.

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
