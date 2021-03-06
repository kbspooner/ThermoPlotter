"""Settings and defaults.

This module sets the default style sheet, tick locators and axis labels;
as well as providing a means to automatically convert the units
presented and add abbreviations that can be used when loading data.
Custom defaults can be set by saving a copy of tprc.yaml (found in the
main ThermoPlotter directory) to ``~/.config/tprc.yaml`` and editing
that.

Functions
---------

    style:
        default style sheet.
    large_style:
        style sheet for large axes.
    locator:
        default tick locators.


    to_tp:
        convert names to tp conventions.
    to_amset:
        convert names to amset conventions.
    to_amset:
        convert names to boltztrap conventions.
    to_phono3py:
        convert names to phono3py conventions.


    amset_conversions:
        unit conversions.
    boltztrap_conversions:
        unit conversions.
    phonopy_conversions:
        unit conversions.
    phono3py_conversions:
        unit conversions.


    units:
        default units used.
    labels:
        default axis labels.
    inverted_labels:
        default inverted axis labels.
    long_labels:
        list of long axis labels.
    short_labels:
        list of short axis labels.
"""

import os
import warnings
import yaml

try:
    filename = '{}/.config/tprc.yaml'.format(os.path.expanduser("~"))
    with open(filename, 'r') as f:
        conf = yaml.safe_load(f)
except yaml.parser.ParserError:
    warnings.warn('Failed to read ~/.config/tprc.yaml')
    conf = None
except Exception:
    conf = None

def __dir__():
   """It's a bit of a hack."""

   names = ['locator',
            'to_tp',
            'to_amset',
            'to_boltztrap',
            'to_phono3py',

            'amset_conversions',
            'boltztrap_conversions',
            'phonopy_conversions',
            'phono3py_conversions',
            'units',
            'labels',
            'inverted_labels',
            'long_labels',
            'short_labels']

   return names

def style():
    """Get paper-style style sheet."""

    if conf is not None and 'style' in conf and conf['style'] is not None:
        style = conf['style']
    else:
        style = ['tp']
    if isinstance(style, str):
        style = [style]

    return style

def large_style():
    """Get presentation-style style sheet."""

    if conf is not None and 'large_style' in conf and \
       conf['large_style'] is not None:
        style = conf['large_style']
    else:
        style = ['tp-large']
    if isinstance(style, str):
        style = [style]

    return style

def locator():
    """Get default locators."""

    import matplotlib.ticker as ticker


    if conf is not None and 'locator' in conf:
        if 'major' in conf['locator'] and conf['locator']['major'] is not None:
            major = conf['locator']['major']
        else:
            major = 5
        if 'minor' in conf['locator'] and conf['locator']['minor'] is not None:
            minor = conf['locator']['minor']
        else:
            minor = 2
    else:
        major = 5
        minor = 2

    locators = {'major': ticker.MaxNLocator(major),
                'minor': ticker.AutoMinorLocator(minor),
                'log':   ticker.LogLocator(),
                'null':  ticker.NullLocator()}

    return locators

def to_tp():
    """Get dictionary to translate to tp."""

    names = {'energies':             'energy',
             'fermi_levels':         'fermi_level',
             'gv':                   'group_velocity',
             'kappa':                'lattice_thermal_conductivity', # because p3p
             'kappae':               'electronic_thermal_conductivity',
             'kappal':               'lattice_thermal_conductivity',
             'ke':                   'electronic_thermal_conductivity',
             'kl':                   'lattice_thermal_conductivity',
             'mfp':                  'mean_free_path',
             'mk':                   'mode_kappa',
             'pf':                   'power_factor',
             'temperatures':         'temperature',
             'thermal_conductivity': 'electronic_thermal_conductivity'}

    if conf is not None and 'to_tp' in conf and conf['to_tp'] is not None:
        names = {**names, **conf['to_tp']}

    return names

def to_amset():
    """Get dictionary to translate to amset."""

    names = {'energy':               'energies',
             'fermi_level':          'fermi_levels',
             'kappa':                'electronic_thermal_conductivity',
             'kappae':               'electronic_thermal_conductivity',
             'ke':                   'electronic_thermal_conductivity',
             'temperature':          'temperatures',
             'thermal_conductivity': 'electronic_thermal_conductivity'}

    if conf is not None and 'to_amset' in conf and \
       conf['to_amset'] is not None:
        names = {**names, **conf['to_amset']}

    return names

