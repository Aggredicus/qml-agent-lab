# Pull Request Template

## Contribution Type
- [ ] Experiment
- [ ] Benchmark Result
- [ ] Improvement
- [ ] Claim Review

## Contribution Packet
Link or include your `agent_contributions` packet:

```
(paste JSON or file path here)
```

## Checklist

- [ ] Classical baseline included
- [ ] Results follow schema
- [ ] Claim status is accurate
- [ ] Limitations documented
- [ ] No unsupported quantum advantage claims
- [ ] Small, focused change

## Summary

Describe what this PR does and why it matters.

## Validation

Commands run:

```bash
python benchmarks/runner.py
python mcp/server.py get_results
```

## Notes

Any risks, limitations, or follow-up work.
