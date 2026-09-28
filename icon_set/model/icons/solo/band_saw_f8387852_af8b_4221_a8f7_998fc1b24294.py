"""A band saw frame beside a toothed wheel.
Plan: SQUARE allocates left space to the machine column and right space to the wheel.
Reduction: Removed small hub, table ledge, upper inner return, and doubled base edge; reduced wheel to eight broad teeth.
Construction: Supplied reference governs frame and gear; Lucide cog reviewed for repeated radial teeth, not its dense internal spokes.
Layout: Asymmetric machine column and right-hand wheel preserve the source arrangement."""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='f8387852-af8b-4221-a8f7-998fc1b24294'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/band saw_f8387852-af8b-4221-a8f7-998fc1b24294.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id='band-saw'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('band', 'saw')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        # SQUARE extremes (6,6)-(42,42). Broad machine column, bottom rail,
        # reduced eight-tooth wheel; upper frame joins the gear at its top.
        self.add_line('column',(6,42),(6,12))
        self.add_arc('corner',(6,12),(12,6),radius_x=6)
        self.add_polyline('top',(12,6),(33,6),(33,15))
        self.add_contour('frame','column','corner','top-1','top-2')
        self.contours=[c for c in self.contours if c.contour_id!='top']
        self.add_line('inner',(14,42),(14,16))
        self.add_polyline('base',(6,42),(14,42),(42,42))
        self.relate('connect','frame','base');self.relate('connect','inner','base')
        self.add_polyline('wheel',(33,15),(36,18),(39,18),(39,21),(42,24),(39,27),(39,30),(36,30),(33,33),(30,30),(27,30),(27,27),(24,24),(27,21),(27,18),(30,18),closed=True)
        self.relate('connect','wheel','frame')

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
