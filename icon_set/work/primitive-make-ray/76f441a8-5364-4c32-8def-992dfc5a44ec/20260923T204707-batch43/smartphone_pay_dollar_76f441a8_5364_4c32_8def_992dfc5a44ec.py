"""A smartphone with a dollar banknote protruding to the right.
Symbol plan: monitor-smartphone: interrupted phone frame around a foreground object; banknote and dollar-sign: note corners and currency glyph.
Keyshape: SQUARE. Visible extremes (4,4)–(44,44), centerline extremes (6,6)–(42,42). This balances the complete composition; for blank watches the diagonal strap endpoints own these extremes.
Reduction: No defining features omitted; both corner decorations and dollar symbol retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='76f441a8-5364-4c32-8def-992dfc5a44ec'
SOURCE_PATH='icon_set/work/todo-references/smartphone pay dollar_76f441a8-5364-4c32-8def-992dfc5a44ec.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='smartphone-pay-dollar'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smartphone', 'pay', 'dollar')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_line('phone-top',(10,6),(22,6))
        self.add_arc('phone-tr',(22,6),(26,10),radius_x=4)
        self.add_line('phone-upper-right',(26,10),(26,12))
        self.add_line('phone-lower-right',(26,34),(26,38))
        self.add_arc('phone-br',(26,38),(22,42),radius_x=4)
        self.add_line('phone-bottom',(22,42),(10,42))
        self.add_arc('phone-bl',(10,42),(6,38),radius_x=4)
        self.add_line('phone-left-lower',(6,38),(6,34))
        self.add_line('phone-left-upper',(6,34),(6,10))
        self.add_arc('phone-tl',(6,10),(10,6),radius_x=4)
        self.add_contour('phone','phone-lower-right','phone-br','phone-bottom','phone-bl','phone-left-lower','phone-left-upper','phone-tl','phone-top','phone-tr','phone-upper-right')
        self.add_line('phone-footer',(6,34),(26,34));self.relate('connect','phone-footer','phone')
        self.rounded('banknote',16,16,42,30,2)
        self.dollar(cx=29,cy=23)
        for name,a,b in [('tl',(16,22),(22,16)),('tr',(36,16),(42,22)),('br',(42,24),(36,30)),('bl',(22,30),(16,24))]:
            self.add_arc('corner-'+name,a,b,radius_x=6,sweep=False);self.relate('connect','corner-'+name,'banknote')

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
