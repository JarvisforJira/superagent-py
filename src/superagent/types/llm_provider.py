# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LlmProvider(str, enum.Enum):
    """
    An enumeration.
    """

    OPENAI = "OPENAI"
    AZURE_OPENAI = "AZURE_OPENAI"
    HUGGINGFACE = "HUGGINGFACE"
    PERPLEXITY = "PERPLEXITY"
    TOGETHER_AI = "TOGETHER_AI"
    ANTHROPIC = "ANTHROPIC"
    BEDROCK = "BEDROCK"

    def visit(
        self,
        openai: typing.Callable[[], T_Result],
        azure_openai: typing.Callable[[], T_Result],
        huggingface: typing.Callable[[], T_Result],
        perplexity: typing.Callable[[], T_Result],
        together_ai: typing.Callable[[], T_Result],
        anthropic: typing.Callable[[], T_Result],
        bedrock: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LlmProvider.OPENAI:
            return openai()
        if self is LlmProvider.AZURE_OPENAI:
            return azure_openai()
        if self is LlmProvider.HUGGINGFACE:
            return huggingface()
        if self is LlmProvider.PERPLEXITY:
            return perplexity()
        if self is LlmProvider.TOGETHER_AI:
            return together_ai()
        if self is LlmProvider.ANTHROPIC:
            return anthropic()
        if self is LlmProvider.BEDROCK:
            return bedrock()
