import pytest
from farm_ng.oak.client import OakCameraClient, OakCameraClientConfig, OakCameraServiceState, oak_pb2


@pytest.fixture
def config() -> OakCameraClientConfig:
    return OakCameraClientConfig(port=50051)


class TestOakClient:
    def test_smoke_config(self, config: OakCameraClientConfig) -> None:
        assert config.port == 50051
        assert config.address == "localhost"
        assert config.update_state_frequency == 2

    def test_smoke(self, config: OakCameraClientConfig) -> None:
        client = OakCameraClient(config)
        assert client is not None
        assert client.server_address == "localhost:50051"

    @pytest.mark.asyncio
    async def test_state(self, config: OakCameraClientConfig) -> None:
        client = OakCameraClient(config)
        state: OakCameraServiceState = await client.get_state()
        assert state.value == oak_pb2.OakServiceState.UNAVAILABLE