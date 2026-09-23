"""laboratory test stool, complete SOLO48 composition.
Symbol plan is recorded in build(). Visible keyshape extremes: (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b873e51-b614-5be9-ba1f-bee4eb0fc739'
SOURCE_PATH = 'icon_set/work/todo-references/laboratory test stool_4b873e51-b614-5be9-ba1f-bee4eb0fc739.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'laboratory-test-stool'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('laboratory test stool',)

    def rounded(self,n,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)

    def laptop(self):
        # Screen and base own shared hinge endpoints; repeated corner radius 4.
        self.add_line('screen-left',(8,32),(8,12))
        self.add_arc('screen-tl',(8,12),(12,8),radius_x=4)
        self.add_line('screen-top',(12,8),(36,8))
        self.add_arc('screen-tr',(36,8),(40,12),radius_x=4)
        self.add_line('screen-right',(40,12),(40,32))
        self.add_line('hinge',(40,32),(8,32))
        self.add_contour('screen','screen-left','screen-tl','screen-top','screen-tr','screen-right','hinge',closed=True)
        self.add_polyline('base',(8,32),(4,40),(44,40),(40,32))
        self.relate('connect','screen','base')

    def build(self):
        # Wide cap over specimen jar with a small tiered stool silhouette.
        self.rounded('lid',8,4,32,8,2)
        self.add_line('jar-left',(8,10),(8,38))
        self.add_arc('jar-bl',(8,38),(14,44),radius_x=6,sweep=False)
        self.add_line('jar-bottom',(14,44),(34,44))
        self.add_arc('jar-br',(34,44),(40,38),radius_x=6,sweep=False)
        self.add_line('jar-right',(40,38),(40,10))
        self.add_contour('jar','jar-left','jar-bl','jar-bottom','jar-br','jar-right')
        self.relate('connect','lid','jar')
        self.add_arc('stool-tip',(24,21),(29,27),radius_x=6)
        self.add_arc('stool-right',(29,27),(28,35),radius_x=5)
        self.add_line('stool-base',(28,35),(20,35))
        self.add_arc('stool-left',(20,35),(20,27),radius_x=3,radius_y=4)
        self.add_arc('stool-rise',(20,27),(24,21),radius_x=5,sweep=False)
        self.add_contour('stool','stool-tip','stool-right','stool-base','stool-left','stool-rise',closed=True)
