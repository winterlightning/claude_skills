"""robbing.
Two aligned figures; the left figure holds a broad sloping blade toward the right figure.
Square; robber head bottom16 to torso24 and victim bottom14 to torso22 give exactly4 ink clearance. Intentional figure-size and pose asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4d29ffb6-bda5-416a-be77-62a701e144e4'
SOURCE_PATH = 'pictographic-primitives/crime/robbing_4d29ffb6-bda5-416a-be77-62a701e144e4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'robbing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('robbing',)

    def build(self) -> None:
        # full_body_ref.png: circular heads aligned to torso axes; exact 4 ink gap.
        for who,x,radius,body_top in (('robber',11,5,24),('victim',39,3,22)):
            self.circle(who+'-head',x,11,radius)
            self.add_line(who+'-torso',(x,body_top),(x,42))
            self.mark_human_figure(who,head=who+'-head',torso=who+'-torso',torso_junction='start')
        self.add_line('arm',(11,30),(19,30))
        self.relate('connect','arm','robber-torso')
        self.add_polyline('knife',(19,30),(19,24),(27,24),(31,36),(19,36),closed=True)
        self.relate('connect','arm','knife')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, l, t, r, b, rad=2):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i in range(8):
            a,z=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

    def arrow(self, name, start, tip, wing1, wing2):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',wing1,tip,wing2)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')

    def heart(self, name, x, top, half, bottom):
        # Mirrored lobes share dimensions and meet the pointed lower silhouette.
        self.add_bezier(name+'-left',(x,top+2),((x-half,top-5),(x-half-3,top+4),(x-half,top+7)),((x-half+2,top+10),(x, bottom),(x,bottom)))
        self.add_bezier(name+'-right',(x,bottom),((x,bottom),(x+half-2,top+10),(x+half,top+7)),((x+half+3,top+4),(x+half,top-5),(x,top+2)))
        self.add_contour(name,name+'-left',name+'-right',closed=True)

# Repair plan: Two aligned figures; the left figure holds a broad sloping blade toward the right figure.
# Omissions: Mask eyes and dollar symbol omitted; blade simplified.
# Construction references: human_ref/full_body_ref.png: circular heads, straight torsos and an action arm.
# Keyshape and proportions: Square; robber head bottom16 to torso24 and victim bottom14 to torso22 give exactly4 ink clearance. Intentional figure-size and pose asymmetry.
