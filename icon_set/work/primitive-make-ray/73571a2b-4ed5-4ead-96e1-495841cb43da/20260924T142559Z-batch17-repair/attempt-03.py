"""smart watch circle euro sign: standalone batch 17 repair.
Retained the circular watch case, paired straps and euro mark. Removed the short strap end caps to eliminate tiny enclosed strap pockets; opened the euro curve and shortened its crossbar.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '73571a2b-4ed5-4ead-96e1-495841cb43da'
SOURCE_PATH = 'pictographic-primitives/other/smart watch circle euro sign_73571a2b-4ed5-4ead-96e1-495841cb43da.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'watch'

class Drawing(Solo48):
    icon_id='smart-watch-circle-euro-sign'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smart', 'watch', 'circle', 'euro', 'sign')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.watch(circular=True)
        self.add_bezier('euro-upper',(29,18),((22,15),(18,19),(18,24)))
        self.add_bezier('euro-lower',(18,24),((18,29),(22,33),(29,30)))
        self.add_contour('euro','euro-upper','euro-lower')
        self.add_polyline('euro-bar',(18,24),(25,24));self.relate('connect','euro','euro-bar')


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
            self.add_line('strap-top-left',(16,10),(18,4))
            self.add_line('strap-top-right',(32,10),(30,4))
            self.add_line('strap-bottom-left',(16,38),(18,44))
            self.add_line('strap-bottom-right',(32,38),(30,44))
        else:
            self.rounded('case',8,8,40,40,5,breaks={0:[(16,8),(32,8)],4:[(32,40),(16,40)]})
            self.add_polyline('strap-top',(16,8),(17,4),(31,4),(32,8))
            self.add_polyline('strap-bottom',(16,40),(17,44),(31,44),(32,40))
        for n in ['strap-top-left','strap-top-right','strap-bottom-left','strap-bottom-right']:self.relate('connect','case',n)

