# Core Scripts Overview

The detailed command and module contracts now live in
[scripts.md](scripts.md). That inventory is the authoritative place to find:

- inputs, outputs, side effects, and exit behavior;
- `normal`, `sub`, and `container` support per tool;
- shared modules and the machine-readable profile registry;
- regression and repository checks; and
- top-level rework and upload orchestration.

Use [icon-pipeline.md](icon-pipeline.md) to decide when each command runs. The
pipeline has five tooling lanes:

| Lane | Purpose | Start in the inventory |
| --- | --- | --- |
| Intake | Inspect a local pack, stage a rework payload, or analyze supplied SVG evidence | [Pipeline commands](scripts.md#pipeline-commands) |
| Build | Retrieve relevant references and emit editable geometry as a design/ship pair | [Pipeline commands](scripts.md#pipeline-commands) |
| Verify | Run structural, grid, overlap, keyshape, hole, pinch, and true-size checks | [Pipeline commands](scripts.md#pipeline-commands) |
| Maintain | Regenerate numeric profile mirrors or inspect a scoped legacy migration | [Registry, compatibility, and migration commands](scripts.md#registry-compatibility-and-migration-commands) |
| Protect | Run unit tests plus documentation/inventory consistency checks | [Regression and repository checks](scripts.md#regression-and-repository-checks) |

Keep type-specific policies in each type's `rules.md` and numeric values in the
profile source and generated pages linked from [icon-types.md](icon-types.md).
[Shared rules](icon-rules.md) and [editable geometry](atomic-shapes.md) own common
geometry requirements. The script pages describe command contracts.
