"""A Vaisakhi drum with two beaters and a wheat sprig.
Symbol plan: drum: barrel silhouette and hoops; wheat: repeated diagonal stalk branches.
Keyshape: SQUARE; fixed profile envelope is recorded in ink_extremes.
Reduction: None; drum, both beaters and stalk retained.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='a0865ae5-c028-46f5-ade5-f26da83b22c2'
SOURCE_PATH='icon_set/work/todo-references/vaisakhi harvest_a0865ae5-c028-46f5-ade5-f26da83b22c2.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='vaisakhi-harvest'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('vaisakhi', 'harvest')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_polyline('beater-left',(6,6),(16,12))
        self.add_polyline('beater-right',(36,6),(26,12))
        self.add_line('drum-top',(12,18),(30,18))
        self.add_bezier('drum-right',(30,18),((33,27),(33,35),(30,42)))
        self.add_line('drum-bottom',(30,42),(12,42))
        self.add_bezier('drum-left',(12,42),((9,35),(9,27),(12,18)))
        self.add_contour('drum','drum-top','drum-right','drum-bottom','drum-left',closed=True)
        for i,y in enumerate((24,36)):self.add_line(f'hoop-{i}',(11,y),(27,y))
        self.add_polyline('wheat-stem',(28,42),(34,36),(38,32),(42,28))
        for name,a,b in [('low',(34,36),(40,36)),('middle',(38,32),(38,26)),('high',(42,28),(42,22))]:
            self.add_line('grain-'+name,a,b);self.relate('connect','grain-'+name,'wheat-stem')

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
