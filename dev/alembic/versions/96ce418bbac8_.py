"""empty message

Revision ID: 96ce418bbac8
Revises: 
Create Date: 2020-07-24 14:25:19.891283

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '96ce418bbac8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('partner_user', sa.Column('created_at', sa.TIMESTAMP(), nullable=True))
    op.add_column('partner_user', sa.Column('version_id', sa.Integer(), nullable=False))
    op.alter_column('partner_user', 'immutable_identity',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('partner_user', 'update_required',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.create_unique_constraint('_partner_id_partner_user_id_uc', 'partner_user', ['partner_id', 'partner_user_id'])
    op.drop_index('partner_id_partner_user_id_uc', table_name='partner_user')
    op.drop_table_comment(
        'partner_user',
        existing_comment='partner_user 表，记录从mirror 通过流 传入的partner的原始数据（ChinaIoT,Xiaomi,Overseas）',
        schema=None
    )
    op.drop_column('partner_user', 'deleted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('partner_user', sa.Column('deleted', mysql.TINYINT(display_width=1), server_default=sa.text("'0'"), autoincrement=False, nullable=False))
    op.create_table_comment(
        'partner_user',
        'partner_user 表，记录从mirror 通过流 传入的partner的原始数据（ChinaIoT,Xiaomi,Overseas）',
        existing_comment=None,
        schema=None
    )
    op.create_index('partner_id_partner_user_id_uc', 'partner_user', ['partner_id', 'partner_user_id'], unique=True)
    op.drop_constraint('_partner_id_partner_user_id_uc', 'partner_user', type_='unique')
    op.alter_column('partner_user', 'update_required',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('partner_user', 'immutable_identity',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.drop_column('partner_user', 'version_id')
    op.drop_column('partner_user', 'created_at')
    op.create_table('gaia_user_device_bindings',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('platform_user_id', mysql.VARCHAR(length=63), nullable=False),
    sa.Column('platform_device_id', mysql.VARCHAR(length=63), nullable=False),
    sa.Column('deleted_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('update_required', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('user_role', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('extra', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('gaia_login_detail',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('account_system_id', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('login_account_id', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('deleted', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('deleted_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('platform_user_id', mysql.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('account_system_id_login_account_id_uc', 'gaia_login_detail', ['account_system_id', 'login_account_id'], unique=True)
    op.create_table('gaia_user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('platform_user_id', mysql.VARCHAR(length=63), nullable=False, comment='先预留，后期platfrom_user_id要用 unique 字符串'),
    sa.Column('deleted', mysql.TINYINT(display_width=1), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
    sa.Column('deleted_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('update_required', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('immutable_identity', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('json_data', mysql.TEXT(), nullable=True),
    sa.Column('updated_at', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('sso_id', mysql.VARCHAR(length=63), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('partner_user_device_bindings',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###