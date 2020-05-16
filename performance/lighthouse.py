import os
import json
import subprocess
from typing import Optional

from pydantic import BaseModel, Extra, Field
from selenium.webdriver.remote.webdriver import WebDriver


class Audit(BaseModel):
    """ Base Lighthouse Audit Object. """
    id: str
    description: str
    title: str
    display_value: Optional[str] = Field(..., alias='displayValue')
    numeric_value: float = Field(..., alias='numericValue')
    score: Optional[float]
    score_display_mode: Optional[str] = Field(..., alias='scoreDisplayMode')


class DetailedAudit(Audit):
    details: dict


class WarningsAudit(DetailedAudit):
    warnings: dict


class Diagnostics(BaseModel):
    """ Collection of useful page vitals. """
    main_document_transfer_size: float = Field(..., alias='mainDocumentTransferSize')
    max_rtt: float = Field(..., alias='maxRtt')
    max_server_latency: float = Field(..., alias='maxServerLatency')
    num_fonts: int = Field(..., alias='numFonts')
    num_requests: int = Field(..., alias='numRequests')
    num_scripts: int = Field(..., alias='numScripts')
    num_stylesheets: int = Field(..., alias='numStylesheets')
    num_tasks: int = Field(..., alias='numTasks')
    num_tasks_over_100ms: int = Field(0, alias='numTasksOver100ms')
    num_tasks_over_10ms: int = Field(0, alias='numTasksOver10ms')
    num_tasks_over_25ms: int = Field(0, alias='numTasksOver25ms')
    num_tasks_over_500ms: int = Field(0, alias='numTasksOver500ms')
    num_tasks_over_50ms: int = Field(0, alias='numTasksOver50ms')
    rtt: float = Field(..., alias='rtt')
    throughput: float = Field(..., alias='throughput')
    total_byte_weight: float = Field(..., alias='totalByteWeight')
    total_task_time: float = Field(..., alias='totalTaskTime')


class Metrics(BaseModel):
    """ Collection of all available metrics. """
    estimated_input_latency: float = Field(..., alias='estimatedInputLatency')
    first_cpu_idle: float = Field(..., alias='firstCPUIdle')
    first_contentful_paint: float = Field(..., alias='firstContentfulPaint')
    first_meaningful_paint: float = Field(..., alias='firstMeaningfulPaint')
    interactive: float = Field(..., alias='interactive')
    observed_dom_content_loaded: int = Field(..., alias='observedDomContentLoaded')
    observed_dom_content_loaded_ts: float = Field(..., alias='observedDomContentLoadedTs')
    observed_first_contentful_paint: int = Field(..., alias='observedFirstContentfulPaint')
    observed_first_contentful_paint_ts: float = Field(..., alias='observedFirstContentfulPaintTs')
    observed_first_meaningful_paint: int = Field(..., alias='observedFirstMeaningfulPaint')
    observed_first_meaningful_paint_ts: float = Field(..., alias='observedFirstMeaningfulPaintTs')
    observed_first_paint: int = Field(..., alias='observedFirstPaint')
    observed_first_paint_ts: float = Field(..., alias='observedFirstPaintTs')
    observed_first_visual_change: int = Field(..., alias='observedFirstVisualChange')
    observed_first_visual_change_ts: float = Field(..., alias='observedFirstVisualChangeTs')
    observed_last_visual_change: int = Field(..., alias='observedLastVisualChange')
    observed_last_visual_change_ts: float = Field(..., alias='observedLastVisualChangeTs')
    observed_load: int = Field(..., alias='observedLoad')
    observed_load_ts: float = Field(..., alias='observedLoadTs')
    observed_navigation_start: int = Field(..., alias='observedNavigationStart')
    observed_navigation_start_ts: float = Field(..., alias='observedNavigationStartTs')
    observed_speed_index: int = Field(..., alias='observedSpeedIndex')
    observed_speed_index_ts: float = Field(..., alias='observedSpeedIndexTs')
    observed_trace_end: int = Field(..., alias='observedTraceEnd')
    observed_trace_end_ts: float = Field(..., alias='observedTraceEndTs')
    speed_index: int = Field(..., alias='speedIndex')
    total_blocking_time: int = Field(..., alias='totalBlockingTime')


