"""cuffed-hands-supporting-faceted-diamond.
Plan: Mirrored cupped hands with retained cuffs support a centered faceted diamond; shared axis x24 and common cuff dimensions.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: Lucide hand-helping: a continuous palm stroke and simple cuff.
Omissions: Small secondary diamond facets.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2a6eda08-c10d-4226-80a2-1ca03654ee6e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cuffed-hands-supporting-faceted-diamond/20260924T105711Z-thuan-mac/reference/diamond give_2a6eda08-c10d-4226-80a2-1ca03654ee6e.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'cuffed-hands-supporting-faceted-diamond'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('diamond', 'give')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        self.add_polyline('gem',(18,6),(30,6),(36,14),(24,24),(12,14),closed=True)
        self.add_line('facet',(12,14),(36,14));self.relate('connect','facet','gem')
        for side in (-1,1):
            def pt(x,y):return (24+side*x,y)
            n='left' if side<0 else 'right'
            self.add_line(n,pt(18,22),pt(18,34))
            path(n+'-thumb',pt(6,34),[pt(6,31),pt(10,27)])
            box(n+'-cuff',6 if side<0 else 30,34,18 if side<0 else 42,42,1)
            self.relate('connect',n,n+'-cuff');self.relate('connect',n+'-thumb',n+'-cuff')
