# {
#    'server':{
#        'host':'127.0.0.1',
#        'port': '10'
#    },
#
#    'configuration':{
#        'ssh':{
#            'acsses': 'true',
#            'login': 'Ivan',
#            'password': 'qwerty'
#        }
#    }
# }

data = dict()
print('\n')
print(data.get("server"))

data["server"] = {
    "host": 
    "127.0.0.1", 
    "port": "10"
    
    }
if data.get("configuration",{}).get("ssh",{}).get("login",{}):
    print("в структуре уже есть логин ")
print(data.get("configuration",{}).get("ssh",{}).get("login",{}))
data["configuration"] = {
    "ssh": {
        "acsses": "true", 
        "login": "Ivan", 
        "password": "qwerty"
        
        }
    }

print(data)
