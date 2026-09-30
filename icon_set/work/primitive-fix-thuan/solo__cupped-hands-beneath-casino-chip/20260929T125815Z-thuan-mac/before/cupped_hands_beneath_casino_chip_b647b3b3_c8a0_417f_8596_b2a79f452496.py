"""Two cupped hands beneath a segmented casino chip.
SQUARE retains bilateral palms and the upper chip. Hands mirror about x=24;
chip quarters and radial rim joins share one center. Source supplies subject
and arrangement; inspected Lucide hand supplies smooth palm/thumb construction.
Small finger and cuff details omitted. Four rim divisions preserve chip identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b647b3b3-c8a0-417f-8596-b2a79f452496'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/casino chip hold_b647b3b3-c8a0-417f-8596-b2a79f452496.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'cupped-hands-beneath-casino-chip'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ("Hands Holding Casino Chip",)
    keywords = ("hands", "chip", "casino", "poker", "round", "palms", "gambling")
    def build(self):

        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        for side in (-1,1):
            x=lambda a:24+side*a
            self.add_bezier(f'hand{side}',(x(7),42),((x(7),39),(x(18),40),(x(18),34)),((x(18),31),(x(18),28),(x(18),24)))
            line(f'thumb{side}',(x(18),34),(x(12),32))
            join(f'hand{side}',f'thumb{side}')
        for name, radius in (("chip",11),("center",2)):
            pts=[(24,17-radius),(24+radius,17),(24,17+radius),(24-radius,17)]
            for j in range(4):
                self.add_arc(f"{name}-{j}",pts[j],pts[(j+1)%4],radius_x=radius,sweep=True)
            self.add_contour(name,*(f"{name}-{j}" for j in range(4)),closed=True)
        for j,(dx,dy) in enumerate(((0,-1),(1,0),(0,1),(-1,0))):
            self.add_line(f"rim-{j}",(24+2*dx,17+2*dy),(24+11*dx,17+11*dy))
            self.relate("connect",f"rim-{j}","chip")
            self.relate("connect",f"rim-{j}","center")
