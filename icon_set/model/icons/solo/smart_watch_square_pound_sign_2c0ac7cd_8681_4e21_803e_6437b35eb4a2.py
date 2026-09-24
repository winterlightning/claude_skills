"""smart watch square pound sign: standalone batch 17 repair.
Retained the rounded square watch case, paired straps and pound mark. Open strap ends and a compact hook with an eight-unit bar-to-baseline gap.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '2c0ac7cd-8681-4e21-803e-6437b35eb4a2'
SOURCE_PATH = 'pictographic-primitives/other/smart watch square pound sign_2c0ac7cd-8681-4e21-803e-6437b35eb4a2.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'pound-sterling'

class Drawing(Solo48):
    icon_id='smart-watch-square-pound-sign'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smart', 'watch', 'square', 'pound', 'sign')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.watch()
        self.pound()


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
            self.add_line('strap-top-left',(16,8),(17,4))
            self.add_line('strap-top-right',(32,8),(31,4))
            self.add_line('strap-bottom-left',(16,40),(17,44))
            self.add_line('strap-bottom-right',(32,40),(31,44))
        for n in ['strap-top-left','strap-top-right','strap-bottom-left','strap-bottom-right']:self.relate('connect','case',n)


    def pound(self):
        self.add_arc('pound-hook',(28,20),(22,20),radius_x=3,sweep=False)
        self.add_polyline('pound-stem',(22,20),(22,23),(22,31))
        self.add_polyline('pound-bar',(18,23),(22,23),(24,23))
        self.add_polyline('pound-base',(20,31),(22,31),(27,31))
        self.relate('connect','pound-hook','pound-stem');self.relate('connect','pound-stem','pound-bar');self.relate('connect','pound-stem','pound-base')

