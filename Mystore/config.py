class Config:
    SECRET_KEY = 'e71121f8359c7c241f56e489f91f32d7'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///text_database.db'
    SQLALCHEMY_BINDS = {
        'usa_fb': 'sqlite:///usa_fb.db',
        'tik_1000': 'sqlite:///tik_1000.db',
        'twi_1000': 'sqlite:///twi_1000.db',
        'twi_2016_2009': 'sqlite:///twi_2016_2009.db',
        'ig_f_2018_2016': 'sqlite:///ig_f_2018_2016.db',
        'ig_po_2020_2012': 'sqlite:///ig_po_2020_2012.db',
        'ig_2000f_2018_2016': 'sqlite:///ig_2000f_2018_2016.db',
        'ig_1000f_2018_2016': 'sqlite:///ig_1000f_2018_2016.db',
        'snap_50k': 'sqlite:///snap_50k.db',
        'snap_100k': 'sqlite:///snap_100k.db',
        'snap_10k': 'sqlite:///snap_10k.db',
        'aged_reddit': 'sqlite:///aged_reddit.db',
        'reddit_1000k': 'sqlite:///reddit_1000k.db',
        'link_100': 'sqlite:///link_100.db',
        'link_200': 'sqlite:///link_200.db'
    }
