from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
rating = Table('rating', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('company_id', Integer),
    Column('user_id', Integer),
    Column('WFH', Integer),
    Column('PTO', Integer),
    Column('Benefits', Integer),
    Column('Collaboration', Integer),
)

rating = Table('rating', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('company_id', Integer),
    Column('user_id', Integer),
    Column('rating', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['rating'].columns['Benefits'].drop()
    pre_meta.tables['rating'].columns['Collaboration'].drop()
    pre_meta.tables['rating'].columns['PTO'].drop()
    pre_meta.tables['rating'].columns['WFH'].drop()
    post_meta.tables['rating'].columns['rating'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['rating'].columns['Benefits'].create()
    pre_meta.tables['rating'].columns['Collaboration'].create()
    pre_meta.tables['rating'].columns['PTO'].create()
    pre_meta.tables['rating'].columns['WFH'].create()
    post_meta.tables['rating'].columns['rating'].drop()
