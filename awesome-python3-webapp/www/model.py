import sqlalchemy as sa
from datetime import datetime

metadata = sa.MetaData()

user = sa.Table(
    "user",
    metadata,
    sa.Column("id",sa.String(50), primary_key=True),
    sa.Column("email",sa.String(50),nullable=False,index=True,default=""),
    sa.Column("passwd",sa.String(50),nullable=False,default=123456),
    sa.Column("admin", sa.Boolean,nullable=False,default=0),
    sa.Column("name", sa.String(50),nullable=False,default="",unique=True),
    sa.Column("image", sa.String(500),nullable=False,default=""),
    sa.Column("created_at", sa.DateTime,nullable=False,default=datetime.now)
)

blog = sa.Table(
    "blog",
    metadata,
    sa.Column("id", sa.String(50), primary_key=True),
    sa.Column("user_id", sa.String(50), nullable=False, default=""),
    sa.Column("user_name", sa.String(50), nullable=False, default="游客"),
    sa.Column("user_image", sa.String(500), nullable=False,default=""),
    sa.Column("name", sa.String(50), nullable=False,default="",unique=True),
    sa.Column("summary", sa.String(50), nullable=False, default="默认总结"),
    sa.Column("content", sa.Text, nullable=False),
    sa.Column("created_at", sa.DateTime, nullable=False,index=True,default=datetime.now)
)

comment = sa.Table(
    "comment",
    metadata,
    sa.Column("id", sa.String(50), primary_key=True),
    sa.Column("blog_id", sa.String(50), nullable=False, default=""),
    sa.Column("user_id", sa.String(50), nullable=False, default=""),
    sa.Column("user_image", sa.String(500), nullable=False,default=""),
    sa.Column("user_name", sa.String(50), nullable=False, default="游客"),
    sa.Column("content", sa.Text, nullable=False, default=""),
    sa.Column("created_at", sa.DateTime, nullable=False,index=True,default=datetime.now)
)