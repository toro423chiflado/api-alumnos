import boto3

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    tenant_id  = event['body']['tenant_id']
    alumno_id  = event['body']['alumno_id']
    alumno_datos = event['body']['alumno_datos']  # dict con fecha_nac, celular, domicilio, etc.

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    table.put_item(
        Item={
            'tenant_id':    tenant_id,
            'alumno_id':    alumno_id,
            'alumno_datos': alumno_datos
        }
    )

    # Salida (json)
    return {
        'statusCode': 201,
        'mensaje':   'Alumno creado exitosamente',
        'tenant_id': tenant_id,
        'alumno_id': alumno_id
    }