"""Create User and Listing models

Revision ID: 450694e2ecbf
Revises: 
Create Date: 2024-02-27 00:23:29.247811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '450694e2ecbf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('listings')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('listings',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('type', postgresql.ENUM(
                        'HOUSE', 'APARTMENT', name='listingtype'), autoincrement=False, nullable=False),
                    sa.Column('availableNow', sa.BOOLEAN(),
                              autoincrement=False, nullable=False),
                    sa.Column('ownerId', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('address', sa.VARCHAR(length=1000),
                              autoincrement=False, nullable=False),
                    sa.Column('createdAt', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updatedAt', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(
                        ['ownerId'], ['users.id'], name='listings_ownerId_fkey'),
                    sa.PrimaryKeyConstraint('id', name='listings_pkey')
                    )
    op.create_table('users',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('userName', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('fullName', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=True),
                    sa.Column('email', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('hashedPassword', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('dob', sa.DATE(),
                              autoincrement=False, nullable=True),
                    sa.Column('gender', postgresql.ENUM('MALE', 'FEMALE', 'NOT_SPECIFIED',
                                                        name='gender'), autoincrement=False, nullable=True),
                    sa.Column('createdAt', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updatedAt', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='users_pkey'),
                    sa.UniqueConstraint('email', name='users_email_key'),
                    sa.UniqueConstraint('userName', name='users_userName_key')
                    )
    # ### end Alembic commands ###
