from calc import add


def test_add_basic():
    assert add(1, 2) == 3


def test_add_regression():
    # 回归测试：之前曾因类型错误失败
    assert add(0, 0) == 0
