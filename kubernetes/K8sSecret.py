#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.md', which is part of this source code package.
#

from kubernetes.K8sObject import K8sObject
from kubernetes.models.v1.Secret import Secret


class K8sSecret(K8sObject):

    def __init__(self, config=None, name=None):
        super(K8sSecret, self).__init__(config=config, obj_type='Secret', name=name)
        self.model = Secret(name=name, namespace=self.config.namespace)

    # -------------------------------------------------------------------------------------  override

    def create(self):
        super(K8sSecret, self).create()
        self.get()
        return self

    def update(self):
        super(K8sSecret, self).update()
        self.get()
        return self

    # ------------------------------------------------------------------------------------- add

    def add_annotation(self, k=None, v=None):
        self.model.add_annotation(k=k, v=v)
        return self

    def add_label(self, k=None, v=None):
        self.model.add_label(k=k, v=v)
        return self

    # ------------------------------------------------------------------------------------- get

    def get(self):
        self.model = Secret(name=self.name, model=self.get_model())
        return self

    def get_data(self, k=None):
        data = self.model.get_data(k=k)
        return data

    def get_type(self):
        return self.model.get_type()

    def get_dockercfg_secret(self):
        return self.model.get_dockercfg_secret()

    # ------------------------------------------------------------------------------------- set

    def set_data(self, k=None, v=None):
        self.model.set_data(k=k, v=v)
        return self

    def set_type(self, secret_type=None):
        self.model.set_type(secret_type=secret_type)
        return self

    def set_dockercfg_secret(self, data=None):
        self.model.set_dockercfg_secret(data=data)
        return self

    def set_dockercfg_json_secret(self, data=None):
        self.model.set_dockercfg_json_secret(data=data)
        return self

    def set_service_account_token(self, account_name=None, account_uid=None, token=None,
                                  kubecfg_data=None, cacert=None):

        self.model.set_service_account_token(
            account_name=account_name,
            account_uid=account_uid,
            token=token,
            kubecfg_data=kubecfg_data,
            cacert=cacert
        )
        return self
