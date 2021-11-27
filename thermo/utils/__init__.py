# -*- coding: utf-8 -*-
'''Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2016, 2017, 2018, 2019, 2020 Caleb Bell <Caleb.Andrew.Bell@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This module contains base classes for temperature `T`, pressure `P`, and
composition `zs` dependent properties. These power the various interfaces for
each property.

For reporting bugs, adding feature requests, or submitting pull requests,
please use the `GitHub issue tracker <https://github.com/CalebBell/chemicals/>`_.

.. contents:: :local:

Temperature Dependent
---------------------
.. autoclass:: TDependentProperty
   :members: name, units, extrapolation, property_min, property_max,
             critical_zero, ranked_methods, __call__, fit_polynomial,
             method, valid_methods, test_property_validity,
             T_dependent_property, plot_T_dependent_property, interpolate,
             add_method, add_tabular_data, fit_add_model, fit_data_to_model, solve_property,
             calculate_derivative, T_dependent_property_derivative,
             calculate_integral, T_dependent_property_integral,
             calculate_integral_over_T, T_dependent_property_integral_over_T,
             extrapolate, test_method_validity, calculate, from_json, as_json,
             interpolation_T, interpolation_T_inv, interpolation_property,
             interpolation_property_inv, T_limits, __repr__,
             add_correlation
   :undoc-members:

Temperature and Pressure Dependent
----------------------------------
.. autoclass:: TPDependentProperty
   :members: name, units, extrapolation, property_min, property_max,
             ranked_methods, __call__,
             method, valid_methods, test_property_validity,
             add_method, add_tabular_data, solve_property,
             extrapolate, test_method_validity, calculate,
             interpolation_T, interpolation_T_inv, interpolation_property,
             interpolation_property_inv, T_limits,
             method_P, valid_methods_P, TP_dependent_property,
             TP_or_T_dependent_property, add_tabular_data_P, plot_isotherm,
             plot_isobar, plot_TP_dependent_property, calculate_derivative_T,
             calculate_derivative_P, TP_dependent_property_derivative_T,
             TP_dependent_property_derivative_P
   :undoc-members:
   :show-inheritance:

Temperature, Pressure, and Composition Dependent
------------------------------------------------
.. autoclass:: MixtureProperty
    :members:
    :undoc-members:
    :show-inheritance:

'''
NEGLIGIBLE = 'NEGLIGIBLE'
LINEAR = 'LINEAR'

POLY_FIT = 'POLY_FIT'
EXP_POLY_FIT = 'EXP_POLY_FIT'
POLY_FIT_LN_TAU = 'POLY_FIT_LN_TAU'
EXP_POLY_FIT_LN_TAU = 'EXP_POLY_FIT_LN_TAU'

DIPPR_PERRY_8E = 'DIPPR_PERRY_8E'
VDI_TABULAR = 'VDI_TABULAR'
VDI_PPDS = 'VDI_PPDS'
COOLPROP = 'COOLPROP'
EOS = 'EOS'


from . import functional
from .functional import *
from . import multi_cheb_1d
from .multi_cheb_1d import *
from . import t_dependent_property
from .t_dependent_property import *
from . import tp_dependent_property
from .tp_dependent_property import *
from . import mixture_property
from .mixture_property import *

__all__ = (
    *functional.__all__,
    *multi_cheb_1d.__all__,
    *t_dependent_property.__all__,
    *tp_dependent_property.__all__,
    *mixture_property.__all__,
)