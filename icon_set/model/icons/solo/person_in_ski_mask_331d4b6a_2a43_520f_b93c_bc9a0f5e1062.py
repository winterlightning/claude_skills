"""Criminal Wearing Ski Mask.

Symbol plan: Continuous balaclava head and neck silhouette with broad shoulders, symmetric about x=24. Visible (6,2)-(42,46). One broad capsule eye opening and a short mouth slit.
Construction references: human_ref/user.svg: broad open shoulders and circular head vocabulary; Lucide venetian-mask: paired eye marks.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '331d4b6a-2a43-520f-b93c-bc9a0f5e1062'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/tools criminal mask_331d4b6a-2a43-520f-b93c-bc9a0f5e1062.svg'
AUTHOR = 'gpt-6'


class PersonInSkiMask(Solo48):
    icon_id = 'person-in-ski-mask'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('person', 'in', 'ski', 'mask', 'sub icon')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x-r,y), [((x+r,y),r,r,True), ((x-r,y),r,r,True)], True)

        path('hood',(8,44), [((14,38),6,6,True),(14,36),((8,30),6,6,True),(8,20),((24,4),16,16,True),((40,20),16,16,True),(40,30),((34,36),6,6,True),(34,38),((40,44),6,6,True)])
        path('eye-opening',(21,14),[(27,14),((27,22),4,4,True),(21,22),((21,14),4,4,True)],True)
        self.add_line('mouth',(22,32),(26,32))


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('8a4bd6ce-492d-5b6a-a9ab-d8e814463361', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/criminal mask_8a4bd6ce-492d-5b6a-a9ab-d8e814463361.svg')]
