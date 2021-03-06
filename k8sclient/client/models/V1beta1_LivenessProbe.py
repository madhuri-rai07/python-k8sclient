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


class V1beta1_LivenessProbe(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        self.swaggerTypes = {
            
            'exec_info': 'V1beta1_ExecAction',
            
            
            'httpGet': 'V1beta1_HTTPGetAction',
            
            
            'initialDelaySeconds': 'long',
            
            
            'tcpSocket': 'V1beta1_TCPSocketAction',
            
            
            'timeoutSeconds': 'long'
            
        }

        
        #parameters for exec-based liveness probe
        
        self.exec_info = None # V1beta1_ExecAction
        
        #parameters for HTTP-based liveness probe
        
        self.httpGet = None # V1beta1_HTTPGetAction
        
        #number of seconds after the container has started before liveness probes are initiated
        
        self.initialDelaySeconds = None # long
        
        #parameters for TCP-based liveness probe
        
        self.tcpSocket = None # V1beta1_TCPSocketAction
        
        #number of seconds after which liveness probes timeout; defaults to 1 second
        
        self.timeoutSeconds = None # long
        
