"""create_users_table

Revision ID: ffdc0a98111c
Revises:
Create Date: 2020-11-20 15:06:02.230689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffdc0a98111c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=50), nullable=False),
        sa.Column('last_name', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('zipcode', sa.Integer(), nullable=False),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.Column('image_url', sa.String(length=2000), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

    op.create_table('shelters',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('address', sa.String(length=200), nullable=False),
        sa.Column('phone_number', sa.String(20), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('office_hours', sa.String(200)),
        sa.Column('description', sa.String(2000)),
        sa.Column('image_url', sa.String(2000)),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('breeds',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.String(2000), nullable=False),
        sa.Column('image_url', sa.String(2000), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('animals',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('type', sa.String(20), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('age', sa.String(10), nullable=False),
        sa.Column('gender', sa.String(6), nullable=False),
        sa.Column('breed_id', sa.Integer(), nullable=False),
        sa.Column('description', sa.String(2000), nullable=False),
        sa.Column('shelter_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['breed_id'], ['breeds.id'], ),
        sa.ForeignKeyConstraint(['shelter_id'], ['shelters.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('adoptions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('animal_id', sa.Integer(), nullalbe=False),
        sa.Column('message', sa.String(2000), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['animal_id'], ['animals.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('photos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('animal_id', sa.Integer(), nullable=False),
        sa.Column('image_url', sa.String(2000), nullable=False),
        sa.ForeignKeyConstraint(['animal_id'], ['animals.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('favorite_animals',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('animal_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['animal_id'], ['animals.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'animal_id')
    )
    # ### end Alembic commands ###qqqqqqqqq


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photos')
    op.drop_table('favorite_animals')
    op.drop_table('animals')
    op.drop_table('breeds')
    op.drop_table('shelters')
    op.drop_table('users')
    # ### end Alembic commands ###
