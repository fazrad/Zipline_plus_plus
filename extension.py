from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities
import pandas as pd

start_session = pd.Timestamp('2021-5-16', tz='utc')
end_session = pd.Timestamp('2021-5-18', tz='utc')

register(
    'binance_minute',
    csvdir_equities(
        ['minute'],
        '/home/farzad/.zipline/custom_data/csv',
    ),
    calendar_name='24/7',
    minutes_per_day=1440,
    start_session=start_session,
    end_session=end_session,
)

register(
    'binance_daily',
    csvdir_equities(
        ['daily'],
        '/home/farzad/.zipline/custom_data/csv',
    ),
    calendar_name='24/7',
    start_session=start_session,
    end_session=end_session,
)
