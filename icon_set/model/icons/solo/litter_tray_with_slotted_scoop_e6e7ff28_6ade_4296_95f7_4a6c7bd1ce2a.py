"""Litter tray with a diagonal handled scoop and one broad slot.
SQUARE envelope (6,6)..(42,42) keeps the tray broad and scoop clearly angled.
Tray owns scoop attachment nodes; scoop top owns the handle junction.
The reference supplies the physical pairing and tilt. Omit the second slot
and doubled rim to keep 8-unit centerline clearances. Lucide shovel informs
the central handle attachment to a broad tool blade, reauthored on this grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6e7ff28-6ade-4296-95f7-4a6c7bd1ce2a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/cat litter_e6e7ff28-6ade-4296-95f7-4a6c7bd1ce2a.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'litter-tray-with-slotted-scoop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ["Litter Box with Scoop"]
    keywords = ["litter", "tray", "scoop", "cat", "pet", "cleaning", "slotted"]
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
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

        poly('tray',(6,32),(8,32),(22,32),(32,32),(42,32),(38,42),(10,42),(6,32))
        poly('scoop',(8,32),(16,14),(26,19),(36,24),(32,32))
        line('handle',(26,19),(34,6))
        line('slot',(24,27),(22,32))
        join('scoop','tray');join('handle','scoop');join('slot','tray')
