"""Smiling striped cat head with two ears, two forehead stripes and closed eyes.
SQUARE envelope (6,6)-(42,42). One symmetric head contour owns two attached
stripes; mirrored eye curves and a small smile preserve expression. Source
supplies the stripes and happy face; Lucide cat supplies the ear/cheek contour
principle. Omit the separate nose, muzzle lobes and open mouth for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2fc1c66-2c6a-4bed-b334-72d7a85619d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/ocelot_e2fc1c66-2c6a-4bed-b334-72d7a85619d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-striped-cat-head'
    keyshape = Keyshape.SQUARE
    category = "Uncategorized"
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ("Happy Striped Cat Face",)
    keywords = ("cat", "head", "smile", "stripes", "animal", "face")
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

        self.add_bezier('left-ear',(6,6),((6,6),(15,8),(16,14)))
        self.add_bezier('forehead-left',(16,14),((17,13),(18,12),(20,12)))
        self.add_line('forehead',(20,12),(28,12))
        self.add_bezier('forehead-right',(28,12),((30,12),(31,13),(32,14)))
        self.add_bezier('right-ear',(32,14),((33,8),(42,6),(42,6)),((42,12),(42,16),(39,20)))
        self.add_bezier('cheeks',(39,20),((42,31),(34,42),(24,42)),((14,42),(6,31),(9,20)),((6,16),(6,12),(6,6)))
        self.add_contour('head','left-ear','forehead-left','forehead','forehead-right','right-ear','cheeks',closed=True)
        for x in (20,28):
            self.add_line(f'stripe-{x}',(x,12),(x,14))
            self.relate('connect','head',f'stripe-{x}')
        self.add_bezier('eye-left',(17,24),((17,22),(20,22),(20,24)))
        self.add_bezier('eye-right',(28,24),((28,22),(31,22),(31,24)))
        self.add_bezier('smile',(21,32),((23,34),(25,34),(27,32)))
