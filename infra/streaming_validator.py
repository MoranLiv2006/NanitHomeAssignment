import requests

from infra.environment_conditions import EnvironmentConditions


class StreamingValidator:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_metrics(self):
        response = requests.get(f"{self.base_url}/metrics")
        response.raise_for_status()
        return response.json()

    def get_health(self):
        response = requests.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()

    def set_network_condition(self, desired_condition: EnvironmentConditions) -> None:
        response = requests.put(f"{self.base_url}/control/network/{desired_condition.value}")
        response.raise_for_status()

    def validate_streaming_performance_parameters(self):
        health = self.get_health()
        metrics = self.get_metrics()

        assert health["status"] == "streaming"
        assert health["network_condition"] == metrics["network"]["current_condition"]
        assert health["bitrate"] == metrics["streaming"]["bitrate"]

    def fetch_streaming_status(self):
        health = self.get_health()
        return health["status"]

    def get_network_latency(self):
        metrics = self.get_metrics()
        return metrics["network"]["settings"]["latency_ms"]
