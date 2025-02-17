# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LlmModel(str, enum.Enum):
    """
    An enumeration.
    """

    GPT_3_5_TURBO = "GPT_3_5_TURBO"
    GPT_3_5_TURBO_16_K_0613 = "GPT_3_5_TURBO_16K_0613"
    GPT_3_5_TURBO_0613 = "GPT_3_5_TURBO_0613"
    GPT_3_5_TURBO_1106 = "GPT_3_5_TURBO_1106"
    GPT_3_5_TURBO_0125 = "GPT_3_5_TURBO_0125"
    GPT_4 = "GPT_4"
    GPT_4_0613 = "GPT_4_0613"
    GPT_4_32_K = "GPT_4_32K"
    GPT_4_32_K_0613 = "GPT_4_32K_0613"
    GPT_4_1106_PREVIEW = "GPT_4_1106_PREVIEW"
    GPT_4_0125_PREVIEW = "GPT_4_0125_PREVIEW"
    GPT_4_TURBO = "GPT_4_TURBO"
    GPT_4_TURBO_PREVIEW = "GPT_4_TURBO_PREVIEW"
    GPT_4_TURBO_2024_04_09 = "GPT_4_TURBO_2024_04_09"
    GPT_4_0 = "GPT_4_0"
    MISTRAL_7_B_INSTRUCT_V_01 = "MISTRAL_7B_INSTRUCT_V01"
    MIXTRAL_8_X_7_B_INSTRUCT_V_01 = "MIXTRAL_8X7B_INSTRUCT_V01"

    def visit(
        self,
        gpt_3_5_turbo: typing.Callable[[], T_Result],
        gpt_3_5_turbo_16_k_0613: typing.Callable[[], T_Result],
        gpt_3_5_turbo_0613: typing.Callable[[], T_Result],
        gpt_3_5_turbo_1106: typing.Callable[[], T_Result],
        gpt_3_5_turbo_0125: typing.Callable[[], T_Result],
        gpt_4: typing.Callable[[], T_Result],
        gpt_4_0613: typing.Callable[[], T_Result],
        gpt_4_32_k: typing.Callable[[], T_Result],
        gpt_4_32_k_0613: typing.Callable[[], T_Result],
        gpt_4_1106_preview: typing.Callable[[], T_Result],
        gpt_4_0125_preview: typing.Callable[[], T_Result],
        gpt_4_turbo: typing.Callable[[], T_Result],
        gpt_4_turbo_preview: typing.Callable[[], T_Result],
        gpt_4_turbo_2024_04_09: typing.Callable[[], T_Result],
        gpt_4_0: typing.Callable[[], T_Result],
        mistral_7_b_instruct_v_01: typing.Callable[[], T_Result],
        mixtral_8_x_7_b_instruct_v_01: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LlmModel.GPT_3_5_TURBO:
            return gpt_3_5_turbo()
        if self is LlmModel.GPT_3_5_TURBO_16_K_0613:
            return gpt_3_5_turbo_16_k_0613()
        if self is LlmModel.GPT_3_5_TURBO_0613:
            return gpt_3_5_turbo_0613()
        if self is LlmModel.GPT_3_5_TURBO_1106:
            return gpt_3_5_turbo_1106()
        if self is LlmModel.GPT_3_5_TURBO_0125:
            return gpt_3_5_turbo_0125()
        if self is LlmModel.GPT_4:
            return gpt_4()
        if self is LlmModel.GPT_4_0613:
            return gpt_4_0613()
        if self is LlmModel.GPT_4_32_K:
            return gpt_4_32_k()
        if self is LlmModel.GPT_4_32_K_0613:
            return gpt_4_32_k_0613()
        if self is LlmModel.GPT_4_1106_PREVIEW:
            return gpt_4_1106_preview()
        if self is LlmModel.GPT_4_0125_PREVIEW:
            return gpt_4_0125_preview()
        if self is LlmModel.GPT_4_TURBO:
            return gpt_4_turbo()
        if self is LlmModel.GPT_4_TURBO_PREVIEW:
            return gpt_4_turbo_preview()
        if self is LlmModel.GPT_4_TURBO_2024_04_09:
            return gpt_4_turbo_2024_04_09()
        if self is LlmModel.GPT_4_0:
            return gpt_4_0()
        if self is LlmModel.MISTRAL_7_B_INSTRUCT_V_01:
            return mistral_7_b_instruct_v_01()
        if self is LlmModel.MIXTRAL_8_X_7_B_INSTRUCT_V_01:
            return mixtral_8_x_7_b_instruct_v_01()
