#!/usr/bin/env python
"""
Copyright 2015 Reverb Technologies, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


class V1beta1_ResourceQuota(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        self.swaggerTypes = {
            
            'annotations': 'V1beta1_TypeMeta_annotations',
            
            
            'apiVersion': 'str',
            
            
            'creationTimestamp': 'str',
            
            
            'generateName': 'str',
            
            
            'id': 'str',
            
            
            'kind': 'str',
            
            
            'labels': 'V1beta1_ResourceQuota_labels',
            
            
            'namespace': 'str',
            
            
            'resourceVersion': 'str',
            
            
            'selfLink': 'str',
            
            
            'spec': 'V1beta1_ResourceQuotaSpec',
            
            
            'status': 'V1beta1_ResourceQuotaStatus',
            
            
            'uid': 'types.UID'
            
        }

        
        #map of string keys and values that can be used by external tooling to store and retrieve arbitrary metadata about the object
        
        self.annotations = None # V1beta1_TypeMeta_annotations
        
        #version of the schema the object should have
        
        self.apiVersion = None # str
        
        #RFC 3339 date and time at which the object was created; populated by the system, read-only; null for lists
        
        self.creationTimestamp = None # str
        
        #an optional prefix to use to generate a unique name; has the same validation rules as name; optional, and is applied only name if is not specified
        
        self.generateName = None # str
        
        #name of the object; must be a DNS_SUBDOMAIN and unique among all objects of the same kind within the same namespace; used in resource URLs; cannot be updated
        
        self.id = None # str
        
        #kind of object, in CamelCase; cannot be updated
        
        self.kind = None # str
        
        #map of string keys and values that can be used to organize and categorize resource quotas
        
        self.labels = None # V1beta1_ResourceQuota_labels
        
        #namespace to which the object belongs; must be a DNS_SUBDOMAIN; &#39;default&#39; by default; cannot be updated
        
        self.namespace = None # str
        
        #string that identifies the internal version of this object that can be used by clients to determine when objects have changed; populated by the system, read-only; value must be treated as opaque by clients and passed unmodified back to the server: https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/api-conventions.md#concurrency-control-and-consistency
        
        self.resourceVersion = None # str
        
        #URL for the object; populated by the system, read-only
        
        self.selfLink = None # str
        
        #spec defines the desired quota
        
        self.spec = None # V1beta1_ResourceQuotaSpec
        
        #status defines the actual enforced quota and current usage
        
        self.status = None # V1beta1_ResourceQuotaStatus
        
        #unique UUID across space and time; populated by the system, read-only; cannot be updated
        
        self.uid = None # types.UID
        
