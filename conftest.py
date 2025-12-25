import os
import pytest
from dotenv import load_dotenv

from infra.environment_conditions import EnvironmentConditions
from infra.mobile_session import MobileSession
from infra.streaming_validator import StreamingValidator

load_dotenv()


@pytest.fixture(scope="function")
def credentials():
    return {
        "email": os.getenv("NANIT_USERNAME"),
        "password": os.getenv("NANIT_PASSWORD"),
    }


@pytest.fixture(scope="function")
def streaming_validator():
    validator = StreamingValidator("http://localhost:8082")
    # setup
    validator.set_network_condition(EnvironmentConditions.NORMAL)
    yield validator
    # teardown
    validator.set_network_condition(EnvironmentConditions.NORMAL)

@pytest.fixture(scope="function")
def mobile_session(request):
    platform = request.param
    session = MobileSession(platform=platform)
    session.launch_app()
    return session
