import subprocess
import re
import matplotlib.pyplot as plt

input_files = [f"data/Input{i}.txt" for i in range(1, 11)]

sizes = []
times = []

for f in input_files:
    with open(f) as fh:
        content = fh.read().splitlines()
    A = content[-2]
    B = content[-1]
    nm = len(A) * len(B)

    out = subprocess.check_output(
        ["py", "src/Programming_assignment_3_algs.py"],
        stdin=open(f),
        text=True
    )
    runtime_line = out.strip().split("\n")[-1]
    t = float(re.search(r"[\d.]+", runtime_line).group())

    sizes.append(nm)
    times.append(t * 1000) 
    print(f"{f}: n*m={nm}, runtime={t:.6f}s")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(sizes, times, marker="o", color="steelblue", linewidth=2, markersize=7)

for i, (x, y) in enumerate(zip(sizes, times)):
    ax.annotate(f"input{str(i+1).zfill(2)}", (x, y),
                textcoords="offset points", xytext=(0, 8),
                ha="center", fontsize=8)

ax.set_xlabel("Input Size (n × m)", fontsize=12)
ax.set_ylabel("Runtime (ms)", fontsize=12)
ax.set_title("HVLCS DP Runtime vs Input Size", fontsize=14)
ax.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("runtime_graph.png", dpi=150)
print("Graph saved to runtime_graph.png")