"""Global defaults.

For example, you can change default width and height of each plot:
```python-repl
>>> import vectorbt as vbt

>>> vbt.settings.layout['width'] = 800
>>> vbt.settings.layout['height'] = 400
```

Changes take effect immediately."""

import numpy as np
import json
import pkgutil

from vectorbt.utils.config import Config

__pdoc__ = {}

# Color schema
color_schema = Config(
    increasing="#1b9e76",
    decreasing="#d95f02"
)
"""_"""

__pdoc__['color_schema'] = f"""Color schema.

```plaintext
{json.dumps(color_schema, indent=2, default=str)}
```
"""

# Contrast color schema
contrast_color_schema = Config(
    blue="#4285F4",
    orange="#FFAA00",
    green="#37B13F",
    red="#EA4335",
    gray="#E2E2E2"
)
"""_"""

__pdoc__['contrast_color_schema'] = f"""Neon color schema.

```plaintext
{json.dumps(contrast_color_schema, indent=2, default=str)}
```
"""

# Templates
light_template = Config(json.loads(pkgutil.get_data(__name__, "templates/light.json")))

__pdoc__['light_template'] = "Light template."

dark_template = Config(json.loads(pkgutil.get_data(__name__, "templates/dark.json")))

__pdoc__['dark_template'] = "Dark template."

seaborn_template = Config(json.loads(pkgutil.get_data(__name__, "templates/seaborn.json")))

__pdoc__['seaborn_template'] = "Seaborn template."

# Layout
layout = Config(
    width=700,
    height=350,
    margin=dict(
        t=30, b=30, l=30, r=30
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        traceorder='normal'
    )
)
"""_"""

__pdoc__['layout'] = f"""Plotly layout.

```plaintext
{json.dumps(layout, indent=2, default=str)}
```
"""


def set_theme(theme):
    if theme == 'light' or theme == 'dark':
        color_schema.update(
            blue="#1f77b4",
            orange="#ff7f0e",
            green="#2ca02c",
            red="#dc3912",
            purple="#9467bd",
            brown="#8c564b",
            pink="#e377c2",
            gray="#7f7f7f",
            yellow="#bcbd22",
            cyan="#17becf"
        )

        layout['template'] = light_template if theme == 'light' else dark_template
    elif theme == 'seaborn':
        color_schema.update(
            blue="rgb(76,114,176)",
            orange="rgb(221,132,82)",
            green="rgb(129,114,179)",
            red="rgb(85,168,104)",
            purple="rgb(218,139,195)",
            brown="rgb(204,185,116)",
            pink="rgb(140,140,140)",
            gray="rgb(100,181,205)",
            yellow="rgb(147,120,96)",
            cyan="rgb(196,78,82)"
        )

        layout['template'] = seaborn_template
    else:
        raise ValueError(f"Theme '{theme}' not supported")


def reset_theme():
    set_theme('light')


reset_theme()

# OHLCV
ohlcv = Config(
    dict(
        column_names=dict(
            open='Open',
            high='High',
            low='Low',
            close='Close',
            volume='Volume'
        )
    ),
    frozen=True
)
"""_"""

__pdoc__['ohlcv'] = f"""Parameters for OHLCV.

```plaintext
{json.dumps(ohlcv, indent=2, default=str)}
```
"""

# Array wrapper
array_wrapper = Config(
    dict(
        column_only_select=False,
        group_select=True,
        freq=None
    ),
    frozen=True
)
"""_"""

__pdoc__['array_wrapper'] = f"""Parameters for array wrapper.

```plaintext
{json.dumps(array_wrapper, indent=2, default=str)}
```
"""

# Broadcasting
broadcasting = Config(
    dict(
        align_index=False,
        align_columns=True,
        index_from='strict',
        columns_from='stack',
        ignore_sr_names=True,
        drop_duplicates=True,
        keep='last',
        drop_redundant=True,
        ignore_default=True
    ),
    frozen=True
)
"""_"""

__pdoc__['broadcasting'] = f"""Broadcasting rules for index and columns.

```plaintext
{json.dumps(broadcasting, indent=2, default=str)}
```
"""

# Caching
caching = Config(
    dict(
        enabled=True,
        whitelist=[
            'ArrayWrapper',
            'ColumnGrouper',
            'ColumnMapper'
        ],
        blacklist=[]
    ),
    frozen=True
)
"""_"""

__pdoc__['caching'] = f"""Parameters for caching.

```plaintext
{json.dumps(caching, indent=2, default=str)}
```

See `vectorbt.utils.decorators.is_caching_enabled`.
"""

# Returns
returns = Config(
    dict(
        year_freq='365 days'
    ),
    frozen=True
)
"""_"""

__pdoc__['returns'] = f"""Parameters for returns.

```plaintext
{json.dumps(returns, indent=2, default=str)}
```
"""

# Portfolio
portfolio = Config(
    dict(
        call_seq='default',
        init_cash=100.,
        size=np.inf,
        size_type='shares',
        signal_size_type='shares',
        fees=0.,
        fixed_fees=0.,
        slippage=0.,
        reject_prob=0.,
        min_size=1e-8,
        max_size=np.inf,
        allow_partial=True,
        raise_reject=False,
        close_first=False,
        accumulate=False,
        log=False,
        conflict_mode='ignore',
        signal_direction='longonly',
        order_direction='all',
        cash_sharing=False,
        row_wise=False,
        seed=None,
        freq=None,
        incl_unrealized=False,
        use_filled_close=True
    ),
    frozen=True
)
"""_"""

__pdoc__['portfolio'] = f"""Parameters for portfolio.

```plaintext
{json.dumps(portfolio, indent=2, default=str)}
```
"""
