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
    click.echo(click.style("Sloth (⊙ω⊙) : A CLI tool for daily report task", fg='blue'))

    print("Select your actions from below. \n")
    click.echo(click.style("1. Edit basic config", fg='red'))
    click.echo(click.style("2. Generate report", fg='red'))
    click.echo(click.style("3. Edit task config", fg='red'))
    click.echo(click.style("4. Clear config", fg='red'))

    prompt_msg = click.style("(⊙ω⊙): Choose your option:", fg='blue')
    if sloth_couch.SlothDataCouch().is_fresh_user():
        input_from = click.prompt(prompt_msg, type=int)
        if input_from == 1:
            print("--- Edit prompt ---")
        elif input_from == 2:
            print("-- Generate report--")
            print(os.getcwd())
            subprocess.call(['python', 'ui_init.py'])

        elif input_from == 3:
            print("Edit task configs")
        elif input_from == 4:
            print("Clear configs")
            sloth_couch.SlothDataCouchWrite.remove_store(key='all')
            click.echo(click.style("(⊙ω⊙): Data cleared successfully", fg='blue'))
        else:
            click.echo(click.style("(⊙ω⊙): Good Bye lazy champ", fg='blue'))
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
            each_msg = click.style(f"(⊙ω⊙): {each}:", fg='blue')
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



if __name__ == '__main__':
    sloth()