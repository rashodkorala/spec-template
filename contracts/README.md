# Contracts

The boundaries between parts.
Each side of a boundary must match these exactly.
A contract change lists every repo it affects and isn't done until all of them are updated.

| Folder | Boundary | Sides | Source of truth while draft | Seed from |
|---|---|---|---|---|
| `api/` | App ↔ backend HTTP API | iOS, Android, Backend | backend source | backend controllers + DTOs |
| `auth/` | App ↔ identity provider | iOS, Android, Backend | provider config + backend guards | |
| `sync/` | Offline data sync rules | iOS, Android, Backend | backend source | |

Each folder holds:

- `README.md`: a `Status:` line (`empty`, `proposed`, `draft` or `verified`), what the citation prefixes mean, and the file index (which `§` is in which file).
- One file per section, keeping its `§` number: overview, flows or sequences, exact tables (endpoints, request / response shapes, error codes, timings), `rules.md`, `mismatches.md`, `open-questions.md`. Read the index, then only the files you need.
- `changelog.md`: dated contract changes, with the commits on each side.

A new section gets its own file and a row in that README's index.
