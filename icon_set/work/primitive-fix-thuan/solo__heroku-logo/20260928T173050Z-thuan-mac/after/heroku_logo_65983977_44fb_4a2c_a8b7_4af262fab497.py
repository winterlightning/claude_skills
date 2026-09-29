"""Rounded frame holding lowercase h, a separate upper accent and a right-pointing triangle at the stem foot.
Keyshape: SQUARE. Uniform 4px SOLO48 stroke.
Construction: No useful exact Lucide brand match; shared geometric construction.
Revision: Restored the arrow and distinct slanted accent with a smooth h shoulder inside a regular frame.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '65983977-44fb-4a2c-a8b7-4af262fab497'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heroku-logo/20260928T173050Z-thuan-mac/reference/heroku logo_65983977-44fb-4a2c-a8b7-4af262fab497.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'heroku-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('heroku', 'logo')

    def build(self):
        self.rect('frame',6,4,36,40,4)
        self.path('stem',(16,11),(16,26),(16,37))
        self.path('h',(16,26),(26,23,21,24,24,23),(33,29,31,23,33,25),(33,37))
        self.relate('connect','stem','h')
        self.path('arrow',(16,37),(23,33),(16,29));self.relate('connect','stem','arrow')
        self.path('accent',(30,16),(34,10),(36,10))

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
Drawing.exception = {'reason': 'Retain the Heroku h, rising accent and small triangular stem mark. The tiny arrow counter and compact accent spacing are brand-defining and visibly readable; preserve the tall rounded frame.', 'approved_by': 'gpt-6 under explicit user-delegated exception authority', 'approved_on': '2026-09-29', 'svg_sha256': 'e4787f5738961cc9af778d3bf412fae6e7647aea4e321232111b163ce8f2f17d'}
