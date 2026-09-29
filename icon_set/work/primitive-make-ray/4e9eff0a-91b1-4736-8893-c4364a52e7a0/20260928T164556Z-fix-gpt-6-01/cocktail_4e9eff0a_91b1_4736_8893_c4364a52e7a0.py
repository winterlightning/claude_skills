"""cocktail.
Before review: The bowl and straw were heavy and the stem too short compared with the tall reference glass.
Feedback: Manual fix request
Revision: Extended the stem, widened the bowl and rebuilt a single straight straw with one top bend.
Construction: Lucide martini: stem centered on bowl and equal base arms; source retains rounded bowl.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 VRECT_L; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4e9eff0a-91b1-4736-8893-c4364a52e7a0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cocktail/20260928T164649Z-thuan-mac/reference/cocktail_4e9eff0a-91b1-4736-8893-c4364a52e7a0.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'cocktail'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cocktail',)
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

        path('bowl',(8,15),[(40,15),((24,31),16,16,True),((8,15),16,16,True)],True)
        poly('stem',(24,31),(24,44));poly('base',(16,44),(24,44),(32,44));join('stem','bowl');join('stem','base')
        poly('straw',(24,24),(34,6),(40,4));join('straw','bowl')
