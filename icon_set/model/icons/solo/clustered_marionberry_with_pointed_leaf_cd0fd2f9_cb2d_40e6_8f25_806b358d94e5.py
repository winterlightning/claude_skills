"""Tapered lobed marionberry with a pointed leaf to the upper right.
VRECT_L 8,4..40,44. A coherent scalloped silhouette replaces overlapping
closed drupelets; omit the crowded internal cell and leaf vein. The leaf and
berry share an attachment edge. Reference supplies taper and upper-right leaf;
Lucide leaf informs the pointed coherent outline, reauthored on this grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd0fd2f9-cb2d-40e6-8f25-806b358d94e5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/marionberry_cd0fd2f9-cb2d-40e6-8f25-806b358d94e5.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'clustered-marionberry-with-pointed-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ("marionberry",)
    keywords = ("berry", "fruit", "leaf", "cluster")
    category = "primitives-generate"
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        bez('berry',(30,18),((34,18),(36,24),(30,26)),((38,29),(34,38),(28,38)),((28,46),(16,46),(16,38)),((12,40),(8,36),(8,32)),((8,29),(9,27),(12,26)),((6,18),(16,12),(22,18)))
        bez('leaf',(22,18),((22,8),(30,4),(40,4)),((40,13),(36,18),(30,18)))
        self.add_contour('outline','berry','leaf',closed=True)
        line('attachment',(22,18),(30,18))
        join('outline','attachment')
