"""Flowing headcloth joins broad shoulders at shared points; circular face touches the shoulder top with zero ink gap.
Reference comparison: Current headcloth resembles short hair and a hat brim; reference has a flowing veil around the face and broad shoulders. Rebuild long cloth contours and smooth paired shoulders, retaining robe placket.
Construction reference: human_ref/user.svg and Lucide user-round: face and shoulder proportions.
SOLO48 keyshape VRECT_L; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='dd92cb2d-e66d-53d1-835f-92be92e0873e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__arabian-man-avatar/20260928T172849Z-thuan-mac/reference/arabian man_dd92cb2d-e66d-53d1-835f-92be92e0873e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='arabian-man-avatar'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='avatars'
    aliases=()
    keywords=('arabian', 'man')

    def build(self):

        # Typed path helpers own continuous contours, repeated radii and real junctions.
        def path(name,start,commands,closed=False):
            here=start;members=[]
            for i,c in enumerate(commands):
                kind,end,*args=c; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C':
                    c1,c2=args
                    self.add_bezier(ident,here,(c1,c2,end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('veil',(12,35),[('C',(8,20),(12,30),(8,26)),('A',(40,20),16,16,True),('C',(36,35),(40,26),(36,30))])
        circle('face',24,20,8)
        path('shoulders',(8,44),[('C',(12,35),(8,40),(8,37)),('C',(24,32),(16,32),(18,32)),('C',(36,35),(30,32),(32,32)),('C',(40,44),(40,37),(40,40))])
        line('robe',(24,32),(24,44));join('robe','shoulders');join('veil','shoulders');join('face','shoulders')
