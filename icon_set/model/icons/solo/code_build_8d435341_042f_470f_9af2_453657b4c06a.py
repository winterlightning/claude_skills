"""A construction crane suspending a code window.
Symbol plan: construction: shared truss nodes; source supplies hanging window and three code strokes.
Reduction: Two truss bays reduced to one; code chevrons and slash retained.
Keyshape: HRECT_L; model supplies exact ink extremes.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='8d435341-042f-470f-9af2-453657b4c06a'
SOURCE_PATH='icon_set/work/todo-references/code build_8d435341-042f-470f-9af2-453657b4c06a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='code-build'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases=()
    keywords=('code', 'build')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('crane',(4,40),(4,16),(4,8),(16,8),(24,8),(36,16),(28,16),(24,16),(12,16),(8,16),(4,16))
        self.add_polyline('truss',(8,16),(16,8),(24,16));self.relate('connect','truss','crane')
        self.add_polyline('mast',(12,16),(12,40),(4,40));self.relate('connect','mast','crane')
        self.add_polyline('hanger',(28,16),(28,20),(24,24));self.relate('connect','hanger','crane')
        self.add_line('hanger-right',(28,20),(32,24));self.relate('connect','hanger-right','hanger')
        self.rounded('window',20,24,44,40,3,breaks={0:[(24,24),(32,24)]})
        self.relate('connect','hanger','window');self.relate('connect','hanger-right','window')
        self.add_polyline('code-left',(27,29),(24,32),(27,35))
        self.add_line('slash',(34,28),(30,36))
        self.add_polyline('code-right',(38,29),(41,32),(38,35))

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

