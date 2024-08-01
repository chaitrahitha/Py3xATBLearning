import pytest

@pytest.fixture()
def sample_data():
    data = [1,2,3,4,5] # type - list
    return data


@pytest.fixture()
def sample_data2():
    return True



def test_consume_sample_1_2(sample_data,sample_data2):
    print(sample_data)
    print(sample_data2)