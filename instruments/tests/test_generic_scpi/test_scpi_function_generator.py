#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing tests for generic SCPI function generator instruments
"""

# IMPORTS ####################################################################

from __future__ import absolute_import

import quantities as pq

import instruments as ik
from instruments.tests import expected_protocol, make_name_test

# TESTS ######################################################################

test_scpi_func_gen_name = make_name_test(ik.generic_scpi.SCPIFunctionGenerator)


def test_scpi_func_gen_amplitude():
    with expected_protocol(
        ik.generic_scpi.SCPIFunctionGenerator,
        [
            "VOLT:UNIT?",
            "VOLT?",
            "VOLT:UNIT VPP",
            "VOLT 2.0",
            "VOLT:UNIT DBM",
            "VOLT 1.5"
        ], [
            "VPP",
            "+1.000000E+00"
        ]
    ) as fg:
        assert fg.amplitude == (1 * pq.V, fg.VoltageMode.peak_to_peak)
        fg.amplitude = 2 * pq.V
        fg.amplitude = (1.5 * pq.V, fg.VoltageMode.dBm)


def test_scpi_func_gen_frequency():
    with expected_protocol(
        ik.generic_scpi.SCPIFunctionGenerator,
        [
            "FREQ?",
            "FREQ 1.005000e+02"
        ], [
            "+1.234000E+03"
        ]
    ) as fg:
        assert fg.frequency == 1234 * pq.Hz
        fg.frequency = 100.5 * pq.Hz


def test_scpi_func_gen_function():
    with expected_protocol(
        ik.generic_scpi.SCPIFunctionGenerator,
        [
            "FUNC?",
            "FUNC SQU"
        ], [
            "SIN"
        ]
    ) as fg:
        assert fg.function == fg.Function.sinusoid
        fg.function = fg.Function.square


def test_scpi_func_gen_offset():
    with expected_protocol(
        ik.generic_scpi.SCPIFunctionGenerator,
        [
            "VOLT:OFFS?",
            "VOLT:OFFS 4.321000e-01"
        ], [
            "+1.234000E+01",
        ]
    ) as fg:
        assert fg.offset == 12.34 * pq.V
        fg.offset = 0.4321 * pq.V