# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .agent_type import AgentType
from .llm_model import LlmModel

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PrismaModelsAgent(pydantic.BaseModel):
    """
    Represents a Agent record
    """

    id: str
    type: AgentType
    name: str
    avatar: typing.Optional[str] = None
    initial_message: typing.Optional[str] = pydantic.Field(alias="initialMessage", default=None)
    description: str
    is_active: bool = pydantic.Field(alias="isActive")
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")
    llms: typing.Optional[typing.List[PrismaModelsAgentLlm]] = None
    llm_model: typing.Optional[LlmModel] = pydantic.Field(alias="llmModel", default=None)
    prompt: typing.Optional[str] = None
    api_user_id: str = pydantic.Field(alias="apiUserId")
    api_user: typing.Optional[PrismaModelsApiUser] = pydantic.Field(alias="apiUser", default=None)
    datasources: typing.Optional[typing.List[PrismaModelsAgentDatasource]] = None
    tools: typing.Optional[typing.List[PrismaModelsAgentTool]] = None
    workflow_steps: typing.Optional[typing.List[PrismaModelsWorkflowStep]] = pydantic.Field(
        alias="workflowSteps", default=None
    )
    metadata: typing.Optional[typing.Any] = None
    output_schema: typing.Optional[str] = pydantic.Field(alias="outputSchema", default=None)

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}


from .prisma_models_agent_datasource import PrismaModelsAgentDatasource  # noqa: E402
from .prisma_models_agent_llm import PrismaModelsAgentLlm  # noqa: E402
from .prisma_models_agent_tool import PrismaModelsAgentTool  # noqa: E402
from .prisma_models_api_user import PrismaModelsApiUser  # noqa: E402
from .prisma_models_workflow_step import PrismaModelsWorkflowStep  # noqa: E402

PrismaModelsAgent.update_forward_refs()
