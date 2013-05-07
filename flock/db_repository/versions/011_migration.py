from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
    Column('password', String(length=64)),
    Column('role', SmallInteger, default=ColumnDefault(0)),
    Column('about_me', String(length=140)),
    Column('last_seen', DateTime),
    Column('age', Integer),
    Column('gender', String(length=64)),
    Column('location', String(length=64)),
    Column('val_collaborative_teams', Integer),
    Column('val_competitive_pay', Integer),
    Column('val_empowerment', Integer),
    Column('val_flex_sched', Integer),
    Column('val_advancement_opps', Integer),
    Column('val_honesty', Integer),
    Column('val_innovation', Integer),
    Column('val_medical_benefits', Integer),
    Column('val_mentoring', Integer),
    Column('val_paid_time_off', Integer),
    Column('val_performance_feedback', Integer),
    Column('val_results_driven', Integer),
    Column('val_retirement', Integer),
    Column('val_training_development', Integer),
    Column('val_work_from_home', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['val_advancement_opps'].create()
    post_meta.tables['user'].columns['val_collaborative_teams'].create()
    post_meta.tables['user'].columns['val_competitive_pay'].create()
    post_meta.tables['user'].columns['val_empowerment'].create()
    post_meta.tables['user'].columns['val_flex_sched'].create()
    post_meta.tables['user'].columns['val_honesty'].create()
    post_meta.tables['user'].columns['val_innovation'].create()
    post_meta.tables['user'].columns['val_medical_benefits'].create()
    post_meta.tables['user'].columns['val_mentoring'].create()
    post_meta.tables['user'].columns['val_paid_time_off'].create()
    post_meta.tables['user'].columns['val_performance_feedback'].create()
    post_meta.tables['user'].columns['val_results_driven'].create()
    post_meta.tables['user'].columns['val_retirement'].create()
    post_meta.tables['user'].columns['val_training_development'].create()
    post_meta.tables['user'].columns['val_work_from_home'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['val_advancement_opps'].drop()
    post_meta.tables['user'].columns['val_collaborative_teams'].drop()
    post_meta.tables['user'].columns['val_competitive_pay'].drop()
    post_meta.tables['user'].columns['val_empowerment'].drop()
    post_meta.tables['user'].columns['val_flex_sched'].drop()
    post_meta.tables['user'].columns['val_honesty'].drop()
    post_meta.tables['user'].columns['val_innovation'].drop()
    post_meta.tables['user'].columns['val_medical_benefits'].drop()
    post_meta.tables['user'].columns['val_mentoring'].drop()
    post_meta.tables['user'].columns['val_paid_time_off'].drop()
    post_meta.tables['user'].columns['val_performance_feedback'].drop()
    post_meta.tables['user'].columns['val_results_driven'].drop()
    post_meta.tables['user'].columns['val_retirement'].drop()
    post_meta.tables['user'].columns['val_training_development'].drop()
    post_meta.tables['user'].columns['val_work_from_home'].drop()
