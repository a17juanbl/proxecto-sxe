# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Cursos(models.Model):
    _name = 'cursos'
    _description = 'Cursos'

    name = fields.Char('Curso', required=True)
    description = fields.Text('Descripción')
    alumnos = fields.Many2many('alumnos', string='Alumnos')
    profesores_id = fields.Many2one('profesores', string='Profesor')

    @api.model
    def get_alumnos(self, alumnos):
        return alumnos.mapped('alumnos.name')

    @api.model
    def get_profesores(self, profesores):
        return profesores.mapped('profesores.name')