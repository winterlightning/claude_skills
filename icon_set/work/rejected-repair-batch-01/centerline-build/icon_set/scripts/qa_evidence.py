"""Validation evidence for the gallery inspector.

Two sources, both tied to the exact SVG the gallery serves:

* library: the release gate's saved ``dist/qa/<family>/<icon>/metrics.json``
  (spacing, internal spacing, negative space), with a flag saying whether it
  was measured on the SVG currently published.
* qa_overlays: ``claude_skills/qa_overlays.py`` run on demand on that SVG, for
  its distance debug PNG and hole debug PNG.

Generated files are cached by SVG hash plus script hash outside the served
dist folder, so a new SVG or an edited checker never shows stale evidence.
"""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import threading
from urllib.parse import quote

QA_OVERLAYS = Path(__file__).resolve().parents[2] / 'qa_overlays.py'
KINDS = {'distance': '_distance_debug.png', 'holes': '_hole_debug.png'}
# matplotlib's pyplot state is process-global; render one icon at a time.
_LOCK = threading.Lock()
_MODULE = None


def _hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _qa_overlays():
    global _MODULE
    if _MODULE is None:
        spec = importlib.util.spec_from_file_location('qa_overlays_evidence', QA_OVERLAYS)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _MODULE = module
    return _MODULE


def icon_lookup(root: Path) -> dict:
    data = json.loads((root / 'gallery/icons.json').read_text(encoding='utf-8'))
    return {item['key']: item for item in data['icons'] + data.get('failed_icons', [])}


def svg_path(root: Path, icon: dict) -> Path:
    path = (root / 'gallery' / icon['preview_url']).resolve()
    if not path.is_relative_to(root) or path.suffix.lower() != '.svg' or not path.is_file():
        raise ValueError('Icon SVG is not available.')
    return path


def library_evidence(root: Path, icon: dict, current_sha: str) -> dict | None:
    folder = root / 'qa' / icon['family'] / icon['icon_id']
    metrics_path = folder / 'metrics.json'
    if not metrics_path.is_file():
        return None
    metrics = json.loads(metrics_path.read_text(encoding='utf-8'))
    spacing = metrics.get('spacing') or {}
    internal = metrics.get('internal_spacing') or {}
    negative = metrics.get('negative_space') or {}
    artifacts = {}
    for name in ('spacing.png', 'holes.png', 'spacing.svg'):
        if (folder / name).is_file():
            artifacts[name] = '../qa/' + icon['family'] + '/' + icon['icon_id'] + '/' + name
    return {
        'status': metrics.get('status'),
        'profile': metrics.get('profile'),
        'errors': metrics.get('errors', []),
        'warnings': metrics.get('warnings', []),
        'checks_run': metrics.get('checks_run', []),
        'needs_review': metrics.get('needs_review'),
        'svg_sha256': metrics.get('svg_sha256'),
        'svg_matches_published': metrics.get('svg_sha256') == current_sha,
        'rules_sha256': metrics.get('rules_sha256'),
        'spacing': {key: spacing.get(key) for key in (
            'status', 'minimumCenterlineDistance', 'requiredCenterline', 'minimumInkClearance',
            'requiredInkClearance', 'reason', 'canvas')},
        'spacing_pairs': len(spacing.get('pairs') or []),
        'internal_spacing': {key: internal.get(key) for key in ('status', 'reason') if key in internal},
        'negative_space': {key: negative.get(key) for key in (
            'status', 'hole_count', 'failed_hole_count', 'pinch_count', 'exception_count',
            'raster_artifact_count', 'minimum_measured_diameter', 'minimum_authored_diameter',
            'measuring_stroke_width')},
        'metrics_url': '../qa/' + icon['family'] + '/' + icon['icon_id'] + '/metrics.json',
        'artifacts': artifacts,
    }


class EvidenceStore:
    def __init__(self, dist: Path, cache: Path):
        self.root = Path(dist).resolve()
        self.cache = Path(cache).resolve()

    def _run(self, icon: dict, svg_bytes: bytes, gate):
        if __package__:
            from .qa_fingerprint import checker_fingerprint
        else:
            from qa_fingerprint import checker_fingerprint
        script_sha = checker_fingerprint()
        folder = self.cache / _hash(svg_bytes + script_sha.encode() + repr(gate).encode())[:40]
        result_file = folder / 'evidence.json'
        if result_file.is_file():
            return json.loads(result_file.read_text(encoding='utf-8')), folder, True
        with _LOCK:
            if result_file.is_file():
                return json.loads(result_file.read_text(encoding='utf-8')), folder, True
            folder.mkdir(parents=True, exist_ok=True)
            # Measure a copy named after the icon so titles and file names match.
            copy = folder / (icon['icon_id'] + '.svg')
            copy.write_bytes(svg_bytes)
            log = io.StringIO()
            with contextlib.redirect_stdout(log):
                metrics = _qa_overlays().process(str(copy), out_dir=str(folder), gate=gate, quiet=True)
            copy.unlink()
            evidence = {'metrics': metrics, 'log': log.getvalue().strip(),
                        'script': QA_OVERLAYS.name, 'script_sha256': script_sha}
            result_file.write_text(json.dumps(evidence, indent=2), encoding='utf-8')
        return evidence, folder, False

    def _resolve(self, key: str):
        icon = icon_lookup(self.root).get(key)
        if icon is None:
            raise KeyError(key)
        svg_bytes = svg_path(self.root, icon).read_bytes()
        current_sha = _hash(svg_bytes)
        library = library_evidence(self.root, icon, current_sha)
        # Gate distance at the icon's own profile rule when the build recorded it.
        gate = (library or {}).get('spacing', {}).get('requiredCenterline')
        return icon, svg_bytes, current_sha, library, gate

    def evidence(self, key: str) -> dict:
        icon, svg_bytes, current_sha, library, gate = self._resolve(key)
        evidence, folder, cached = self._run(icon, svg_bytes, gate)
        metrics = evidence['metrics']
        images = {kind: f'/api/qa-evidence/image?icon={quote(key, safe="")}&kind={kind}'
                  for kind, suffix in KINDS.items() if (folder / (icon['icon_id'] + suffix)).is_file()}
        return {
            'icon': key,
            'svg_url': icon['preview_url'],
            'svg_sha256': current_sha,
            'catalog_sha_matches': icon.get('svg_sha256') in (None, current_sha),
            'library': library,
            'qa_overlays': {
                'script': evidence['script'],
                'script_sha256': evidence['script_sha256'],
                'cached': cached,
                'log': evidence['log'],
                'distance': {key: metrics.get(key) for key in (
                    'distance_passed', 'distance_measured', 'lowest_distance', 'distance_gate',
                    'min_gap_kind', 'canvas', 'path_count')},
                'holes': {key: metrics.get(key) for key in (
                    'negative_space_status', 'negative_space_passed', 'hole_count', 'failed_hole_count',
                    'pinch_count', 'hole_exception_count', 'raster_artifact_count',
                    'minimum_measured_radius', 'minimum_authored_radius', 'holes', 'pinches')},
                'images': images,
            },
        }

    def image(self, key: str, kind: str) -> bytes:
        if kind not in KINDS:
            raise ValueError('Unknown evidence image.')
        icon, svg_bytes, _, _, gate = self._resolve(key)
        _, folder, _ = self._run(icon, svg_bytes, gate)
        path = folder / (icon['icon_id'] + KINDS[kind])
        if not path.is_file():
            raise FileNotFoundError(kind)
        return path.read_bytes()
