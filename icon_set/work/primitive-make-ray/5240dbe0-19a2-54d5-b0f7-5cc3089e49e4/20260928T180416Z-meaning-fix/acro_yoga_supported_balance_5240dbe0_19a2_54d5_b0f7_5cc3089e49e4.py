"""Keep exactly two right-facing detached heads and two horizontal torsos, with the upper curled leg and lower bent leg.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: An extra head-like ring at the top and a single shared body obscured the two-person pose.
Construction: human_ref/full_body_ref.png.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5240dbe0-19a2-54d5-b0f7-5cc3089e49e4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__acro-yoga-supported-balance/20260928T175901Z-thuan-mac/reference/acro yoga pose_5240dbe0-19a2-54d5-b0f7-5cc3089e49e4.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'acro-yoga-supported-balance'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('acro', 'yoga', 'pose')

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

        circle('upper-head',38,24,4);circle('lower-head',38,42,4)
        line('upper-torso',(26,24),(10,24))
        path('upper-leg',(26,24),[C((23,12),(31,20),(22,16)),C((26,5),(19,5),(23,3)),C((28,9),(29,5),(30,8))])
        join('upper-torso','upper-leg')
        line('lower-torso',(26,42),(12,42))
        path('lower-leg',(26,42),[C((26,25),(28,38),(26,30))]);join('lower-torso','lower-leg')
        self.mark_human_figure('upper',head='upper-head',torso='upper-torso',torso_junction='start')
        self.mark_human_figure('lower',head='lower-head',torso='lower-torso',torso_junction='start')
