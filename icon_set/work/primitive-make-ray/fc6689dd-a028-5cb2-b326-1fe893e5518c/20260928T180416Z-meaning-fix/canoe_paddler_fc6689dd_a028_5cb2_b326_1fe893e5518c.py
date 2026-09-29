"""Restore the leaning seated figure, bent arm, diagonal paddle, pointed canoe bow and two wave troughs.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The hull read as a bowl and the paddler had no clear bent arm or seated lean; water was omitted.
Construction: sailboat + human_ref/full_body_ref.png.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fc6689dd-a028-5cb2-b326-1fe893e5518c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__canoe-paddler/20260928T175901Z-thuan-mac/reference/canoe person_fc6689dd-a028-5cb2-b326-1fe893e5518c.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'canoe-paddler'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('canoe', 'person')

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

        circle('head',18,8,4)
        line('torso',(18,20),(14,31))
        poly('arm',(18,20),(26,22),(33,16));join('torso','arm')
        poly('leg',(14,31),(24,31),(25,28));join('torso','leg')
        line('paddle',(38,7),(24,34))
        path('canoe',(4,32),[L((34,32)),C((41,27),(39,32),(40,30)),C((41,39),(46,30),(46,36))])
        path('water',(4,41),[C((16,40),(9,44),(12,44)),C((28,40),(20,44),(24,44)),C((40,41),(32,44),(36,44))])
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
