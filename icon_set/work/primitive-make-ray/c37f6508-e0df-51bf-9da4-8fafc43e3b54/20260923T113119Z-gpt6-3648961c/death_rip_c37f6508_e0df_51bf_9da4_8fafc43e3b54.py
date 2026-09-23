"""An arched RIP gravestone seated on a rectangular plinth. Shared center axis 24; outer arch radius 12, top y4, plinth y36..44. Keep the hand-drawn RIP inscription.
No useful local Lucide match for this composition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c37f6508-e0df-51bf-9da4-8fafc43e3b54'
SOURCE_PATH = 'icon_set/work/todo-references/death rip_c37f6508-e0df-51bf-9da4-8fafc43e3b54.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'death-rip'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/devices"
    aliases = ()
    keywords = ('death', 'rip')

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

        self.add_line('stone-left',(12,36),(12,16))
        self.add_arc('stone-arch',(12,16),(36,16),radius_x=12)
        self.add_line('stone-right',(36,16),(36,36))
        self.add_contour('stone','stone-left','stone-arch','stone-right')
        self.add_polyline('plinth',(8,36),(12,36),(36,36),(40,36),(40,44),(8,44),closed=True)
        self.relate('connect','stone','plinth')
        self.add_polyline('r',(17,28),(17,18),(21,18),(21,23),(17,23),(22,28))
        self.add_line('i',(26,18),(26,28))
        self.add_polyline('p',(31,28),(31,18),(35,18),(35,23),(31,23))
