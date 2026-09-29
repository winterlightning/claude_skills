"""Rounded page outline, folded top corner and two-column spreadsheet panel.
Keyshape: VRECT_L. Uniform 4px SOLO48 stroke.
Construction: Lucide file-spreadsheet original and atomic-debug: rounded page and shared fold junctions.
Revision: Rounded the page, restored the corner fold, and opened an even two-by-two table.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b10704f2-58af-44bd-849f-dcd977ac9d2f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-sheets-logo/20260928T173050Z-thuan-mac/reference/google sheets logo_b10704f2-58af-44bd-849f-dcd977ac9d2f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'google-sheets-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'sheets', 'logo')

    def build(self):
        self.path('page',(12,4),(28,4),(40,16),(40,40),(36,44,4,4,True),(12,44),
                  (8,40,4,4,True),(8,8),(12,4,4,4,True),closed=True)
        self.path('fold',(28,4),(28,12),(32,16,4,4,False),(40,16))
        self.relate('connect','page','fold')
        self.path('table',(16,23),(24,23),(32,23),(32,30),(32,37),(24,37),(16,37),(16,30),(16,23),closed=True)
        self.path('row',(16,30),(24,30),(32,30))
        self.path('column',(24,23),(24,30),(24,37))
        for a,b in [('table','row'),('table','column'),('row','column')]:self.relate('connect',a,b)

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
