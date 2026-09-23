"""A wireless television beside a smartphone.
Symbol plan: monitor-smartphone: offset screen pair and open overlap region; wifi: arc above the TV.
Keyshape: HRECT_L. Visible extremes (2,6)–(46,42), centerline extremes (4,8)–(44,40). The wide composition benefits from the 40-unit horizontal centerline span.
Reduction: One inner wireless arc omitted to keep signal-to-screen clearance.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='77e358dc-c96c-49a8-995c-75ae3db00556'
SOURCE_PATH='icon_set/work/todo-references/smart tv and phone_77e358dc-c96c-49a8-995c-75ae3db00556.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='smart-tv-and-phone'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smart', 'tv', 'and', 'phone')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_line('tv-top',(8,19),(23,19))
        self.add_arc('tv-tl',(4,23),(8,19),radius_x=4)
        self.add_line('tv-left',(4,28),(4,23))
        self.add_arc('tv-bl',(8,32),(4,28),radius_x=4)
        self.add_line('tv-bottom-1',(18,32),(8,32))
        self.add_line('tv-bottom-2',(23,32),(18,32))
        self.add_contour('tv','tv-bottom-2','tv-bottom-1','tv-bl','tv-left','tv-tl','tv-top')
        self.add_line('stand',(18,32),(18,40));self.relate('connect','stand','tv')
        self.add_polyline('stand-foot',(12,40),(18,40),(24,40));self.relate('connect','stand','stand-foot')
        self.wifi('wireless-arc',15,10,5,2)
        self.rounded('phone',32,16,44,34,3,breaks={2:[(44,26)],6:[(32,26)]})
        self.add_line('phone-footer',(32,26),(44,26));self.relate('connect','phone-footer','phone')

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
