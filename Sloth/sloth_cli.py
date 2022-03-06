import click
from art import text2art
import os
import subprocess
import sloth_couch



@click.command()
def sloth():
    title = text2art("Sloth", font='big')
    click.echo(click.style(title, blink=True, bold=True, fg='red'))
    click.echo(click.style("░W░h░y░ ░s░o░ ░l░a░z░y░?░", fg='green'))
    click.echo(click.style("Sloth: A CLI tool for daily report task", fg='yellow'))
    print('')
    print("Select your actions from below. \n")
    click.echo(click.style("1. 🚀 Edit basic config", fg='red'))
    click.echo(click.style("2. 🚀 Generate report", fg='red'))
    click.echo(click.style("3. 🚀 Task manager", fg='red'))
    click.echo(click.style("4. 🚀 Clear config", fg='red'))

    prompt_msg = click.style("💬 : Choose your option:", fg='blue')
    if not sloth_couch.SlothDataCouch().is_fresh_user():
        input_from = click.prompt(prompt_msg, type=int)
        if input_from == 1:
            print("--- Edit prompt ---")
            subprocess.call(['python', 'ui_init.py', '-owner', "admin"])
        elif input_from == 2:
            print("-- Generate report--")
            print(os.getcwd())
            subprocess.call(['python', 'ui_init.py'])
        elif input_from == 3:
            tasks = sloth_couch.SlothDataCouchRead().read_task_info() or []
            print(tasks)
            click.echo(click.style("Press following key for action", fg='blue'))
            click.echo(click.style("(n) -> Add as new task:", fg='green'))
            click.echo(click.style("(a) -> Append new task:", fg='blue'))
            click.echo(click.style("(c) -> Change status of a task:", fg='yellow'))
            click.echo(click.style(f"💬 : Please enter your key:", fg='blue'),nl=False)
            #click.pause()
            user_input = click.getchar()
            if user_input == 'n':
                tasks.clear()
                task_name = click.prompt("Please enter task name:", type=str)
                task_status = click.prompt("Please enter task name:", type=str)
                tasks.append({'status':task_status,'name':task_name})
            elif user_input == 'a':
                task_name = click.prompt("Please enter task name:", type=str)
                task_status = click.prompt("Please enter task status:", type=str)
                tasks.append({'status': task_status, 'name': task_name})
            elif user_input == 'c':
                for task in tasks:
                    task_status = click.prompt(f"Please enter current status of Task -> {task['name']}:", type=str)
                    if task_status:
                        task['status'] = task_status
            else:
                click.echo(click.style(f"💬 : wrong input", fg='blue'))

            msg = sloth_couch.SlothDataCouchWrite().write_tasks(tasks)
            msg = 'success' if msg else 'failed'
            click.echo(click.style(f"💬 : {msg}", fg='blue'))

        elif input_from == 4:
            print("Clear configs")
            sloth_couch.SlothDataCouchWrite().remove_store(key='all')
            click.echo(click.style("💬 : Data cleared successfully", fg='blue'))
        else:
            click.echo(click.style("💬 : Good Bye lazy champ", fg='blue'))
    else:
        print("Please enter below info:\n")
        basic_info = {
            "name": "",
            "to": "",
            "content": "",
            "project": "",
            "login_time": "",
            "log_out_time": ""
        }
        for each in ['Name', 'Project', 'Log-out time(pm)', 'Log-in time(am)', 'Reporting Manager', 'Content (mail)']:
            each_msg = click.style(f"💬 :-> {each}:", fg='blue')
            input_from = click.prompt(each_msg, type=str)
            if each == 'Name':
                basic_info["name"] = input_from
            if each == 'Project':
                basic_info["project"] = input_from
            if each == 'Log-out time(pm)':
                basic_info["log_out_time"] = input_from
            if each == 'Log-in time(am)':
                basic_info["login_time"] = input_from
            if each == 'Reporting Manager':
                basic_info["to"] = input_from
            if each == 'Content (mail)':
                basic_info["content"] = input_from

        msg = sloth_couch.SlothDataCouchWrite().write_info(basic_info)
        click.echo(click.style(f"💬 :{msg}:", fg='blue'))

if __name__ == '__main__':
    sloth()