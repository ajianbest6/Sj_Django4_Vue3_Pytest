from pathlib import Path

import pytest

from pytest_result_sender import plugin

pytest_plugins = "pytester"  # 测试开发


@pytest.fixture(autouse=True)
def mock():
    """测试前初始化"""
    bak_data = plugin.data
    plugin.data = {
        "passed": 0,
        "failed": 0,
    }
    yield

    # 恢复测试环境
    plugin.data = bak_data


@pytest.mark.parametrize("send_when", ["every", "on_fail"])
def test_send_when(send_when, pytester: pytest.Pytester, tmp_path: Path):
    """动态临时配置文件"""
    config_path = tmp_path.joinpath("pytest.ini")  # 放置配置文件
    config_path.write_text(
        f"""
[pytest]
send_when = {send_when}
send_api = https://baidu.com
"""
    )

    # 判断加载成功
    config = pytester.parseconfig(config_path)  # 放置配置文件
    assert config.getini("send_when") == send_when

    pytester.makepyfile(
        """
        def test_pass():
            ...
        """
    )  # 创建临时 python 测试文件
    pytester.runpytest("-c", str(config_path))
    print(plugin.data)

    if plugin.data["send_when"] == "every":
        assert plugin.data["send_done"] == 1
    else:
        assert plugin.data.get("send_done") is None


@pytest.mark.parametrize("send_api", ["https://baidu.com", ""])
def test_send_api(send_api, pytester: pytest.Pytester, tmp_path: Path):
    config_path = tmp_path.joinpath("pytest.ini")  # 放置配置文件
    config_path.write_text(
        f"""
[pytest]
send_when = every
send_api = {send_api}
    """
    )

    # 判断加载成功
    config = pytester.parseconfig(config_path)  # 放置配置文件
    assert config.getini("send_api") == send_api

    pytester.makepyfile(
        """
        def test_pass():
            ...
        """
    )  # 创建临时 python 测试文件
    pytester.runpytest("-c", str(config_path))
    print(plugin.data)

    if plugin.data["send_api"]:
        assert plugin.data["send_done"] == 1
    else:
        assert plugin.data.get("send_done") is None
