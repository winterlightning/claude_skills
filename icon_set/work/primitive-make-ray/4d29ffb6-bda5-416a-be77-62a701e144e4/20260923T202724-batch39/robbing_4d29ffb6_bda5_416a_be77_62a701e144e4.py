"""A robber threatening another person with a knife for money.

Plan: Two shared circular heads with exact detached torso gap, bent threatening arm, blade and dollar symbol.
Construction: human_ref/user.svg and full_body_ref.png: circular heads and coherent bent limbs
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4d29ffb6-bda5-416a-be77-62a701e144e4'
SOURCE_PATH = 'icon_set/work/todo-references/robbing_4d29ffb6-bda5-416a-be77-62a701e144e4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'robbing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('robbing',)

    def build(self):
        # Heads end at y16 and y18; actual torso starts y24 and y26: 8 centerline / 4 ink gap.
        self.circle('robber-head',14,11,5)
        self.circle('victim-head',36,14,4)
        self.add_line('robber-torso',(14,24),(14,42))
        self.add_line('victim-torso',(36,26),(36,42))
        self.mark_human_figure('robber',head='robber-head',torso='robber-torso',torso_junction='start')
        self.mark_human_figure('victim',head='victim-head',torso='victim-torso',torso_junction='start')
        self.add_polyline('arm',(14,24),(6,28),(6,34),(20,34))
        self.relate('connect','arm-1','robber-torso')
        self.add_polyline('knife',(20,34),(20,28),(28,28),(32,34),closed=True)
        self.relate('connect','arm-3','knife-1');self.relate('connect','arm-3','knife-4')
        self.add_bezier('money',(42,29),((35,26),(35,33),(40,34)),((44,35),(43,40),(38,39)))
        self.add_line('money-stem',(40,26),(40,42))

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
