task_config = {
    "task_role": {
        "classify": "classifier",
        "extract": "extractor",
        "qa": "assistant",
        "summarize": "assistant",
        "generate": "writer",
    },
    "action_msg": {
        "classify": "please inference the label of the new data",
        "extract": "please extract related entities from the new data",
        "qa": "please answer the questions in new data section",
        "summarize": "please summarize the text in new data section",
        "generate": "please generate specific type of content from the new data section",  # noqa: E501
    },
    "result_type": {
        "classify": "label",
        "extract": "entity",
        "qa": "answer",
        "summarize": "summarization",
        "generate": "generated content",
    },
}
