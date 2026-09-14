"""Woman with hair and sash at podium; omit fine center part. Lucide user informs head and shoulder construction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eba4aafc-3b5a-4a20-83b4-e185461b7ebd'
SOURCE_PATH = 'pictographic-primitives/school-learning/election politician podium woman_eba4aafc-3b5a-4a20-83b4-e185461b7ebd.svg'
AUTHOR = 'gpt-6'


class WomanWithSashAtPodium(Solo48):
    icon_id = 'woman-with-sash-at-podium'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/education"
    aliases = ()
    keywords = ('woman', 'podium', 'politician', 'speech', 'sash', 'election')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def shoulder(self, name, x, y, rx, ry):
        self.add_arc(name, (x-rx,y), (x+rx,y), radius_x=rx, radius_y=ry)

    def bust(self, name, x, y, r=3, w=4, h=5):
        self.circle(name+'-head', x, y, r)
        top=(x,y+r)
        self.add_arc(name+'-left',(x-w,y+r+h),top,radius_x=w,radius_y=h)
        self.add_arc(name+'-right',top,(x+w,y+r+h),radius_x=w,radius_y=h)
        self.add_contour(name+'-shoulders',name+'-left',name+'-right')
        self.relate('connect',name+'-head',name+'-shoulders')

    def build(self) -> None:
        self.circle('head',24,9,3)
        self.add_arc('shoulder-left',(12,32),(24,21),radius_x=12,radius_y=11)
        self.add_arc('shoulder-right',(24,21),(36,32),radius_x=12,radius_y=11)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        self.add_polyline('ledge',(6,32),(12,32),(36,32),(42,32))
        self.relate('connect','shoulders','ledge')
        for side,x,end in (('left',12,15),('right',36,33)):
            self.add_line(side,(x,32),(end,42))
            self.relate('connect',side,'ledge')
            self.relate('connect',side,'shoulders')
        self.add_line('hair-left',(21,9),(19,15))
        self.add_line('hair-right',(27,9),(29,15))
        self.relate('connect','head','hair-left')
        self.relate('connect','head','hair-right')
