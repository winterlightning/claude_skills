"""Optional checks of the actual uploaded SVG, without inventing authored geometry."""
from datetime import datetime, timezone
import hashlib


def validate_upload(document, canvas, *, bypass=True):
    report = {
        'status': 'not-run', 'bypassed': bypass,
        'checks_run': ['static SVG', 'canvas', 'render'], 'errors': [],
        'warnings': ['Uploaded artwork requires human review.'],
        'scope': 'Uploaded SVG safety and rendering; optional rendered holes/pinches QA.',
        'checks_not_run': ['authored primitive grid/style', 'keyshape fit', 'vector spacing', 'geometry symmetry'],
        'svg_sha256': hashlib.sha256(document.encode('utf-8')).hexdigest(),
        'checked_at': datetime.now(timezone.utc).isoformat(),
    }
    if bypass:
        return report
    report['checks_run'].append('holes/pinches')
    try:
        from icon_set.validation.library_qa import measure_negative_space
        findings = measure_negative_space(document, canvas)
    except Exception:
        report.update(status='error', errors=['SVG validation could not complete. Check the rendering dependencies and retry.'])
        return report
    report['negative_space'] = findings
    report['status'] = findings['status']
    if report['status'] != 'pass':
        report['errors'].append(
            f"holes/pinches: {findings['failed_hole_count']} undersized holes; {findings['pinch_count']} pinches")
    return report
