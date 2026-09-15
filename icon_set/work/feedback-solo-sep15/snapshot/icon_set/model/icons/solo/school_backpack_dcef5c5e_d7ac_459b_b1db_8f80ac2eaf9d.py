"""A domed school bag has a carrying loop and zipped front pocket. Lucide backpack informs its shared pocket/base and top loop; side pockets are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcef5c5e-d7ac-459b-b1db-8f80ac2eaf9d'
SOURCE_PATH = 'pictographic-primitives/school-learning/school bag_dcef5c5e-d7ac-459b-b1db-8f80ac2eaf9d.svg'
AUTHOR = 'gpt-6'


class SchoolBackpack(Solo48):
    icon_id = 'school-backpack'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "education/school"
    aliases = ()
    keywords = ('backpack', 'school', 'bag', 'pocket', 'student', 'satchel')

    def run(self, name, *points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(name+"-"+str(j),a,b)

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self) -> None:
        # Current centerline bounds: SQUARE 6,6-42,42; HRECT 4,8-44,40; VRECT 8,4-40,44.

        self.add_arc('loop',(16,12),(32,12),radius_x=8)
        self.add_line('top',(16,12),(32,12))
        self.add_arc('top-right',(32,12),(40,20),radius_x=8)
        self.add_line('right',(40,20),(40,40))
        self.add_arc('bottom-right',(40,40),(36,44),radius_x=4)
        self.run('base',(36,44),(31,44),(17,44),(12,44))
        self.add_arc('bottom-left',(12,44),(8,40),radius_x=4)
        self.add_line('left',(8,40),(8,20))
        self.add_arc('top-left',(8,20),(16,12),radius_x=8)
        self.add_contour('body','top','top-right','right','bottom-right','base-1','base-2','base-3','bottom-left','left','top-left',closed=True)
        self.relate('connect','loop','body')
        self.run('pocket-left',(17,44),(17,35),(17,31))
        self.add_arc('pocket-tl',(17,31),(21,27),radius_x=4)
        self.add_line('pocket-top',(21,27),(27,27))
        self.add_arc('pocket-tr',(27,27),(31,31),radius_x=4)
        self.run('pocket-right',(31,31),(31,35),(31,44))
        self.add_contour('pocket','pocket-left-1','pocket-left-2','pocket-tl','pocket-top','pocket-tr','pocket-right-1','pocket-right-2')
        self.add_line('zipper',(17,35),(31,35))
        self.relate('connect','pocket','zipper')
        self.relate('connect','body','pocket')
