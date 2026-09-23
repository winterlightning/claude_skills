"""A broadcast user icon above the word LIVE.
Symbol plan: radio: nested broadcast arcs; human_ref/user.svg: circular head and smooth shoulder run.
Keyshape: SQUARE; fixed profile envelope is recorded in ink_extremes.
Reduction: None; all four letters retained as authored strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ec05ecd3-fd02-4b5d-ae99-33f8a6f16464'
SOURCE_PATH='icon_set/work/todo-references/user live_ec05ecd3-fd02-4b5d-ae99-33f8a6f16464.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='user-live'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('user', 'live')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_arc('signal-outer',(6,24),(42,24),radius_x=18)
        self.add_arc('signal-inner',(14,24),(34,24),radius_x=10)
        self.circle('head',24,20,3)
        self.add_arc('shoulders',(18,34),(30,34),radius_x=6,radius_y=3)
        self.add_polyline('letter-l',(6,34),(6,42),(12,42))
        self.add_line('letter-i',(17,34),(17,42))
        self.add_polyline('letter-v',(22,34),(26,42),(30,34))
        self.add_polyline('letter-e',(42,34),(35,34),(35,38),(35,42),(42,42))
        self.add_line('e-middle',(35,38),(40,38));self.relate('connect','letter-e','e-middle')

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
