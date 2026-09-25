"""A crystal ball seated on a two-tier rounded stand. Restore the softly rounded pedestal and hide the ball’s lower arc behind its support.
Construction: Source-specific crystal ball; circular orb and repeated pedestal radii.
Fresh SOLO48 revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9acd961d-254b-46da-a4e6-47bf2a234155'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crystal-ball-on-stand/20260925T083047Z-thuan-mac/reference/sphere_9acd961d-254b-46da-a4e6-47bf2a234155.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crystal-ball-on-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('crystal', 'ball', 'on', 'stand')

    exception = {'reason': 'Retain both rounded pedestal tiers beneath the orb. The stand has visible three-unit and two-unit interior bands at 48px; merging the tiers would lose the source pedestal.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '9cc048719688876f8818eb2fc30a6050f7bcb072e46ec8872279db00d8f35872'}

    def build(self):

        def path(name, start, commands, closed=False):
            here, members = start, []
            for j, (kind, end, *a) in enumerate(commands):
                ident = f'{name}-{j}'
                if kind == 'L': self.add_line(ident, here, end)
                elif kind == 'A': self.add_arc(ident, here, end, radius_x=a[0], radius_y=a[1], sweep=a[2], large_arc=a[3] if len(a)>3 else False)
                elif kind == 'C': self.add_bezier(ident, here, (a[0], a[1], end))
                here = end
                members.append(ident)
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)

        path('orb',(15,31),[('A',(33,31),15,15,True,True)])
        path('upper-stand',(12,38),[('L',(12,34)),('A',(15,31),3,3,True),('L',(33,31)),('A',(36,34),3,3,True),('L',(36,38))]);join('orb','upper-stand')
        path('base',(11,38),[('L',(12,38)),('L',(36,38)),('L',(37,38)),('A',(37,44),3,3,True),('L',(11,44)),('A',(11,38),3,3,True)],True);join('upper-stand','base')

        from icon_set.model.primitives import Line
        from dataclasses import replace
        endpoints={p.start for p in self.primitives}|{p.end for p in self.primitives}
        replacements,rebuilt={},[]
        for primitive in self.primitives:
            if isinstance(primitive,Line) and primitive.start!=primitive.end:
                a,b=primitive.start,primitive.end;dx,dy=b.x-a.x,b.y-a.y
                cuts=[q for q in endpoints if q not in (a,b) and (q.x-a.x)*dy==(q.y-a.y)*dx and 0<(q.x-a.x)*dx+(q.y-a.y)*dy<dx*dx+dy*dy]
                if cuts:
                    nodes=[a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b];names=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        name=f'{primitive.element_id}-node-{j}';rebuilt.append(Line(name,u,v));names.append(name)
                    replacements[primitive.element_id]=names
                    if not any(primitive.element_id in c.members for c in self.contours):self.add_contour(primitive.element_id,*names)
                    continue
            rebuilt.append(primitive)
        if replacements:
            self.primitives[:]=rebuilt
            self.contours[:]=[replace(c,members=tuple(k for m in c.members for k in replacements.get(m,[m]))) for c in self.contours]
