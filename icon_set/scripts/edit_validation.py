"""Build validation for catalog geometry plus editor transforms, without executing icon source."""
from datetime import datetime, timezone
import hashlib
import json


def validate_graph(graph):
    from icon_set.model.icons.base import Icon
    from icon_set.model.keyshapes import Keyshape, FreeKeyshapeSpec
    from icon_set.model.profiles import Profile
    from icon_set.model.primitives import primitive_from_dict, Contour, Relationship, Point, HumanFigure
    from icon_set.validation.library_qa import inspect_icon
    from icon_set.validation.circle_exceptions import circle_candidates
    from icon_set.model import contracts

    free = graph.get('free_keyshape')
    icon = Icon(graph['icon_id'], Profile[graph['profile']],
                semantic_role=graph.get('semantic_role'), keyshape=Keyshape[graph['keyshape']],
                free_keyshape=FreeKeyshapeSpec(*free['bounds'], free['rationale'], free.get('approval_id')) if free else None,
                primitives=[primitive_from_dict(p) for p in graph['primitives']],
                contours=[Contour(c['contour_id'], tuple(c['members']), c['closed']) for c in graph.get('contours', [])],
                relationships=[Relationship(r['kind'], tuple(r['members'])) for r in graph.get('relationships', [])])
    for field in ('family', 'semantic_kind', 'category', 'composition_class'):
        if field in graph:
            setattr(icon, field, graph[field])
    for field, attribute in (('stroke_width', 'STROKE_WIDTH'), ('line_cap', 'LINE_CAP'), ('line_join', 'LINE_JOIN'), ('grid', 'GRID')):
        if field in graph.get('style', {}):
            setattr(icon, attribute, graph['style'][field])
    icon.anchors = {name: Point(*point) for name, point in graph.get('anchors', {}).items()}
    icon.human_figures = [HumanFigure(f['figure_id'], f['head'], f['torso'], f['torso_junction']) for f in graph.get('human_figures', [])]
    report = inspect_icon(icon)
    result = {key: report[key] for key in ('status', 'errors', 'warnings', 'checks_run', 'needs_review', 'svg_sha256', 'rules_sha256') if key in report}
    result['checks'] = {key: report.get(key, {}).get('status', 'not_run')
                        for key in ('spacing', 'internal_spacing', 'negative_space', 'symmetry')}
    # The editor sizes include the stroke; the exception contract measures the path.
    # Report both so restoring a visually round detail does not imply an exemption.
    result['circles'] = []
    if report.get('_svg'):
        allowed = contracts.load('negative-space.v1')['circle_hole_exception']['centerline_diameters']
        negative = report.get('negative_space', {})
        exempt_ids = {h['exception']['element_id'] for h in
                      negative.get('holes', []) + negative.get('authored_holes', []) if 'exception' in h}
        for circle in circle_candidates(report['_svg'], icon.draw()):
            diameter = circle['centerline_diameter']
            result['circles'].append({
                'element_id': circle['element_id'], 'path_diameter': diameter,
                'visible_diameter': diameter + icon.STROKE_WIDTH,
                'approved_path_diameters': allowed,
                'approved_visible_diameters': [d + icon.STROKE_WIDTH for d in allowed],
                'size_eligible': any(abs(diameter-d) <= 1e-9 for d in allowed),
                'exception_applied': circle['element_id'] in exempt_ids,
            })
    result.update(keyshape=graph['keyshape'], keyshape_bounds=graph['keyshape_bounds'],
                  checked_at=datetime.now(timezone.utc).isoformat(),
                  graph_sha256=hashlib.sha256(json.dumps(graph, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
                  scope='Build validation of the edited geometry; authored source is unchanged.')
    return result
