import pytest
from resources.models import Resource

# Create your tests here.
@pytest.mark.django_db
def test_resource_creation():
    resource = Resource.objects.create(
        type="VIDEO",
        title="Test",
        summary="Test summary"
    )
    assert resource.title == "Test"