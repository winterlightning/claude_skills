"""Diagonal tag with rounded corners, eyelet at upper right and centered curved G.
Keyshape: SQUARE. Uniform 4px SOLO48 stroke.
Construction: No useful exact Lucide brand match; shared geometric construction.
Revision: Restored the diagonal tag, round eyelet and curved G with separate clear counters.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ef272f31-527b-4b06-8cdb-28e8d4532728'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-shopping-logo/20260928T173050Z-thuan-mac/reference/google shopping logo_ef272f31-527b-4b06-8cdb-28e8d4532728.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'google-shopping-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'shopping', 'logo')

    def build(self):
        self.path('tag',(28,6),(38,6),(42,10,4,4,True),(42,21),
                  (40,25,42,23,42,23),(23,42),(19,42,22,43,20,43),(6,29),
                  (6,25,5,28,5,26),(24,8),(28,6,25,7,26,6),closed=True)
        self.ring('eye',34,14,3)
        self.path('g',(26,22),(22,20,25,20,24,20),(17,26,19,20,17,23),
                  (23,32,17,30,20,32),(29,26,27,32,29,30),(24,26))

    def path(self, name, start, *steps, closed=False):
        members=[]; here=start
        for j,step in enumerate(steps):
            member=f'{name}-{j}'
            if len(step)==2:
                self.add_line(member,here,step); end=step
            elif len(step)==5:
                x,y,rx,ry,sweep=step;end=(x,y)
                self.add_arc(member,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            else:
                x,y,c1x,c1y,c2x,c2y=step;end=(x,y)
                self.add_bezier(member,here,((c1x,c1y),(c2x,c2y),end))
            members.append(member);here=end
        self.add_contour(name,*members,closed=closed)

    def ring(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),(x,y-ry,rx,ry,True),(x+rx,y,rx,ry,True),
                  (x,y+ry,rx,ry,True),(x-rx,y,rx,ry,True),closed=True)

    def rect(self,name,x,y,w,h,r=3):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),(x+w,y+h-r),
                  (x+w-r,y+h,r,r,True),(x+r,y+h),(x,y+h-r,r,r,True),
                  (x,y+r),(x+r,y,r,r,True),closed=True)


    def cups(self,top=24,bottom=44):
        for side,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            def c(x,y,a,b,d,e):return (*p(x,y),*p(a,b),*p(d,e))
            self.path(side+'-hand',p(11,bottom),c(4,top+9,11,bottom-4,4,top+14),p(4,top),
                      (*p(10,top),3,3,s==1),p(10,top+7),
                      c(14,top+5,10,top+4,12,top+3),p(18,top+10),
                      c(20,top+14,19,top+11,20,top+12),p(20,bottom))
            self.add_line(side+'-thumb-crease',p(10,top+7),p(14,top+12))
            self.relate('connect',side+'-hand',side+'-thumb-crease')

# User explicitly delegated drawing-specific exception decisions. Automatic findings are retained.
Drawing.exception = {'reason': 'Retain the diagonal price-tag silhouette, round eyelet and curved G. The eyelet margin and compact G are visually separate at native size; allow the optical envelope and compact logo spacing.', 'approved_by': 'gpt-6 under explicit user-delegated exception authority', 'approved_on': '2026-09-29', 'svg_sha256': 'e9225ea4a3539f8e93a7c4acc63fee6d212f9eb5aae91637f6b0b421a4d40860'}
