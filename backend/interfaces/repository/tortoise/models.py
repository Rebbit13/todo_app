from tortoise import Model, fields


class UserTortoise(Model):
    uuid = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=200, unique=True, index=True)
    password = fields.TextField()


class TodoTortoise(Model):
    uuid = fields.UUIDField(pk=True)
    title = fields.TextField()
    text = fields.TextField()
    owner: fields.ForeignKeyRelation[UserTortoise] = fields.ForeignKeyField(
        "models.UserTortoise", source_field="owner_uuid", related_name="todos"
    )
    done = fields.BooleanField(default=False)
