from helpers.validator import SchemaValidator
import sys
import pytest

sys.path.insert(0, '/Users/agriciunas/Desktop/Repos/data-infrastructure-sample/stream/integration/collector/src/helpers')


@pytest.mark.parametrize("pass_validation", [
    {
        'source': 'any string',
        'artifact': 'any string',
        'v_schema': 'any string',
        'data': {}
    },
    {
        'source': 'any string',
        'artifact': 'any string',
        'v_schema': 'any string',
        'data': {'any string': 'any string'}
    }
])
def test_validator_pass(pass_validation):

    assert SchemaValidator(pass_validation).validation_output.get('status')


@pytest.mark.parametrize("fail_validation", [
    {
        'artifact': 'any string',
        'v_schema': 'any string',
        'data': {}
    },
    {
        'source': 'any string',
        'v_schema': 'any string',
        'data': {}
    },
    {
        'source': 'any string',
        'artifact': 'any string',
        'data': {}
    },
    {
        'source': 'any string',
        'artifact': 'any string',
        'v_schema': 'any string'
    },
    {
        'source': 'any string',
        'artifact': 'any string',
        'v_schema': 'any string',
        'data': []
    },
    {
        'source': 1,
        'artifact': 'any string',
        'v_schema': 'any string',
        'data': {}
    },
    {
        'source': 'any string',
        'artifact': 'any string',
        'v_schema': 'any string',
        'data': {},
        'some additional key': 'any string'
    }
])
def test_validator_fail(fail_validation):

    assert not SchemaValidator(fail_validation).validation_output.get('status')
