# Variant of expanded-dropdown-menu; parent file remains unchanged.
"""Expanded Dropdown Menu; re-authored from the supplied visual reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5bf99203-19b4-4e87-a78c-325d7aec91d7'
SOURCE_PATH = 'pictographic-primitives/websites/web form drop down menu form_5bf99203-19b4-4e87-a78c-325d7aec91d7.svg'
SOURCE_REFERENCES = ({'source_icon_id': '5bf99203-19b4-4e87-a78c-325d7aec91d7', 'source_path': 'pictographic-primitives/websites/web form drop down menu form_5bf99203-19b4-4e87-a78c-325d7aec91d7.svg'},)
AUTHOR = 'gpt-6'

class ExpandedDropdownMenuVariant2(Solo48):
    icon_id = 'expanded-dropdown-menu-v2'
    variant_of = 'expanded-dropdown-menu'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('dropdown', 'menu', 'form', 'options', 'interface', 'chevron', 'selection')

    def build(self) -> None:
        self.box('field', 8, 4, 40, 12, r=2, joins=((12, 12),))
        self.add_polyline('panel', (12, 12), (12, 42), (40, 42), (40, 10))
        self.relate('connect', 'field', 'panel')
        self.add_line('option', (20, 21), (31, 21))
        self.add_polyline('down', (20, 30), (26, 36), (32, 30))

    def box(self, name, x0, y0, x1, y1, r=2, joins=()):
        points = [(x0 + r, y0), (x1 - r, y0), (x1, y0 + r), (x1, y1 - r), (x1 - r, y1), (x0 + r, y1), (x0, y1 - r), (x0, y0 + r)]
        members = []
        for i, p in enumerate(points):
            q = points[(i + 1) % 8]
            if i % 2:
                name_i = f'{name}-{i}'
                self.add_arc(name_i, p, q, radius_x=r)
                members.append(name_i)
            else:
                mid = [v for v in joins if v != p and v != q and (p[0] == q[0] == v[0] and min(p[1], q[1]) < v[1] < max(p[1], q[1]) or (p[1] == q[1] == v[1] and min(p[0], q[0]) < v[0] < max(p[0], q[0])))]
                run = [p] + sorted(mid, key=lambda v: (v[0] - p[0]) ** 2 + (v[1] - p[1]) ** 2) + [q]
                for j, (a, b) in enumerate(zip(run, run[1:])):
                    name_i = f'{name}-{i}-{j}'
                    self.add_line(name_i, a, b)
                    members.append(name_i)
        self.add_contour(name, *members, closed=True)
