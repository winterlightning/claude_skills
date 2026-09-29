from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '5b5a5348-95e6-489c-abb3-fe356243022b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__type-b-outlet-with-two-slots-and-ground-hole/20260929T090755Z-thuan-mac/reference/power outlet type b_5b5a5348-95e6-489c-abb3-fe356243022b.svg'
AUTHOR = "gpt-6"
# Plan: Restore the outlet plate, flattened round recess, vertical slots and arch-shaped ground opening.
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
    icon_id = 'type-b-outlet-with-two-slots-and-ground-hole'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve the flattened circular recess, slots and arch-shaped ground within the faceplate; larger square envelope and small openings remain readable.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9e78c46cf96f6c82bdcdf98e21b4ae6120ee4bf2272344ea9bcaf24245733067'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'plate', 'M 9 4 L 39 4 A 5 5 1 44 9 L 44 39 A 5 5 1 39 44 L 9 44 A 5 5 1 4 39 L 4 9 A 5 5 1 9 4 Z')
        _draw(self, 'recess', 'M 18 12 L 30 12 C 40 19 40 30 31 37 L 17 37 C 8 30 8 19 18 12 Z')
        _draw(self, 'slot-left', 'M 19 18 L 19 20')
        _draw(self, 'slot-right', 'M 29 18 L 29 20')
        _draw(self, 'ground', 'M 20 31 L 20 29 A 4 4 1 28 29 L 28 31 Z')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
