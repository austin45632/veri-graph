## Summary

- What changed
- Why it changed

## Axes Impacted

- [ ] Verification axis (`REQ -> TR -> TI -> TC -> TS`)
- [ ] Automotive semantics axis (`FEAT / VSTATE / SIG / FAULT / DIAG / VAR / SG`)
- [ ] Result layer (`BUILD / RUN / RES / EVID`)
- [ ] Governance / ADR / workflow only

## Traceability Impact

- Changed IDs:
- Changed relations:
- Matrix files updated:

## Verification

```powershell
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts\check_all.py
```

## Review Checklist

- [ ] CI `verify` passes
- [ ] Required matrices were updated if semantics changed
- [ ] ADR / decision log updated if model or process changed
- [ ] Comments are resolved before merge
