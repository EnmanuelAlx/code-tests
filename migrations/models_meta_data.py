# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = [mymodel.metadata]


from app.auth.infrastructure.models import User
from app.codes.infrastructure.models import Code

targets_metadata = [User.metadata, Code.metadata]
