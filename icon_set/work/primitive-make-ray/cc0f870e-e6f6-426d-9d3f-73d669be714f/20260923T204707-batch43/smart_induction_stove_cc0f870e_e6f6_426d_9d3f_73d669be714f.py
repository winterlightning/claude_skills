"""A wireless induction stove with sloping top and a segmented front panel.
Symbol plan: wifi: nested arcs; rounded appliance corners from refrigerator.
Keyshape: SQUARE. Visible extremes (4,4)–(44,44), centerline extremes (6,6)–(42,42). This balances the complete composition; for blank watches the diagonal strap endpoints own these extremes.
Reduction: Tiny front dashes and near-invisible wireless point omitted; main panel divisions retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cc0f870e-e6f6-426d-9d3f-73d669be714f'
SOURCE_PATH='icon_set/work/todo-references/smart induction stove_cc0f870e-e6f6-426d-9d3f-73d669be714f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='smart-induction-stove'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smart', 'induction', 'stove')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_polyline('top',(6,28),(10,6),(38,6),(42,28))
        self.add_polyline('front-top',(6,28),(18,28),(30,28),(42,28))
        self.add_polyline('front',(42,28),(42,34),(38,38),(30,38),(18,38),(10,38),(6,34),(6,28))
        self.relate('connect','top','front-top');self.relate('connect','top','front');self.relate('connect','front-top','front')
        for x in (18,30):
            self.add_line(f'division-{x}',(x,28),(x,38));self.relate('connect',f'division-{x}','front-top');self.relate('connect',f'division-{x}','front')
        self.add_polyline('base',(10,38),(12,42),(36,42),(38,38))
        self.relate('connect','base','front')
        self.wifi('wifi-outer',24,16,8,4)
        self.wifi('wifi-inner',24,23,4,2)

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
            # Circular silhouette with integer attachment knots and continuous tangents.
            self.add_bezier('case-upper-left',(8,24),((8,18),(11,12),(16,10)),((21,8),(22,8),(24,8)))
            self.add_bezier('case-upper-right',(24,8),((26,8),(27,8),(32,10)),((37,12),(40,18),(40,24)))
            self.add_bezier('case-lower-right',(40,24),((40,30),(37,36),(32,38)),((27,40),(26,40),(24,40)))
            self.add_bezier('case-lower-left',(24,40),((22,40),(21,40),(16,38)),((11,36),(8,30),(8,24)))
            self.add_contour('case','case-upper-left','case-upper-right','case-lower-right','case-lower-left',closed=True)
            self.add_polyline('strap-top',(16,10),(18,4),(30,4),(32,10))
            self.add_polyline('strap-bottom',(16,38),(18,44),(30,44),(32,38))
        else:
            self.rounded('case',8,8,40,40,5,breaks={0:[(16,8),(32,8)],4:[(32,40),(16,40)]})
            self.add_polyline('strap-top',(16,8),(17,4),(31,4),(32,8))
            self.add_polyline('strap-bottom',(16,40),(17,44),(31,44),(32,40))
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
