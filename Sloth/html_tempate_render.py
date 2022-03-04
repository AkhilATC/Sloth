def preload(fun_):
    def wrap_(*args):
        outer = "<p>ccd</p>"
        print(args)
        return fun_(outer)
    return wrap_

@preload
def template_preload(temp):
    return f"{str(temp)} <table> <tr> <th>Company</th> <th>Contact</th> <th>Country</th> </tr><tr> <td>Alfreds Futterkiste</td><td>Maria Anders</td><td>Germany</td></tr><tr> <td>Centro comercial Moctezuma</td><td>Francisco Chang</td><td>Mexico</td></tr><tr> <td>Ernst Handel</td><td>Roland Mendel</td><td>Austria</td></tr><tr> <td>Island Trading</td><td>Helen Bennett</td><td>UK</td></tr><tr> <td>Laughing Bacchus Winecellars</td><td>Yoshi Tannamuri</td><td>Canada</td></tr><tr> <td>Magazzini Alimentari Riuniti</td><td>Giovanni Rovelli</td><td>Italy</td></tr></table>"

if __name__ == '__main__':
   a = template_preload()
   print(a)