def to_boltztrap():
    """Get dictionary to translate to boltztrap."""

    names = {'kappa':                'electronic_thermal_conductivity',
             'kappae':               'electronic_thermal_conductivity',
             'ke':                   'electronic_thermal_conductivity',
             'thermal_conductivity': 'electronic_thermal_conductivity'}

    if conf is not None and 'to_boltztrap' in conf and \
       conf['to_boltztrap'] is not None:
        names = {**names, **conf['to_boltztrap']}

    return names

def to_phono3py():
    """Get dictionary to convert to phono3py."""

    names = {'gv':                           'group_velocity',
             'kappal':                       'kappa',
             'kl':                           'kappa',
             'lattice_thermal_conductivity': 'kappa',
             'mfp':                          'mean_free_path',
             'mk':                           'mode_kappa',
             'temperatures':                 'temperature'}

    if conf is not None and 'to_phono3py' in conf and \
       conf['to_phono3py'] is not None:
        names = {**names, **conf['to_phono3py']}

    return names

def amset_conversions():
    """Get dictionary of unit conversions for amset.

    If modified, you will probably want to change tp.settings.units,
    tp.settings.long_labels, tp.settings.short_labels and maybe
    tp.settings.boltztrap_conversions.
    """

    conversions = {}

    if conf is not None and 'amset_conversions' in conf and \
       conf['amset_conversions'] is not None:
        conversions = {**conversions, **conf['amset_conversions']}

    return conversions

def boltztrap_conversions():
    """Get dictionary of unit conversions for boltztrap.

    If modified, you will probably want to change tp.settings.units,
    tp.settings.long_labels, tp.settings.short_labels and maybe
    tp.settings.amset_conversions.
    """

    conversions = {}

    if conf is not None and 'boltztrap_conversions' in conf and \
       conf['boltztrap_conversions'] is not None:
        conversions = {**conversions, **conf['boltztrap_conversions']}

    return conversions

def phonopy_conversions():
    """Get dictionary of unit conversions for phonopy.

    If modified, you will probably want to change tp.settings.units,
    tp.settings.long_labels and tp.settings.short_labels.
    """

    conversions = {}

    if conf is not None and 'phonopy_conversions' in conf and \
       conf['phonopy_conversions'] is not None:
        conversions = {**conversions, **conf['phonopy_conversions']}

    return conversions

def phono3py_conversions():
    """Get dictionary of unit conversions for phono3py.

    If modified, you will probably want to change tp.settings.units,
    tp.settings.long_labels and tp.settings.short_labels.
    """

    conversions = {'group_velocity': 1e2,         # THz AA to m s-1
                   'gv_by_gv':       1e4,         # THz2 AA2 to m2 s-2
                   'heat_capacity':  1.60218e-19, # eV K-1 to J K-1
                   'lifetime':       1e-12,       # THz-1 to s
                   'mean_free_path': 1e-10}       # AA to m

    if conf is not None and 'phono3py_conversions' in conf and \
       conf['phono3py_conversions'] is not None:
        conversions = {**conversions, **conf['phono3py_conversions']}

    return conversions

def units():
    """Get dictionary of units of quantities used in tp."""

    units = {'average_eff_mass':                'm_e',
             'chemical_potential':              'eV',
             'conductivity':                    'S m-1',
             'doping':                          'cm-3',
             'efermi':                          'eV',
             'effective_mass':                  'm_e',
             'electronic_thermal_conductivity': 'W m-1 K-1',
             'energy':                          'eV',
             'fermi_level':                     'eV',
             'frequency':                       'THz',
             'gamma':                           'THz',
             'group_velocity':                  'm s-1',
             'gv_by_gv':                        'm2 s-2',
             'hall_carrier_concentration':      'cm-3',
             'heat_capacity':                   'J K-1',
             'lattice_thermal_conductivity':    'W m-1 K-1',
             'lifetime':                        's',
             'mean_free_path':                  'm',
             'mobility':                        'cm^2 V-1 s-1',
             'mode_kappa':                      'W m-1 K-1',
             'mu_bounds':                       'eV',
             'occupation':                      'phonons',
             'power_factor':                    'W m-1 K-2',
             'scattering_rates':                's-1',
             'seebeck':                         'muV K-1',
             'seebeck_effective_mass':          'm_e',
             'temperature':                     'K',
             'zt':                              ''}

    if conf is not None and 'units' in conf and conf['units'] is not None:
        units = {**units, **conf['units']}

    return units

