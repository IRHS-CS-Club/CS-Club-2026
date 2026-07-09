FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# Curriculum code is pure standard library (heapq, math, time, functools) —
# no requirements.txt needed. Kept as a separate layer so future dependencies
# don't require touching devcontainer.json.
RUN python3 -m pip install --no-cache-dir --upgrade pip
