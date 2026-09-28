"""Drawing-bound, user-approved exceptions to the publication gate.

This does not modify geometry checks or their findings. Family canvas/stroke
requirements and checker errors remain blocking.
"""
import xml.etree.ElementTree as ET


def apply_exception(icon, row):
    approval = getattr(icon, 'exception', None)
    if not approval or row['status'] == 'error' or not row.get('_svg'):
        return row
    valid = (isinstance(approval, dict)
             and all(isinstance(approval.get(k), str) and approval[k].strip()
                     for k in ('reason', 'approved_by', 'svg_sha256'))
             and approval['svg_sha256'] == row.get('svg_sha256'))
    if not valid:
        row['errors'].append('exception: invalid approval or drawing changed; review required')
        row['status'] = 'fail'
        return row
    root = ET.fromstring(row['_svg'])
    widths = {e.get('stroke-width') for e in root.iter() if e.get('stroke-width') is not None}
    canvas = {('sub', 'SUB32'): '32', ('solo', 'SOLO48'): '48'}.get(
        (row['family'], row['profile']))
    if (canvas is None
            or (root.get('width'), root.get('height'), root.get('viewBox')) != (canvas, canvas, f'0 0 {canvas} {canvas}')
            or widths != {'4'}):
        row['errors'].append('exception: requires plain SUB32 32x32 or SOLO48 48x48, and uniform 4px strokes')
        row['status'] = 'fail'
        return row
    row['automatic_status'] = row['status']
    row['exception'] = dict(approval)
    row['status'] = 'pass'
    return row
