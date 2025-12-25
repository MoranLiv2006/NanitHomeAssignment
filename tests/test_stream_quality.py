import pytest

from infra.environment_conditions import EnvironmentConditions


class TestEnvironmentConditions:

    @pytest.mark.api
    def test_stream_quality_degrades_under_poor_network(self, streaming_validator):
        streaming_validator.validate_streaming_performance_parameters()
        normal_latency = streaming_validator.get_network_latency()

        streaming_validator.set_network_condition(EnvironmentConditions.POOR)
        streaming_validator.validate_streaming_performance_parameters()
        poor_latency = streaming_validator.get_network_latency()

        assert poor_latency > normal_latency, f"Expected latency to increase under poor network. Normal: {normal_latency}, Poor: {poor_latency}"
