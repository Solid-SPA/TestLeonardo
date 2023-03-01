# Copyright 2023 Leo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class Car_service(models.Model):

    _name = "car_service"
    _description = "Car_service"  # TODO

    name = fields.Char(
        label="Nombre"
    )
