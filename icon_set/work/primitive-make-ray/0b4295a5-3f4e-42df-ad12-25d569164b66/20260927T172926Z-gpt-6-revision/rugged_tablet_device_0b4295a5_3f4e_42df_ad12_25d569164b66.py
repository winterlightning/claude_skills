"""Upright rugged tablet with a broad blank display. The tiny home key was omitted to preserve a clear display opening at SOLO48; no exact Lucide match was useful."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0b4295a5-3f4e-42df-ad12-25d569164b66'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rugged-tablet-device/20260927T172707Z-thuan-mac-1/reference/tablet rugged_0b4295a5-3f4e-42df-ad12-25d569164b66.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'rugged-tablet-device'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('rugged', 'tablet', 'device')

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

        # The source uses a tall blank display and a restrained bottom key.
        box('case',8,4,40,44,5);box('screen',17,13,31,35,2)
