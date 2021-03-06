# -*- coding: utf-8 -*-
# Copyright 2016-2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
import logging
from ...unit.backend_adapter import ExchangeAdapter
from ...backend import exchange_2010

_logger = logging.getLogger(__name__)

try:
    from exchangelib import FolderCollection
except (ImportError, IOError) as err:
    _logger.debug(err)


@exchange_2010
class PartnerBackendAdapter(ExchangeAdapter):
    _model_name = ['exchange.res.partner']

    def create(self, folder, exchange_contact_obj):
        return self.account.bulk_create(folder=folder,
                                        items=exchange_contact_obj)

    def write(self, external_id, exchange_contact_obj):
        return exchange_contact_obj.save()

    def find_folder(self, account, odoo_folder):
        f = account.Contacts.glob(odoo_folder.name)
        return f

    def create_folder(self, account, odoo_folder):
        f = FolderCollection(parent=account.Contacts, name=odoo_folder.name)
        return f
