# ---------- Builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target /deps

COPY . .

# ---------- Runtime (distroless) ----------
FROM gcr.io/distroless/python3-debian12

WORKDIR /app

# Copy installed deps
COPY --from=builder /deps /deps
ENV PYTHONPATH=/deps

# Copy app code
COPY --from=builder /app /app

EXPOSE 8000

CMD ["-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]

