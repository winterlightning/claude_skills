"""Key with intrinsic heart bow opening, short shaft and one tooth.
VRECT_L 8,4..40,44 budgets the heart inside a broad bow. Bow and shaft share
the bottom cardinal node; heart mirrors about x24. Reorient upright and omit
one tooth to maintain clearance. Source gives heart identity; Lucide key-round
supplies a simple bow/shaft construction principle, reauthored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a99dc4a0-50a0-4f59-b6d5-d30eb8b0581c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/love heart key_a99dc4a0-50a0-4f59-b6d5-d30eb8b0581c.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'key-with-heart-shaped-bow-opening'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ("heart key",)
    keywords = ("key", "heart", "romance")
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

        self.add_arc('bow-left',(24,36),(24,4),radius_x=16)
        self.add_arc('bow-right',(24,4),(24,36),radius_x=16)
        self.add_contour('bow','bow-left','bow-right',closed=True)
        poly('shaft',(24,36),(24,44),(34,44));join('shaft','bow')
        self.add_arc('heart-left',(24,17),(18,17),radius_x=3,sweep=False)
        line('heart-side1',(18,17),(24,27));line('heart-side2',(24,27),(30,17))
        self.add_arc('heart-right',(30,17),(24,17),radius_x=3,sweep=False)
        self.add_contour('heart','heart-left','heart-side1','heart-side2','heart-right',closed=True)
