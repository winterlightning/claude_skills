"""A folded velvet sheet with a turned corner and trailing edge.
Symbol plan: rectangle-vertical: consistent rounded cloth corners; source defines the fold hierarchy.
Keyshape: VRECT_L; fixed profile envelope is recorded in ink_extremes.
Reduction: None.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='b285a9ad-1d8d-44fa-8ec0-6e31ab68ccc4'
SOURCE_PATH='icon_set/work/todo-references/velvet_b285a9ad-1d8d-44fa-8ec0-6e31ab68ccc4.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='velvet'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('velvet',)
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_line('sheet-top',(12,4),(36,4))
        self.add_arc('sheet-tr',(36,4),(40,8),radius_x=4)
        self.add_line('sheet-right',(40,8),(40,22))
        self.add_line('fold-diagonal',(40,22),(24,38))
        self.add_line('sheet-bottom',(24,38),(12,38))
        self.add_arc('sheet-bl',(12,38),(8,34),radius_x=4)
        self.add_line('sheet-left',(8,34),(8,8))
        self.add_arc('sheet-tl',(8,8),(12,4),radius_x=4)
        self.add_contour('sheet','sheet-top','sheet-tr','sheet-right','fold-diagonal','sheet-bottom','sheet-bl','sheet-left','sheet-tl',closed=True)
        self.add_polyline('fold',(24,38),(24,26),(28,22),(40,22));self.relate('connect','fold','sheet')
        self.add_polyline('trailing-edge',(40,22),(40,44),(24,44));self.relate('connect','trailing-edge','sheet')

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


    def person(self,name,cx,cy,r,bottom):
        # Shared human reference: exact detached head gap at the shoulder apex.
        self.circle(name+'-head',cx,cy,r)
        top=cy+r+8;w=6
        self.add_arc(name+'-shoulder-left',(cx-w,top+6),(cx,top),radius_x=w)
        self.add_arc(name+'-shoulder-right',(cx,top),(cx+w,top+6),radius_x=w)
        self.add_line(name+'-right',(cx+w,top+6),(cx+w,bottom))
        self.add_line(name+'-bottom-right',(cx+w,bottom),(cx,bottom))
        self.add_line(name+'-bottom-left',(cx,bottom),(cx-w,bottom))
        self.add_line(name+'-left',(cx-w,bottom),(cx-w,top+6))
        self.add_contour(name+'-body',name+'-shoulder-left',name+'-shoulder-right',name+'-right',name+'-bottom-right',name+'-bottom-left',name+'-left',closed=True)

    def dollar(self,cx,cy):
        self.add_bezier('dollar',(cx+3,cy-6),((cx-3,cy-9),(cx-6,cy-3),(cx,cy)),((cx+6,cy+3),(cx+3,cy+9),(cx-3,cy+6)))
        self.add_polyline('dollar-stem',(cx,cy-9),(cx,cy),(cx,cy+9))
        self.relate('connect','dollar','dollar-stem')
