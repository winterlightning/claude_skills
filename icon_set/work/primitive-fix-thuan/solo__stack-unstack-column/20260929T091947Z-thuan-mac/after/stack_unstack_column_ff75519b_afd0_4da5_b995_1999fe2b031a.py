from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'ff75519b-afd0-4da5-b995-1999fe2b031a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__stack-unstack-column/20260929T091947Z-thuan-mac/reference/stack unstack column_ff75519b-afd0-4da5-b995-1999fe2b031a.svg'
AUTHOR = "gpt-6"
# Plan: Restore a descending two-two-one column stack and two curved unstack arrows.
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
    icon_id = 'stack-unstack-column'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve all five descending cells and both curved return arrows; compact cell openings and arrow clearances are intentional.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '8ed69be0f76a9bc5816eef22f4ac2ed5e340f4fe884beb03929cee1a944dbf5d'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'top', 'M 7 6 L 14 6 A 1 1 1 15 7 L 15 19 A 1 1 1 14 20 L 7 20 A 1 1 1 6 19 L 6 7 A 1 1 1 7 6 Z')
        _draw(self, 'top-rule', 'M 6 13 L 15 13')
        _draw(self, 'middle', 'M 16 20 L 23 20 A 1 1 1 24 21 L 24 33 A 1 1 1 23 34 L 16 34 A 1 1 1 15 33 L 15 21 A 1 1 1 16 20 Z')
        _draw(self, 'middle-rule', 'M 15 27 L 24 27')
        _draw(self, 'bottom', 'M 25 34 L 32 34 A 1 1 1 33 35 L 33 41 A 1 1 1 32 42 L 25 42 A 1 1 1 24 41 L 24 35 A 1 1 1 25 34 Z')
        _draw(self, 'arrow-a', 'M 26 8 C 36 8 37 16 34 20 C 33 22 31 24 28 24')
        _draw(self, 'head-a', 'M 32 20 L 28 24 L 32 27')
        _draw(self, 'arrow-b', 'M 40 25 C 47 27 43 38 38 38')
        _draw(self, 'head-b', 'M 41 34 L 37 38 L 41 42')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
