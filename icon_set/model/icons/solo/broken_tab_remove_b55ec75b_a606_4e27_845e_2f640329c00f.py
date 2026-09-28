"""A broken tab with an X on its separated right fragment.
Symbol plan: No useful broken-tab match; source fracture layout, with coherent rounded exterior corners.
Reduction: None.
Keyshape: HRECT_M; exact bounds are obtained from the model.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='b55ec75b-a606-4e27-845e-2f640329c00f'
SOURCE_PATH='icon_set/work/todo-references/broken tab remove_b55ec75b-a606-4e27-845e-2f640329c00f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='broken-tab-remove'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('broken', 'tab', 'remove')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('left-main',(8,10),(14,10),(8,24),(14,38),(8,38))
        self.add_arc('left-bl',(8,38),(4,34),radius_x=4)
        self.add_line('left-wall',(4,34),(4,14))
        self.add_arc('left-tl',(4,14),(8,10),radius_x=4)
        self.relate('connect','left-main','left-bl');self.relate('connect','left-main','left-tl')
        self.relate('connect','left-wall','left-bl');self.relate('connect','left-wall','left-tl')
        self.add_line('right-top',(24,10),(40,10))
        self.add_arc('right-tr',(40,10),(44,14),radius_x=4)
        self.add_line('right-wall',(44,14),(44,34))
        self.add_arc('right-br',(44,34),(40,38),radius_x=4)
        self.add_polyline('fracture',(40,38),(24,38),(18,24),(24,10))
        self.add_contour('fragment','right-top','right-tr','right-wall','right-br','fracture-1','fracture-2','fracture-3',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='fracture']
        self.add_polyline('cross-a',(29,21),(32,24),(35,27))
        self.add_polyline('cross-b',(29,27),(32,24),(35,21));self.relate('connect','cross-a','cross-b')

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
