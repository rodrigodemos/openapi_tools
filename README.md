# OpenAPI Tools

This repository contains OpenAPI specifications and scripts for tools that can be imported into Azure AI Agents.

## Notes on ADO Tools

- ADO Specs where obtained from this repo: https://github.com/MicrosoftDocs/vsts-rest-api-specs/tree/master/specification
- Specs were upgraded to OpenAPI 3.0 using [Swagger Editor](https://editor-next.swagger.io/)
- OpenAPI Tools in Azure AI Agent Service have some prerequisites (i.e. no spaces in operationId), [more details here](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview)
- The [ado_openapi_aiagents_prep.py](./ADO/v7.2/scripts/ado_openapi_aiagents_prep.py) python script will prepare the file for Azure AI Agent Service
- Specs ready to be imported into Azure AI Agents are in the [ready_to_use](./ADO/v7.2/ready_to_use) folder

