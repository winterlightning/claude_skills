"""Clipboard with a rounded top clip and two hands gripping its sides; shared bilateral hand definition.
Keyshape: VRECT_L. Uniform 4px SOLO48 stroke.
Construction: Lucide file-spreadsheet enclosure construction; supplied hand reference and human round-ended anatomy.
Revision: Restored rounded gripping hands, clipboard edges and two clean content lines.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fbccdc7f-b56b-54f5-a0fb-becef5e101fb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-holding-clipboard/20260928T173050Z-thuan-mac/reference/food delivery order manage_fbccdc7f-b56b-54f5-a0fb-becef5e101fb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-holding-clipboard'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hands', 'holding', 'clipboard')

    def build(self):
        self.path('board',(12,8),(19,8),(29,8,5,5,True),(36,8),(36,25))
        self.path('board-bottom',(14,39),(34,39))
        self.add_line('text-1',(18,16),(30,16));self.add_line('text-2',(18,23),(28,23))
        for side,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            def c(x,y,a,b,d,e):return (*p(x,y),*p(a,b),*p(d,e))
            self.path(side+'-edge',p(12,8),p(12,25))
            self.path(side+'-outer',p(5,43),p(5,30),c(12,20,5,25,9,23))
            self.path(side+'-grip',p(10,30),p(15,25),c(20,29,18,22,23,25),p(16,35),p(14,39),p(11,44))
            self.relate('connect',side+'-outer',side+'-edge')
        self.relate('connect','board','left-edge');self.relate('connect','board','right-edge')

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
