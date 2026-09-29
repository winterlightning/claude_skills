"""Restore a rounded handset with bottom separator and a recognizable curved pound stem and baseline.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The device lacked its lower phone panel and the pound glyph had a straight bar-like foot.
Construction: smartphone.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a70db137-a446-4f4c-b656-4fea14660981'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-phone-pound-sign/20260928T175901Z-thuan-mac/reference/mobile phone pound sign_a70db137-a446-4f4c-b656-4fea14660981.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'mobile-phone-pound-sign'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('mobile', 'phone', 'pound', 'sign')

    def build(self):

        def path(name,start,commands,closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(commands):
                if end==here and kind=='L':continue
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        L=lambda end:('L',end)
        C=lambda end,c1,c2:('C',end,c1,c2)
        A=lambda end,rx,ry,sweep:('A',end,rx,ry,sweep)
        line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        rounded('phone',10,4,38,44,5)
        line('phone-bottom',(10,36),(38,36))
        path('pound',(28,16),[C((24,12),(28,13),(27,12)),C((20,16),(21,12),(20,13)),L((20,25)),C((18,28),(20,27),(19,28)),L((29,28))])
        line('pound-crossbar',(18,20),(26,20))
