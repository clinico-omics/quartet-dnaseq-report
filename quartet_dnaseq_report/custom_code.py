#!/usr/bin/env python
""" quartet-dnaseq-report plugin functions

We can add any custom Python functions here and call them
using the setuptools plugin hooks. 
"""

from __future__ import print_function
from pkg_resources import get_distribution
import logging

from multiqc.utils import report, util_functions, config

# Initialise the main MultiQC logger
log = logging.getLogger('multiqc')

# Save this plugin's version number (defined in setup.py) to the MultiQC config
config.quartet_dnaseq_report_version = get_distribution('quartet_dnaseq_report').version


# Add default config options for the things that are used in MultiQC_NGI
def quartet_dnaseq_report_execution_start():
    """ Code to execute after the config files and
    command line flags have been parsedself.

    This setuptools hook is the earliest that will be able
    to use custom command line flags.
    """
    
    # Halt execution if we've disabled the plugin
    if config.kwargs.get('disable_plugin', True):
        return None

    log.info('Running Quartet DNA MultiQC Plugin v{}'.format(config.quartet_dnaseq_report_version))

    # Add to the main MultiQC config object.
    # User config files have already been loaded at this point
    # so we check whether the value is already set. This is to avoid
    # clobbering values that have been customised by users.

    # Module-data_generation_information
    if 'data_generation_information/information' not in config.sp:
        config.update_dict( config.sp, { 'data_generation_information/information': { 'fn_re': 'information.json' } } )
    

    # Module-pre_alignment_qc
    if 'pre_alignment_qc/summary' not in config.sp:
        config.update_dict( config.sp, { 'pre_alignment_qc/summary': { 'fn_re': '^pre_alignment.txt$' } } )

    if 'pre_alignment_qc/fastqc_data' not in config.sp:
        config.update_dict( config.sp, { 'pre_alignment_qc/fastqc_data': { 'fn_re': 'fastqc_data.txt' } } )

    if 'pre_alignment_qc/fastqc_zip' not in config.sp:
        config.update_dict( config.sp, { 'pre_alignment_qc/fastqc_zip': { 'fn_re': '.*_fastqc.zip' } } )

    if 'pre_alignment_qc/fastqc_theoretical_gc' not in config.sp:
        config.update_dict( config.sp, { 'pre_alignment_qc/fastqc_theoretical_gc': { 'fn_re': '^fastqc_theoretical_gc_hg38_genome.txt$' } } )
    

    # Module-post_alignment_qc
    if 'post_alignment_qc/summary' not in config.sp:
        config.update_dict( config.sp, { 'post_alignment_qc/summary': { 'fn_re': '^post_alignment.txt$' } } )

    if 'post_alignment_qc/bamqc/genome_results' not in config.sp:
        config.update_dict( config.sp, { 'post_alignment_qc/bamqc/genome_results': { 'fn_re': '^genome_results.txt$' } } )

    if 'post_alignment_qc/bamqc/coverage' not in config.sp:
        config.update_dict( config.sp, { 'post_alignment_qc/bamqc/coverage': { 'fn_re': '^coverage_histogram.txt$' } } )

    if 'post_alignment_qc/bamqc/insert_size' not in config.sp:
        config.update_dict( config.sp, { 'post_alignment_qc/bamqc/insert_size': { 'fn_re': '^insert_size_histogram.txt$' } } )

    if 'post_alignment_qc/bamqc/genome_fraction' not in config.sp:
        config.update_dict( config.sp, { 'post_alignment_qc/bamqc/genome_fraction': { 'fn_re': '^genome_fraction_coverage.txt$' } } )

    if 'post_alignment_qc/bamqc/gc_dist' not in config.sp:
        config.update_dict( config.sp, { 'post_alignment_qc/bamqc/gc_dist': { 'fn_re': '^mapped_reads_gc-content_distribution.txt$' } } )
    

    # Module-variant_calling_qc
    if 'variant_calling_qc/snv_indel_summary' not in config.sp:
        config.update_dict( config.sp, { 'variant_calling_qc/snv_indel_summary': { 'fn_re': '^variants.calling.qc.txt$' } } )

    if 'variant_calling_qc/precision_recall' not in config.sp:
        config.update_dict( config.sp, { 'variant_calling_qc/precision_recall': { 'fn_re': '^reference_datasets_aver-std.txt$' } } )  
    
    if 'variant_calling_qc/mendelian_summary' not in config.sp:
        config.update_dict( config.sp, { 'variant_calling_qc/mendelian_summary': { 'fn_re': '^mendelian.txt$' } } )
        
    if 'variant_calling_qc/quartet_indel' not in config.sp:
        config.update_dict( config.sp, { 'variant_calling_qc/quartet_indel': { 'fn_re': '^quartet_indel_aver-std.txt$' } } )
    
    if 'variant_calling_qc/quartet_snv' not in config.sp:
        config.update_dict( config.sp, { 'variant_calling_qc/quartet_snv': { 'fn_re': '^quartet_snv_aver-std.txt$' } } )
    
    config.module_order = ['data_generation_information', 'pre_alignment_qc', 'post_alignment_qc', 'variant_calling_qc', 'supplementary']

    config.exclude_modules = ['fastqc', 'fastq_screen', 'qualimap']
    
    config.log_filesize_limit = 2000000000