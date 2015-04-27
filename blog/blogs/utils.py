from ..models import (Setting,
                      SETTING_BLOG_NAME
                      )
from ..control_panel.utils import NotSetup


def load_page_meta(title_prefix=None):
    ds = Setting.load_settings([SETTING_BLOG_NAME])

    if SETTING_BLOG_NAME not in ds:
        raise NotSetup

    page_meta = {
        "Title": ds[SETTING_BLOG_NAME][0] if title_prefix is None else
        "%s | %s" % (title_prefix, ds[SETTING_BLOG_NAME]),
        "Brand": ds[SETTING_BLOG_NAME][0]
    }

    return page_meta

