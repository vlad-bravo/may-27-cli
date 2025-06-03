import payout
import report_template

REPORTS = (
    ('payout', payout.init, payout.process, payout.result),
    ('test', report_template.init, report_template.process, report_template.result),
)
