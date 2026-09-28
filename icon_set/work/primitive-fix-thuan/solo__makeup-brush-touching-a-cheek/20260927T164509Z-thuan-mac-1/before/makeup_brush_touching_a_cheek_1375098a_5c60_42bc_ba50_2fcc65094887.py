"""A cosmetic brush applies makeup to a partial facial profile.
SQUARE reaches (6,6)-(42,42); the diagonal brush leaves room for the lips and jaw.
The source supplies the partial face, bristle head and diagonal handle.
Human user.svg informs smooth minimal anatomy; Lucide paintbrush informs the
separate handle and bristle contours. Fine facial detail and bristle texture
are omitted. Reused the existing draft, removing the returning lower-lip curl after export
QA found an undersized opening at the mouth.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1375098a-5c60-42bc-ba50-2fcc65094887'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/beauty massage spread_1375098a-5c60-42bc-ba50-2fcc65094887.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'makeup-brush-touching-a-cheek'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ["Makeup Brush and Facial Cream"]
    keywords = ["makeup", "brush", "cheek", "face", "cosmetic", "beauty", "application"]
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

        bez('face',(14,6),((18,12),(13,14),(8,14)),((6,14),(6,16),(6,18)))
        bez('mouth',(6,28),((8,26),(10,26),(12,28)))
        bez('jaw',(6,42),((14,42),(22,42),(26,38)),((30,34),(30,32),(30,30)))
        poly('brush',(26,16),(36,6),(42,12),(36,22),(26,16));poly('bristles',(26,16),(22,24),(30,30),(36,22));join('brush','bristles');join('jaw','bristles')
