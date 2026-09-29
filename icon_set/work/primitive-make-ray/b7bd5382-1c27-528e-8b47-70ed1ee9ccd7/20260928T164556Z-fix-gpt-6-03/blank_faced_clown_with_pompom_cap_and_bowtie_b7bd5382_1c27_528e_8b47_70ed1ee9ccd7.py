"""circus clown.
Before review: The cap bisected a circular face, the hair became ears and the bowtie dominated the portrait.
Feedback: Manual fix request
Revision: Lengthened the blank face below the cap brim, restored scalloped side hair, and reduced the bowtie around a distinct round knot.
Construction: human_ref/user.svg: circular jaw vocabulary; no useful exact Lucide clown match.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 VRECT_L; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b7bd5382-1c27-528e-8b47-70ed1ee9ccd7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__blank-faced-clown-with-pompom-cap-and-bowtie/20260928T164556Z-thuan-mac/reference/circus clown_b7bd5382-1c27-528e-8b47-70ed1ee9ccd7.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'blank-faced-clown-with-pompom-cap-and-bowtie'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('circus', 'clown')
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                ident=f'{name}-{i}'
                if len(step)==2:
                    self.add_line(ident,here,step); end=step
                elif step[0]=='C':
                    _,end,c1,c2=step
                    self.add_bezier(ident,here,(c1,c2,end))
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def rounded(name,l,t,r,b,k):
            path(name,(l+k,t),[(r-k,t),((r,t+k),k,k,True),(r,b-k),((r-k,b),k,k,True),(l+k,b),((l,b-k),k,k,True),(l,t+k),((l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('face',(16,18),[(16,24),((32,24),8,8,False),(32,18)],False)
        path('cap',(16,18),[((24,10),8,8,True),((32,18),8,8,True),(16,18)],True);join('face','cap')
        circle('pompom',24,6,2);line('hat-tip',(24,8),(24,10));join('hat-tip','pompom');join('hat-tip','cap')
        path('hair-left',(16,18),[((10,19),4,4,False),((10,26),4,4,False),((16,27),4,4,False)])
        path('hair-right',(32,18),[((38,19),4,4,True),((38,26),4,4,True),((32,27),4,4,True)])
        join('hair-left','face');join('hair-left','cap');join('hair-right','face');join('hair-right','cap')
        circle('knot',24,40,2)
        path('bow-left',(22,40),[(13,36),(13,44),(22,40)],True);path('bow-right',(26,40),[(35,36),(35,44),(26,40)],True)
        join('knot','bow-left');join('knot','bow-right')
