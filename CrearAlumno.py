import boto3
import json

def lambda_handler(event, context):
    print(event)
    
    # Si body llega como string, parsearlo
    body = event['body'] if isinstance(event['body'], dict) else json.loads(event['body'])

    tenant_id = body['tenant_id']
    alumno_id = body['alumno_id']

    alumno_datos = {
        'nombre':    body['nombre'],
        'fecha_nac': body['fecha_nac'],
        'celular':   body['celular'],
        'sexo':      body['sexo'],
        'domicilio': body['domicilio']
    }

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    table.put_item(
        Item={
            'tenant_id':    tenant_id,
            'alumno_id':    alumno_id,
            'alumno_datos': alumno_datos
        }
    )

    return {
        'statusCode': 201,
        'mensaje':   'Alumno creado exitosamente',
        'tenant_id': tenant_id,
        'alumno_id': alumno_id
    }