'Teapot on Serving Tray.\nPlan: Teapot with spout, knob and high loop handle resting on a rectangular stand with two feet.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Lid seam omitted; spout, lid knob, handle, stand and feet retained.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df688f36-b5fe-4f17-ae65-8d71d00de128'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tea pot 1_df688f36-b5fe-4f17-ae65-8d71d00de128.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'teapot-serving-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('teapot', 'serving', 'stand')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('pot',(22,12),[((28,14),10,10,True),((32,22),10,10,True),((22,32),10,10,True),(14,32),(6,26),(6,14),(14,14),(14,16),((22,12),10,10,True)],True)
        path('handle',(28,14),[((42,18),14,4,True),((32,22),10,4,True)]);self.relate('connect','pot','handle')
        circle('knob',22,8,2);self.add_line('stem',(22,10),(22,12));self.relate('connect','stem','knob');self.relate('connect','stem','pot')
        path('tray',(6,32),[(14,32),(22,32),(42,32),(42,40),(34,40),(14,40),(6,40),(6,32)],True);self.relate('connect','tray','pot')
        for x in (14,34):
         self.add_line(f'foot-{x}',(x,40),(x,42));self.relate('connect',f'foot-{x}','tray')
