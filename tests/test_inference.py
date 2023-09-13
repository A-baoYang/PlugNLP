from test_data import example_data, new_data

from PlugNLP.inference import PlugNLP

plugnlp = PlugNLP(credential_file="/home/jovyan/study/openai/secret.cfg")


def test_inference_classify():
    results = plugnlp.classify(
        example_list=example_data["classify"],
        text_list=new_data["classify"],
    )
    assert len(results.split(",")) == len(new_data["classify"])


def test_inference_extract():
    results = plugnlp.extract(
        example_list=example_data["extract"],
        text_list=new_data["extract"],
    )
    assert results


def test_inference_qa():
    results = plugnlp.qa(
        example_list=example_data["qa"],
        text_list=new_data["qa"],
    )
    assert results


def test_inference_summarize():
    results = plugnlp.summarize(
        text_list=new_data["summarize"],
    )
    assert results


def test_inference_generate():
    results = plugnlp.generate(
        text_list=new_data["generate"],
    )
    assert results


test_inference_classify()
