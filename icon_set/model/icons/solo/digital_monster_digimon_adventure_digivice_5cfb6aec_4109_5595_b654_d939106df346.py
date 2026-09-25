"""A Digimon Digivice with a scalloped casing, double circular display, paired left buttons, right button, and two antenna strokes. Bilateral case contour centered at (24,24); intentional asymmetric controls preserved. Extremes (4,8)-(44,40).
Lucide gamepad: repeated control definitions and clear outer enclosure; distinctive case and concentric display taken from supplied Digivice.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cfb6aec-4109-5595-b654-d939106df346'
SOURCE_PATH = 'icon_set/work/todo-references/digital monster digimon adventure digivice_5cfb6aec-4109-5595-b654-d939106df346.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'digital-monster-digimon-adventure-digivice'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('digital', 'monster', 'digimon', 'adventure', 'digivice')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, l, t, r, b, radius):
        q=radius
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
        for j in range(8):
            if j%2: self.add_arc(name+str(j),pts[j],pts[j+1],radius_x=q)
            else: self.add_line(name+str(j),pts[j],pts[j+1])
        self.add_contour(name, *(name+str(j) for j in range(8)), closed=True)

    def build(self):

        self.add_bezier('shell',(18,8),((16,8),(15,13),(12,14)),((9,16),(4,15),(4,20)),((4,24),(4,28),(5,31)),((6,34),(12,33),(15,36)),((16,38),(16,40),(19,40)),((22,40),(26,40),(29,40)),((32,40),(32,37),(35,35)),((38,33),(43,34),(44,30)),((44,26),(44,22),(44,20)),((44,16),(38,16),(35,14)),((32,12),(32,8),(30,8)),((26,8),(22,8),(18,8)))
        self.add_contour('case','shell',closed=True)
        self.circle('bezel',25,24,11)
        self.circle('display',25,24,6)
        for j,y in enumerate((21,28)):self.circle('button-'+str(j),9,y,2)
        self.add_polyline('right-button',(36,22),(40,22),(40,26),(36,26))
        self.add_line('antenna-1',(10,15),(8,12))
        self.add_line('antenna-2',(14,13),(12,10))
