"""Hard hat above supporting palms. Lucide hard-hat: circular dome and straight brim. Hands mirror x24. Omit small crown ribs and cuffs.
Keyshape SQUARE: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '20214d85-2a10-45f3-974e-7a15e7241f74'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-supporting-hard-hat/20260924T162025Z-thuan-mac/reference/labor hands action_20214d85-2a10-45f3-974e-7a15e7241f74.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-supporting-hard-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('hands', 'supporting', 'hard', 'hat')

    def build(self):
        self.path('helmet',(12,20),[(12,18),((24,6),12,12,True),((36,18),12,12,True),(36,20)])
        self.add_polyline('brim',(10,20),(12,20),(36,20),(38,20));self.relate('connect','helmet','brim')
        self.cups()

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
        # Mirrored hands about x24; equal fingertip radii and tangent S-curves into the wrists.
        for n,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            self.path(n+'-hand',p(10,42),[(p(6,34),10,10,s>0),p(6,33),(p(14,33),4,4,s>0),(p(16,35),2,2,s<0),(p(18,37),2,2,s>0),p(18,42)])
