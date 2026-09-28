'Single Finger Tap Gesture.\nPlan and review: Retained raised index finger, curled palm, projecting thumb and open touch halo. Widened thumb opening; the halo remains part of the physical gesture.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: human_ref rounded limb vocabulary and Lucide hand; halo is intrinsic to touch gesture, not independent status.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef8f2fd7-4136-4eac-be53-e53b7781ca3d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/touch finger_ef8f2fd7-4136-4eac-be53-e53b7781ca3d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'finger-tap-gesture-reference-ef8f2fd7'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('finger', 'tap', 'gesture', 'reference', 'ef8f2fd7')

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

        path('hand',(18,44),[(10,36),((16,30),5,5,True),(20,34),(20,22),((28,22),4,4,True),(28,30),(40,34),(38,44)])
        path('halo',(8,22),[((40,22),16,18,True)])
