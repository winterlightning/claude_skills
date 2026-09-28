"""A diagonal vector pen nib with an upper-left plus sign.
Symbol plan: pen-tool: coherent nib, cap and slit; plus: centered intersecting arms.
Keyshape: SQUARE; fixed profile envelope is recorded in ink_extremes.
Reduction: None; cap, nib, slit and plus retained.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='49a3ae80-8be9-4e8e-9359-748e0b24459f'
SOURCE_PATH='icon_set/work/todo-references/vectors pen add 1_49a3ae80-8be9-4e8e-9359-748e0b24459f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='vectors-pen-add-1'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('vectors', 'pen', 'add', '1')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_polyline('nib',(6,42),(20,24),(28,20),(34,26),(30,34),(6,42))
        self.add_polyline('cap',(28,20),(34,6),(42,14),(34,26))
        self.relate('connect','cap','nib')
        self.add_line('slit',(6,42),(21,27));self.relate('connect','slit','nib')
        self.add_polyline('plus-h',(6,12),(12,12),(18,12))
        self.add_polyline('plus-v',(12,6),(12,12),(12,18));self.relate('connect','plus-h','plus-v')

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
