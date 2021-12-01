
import os, re, gc
from time import perf_counter_ns

BENCHMARK_GLOBALS = { "print": lambda *args, **kwargs: None }
FILENAME_RE = re.compile(r"(\d+)\_(\d+)\.py")

def benchmark(filename):
    with open(filename) as file:
        source = file.read()
    
    code = compile(source, filename, "exec")

    measurements = []
    for _ in range(10):
        st = perf_counter_ns()
        exec(code, BENCHMARK_GLOBALS)
        et = perf_counter_ns()

        measurements.append(et-st)
        gc.collect()

    return measurements

results = {}
for path in os.listdir("."):
    if not (match := FILENAME_RE.match(path)):
        continue

    day, part = map(int, match.groups())
    
    measurements = benchmark(path)
    results[(day, part)] = measurements

    print(f"Puzzle {day:2}.{part} {min(measurements)//10**3:>16,} µs")
