# R223S blocked scope and hold conditions

## Blocked scope

R223S does not allow:

- R97B route modification
- formal route addition
- frontend/backend implementation
- runtime/provider/model connection
- prompt modification
- database persistence
- lesson body writeback
- R223M standard v0.2 publication
- R222D component library modification
- existing R223M/N/O draft mutation
- classroom component execution
- formal apply

## Hold conditions for R223T

R223T must hold if:

1. The preview needs R97B changes.
2. The preview needs backend route changes.
3. The preview calls runtime/model/prompt/db.
4. Teacher default draft shows backend field names.
5. Component triggers look executable.
6. v0.2 candidate is described as published.
7. Review ledger becomes the main reading surface.
8. Lesson body writeback appears.
9. v0.1 / v0.2 comparison is missing.
10. Sandbox state is persistent or hard to delete.

## Rollback expectation

Because R223T should be fixture-only, rollback should be file deletion only. No app-code rollback should be needed.

