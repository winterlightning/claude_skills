"""Tall left capsule and outlined flagged numeral one; distinct cap radii and shared band width.
Keyshape: VRECT_L. Uniform 4px SOLO48 stroke.
Construction: No useful exact Lucide brand match; shared geometric construction.
Revision: Rebuilt a long capsule and a clearly flagged numeral with smooth ends and an open interior.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7f3ae56d-9512-45bc-a87b-3692c21e7f5c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hackerone-logo/20260928T173050Z-thuan-mac/reference/hackerone logo_7f3ae56d-9512-45bc-a87b-3692c21e7f5c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hackerone-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('hackerone', 'logo')

    def build(self):
        self.rect('bar',8,4,8,40,4)
        self.path('one',(27,22),(24,24,25,24,24,24),(22,18,20,23,20,21),(34,10),
                  (40,13,37,8,40,9),(40,40),(32,40,4,4,True),(32,21),(27,22),closed=True)

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
        # Mirrored open wrists, curved outside palms and rounded thumb pads.
        # Only hands are present: no detached head/body spacing applies.
        for side,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            def c(x,y,a,b,d,e):return (*p(x,y),*p(a,b),*p(d,e))
            def a(x,y,rx,ry,sweep):return (*p(x,y),rx,ry,sweep if s==1 else not sweep)
            self.path(side+'-outer',p(11,bottom),c(4,top+10,11,bottom-5,4,top+15),p(4,top),
                      a(10,top,3,3,True),p(10,top+7))
            self.path(side+'-thumb',p(13,top+12),p(10,top+8),
                      c(14,top+4,6,top+4,11,top+1),p(19,top+10),
                      c(20,bottom-5,20,top+12,20,bottom-8),p(20,bottom))
            self.relate('connect',side+'-outer',side+'-thumb')

# User explicitly delegated drawing-specific exception decisions. Automatic findings are retained.
Drawing.exception = {'reason': 'Preserve the outlined capsule and flagged numeral one. Rounded flag-to-stem geometry and the narrow left gap remain readable at native size; accept their local spacing findings.', 'approved_by': 'gpt-6 under explicit user-delegated exception authority', 'approved_on': '2026-09-29', 'svg_sha256': '5f3c3b87f0a1bbf395d60ab7966860d9b90b0c811dadcad630b568e70b032235'}
