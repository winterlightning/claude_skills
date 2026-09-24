"""A rock-concert horns hand gesture surrounded by three lightning marks.
Plan: All identifying parts retained; fine palm crease simplified to the thumb contour. Human references inspected: user.svg and full_body_ref.png; no isolated hand there, so hand-metal informs finger construction. No detached head/body gap applies.
Lucide construction references: hand-metal.
Keyshape SQUARE: (4,4)-(44,44) ink.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape

SOURCE_ICON_ID = '3a11e17f-1153-59b2-b135-910a41a584c7'
SOURCE_PATH = 'pictographic-primitives/entertainment/concert rock_3a11e17f-1153-59b2-b135-910a41a584c7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'concert-rock'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('concert', 'rock')

    def circle(self, name, cx, cy, radius):
        self.add_arc(name+'-top',(cx-radius,cy),(cx+radius,cy),radius_x=radius)
        self.add_arc(name+'-bottom',(cx+radius,cy),(cx-radius,cy),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, left, top, right, bottom, radius):
        # Shared corner radius and a bottom-centre attachment node.
        mid=(left+right)//2
        pts=[(left+radius,top),(right-radius,top),(right,top+radius),
             (right,bottom-radius),(right-radius,bottom),(mid,bottom),
             (left+radius,bottom),(left,bottom-radius),(left,top+radius),(left+radius,top)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            key=f'{name}-{i}';members.append(key)
            if i in (1,3,6,8): self.add_arc(key,a,b,radius_x=radius)
            else: self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Human-reference vocabulary: rounded continuous hand silhouette; no detached head.
        # Paired raised outer fingers, two curled middle knuckles, thumb and three energy bolts.
        self.add_arc('index-cap',(8,22),(16,22),radius_x=4)
        self.add_line('index-inner',(16,22),(16,30))
        self.add_arc('middle-knuckle',(16,30),(24,30),radius_x=4)
        self.add_arc('ring-knuckle',(24,30),(32,30),radius_x=4)
        self.add_line('little-inner',(32,30),(32,22))
        self.add_arc('little-cap',(32,22),(40,22),radius_x=4)
        self.add_line('right-palm',(40,22),(40,30))
        self.add_arc('palm-right',(40,30),(28,42),radius_x=12)
        self.add_line('palm-bottom',(28,42),(20,42))
        self.add_arc('palm-left',(20,42),(8,30),radius_x=12)
        self.add_line('left-palm',(8,30),(8,22))
        self.add_contour('hand','index-cap','index-inner','middle-knuckle','ring-knuckle','little-inner','little-cap','right-palm','palm-right','palm-bottom','palm-left','left-palm',closed=True)
        # Omit cramped palm creases; raised outer fingers and curled middle pair remain.
        for name,points in [('left-bolt',[(6,6),(10,10)]),('top-bolt',[(26,6),(22,12)]),('right-bolt',[(42,6),(38,10)])]:
            self.add_polyline(name,*points)

