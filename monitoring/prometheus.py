from prometheus_client import Counter

INFERENCE_COUNT = Counter(
    "inference_requests_total",
    "Total inference requests"
)
