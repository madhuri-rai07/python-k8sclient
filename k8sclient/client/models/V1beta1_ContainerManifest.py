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


class V1beta1_ContainerManifest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        self.swaggerTypes = {
            
            'containers': 'list[V1beta1_Container]',
            
            
            'dnsPolicy': 'V1beta1_DNSPolicy',
            
            
            'id': 'str',
            
            
            'restartPolicy': 'V1beta1_RestartPolicy',
            
            
            'uuid': 'types.UID',
            
            
            'version': 'str',
            
            
            'volumes': 'list[V1beta1_Volume]'
            
        }

        
        #list of containers belonging to the pod; containers cannot currently be added or removed
        
        self.containers = None # list[V1beta1_Container]
        
        #DNS policy for containers within the pod; one of &#39;ClusterFirst&#39; or &#39;Default&#39;
        
        self.dnsPolicy = None # V1beta1_DNSPolicy
        
        #manifest name; must be a DNS_SUBDOMAIN; cannot be updated
        
        self.id = None # str
        
        #restart policy for all containers within the pod; one of RestartPolicyAlways, RestartPolicyOnFailure, RestartPolicyNever
        
        self.restartPolicy = None # V1beta1_RestartPolicy
        
        #manifest UUID, populated by the system, read-only
        
        self.uuid = None # types.UID
        
        #manifest version; must be v1beta1
        
        self.version = None # str
        
        #list of volumes that can be mounted by containers belonging to the pod
        
        self.volumes = None # list[V1beta1_Volume]
        
