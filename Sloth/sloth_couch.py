import shelve


class SlothDataCouch:

    def __init__(self, write_back=False):
        self.shelf_file = shelve.open("shelf_file", writeback=write_back)

    def return_shelf(self):
        return self.shelf_file
    
    
class SlothDataCouchRead(SlothDataCouch):
    
    def __init__(self):
        super().__init__()

    def read_basic_info(self, key=None):
        try:
            basic = self.shelf_file['basic_info']
            return basic[key] if key else basic
        except Exception as e:
            print(e)

    def read_task_info(self):
        try:
            tasks = self.shelf_file['tasks']
            return tasks
        except Exception as e:
            print(e)


class SlothDataCouchWrite(SlothDataCouch):
    def __init__(self):
        super().__init__(write_back=True)

    def write_info(self, data):
        try:
            print("----")
            name = data.get('name')  # sloth user
            to_name = data.get('to')  # salutation
            content = data.get('content')  # mail content
            project = data.get('project')  # project name
            login_time = data.get('login_time')  # login-time
            log_out_time = data.get('log_out_time')  # logout time
            print(self.shelf_file)
            if name:
                self.shelf_file['basic_info']['name'] = name
            if to_name:
                self.shelf_file['basic_info']['to_name'] = to_name
            if content:
                self.shelf_file['basic_info']['content'] = content
            if project:
                self.shelf_file['basic_info']['project'] = project
            if login_time:
                self.shelf_file['basic_info']['login_time'] = login_time
            if log_out_time:
                self.shelf_file['basic_info']['log_out_time'] = log_out_time
            self.shelf_file.sync()
            self.shelf_file.close()
            return True
        except Exception as e:
            print(e)
            return False

    def write_tasks(self, tasks=[]):
        try:
            if tasks:
                self.shelf_file['tasks'] = tasks
                self.shelf_file.sync()
                self.shelf_file.close()
            return True
        except Exception as e:
            return False


if __name__ == '__main__':

    input_data = {
        "name": "akhil",
        "to": "Nirmal",
        "content": "PFA:kuku",
        "project": "RTB",
        "login_time": "9:30",
        "log_out_time": "6:00"
    }

    SlothDataCouchWrite().write_tasks([{"name":"RTB DISCUSIION","status":"DONE"}])
    a = SlothDataCouchRead()
    print(a.read_task_info())