def labels():
    """Get the default labels for use in tp."""

    labels = {'short':  short_labels,
              'medium': medium_labels,
              'long':   long_labels}

    if conf is not None and 'labels' in conf and conf['labels'] is not None:
        length = conf['labels']
    else:
        length = 'long'

    return labels[length]()

def inverted_labels():
    """Get the default labels for inverted axes in tp."""

    labels = {'short':  short_labels,
              'medium': medium_labels,
              'long':   long_labels}

    if conf is not None and 'inverted_labels' in conf and \
       conf['inverted_labels'] is not None:
        length = conf['inverted_labels']
    else:
        length = 'short'

    return labels[length]()

def large_labels():
    """Get the default labels for large axes (command-line only)."""

    labels = {'short':  short_labels,
              'medium': medium_labels,
              'long':   long_labels}

    if conf is not None and 'large_labels' in conf and \
       conf['large_labels'] is not None:
        length = conf['large_labels']
    else:
        length = 'medium'

    return labels[length]()

def long_labels():
    """Get a dictionary of long-form axis labels."""

    labels = {'chemical_potential':
                  'Chemical Potential (eV)',
              'complexity_factor':
                  'Complexity Factor',
              'conductivity':
                  'Conductivity (S m$\mathregular{^{-1}}$)',
              'cumulative_kappa':
                  'Cumulative Lattice Thermal Conductivity (W m$\mathregular{^{-1}\ K^{-1}}$)',
              'doping':
                  'Carrier Concentration (cm$\mathregular{^{-1}}$)',
              'dos':
                  'Density of States',
              'efermi':
                  'Fermi Energy (eV)',
              'effective_mass':
                  'Effective Mass (m$\mathregular{_e}$)',
              'energy':
                  'Energy (eV)',
              'electronic_thermal_conductivity':
                  'Electronic Thermal Conductivity (W m$\mathregular{^{-1}\ K^{-1}}$)',
              'fermi_level':
                  'Fermi Level (eV)',
              'frequency':
                  'Frequency (THz)',
              'gamma':
                  'Imaginary Self Energy (THz)',
              'group_velocity':
                  'Group Velocity (m s$\mathregular{^{-1}}$)',
              'gv_by_gv':
                  'Group Velocity Outer Product (m$\mathregular{^2\ s^{-2}}$)',
              'heat_capacity':
                  'Heat Capacity (J K$\mathregular{^{-1}}$)',
              'lattice_thermal_conductivity':
                  'Lattice Thermal Conductivity (W m$\mathregular{^{-1}\ K^{-1}}$)',
              'lifetime':
                  'Lifetime (s)',
              'mean_free_path':
                  'Mean Free Path (m)',
              'mobility':
                  'Mobility (cm$\mathregular{^2\ V^{-1}\ s^{-1}}$)',
              'mode_kappa':
                  'Lattice Thermal Conductivity (W m$\mathregular{^{-1}\ K^{-1}}$)',
              'power_factor':
                  'Power Factor (W m$\mathregular{^{-1}\ K^{-2}}$)',
              'occupation':
                  'Occupation',
              'scattering_rates':
                  'Scattering Rates (s$\mathregular{^{-1}}$)',
              'seebeck':
                  'Seebeck Coefficient ($\mathregular{\mu V\ K^{-1}}$)',
              'temperature':
                  'Temperature (K)',
              'thermal_conductivity':
                  'Thermal Conductivity (W m$\mathregular{^{-1}\ K^{-1}}$)',
              'wavevector':
                  'Wavevector',
              'zt':
                  'ZT'}

    if conf is not None and 'long_labels' in conf and \
       conf['long_labels'] is not None:
        labels = {**labels, **conf['long_labels']}

    return labels

