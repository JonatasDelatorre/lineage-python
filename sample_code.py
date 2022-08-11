from openlineage.client.client import OpenLineageClient
from openlineage.client.run import RunEvent, RunState, Run, Job

client = OpenLineageClient(url="http://localhost:3000")

namespace = 'Pipeline_1' # Nome do Pipeline que vai ser executado
process = 'Lambda_1' # Nome do processamento que está sendo realizado
source = 's3-raw' # Nome da origem onde está o dado
destination = 's3-processed-tb-1' # Nome do destino para onde o dado vai
process_id = 'd46e465b-d358-4d32-83d4-df660ff222bb' # uuid para identificar o processo

client.emit(
    RunEvent(
        eventType=RunState.START,
        eventTime="2021-01-03T20:00:00.001+10:00",
        run=Run(process_id),
        job=Job(namespace, process),
        producer="meu_repo_v1.0.2",
        inputs=[{
          "namespace": namespace,
          "name": source
        }],
    )
)

client.emit(
    RunEvent(
        eventType=RunState.COMPLETE,
        eventTime="2021-01-04T21:00:00.001+10:00",
        run=Run(process_id),
        job=Job(namespace, process),
        producer="meu_repo_v1.0.2",
        inputs=[{
          "namespace": namespace,
          "name": source
        }],
        outputs=[{
          "namespace": namespace,
          "name": destination,
          "facets": {
            "schema": {
              "_producer": "meu_repositorio_1",
              "_schemaURL": "minha_doc_do_schema",
              "fields": [
                { "name": "nome", "type": "VARCHAR"},
                { "name": "idade", "type": "INT"},
                { "name": "sobrenome", "type": "VARCHAR"},
                { "name": "CPF", "type": "VARCHAR"}
              ]
            },
            "lambda_version": process_id
          }
        }],
    )
)

