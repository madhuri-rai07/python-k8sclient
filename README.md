# python-k8sclient
This is swagger-codegen generated python client for Kubernetes.

Usage example, based on the swagger k8s API code:

```python
# include the client module
from client import *

# build a client connection.  In this example, we are passing the hostname as arg0, and
# sending a header with name `api_key` and value `special-key` on each call to the api.

# Initalise with the Kubernete master url.
KUBERNETES_MASTER_URL=

client = swagger.ApiClient(KUBERNETES_MASTER_URL, 'api_key', 'special-key')

# create the API class with the client we just created

api = ApivbetaApi.ApivbetaApi(client)

# call the API and list pods
pod = api.listPod()

# write it into pretty JSON
json = client.sanitizeForSerialization(pod)
print json

