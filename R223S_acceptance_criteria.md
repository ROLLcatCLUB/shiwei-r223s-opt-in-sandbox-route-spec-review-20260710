# R223S acceptance criteria

## Pass requirements

R223S passes if it defines:

- independent opt-in sandbox route shape
- fixture-only data contract
- non-persistent preview state
- teacher_confirmed=false
- formal_apply_allowed=false
- no lesson body writeback
- teacher default draft preview policy
- review ledger summary policy
- v0.1 / v0.2 candidate comparison policy
- component trigger safety policy
- blocked scope and hold conditions

## Decision outputs

Only these decision outputs are allowed:

```text
PASS_CONTINUE_TO_R223T_FIXTURE_ONLY_SANDBOX_PREVIEW
HOLD_FOR_SANDBOX_SPEC_REDUCTION
HOLD_FORMAL_V0_2_NOT_READY
```

## Current decision

```text
PASS_CONTINUE_TO_R223T_FIXTURE_ONLY_SANDBOX_PREVIEW
```

## Explicit non-goals

R223S does not:

- implement preview page
- implement route
- modify R97B
- connect runtime/model/prompt/db
- publish v0.2
- write lesson body

