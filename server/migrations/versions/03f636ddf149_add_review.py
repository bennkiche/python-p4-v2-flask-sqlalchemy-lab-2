"""add review

Revision ID: 03f636ddf149
Revises: b87a6d1593f8
Create Date: 2025-01-24 16:04:50.999647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03f636ddf149'
down_revision = 'b87a6d1593f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name=op.f('fk_reviews_customer_id_customers')),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name=op.f('fk_reviews_item_id_items')),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('customers', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('items', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('items', 'price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('price', sa.FLOAT(), nullable=True))
    op.alter_column('items', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('customers', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_table('reviews')
    # ### end Alembic commands ###
