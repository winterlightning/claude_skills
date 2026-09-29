from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'facf19d7-e5b7-4559-806e-6d1d682ef4d0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-dollar-money-bags/20260929T090755Z-thuan-mac/reference/money bags_facf19d7-e5b7-4559-806e-6d1d682ef4d0.svg'
AUTHOR = "gpt-6"
# Plan: Restore two rounded tied bags in depth, scalloped open tops and a clear dollar on the front bag.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: none.

def _draw(icon, name, description):
    tokens=description.split(); pos=0; part=0; count=0; members=[]; start=None; point=None
    def finish(closed=False):
        nonlocal members,part
        if members: icon.add_contour(name if part==0 else f"{name}-part{part}",*members,closed=closed)
        members=[];part+=1
    while pos<len(tokens):
        op=tokens[pos];pos+=1
        if op=='M':
            if members: finish()
            point=tuple(map(int,tokens[pos:pos+2]));pos+=2;start=point
        elif op=='Z':
            if point!=start:
                count+=1;eid=f"{name}-{count}";icon.add_line(eid,point,start);members.append(eid);point=start
            finish(True)
        else:
            count+=1;eid=f"{name}-{count}";members.append(eid)
            if op=='L':
                end=tuple(map(int,tokens[pos:pos+2]));pos+=2;icon.add_line(eid,point,end)
            elif op=='C':
                values=list(map(int,tokens[pos:pos+6]));pos+=6;c1=tuple(values[:2]);c2=tuple(values[2:4]);end=tuple(values[4:]);icon.add_bezier(eid,point,(c1,c2,end))
            elif op=='A':
                rx,ry,sweep,x,y=map(int,tokens[pos:pos+5]);pos+=5;end=(x,y);icon.add_arc(eid,point,end,radius_x=rx,radius_y=ry,sweep=bool(sweep))
            point=end
    if members: finish()

class Revision(Solo48):
    icon_id = 'two-dollar-money-bags'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve overlapping scalloped money bags and the dollar symbol; compact currency mark and organic bounds are intentional.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'a0ca44369f94133160a9e3e957306bd2bd954e4e4c9ff31332d22b3bb598ab29'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'front', 'M 23 15 C 18 20 14 28 14 33 C 14 40 20 42 29 42 C 38 42 42 39 42 33 C 42 28 37 20 33 15 L 37 7 C 33 9 32 3 28 7 C 24 3 23 9 19 7 L 23 15 Z')
        _draw(self, 'tie', 'M 23 15 L 33 15')
        _draw(self, 'rear', 'M 12 36 C 3 36 4 24 11 17 L 8 11 L 13 12 L 16 9 L 20 12')
        _draw(self, 'dollar', 'M 33 24 L 27 24 C 22 24 22 29 28 29 C 34 29 34 35 28 35 L 23 35')
        _draw(self, 'bar', 'M 28 21 L 28 38')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
