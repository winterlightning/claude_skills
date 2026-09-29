"""person with plus.
Before review: The plus is undersized relative to the head, as the reviewer explicitly noted.
Feedback: Manual fix request

plus icon is small size
Revision: Enlarged plus arms by 50 percent, enlarged the circular head and rebalanced the shoulders; retained the exact 4-unit detached head gap.
Construction: human_ref/user.svg: circular head and smooth shoulders; Lucide user-round-plus original and atoms: orthogonal plus and shared shoulder arc.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 HRECT_L; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e68e4095-a045-40e9-81f2-491f7d5b6a83'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__add-user-profile-content/20260928T164556Z-thuan-mac/reference/person with plus_e68e4095-a045-40e9-81f2-491f7d5b6a83.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'add-user-profile-content'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('person', 'with', 'plus')
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

        def pt(x,y): return (48-x,y) if False else (x,y)
        cx=16 if not False else 32
        circle('head',cx,15,7)
        path('shoulders',pt(4,40),[(pt(16,30),12,10,True),(pt(28,40),12,10,True)])
        poly('plus-h',pt(32,15),pt(38,15),pt(44,15))
        poly('plus-v',pt(38,9),pt(38,15),pt(38,21))
        join('plus-h','plus-v')
