"""Fit separated region shapes to an object box with explicit edge-gap constraints.

One shared x/y shape scale preserves corresponding edge directions. Each region
gets its own translation. Source boundary alignment and centered placement are
retained. Never silently return a result when spacing and bounds conflict.
Distances are in SVG user units (pixels at the collection's native 48px size).
"""
from itertools import combinations
import numpy as np
from scipy.linalg import qr
from scipy.optimize import minimize
from shapely.affinity import affine_transform
from shapely.ops import nearest_points


def measure_pairs(regions, pairs, ids=None):
    ids = ids or [str(i) for i in range(len(regions))]
    result = []
    for i, j, requested in pairs:
        a, b = nearest_points(regions[i], regions[j])
        result.append(dict(regions=[ids[i], ids[j]], required_gap=requested,
                           measured_gap=regions[i].distance(regions[j]),
                           nearest_points=[list(a.coords[0]), list(b.coords[0])]))
    return result


def fit_regions_with_gaps(regions, target_bounds, pairs, *, ids=None,
                          reference_regions=None, tolerance=.001,
                          minimum_clearance=4, alignment_tolerance=.01):
    """Return fitted polygons and measurements, or raise if constraints fail.

`pairs` contains (region_index, region_index, target_edge_gap). Only declared
neighbors must reach the requested gap; distant pairs are not pulled together.
`reference_regions` supplies Normal's layout anchors for every style.
"""
    if not regions or any(p.is_empty or not p.is_valid or p.geom_type != 'Polygon' for p in regions):
        raise ValueError('Expected nonempty valid Polygon regions')
    n = len(regions)
    reference_regions = reference_regions or regions
    if len(reference_regions) != n:
        raise ValueError('Reference region count differs')
    if tolerance <= 0 or minimum_clearance < 0:
        raise ValueError('Invalid spacing tolerance or minimum clearance')
    if any(i == j or not 0 <= i < n or not 0 <= j < n or gap <= 0 for i, j, gap in pairs):
        raise ValueError('Invalid neighboring-region constraint')
    target = np.asarray(target_bounds, dtype=float)
    if target.shape != (4,) or not np.isfinite(target).all():
        raise ValueError('Invalid target bounds')
    extent = target[2:] - target[:2]
    if min(extent) <= 0:
        raise ValueError('Invalid target bounds')
    bounds = np.asarray([p.bounds for p in regions])
    ref = np.asarray([p.bounds for p in reference_regions])
    sizes = bounds[:, 2:] - bounds[:, :2]
    if min(sizes.flatten()) <= 0:
        raise ValueError('Degenerate input region')
    low, high = bounds[:, :2].min(axis=0), bounds[:, 2:].max(axis=0)
    ref_low, ref_high = ref[:, :2].min(axis=0), ref[:, 2:].max(axis=0)
    centers = (bounds[:, :2] + bounds[:, 2:]) / 2
    base_scale = extent / (high - low)
    x0 = np.r_[base_scale, np.tile(target[:2] - base_scale * low, n)]
    initial_centers = centers * base_scale + x0[2:].reshape(-1, 2)
    length = max(extent)
    equations, values, anchors = [], [], []

    def pin(i, axis, coordinate, target_coordinate, label):
        row = np.zeros(2 + 2*n)
        row[axis], row[2+2*i+axis] = coordinate, 1
        equations.append(row)
        values.append(target_coordinate)
        anchors.append(dict(region=i, axis=axis, alignment=label))

    for i in range(n):
        for axis in range(2):
            for edge, goal, label in ((axis, target[axis], 'minimum'),
                                      (axis+2, target[axis+2], 'maximum')):
                reference_extreme = ref_low[axis] if edge < 2 else ref_high[axis]
                if abs(ref[i, edge] - reference_extreme) <= alignment_tolerance:
                    pin(i, axis, bounds[i, edge], goal, label)
            ref_center = (ref[i, axis] + ref[i, axis+2]) / 2
            if abs(ref_center - (ref_low[axis]+ref_high[axis])/2) <= alignment_tolerance:
                pin(i, axis, centers[i, axis], (target[axis]+target[axis+2])/2, 'center')
    full_a, full_b = np.asarray(equations), np.asarray(values)
    # Remove redundant linear equations, e.g. a centered region pinned at both edges.
    _, _, pivot = qr(full_a.T, pivoting=True)
    rank = np.linalg.matrix_rank(full_a)
    a, b = full_a[pivot[:rank]], full_b[pivot[:rank]]
    solution = np.linalg.lstsq(a, b, rcond=None)[0]
    if max(abs(full_a @ solution - full_b)) > tolerance:
        raise ValueError('Source alignment constraints conflict with target bounds')

    cache_key, cache_geometry = None, None
    def geometry(x):
        nonlocal cache_key, cache_geometry
        key = tuple(x)
        if key != cache_key:
            cache_geometry = [affine_transform(p, [x[0], 0, 0, x[1], x[2+2*i], x[3+2*i]])
                              for i, p in enumerate(regions)]
            cache_key = key
        return cache_geometry

    def transformed_bounds(x):
        return bounds * np.tile(x[:2], 2) + np.tile(x[2:].reshape(-1, 2), (1, 2))

    def inequalities(x):
        shapes = geometry(x)
        bb = transformed_bounds(x)
        required = [shapes[i].distance(shapes[j]) - gap for i, j, gap in pairs]
        # A tight solver band leaves room for final six-decimal SVG serialization.
        values = [*required, *[tolerance/2-d for d in required]]
        covered = {tuple(sorted((i, j))) for i, j, gap in pairs if gap >= minimum_clearance}
        values += [shapes[i].distance(shapes[j])-minimum_clearance for i, j in combinations(range(n), 2)
                   if (i, j) not in covered]
        values += list((bb[:, :2]-target[:2]+1e-6).flatten())
        values += list((target[2:]-bb[:, 2:]+1e-6).flatten())
        return np.asarray(values) / length

    def objective(x):
        positions = centers*x[:2] + x[2:].reshape(-1, 2)
        return np.sum(((positions-initial_centers)/length)**2) + np.sum(np.log(x[:2]/base_scale)**2)

    limits = [(1e-5, extent[axis]/max(sizes[:, axis])) for axis in range(2)] + [(None, None)]*(2*n)
    result = minimize(objective, x0, method='SLSQP', bounds=limits,
                      constraints=[dict(type='eq', fun=lambda x: (a@x-b)/length, jac=lambda x: a/length),
                                   dict(type='ineq', fun=inequalities)],
                      options=dict(ftol=1e-12, maxiter=300))
    fitted = geometry(result.x)
    bb = transformed_bounds(result.x)
    output_bounds = np.r_[bb[:, :2].min(axis=0), bb[:, 2:].max(axis=0)]
    measured = measure_pairs(fitted, pairs, ids)
    errors = [abs(m['measured_gap']-m['required_gap']) for m in measured]
    if (not result.success or max(abs(output_bounds-target)) > 1e-5
            or max(errors, default=0) > tolerance
            or min(inequalities(result.x), default=0) * length < -1e-5):
        raise ValueError('Cannot satisfy object bounds, layout and gaps: ' + result.message)
    return fitted, dict(method='constrained region scaling and translation',
                        shape_scale=result.x[:2].tolist(),
                        region_translations=result.x[2:].reshape(-1, 2).tolist(),
                        normal_layout_anchors=anchors,
                        normal_reference_bounds=target.tolist(), output_bounds=output_bounds.tolist(),
                        tolerance=tolerance, minimum_clearance=minimum_clearance,
                        pairs=measured, solver_converged=True, bounds_check='passed', spacing_check='passed')
