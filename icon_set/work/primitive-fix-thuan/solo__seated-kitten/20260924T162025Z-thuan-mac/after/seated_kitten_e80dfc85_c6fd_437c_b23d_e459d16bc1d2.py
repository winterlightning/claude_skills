"""Seated kitten with pointed ears, rounded cheeks, smooth haunches and left curling tail. Lucide cat informs curved cheeks and pointed ears. Omit face marks; retain sitting forelegs.
Keyshape VRECT_L: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e80dfc85-c6fd-437c-b23d-e459d16bc1d2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-kitten/20260924T162025Z-thuan-mac/reference/kitten_e80dfc85-c6fd-437c-b23d-e459d16bc1d2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seated-kitten'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('seated', 'kitten')

    def build(self):
        # One outer contour owns both the haunches and the curling tail; no overlapping outlines.
        self.path('cat',(14,4),[(21,9),((29,9),14,14,True),(36,4),(36,15),((31,25),11,11,True),((40,38),16,16,True),(40,40),((36,44),4,4,True),(26,44),(16,44),((8,36),8,8,True),((18,26),10,10,True),(18,25),((14,15),11,11,True),(14,4)],True)
        self.add_line('tail-crease',(16,36),(16,44));self.relate('connect','tail-crease','cat')
        self.add_line('legs',(26,34),(26,44));self.relate('connect','legs','cat')

    def path(self, name, start, steps, closed=False):
        members=[]; here=start
        for j,step in enumerate(steps):
            eid=f'{name}-{j}'
            if len(step)==2:
                self.add_line(eid,here,step); end=step
            else:
                end,rx,ry,sweep=step
                self.add_arc(eid,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)

    def cups(self):
        # Identical supporting palms mirrored about x24; vertical to horizontal tangent quarters.
        for n,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            self.path(n+'-hand',p(6,30),[p(6,32),(p(16,42),10,10,s<0),p(20,42)])
