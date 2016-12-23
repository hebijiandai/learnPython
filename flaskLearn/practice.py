from hello import app
from flask import current_app

print(app.url_map)
#激活程序上下文
app_ctx=app.app_context()
app_ctx.push()
print(current_app.name)
app_ctx.pop()