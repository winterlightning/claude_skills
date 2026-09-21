'Paired open hands around held object. Fingers reduced to cupped gesture; cuffs and small internal detail omitted. Shared human reference and Lucide hand construction inspected.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b647b3b3-c8a0-417f-8596-b2a79f452496'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/casino chip hold_b647b3b3-c8a0-417f-8596-b2a79f452496.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cupped-hands-beneath-casino-chip'
    keyshape = Keyshape.SQUARE
    category = "objects"
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
        circle('chip',24,17,11);circle('center',24,17,2)
