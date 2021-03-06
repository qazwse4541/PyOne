#-*- coding=utf-8 -*-
import eventlet
eventlet.monkey_patch()
import os
from flask_script import Manager, Shell
from app import create_app
from self_config import *
from function import *

app = create_app()
manager = Manager(app)

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

######################初始化变量
rd.set('title',title)
rd.set('tj_code',tj_code)
rd.set('downloadUrl_timeout',downloadUrl_timeout)
rd.set('allow_site',','.join(allow_site))
rd.set('ARIA2_HOST',ARIA2_HOST)
rd.set('ARIA2_PORT',ARIA2_PORT)
rd.set('ARIA2_SECRET',ARIA2_SECRET)
rd.set('ARIA2_SCHEME',ARIA2_SCHEME)
rd.set('password',password)
config_path=os.path.join(config_dir,'self_config.py')
with open(config_path,'r') as f:
    text=f.read()
rd.set('users',re.findall('od_users=([\w\W]*})',text)[0])
key='themelist'
rd.delete(key)
######################函数
app.jinja_env.globals['FetchData']=FetchData
app.jinja_env.globals['path_list']=path_list
app.jinja_env.globals['CanEdit']=CanEdit
app.jinja_env.globals['quote']=urllib.quote
app.jinja_env.globals['len']=len
app.jinja_env.globals['enumerate']=enumerate
app.jinja_env.globals['os']=os
app.jinja_env.globals['re']=re
app.jinja_env.globals['file_ico']=file_ico
app.jinja_env.globals['GetConfig']=GetConfig
app.jinja_env.globals['GetThemeList']=GetThemeList
app.jinja_env.globals['get_od_user']=get_od_user

################################################################################
#####################################启动#######################################
################################################################################
if __name__ == '__main__':
    manager.run()





