"""chat table

Revision ID: 29ca0e407b46
Revises: f9c1f9e16c87
Create Date: 2025-04-08 22:07:36.593635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29ca0e407b46'
down_revision = 'f9c1f9e16c87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('subject', sa.String(length=120), nullable=True),
    sa.Column('message', sa.Text(length=2000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_chat_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_chat_message'), ['message'], unique=True)
        batch_op.create_index(batch_op.f('ix_chat_subject'), ['subject'], unique=True)
        batch_op.create_index(batch_op.f('ix_chat_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_chat_username'))
        batch_op.drop_index(batch_op.f('ix_chat_subject'))
        batch_op.drop_index(batch_op.f('ix_chat_message'))
        batch_op.drop_index(batch_op.f('ix_chat_email'))

    op.drop_table('chat')
    # ### end Alembic commands ###
