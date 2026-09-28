"""HRECT_L centerline bounds (4,8)-(44,40). Mirrored arch curves attach to the outer lobes of a heart. Paired circular heads end at y27; compact bodies begin at y35, giving exactly 4 units of visible clearance. The groom has separated legs and the bride an open flared gown; arms and clothing detail are omitted at 48 units.

Construction reference: Shared human_ref/full_body_ref.png; round detached heads and simplified bodies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55e06d00-edc0-4555-a59a-bfe50151ffb9'
SOURCE_PATH = 'pictographic-primitives/romance/wedding couple_55e06d00-edc0-4555-a59a-bfe50151ffb9.svg'
SOURCE_ICON_IDS = ('55e06d00-edc0-4555-a59a-bfe50151ffb9',)
AUTHOR = 'gpt-6'

def circle(m, name, cx, cy, r):
    # A single circular loop owns its radius and shared antipodal endpoints.
    m.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
    m.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
    m.add_contour(name,name+"-top",name+"-bottom",closed=True)


def rounded(m, name, left, top, right, bottom, r):
    # One rectangle owns all four equal tangent quarter-circle corners.
    points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
            (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
    for i,start in enumerate(points):
        end=points[(i+1)%8]
        if i%2: m.add_arc(f"{name}-{i}",start,end,radius_x=r)
        else: m.add_line(f"{name}-{i}",start,end)
    m.add_contour(name,*(f"{name}-{i}" for i in range(8)),closed=True)


class WeddingCoupleHeartArchScene(Solo48):
    icon_id = 'wedding-couple-heart-arch-scene'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    categories = ('primitives', 'romance')
    aliases = ()
    keywords = ('wedding', 'couple', 'heart', 'arch', 'scene')

    def build(self) -> None:
        # HRECT_L bounds (4,8)-(44,40). The heart is an attached arch
        # ornament. Groom uses a compact stick figure; bride an open gown.
        self.add_arc('heart-left',(16,12),(24,12),radius_x=4)
        self.add_arc('heart-right',(24,12),(32,12),radius_x=4)
        self.add_bezier('heart-lower-right',(32,12),((32,14),(28,15),(24,17)))
        self.add_bezier('heart-lower-left',(24,17),((20,15),(16,14),(16,12)))
        self.add_contour('heart','heart-left','heart-right','heart-lower-right','heart-lower-left',closed=True)
        for sign,name in ((1,'left'),(-1,'right')):
            def pt(x,y):return (24+sign*(x-24),y)
            self.add_bezier(name+'-arch',pt(4,22),(pt(4,16),pt(10,12),pt(16,12)))
            self.add_line(name+'-post',pt(4,40),pt(4,22))
            self.relate('connect',name+'-arch',name+'-post')
            self.relate('connect',name+'-arch','heart')
        for name,x in (('groom',16),('bride',32)):
            circle(self,name+'-head',x,25,2)
        # Both heads end at27 and upper torsos begin35: ink gap exactly4.
        self.add_line('groom-torso',(16,35),(16,37))
        self.add_polyline('groom-legs',(12,40),(16,37),(20,40))
        self.relate('connect','groom-torso','groom-legs')
        self.mark_human_figure('groom',head='groom-head',torso='groom-torso',torso_junction='start')
        self.add_polyline('bride-gown',(28,40),(32,35),(36,40))
