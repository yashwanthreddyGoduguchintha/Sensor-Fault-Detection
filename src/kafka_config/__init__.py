
import os


SECURITY_PROTOCOL="SASL_SSL" #os.getenv('SECURITY_PROTOCOL',None)
SSL_MACHENISM="PLAIN" #os.getenv('SSL_MECHENISM',None)
#cloud api details
API_KEY = "RB4DOJJSBUTONMH6"#os.getenv('API_KEY',None)
API_SECRET_KEY = "6n5B/bAfmsYB9wauYdp1YaFkF6WguARXcg1K1jicfMFYI0jt9rMgfCShz4K6VBSP" #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = "pkc-lzvrd.us-west4.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)
#SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
#SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
#SCHEMARELATED aip Details
ENDPOINT_SCHEMA_URL  = "https://psrc-5zq9g.ap-southeast-2.aws.confluent.cloud"#os.getenv('ENDPOINT_SCHEMA_URL',None)
SCHEMA_REGISTRY_API_KEY ="RQ3XC7BHEUSJA343" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "PnajAO8G1B3fceQTAXhnEWq09Y4DQhNx26yfWdx9wSg0YtHdTyJ1nhzJOw9Barek"#os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

