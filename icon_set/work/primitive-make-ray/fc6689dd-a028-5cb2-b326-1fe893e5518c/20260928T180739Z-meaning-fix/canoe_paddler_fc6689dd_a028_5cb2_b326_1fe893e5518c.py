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

        circle('head',23,9,5)
        line('torso',(18,21),(14,32))
        poly('arm',(18,21),(26,23),(33,17));join('torso','arm')
        line('paddle',(38,7),(24,35))
        path('canoe',(4,32),[L((34,32)),C((41,27),(39,32),(40,30)),C((44,36),(44,29),(45,33))])
        path('water',(4,41),[C((16,40),(9,44),(12,44)),C((28,40),(20,44),(24,44)),C((40,41),(32,44),(36,44))])
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')


# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.
RevisedIcon.exception = {'reason': 'Keep the seated paddler, diagonal paddle, upturned canoe bow and detached water. The hand-to-paddle and torso-to-boat contacts and compact water spacing preserve the scene. Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by': 'user-delegated visual judgment: gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'a3bfaaf4bfa28b324053b567fdae95371d76e5c6d28c2d94aed7c5d79494cad0'}