class Audits(BaseModel):
    bootup_time: DetailedAudit = Field(..., alias='bootup-time')
    dom_size: DetailedAudit = Field(..., alias='dom-size')
    estimated_input_latency: Audit = Field(..., alias='estimated-input-latency')
    first_contentful_paint: Audit = Field(..., alias='first-contentful-paint')
    first_cpu_idle: Audit = Field(..., alias='first-cpu-idle')
    first_meaningful_paint: Audit = Field(..., alias='first-meaningful-paint')
    interactive: Audit
    main_thread_tasks: DetailedAudit = Field(..., alias='main-thread-tasks')
    main_thread_work_breakdown: DetailedAudit = Field(..., alias='mainthread-work-breakdown')
    max_potential_fid: Audit = Field(..., alias='max-potential-fid')
    network_requests: DetailedAudit = Field(..., alias='network-requests')
    network_server_latency: DetailedAudit = Field(..., alias='network-server-latency')
    render_blocking_resources: DetailedAudit = Field(..., alias='render-blocking-resources')
    speed_index: Audit = Field(..., alias='speed-index')
    time_to_first_byte: DetailedAudit = Field(..., alias='time-to-first-byte')
    total_blocking_time: Audit = Field(..., alias='total-blocking-time')
    total_byte_weight: DetailedAudit = Field(..., alias='total-byte-weight')
    unminified_css: DetailedAudit = Field(..., alias='unminified-css')
    unminified_javascript: WarningsAudit = Field(..., alias='unminified-javascript')
    unused_css_rules: DetailedAudit = Field(..., alias='unused-css-rules')
    uses_long_cache_ttl: DetailedAudit = Field(..., alias='uses-long-cache-ttl')
    uses_optimized_images: WarningsAudit = Field(..., alias='uses-optimized-images')
    uses_responsive_images: WarningsAudit = Field(..., alias='uses-responsive-images')
    uses_text_compression: DetailedAudit = Field(..., alias='uses-text-compression')
    uses_webp_images: WarningsAudit = Field(..., alias='uses-webp-images')

    class Config:
        extra: Extra.ignore


class LighthousePerformance:
    """ User-friendly Python object representing the Lighthouse audits and metrics.

    All scores are 0-1, with 0 being the lowest and 1 being the highest (a score of 0.89 is 89%).
    If its score is null or None, then look at its numericValue.
    """
    def __init__(self, lh_json: dict):
        self.overall_performance_score: float = lh_json['categories']['performance']['score']
        self.final_url: str = lh_json['finalUrl']
        self.diagnostics = Diagnostics(**lh_json['audits']['diagnostics']['details']['items'][0])
        self.metrics = Metrics(**lh_json['audits']['metrics']['details']['items'][0])
        self.audits = Audits(**lh_json['audits'])

    def to_dict(self):
        return {
            'overall_performance_score': self.overall_performance_score,
            'final_url': self.final_url,
            'diagnostics': self.diagnostics.dict(), 'metrics': self.metrics.dict(),
            'audits': self.audits.dict()
        }

    def __str__(self):
        return str(self.to_dict())


def run(driver: WebDriver) -> LighthousePerformance:
    """ Execute Lighthouse against a currently running Chrome container's current web page. """
    if driver.name != 'chrome':
        raise ValueError('WebDriver must be chrome but was ' + driver.name)

    debug_port = driver.desired_capabilities['goog:chromeOptions']['debuggerAddress'].split(':')[-1]
    run_lighthouse_script_path = os.path.dirname(os.path.abspath(__file__)) + '/run_lighthouse.sh'

    try:
        response = subprocess.run(
            [run_lighthouse_script_path, driver.current_url, debug_port, driver.session_id],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as error:
        raise EnvironmentError("Error thrown when executing run_lighthouse.sh: " + error.output)

    stdout: str = response.stdout.decode('utf-8')

    if 'Generating results...' in stdout:
        json_string = stdout.split('Generating results...')[1].strip()
    else:
        raise EnvironmentError("Error thrown when executing run_lighthouse.sh: " + stdout)

    json_obj = json.loads(json_string, strict=False)
    return LighthousePerformance(json_obj)


def run_cli(driver: WebDriver) -> LighthousePerformance:
    """ Execute the Lighthouse CLI command against the local driver's current web page. """
    if driver.name != 'chrome':
        raise ValueError('WebDriver must be chrome but was ' + driver.name)

    debug_port = driver.desired_capabilities['goog:chromeOptions']['debuggerAddress'].split(':')[-1]

    response = subprocess.run([
        'lighthouse', f'{driver.current_url}',
        '--port', f'{debug_port}',
        '--emulated-form-factor', 'desktop',
        '--output', 'json',
        '--only-categories', 'performance'
    ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    if response.stderr is not None:
        raise EnvironmentError('An error occurred while trying to execute Lighthouse CLI.\n'
                               'Is Lighthouse installed on this machine? Verify this by running:\n'
                               '    $ lighthouse --version \n\n'
                               'To install lighthouse, simply run:\n'
                               '    $ npm install -g lighthouse\n\n'
                               'stderr output:\n' + response.stderr.decode('utf-8'))

    stdout: str = response.stdout.decode('utf-8')
    if 'Generating results...' in stdout:
        json_string = stdout.split('Generating results...')[1].strip()
    else:
        raise EnvironmentError("Error thrown when executing run_lighthouse.sh: " + stdout)

    json_obj = json.loads(json_string, strict=False)
    return LighthousePerformance(json_obj)
