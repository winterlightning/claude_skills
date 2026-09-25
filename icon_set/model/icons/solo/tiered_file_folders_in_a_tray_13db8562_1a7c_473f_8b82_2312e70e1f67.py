'Tiered File Folders in a Tray\nPlan: Two elevated folder backs rise behind a notched tray; flat back edges leave eight units of open spacing.\nReference: Lucide archive: broad rounded tray with a finger recess.\nReduction: Two simple folder top edges replace three narrow rounded backs.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13db8562-1a7c-473f-8b82-2312e70e1f67'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/archive folder_13db8562-1a7c-473f-8b82-2312e70e1f67.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tiered-file-folders-in-a-tray'
    keyshape = Keyshape.VRECT_L
    category = "primitives-generate"
    keywords = ('tiered', 'file', 'folders', 'in', 'a', 'tray')

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
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        self.add_line('back',(12,4),(36,4))
        self.add_line('middle',(12,14),(36,14))
        path('tray',(12,24),[(18,24),((22,28),4,4,False),(26,28),((30,24),4,4,False),(36,24),((40,28),4,4,True),(40,40),((36,44),4,4,True),(12,44),((8,40),4,4,True),(8,28),((12,24),4,4,True)],True)
