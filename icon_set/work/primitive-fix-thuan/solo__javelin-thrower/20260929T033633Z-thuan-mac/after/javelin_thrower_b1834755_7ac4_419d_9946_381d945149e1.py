"""javelin throwing.
Plan: Restored a bent rear throwing arm gripping the inclined javelin, a compact forward arm, torso and bent running legs.
Construction: human_ref/full_body_ref.png and person-standing: outlined circular head, coherent limb strokes.
Keyshape: SQUARE; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'b1834755-7ac4-419d-9946-381d945149e1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__javelin-thrower/20260929T033633Z-thuan-mac/reference/javelin throwing_b1834755-7ac4-419d-9946-381d945149e1.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'javelin-thrower'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('javelin', 'throwing')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.add_line('javelin',(4,12),(44,2))
        self.circle('head',24,18,4)
        self.add_line('torso',(24,30),(24,33))
        self.add_line('lower-torso',(24,33),(26,36));self.relate('connect','torso','lower-torso')
        self.add_polyline('throwing-arm',(24,30),(16,27),(12,10));self.relate('connect','throwing-arm','torso');self.relate('connect','throwing-arm','javelin')
        self.add_polyline('front-arm',(24,30),(32,30),(34,27));self.relate('connect','front-arm','torso')
        self.add_polyline('rear-leg',(26,36),(21,39),(15,44));self.add_polyline('front-leg',(26,36),(35,35),(40,44));self.relate('connect','rear-leg','lower-torso');self.relate('connect','front-leg','lower-torso')
        self.mark_human_figure('thrower',head='head',torso='torso',torso_junction='start')

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve an inclined held javelin, bent throwing arm and running legs. Compact limb spacing and optical envelope retain the action; the upper torso is vertical under its head with an exact 4px visible gap.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '76985f2e92552706c06e511b5c1da40dd7249fa2bfd69a0eb868aebfde37cb94'}
