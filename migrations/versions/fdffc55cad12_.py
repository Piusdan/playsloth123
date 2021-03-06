"""empty message

Revision ID: fdffc55cad12
Revises: 
Create Date: 2017-03-03 16:22:36.525000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdffc55cad12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist', sa.String(length=250), nullable=True),
    sa.Column('album_title', sa.String(length=250), nullable=True),
    sa.Column('genre', sa.String(length=100), nullable=True),
    sa.Column('album_logo', sa.String(length=250), nullable=True),
    sa.Column('logo_url', sa.String(), nullable=True),
    sa.Column('is_favorite', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_title', sa.String(), nullable=True),
    sa.Column('audio_file', sa.String(), nullable=True),
    sa.Column('audio_url', sa.String(), nullable=True),
    sa.Column('is_favorite', sa.Boolean(), nullable=True),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('songs')
    op.drop_table('albums')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
