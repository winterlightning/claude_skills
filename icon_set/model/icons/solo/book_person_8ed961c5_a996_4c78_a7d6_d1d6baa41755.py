"""Book bearing a person with curved arms.
Plan: Tall book and lower page band. Head bottom y19 and torso start y27 give exactly 8 centerline / 4 ink units. Head and torso align at x24; central straight shoulders join tangent outer curves.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='8ed961c5-a996-4c78-a7d6-d1d6baa41755'
SOURCE_PATH = 'pictographic-primitives/other/book person_8ed961c5-a996-4c78-a7d6-d1d6baa41755.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='book-person'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('book', 'person')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.rounded('book',8,4,40,44,4,breaks={2:[(40,36)],6:[(8,36)]})
        self.add_line('pages',(8,36),(40,36));self.relate('connect','pages','book')
        self.circle('head',24,16,3)
        self.add_bezier('arm-left',(17,25),((18,26),(20,27),(22,27)))
        self.add_line('shoulder-left',(22,27),(24,27))
        self.add_line('shoulder-right',(24,27),(26,27))
        self.add_bezier('arm-right',(26,27),((28,27),(30,26),(31,25)))
        self.relate('connect','arm-left','shoulder-left')
        self.relate('connect','shoulder-left','shoulder-right')
        self.relate('connect','shoulder-right','arm-right')
        self.add_polyline('torso',(24,27),(24,28));self.relate('connect','shoulder-left','torso');self.relate('connect','shoulder-right','torso')
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
        # Head bottom19, torso start27 => exact8 centerline /4 ink; front-facing axis x24.

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

PLAN = 'Book bearing a person with curved arms. Tall book and lower page band.'
OMISSIONS = 'None.'
CONSTRUCTION_REFERENCES = ['icon_set/references/lucide/original/book-user.svg', 'icon_set/references/lucide/atomic-debug/book-user.svg', 'icon_set/references/human_ref/user.svg', 'icon_set/references/human_ref/full_body_ref.png']
PARENT_SOURCE = 'icon_set/model/icons/solo/book_person_8ed961c5_a996_4c78_a7d6_d1d6baa41755.py'
