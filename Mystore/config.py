class Config:
    SECRET_KEY = 'e71121f8359c7c241f56e489f91f32d7'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///text_database.db'
    SQLALCHEMY_BINDS = {
        'usa_fb': 'sqlite:///usa_fb.db',
        'tik_1000': 'sqlite:///tik_1000.db',
        'twi_1000': 'sqlite:///twi_1000.db',
        'twi_2016_2009': 'sqlite:///twi_2016_2009.db',
        'ig_f_2018_2016': 'sqlite:///ig_f_2018_2016.db',
        'ig_po_2020_2012': 'sqlite:///ig_po_2020_2012.db'
    }