def medium_labels():
    """Get a dictionary of medium-length axis labels."""

    labels = {'chemical_potential':
                  'Chemical Potential (eV)',
              'complexity_factor':
                  'Complexity Factor',
              'conductivity':
                  'Conductivity (S m$\mathregular{^{-1}}$)',
              'cumulative_kappa':
                  'Cum. LTC (W m$\mathregular{^{-1}\ K^{-1}}$)',
              'doping':
                  'Carrier Concentration (cm$\mathregular{^{-1}}$)',
              'dos':
                  'Density of States',
              'efermi':
                  'Fermi Energy (eV)',
              'effective_mass':
                  'Effective Mass (m$\mathregular{_e}$)',
              'energy':
                  'Energy (eV)',
              'electronic_thermal_conductivity':
                  'Elec. Therm. Cond. (W m$\mathregular{^{-1}\ K^{-1}}$)',
              'fermi_level':
                  'Fermi Level (eV)',
              'frequency':
                  'Frequency (THz)',
              'gamma':
                  'Imaginary Self Energy (THz)',
              'group_velocity':
                  'Group Velocity (m s$\mathregular{^{-1}}$)',
              'gv_by_gv':
                  'Group Vel. Outer Prod. (m$\mathregular{^2\ s^{-2}}$)',
              'heat_capacity':
                  'Heat Capacity (J K$\mathregular{^{-1}}$)',
              'lattice_thermal_conductivity':
                  'Lat. Therm. Cond. (W m$\mathregular{^{-1}\ K^{-1}}$)',
              'lifetime':
                  'Lifetime (s)',
              'mean_free_path':
                  'Mean Free Path (m)',
              'mobility':
                  'Mobility (cm$\mathregular{^2\ V^{-1}\ s^{-1}}$)',
              'mode_kappa':
                  'Lat. Therm. Cond. (W m$\mathregular{^{-1}\ K^{-1}}$)',
              'power_factor':
                  'Power Factor (W m$\mathregular{^{-1}\ K^{-2}}$)',
              'occupation':
                  'Occupation',
              'scattering_rates':
                  'Scattering Rates (s$\mathregular{^{-1}}$)',
              'seebeck':
                  'Seebeck Coefficient ($\mathregular{\mu V\ K^{-1}}$)',
              'temperature':
                  'Temperature (K)',
              'thermal_conductivity':
                  'Thermal Cond. (W m$\mathregular{^{-1}\ K^{-1}}$)',
              'wavevector':
                  'Wavevector',
              'zt':
                  'ZT'}

    if conf is not None and 'medium_labels' in conf and \
       conf['medium_labels'] is not None:
        labels = {**labels, **conf['medium_labels']}

    return labels

def short_labels():
    """Get dictionary of short-form axis labels."""

    labels = {'chemical_potential':
                  '$\mathregular{\mu}$ (eV)',
              'complexity_factor':
                  '$\mathregular{N_v*K*}$',
              'conductivity':
                  '$\mathregular{\sigma\ (S\ m^{-1})}$',
              'cumulative_kappa':
                  '$\mathregular{\kappa_l\ (W\ m^{-1}\ K^{-1})}$',
              'doping':
                  'n (cm$\mathregular{^{-1}}$)',
              'dos':
                  'Density\nof States',
              'efermi':
                  'E$\mathregular{_{F}}$ (eV)',
              'effective_mass':
                  '$\mathregular{m*\ (m_e})$',
              'energy':
                  'E (eV)',
              'electronic_thermal_conductivity':
                  '$\mathregular{\kappa_e\ (W\ m^{-1}\ K^{-1})}$',
              'fermi_level':
                  'E$\mathregular{_{F}}$ (eV)',
              'frequency':
                  '$\mathregular{\\nu}$ (THz)',
              'gamma':
                  '$\mathregular{\Gamma}$ (THz)',
              'group_velocity':
                  '$\mathregular{g_v\ (m\ s^{-1})}$',
              'gv_by_gv':
                  '$\mathregular{g_v \otimes g_v\ (m^2\ s^{-2})}$',
              'heat_capacity':
                  'C (J K$\mathregular{^{-1}}$)',
              'lattice_thermal_conductivity':
                  '$\mathregular{\kappa_l\ (W\ m^{-1}\ K^{-1})}$',
              'lifetime':
                  '$\mathregular{\\tau}$ (s)',
              'mean_free_path':
                  '$\mathregular{\Lambda}$ (m)',
              'mobility':
                  '$\mathregular{\mu\ (cm^2\ V^{-1}\ s^{-1})}$',
              'mode_kappa':
                  '$\mathregular{\kappa_l\ (W\ m^{-1}\ K^{-1})}$',
              'power_factor':
                  'PF (W m$\mathregular{^{-1}\ K^{-2}}$)',
              'occupation':
                  'Occupation',
              'scattering_rates':
                  '$\mathregular{\\tau^{-1}\ (s^{-1})}$',
              'seebeck':
                  '$\mathregular{\\alpha\ (\mu V\ K^{-1})}$',
              'temperature':
                  'T (K)',
              'thermal_conductivity':
                  '$\mathregular{\kappa\ (W\ m^{-1}\ K^{-1}}$)',
              'wavevector':
                  'q',
              'zt':
                  'ZT'}

    if conf is not None and 'short_labels' in conf and \
       conf['short_labels'] is not None:
        labels = {**labels, **conf['short_labels']}

    return labels
