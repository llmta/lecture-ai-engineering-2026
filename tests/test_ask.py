from types import SimpleNamespace

from app import ask as ask_module


def test_ask_displays_input_and_output_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(
        text="回答",
        usage_metadata=SimpleNamespace(
            prompt_token_count=12,
            candidates_token_count=34,
        ),
    )

    class FakeModels:
        def generate_content(self, *, model, contents):
            assert model == "test-model"
            assert contents == "質問"
            return response

    class FakeClient:
        def __init__(self, *, api_key):
            assert api_key == "test-api-key"
            self.models = FakeModels()

    monkeypatch.setattr(ask_module.genai, "Client", FakeClient)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-api-key")
    monkeypatch.setattr(ask_module, "MODEL", "test-model")

    assert ask_module.ask("質問") == "回答"

    assert capsys.readouterr().out == "[トークン数] 入力: 12, 出力: 34\n"


def test_ask_displays_unknown_when_usage_metadata_is_missing(monkeypatch, capsys):
    response = SimpleNamespace(text="回答", usage_metadata=None)

    class FakeModels:
        def generate_content(self, *, model, contents):
            assert model == "test-model"
            assert contents == "質問"
            return response

    class FakeClient:
        def __init__(self, *, api_key):
            assert api_key == "test-api-key"
            self.models = FakeModels()

    monkeypatch.setattr(ask_module.genai, "Client", FakeClient)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-api-key")
    monkeypatch.setattr(ask_module, "MODEL", "test-model")

    assert ask_module.ask("質問") == "回答"

    assert capsys.readouterr().out == "[トークン数] 入力: 不明, 出力: 不明\n"
